import cv2, numpy as np, sys
from PIL import Image
U='/tmp/claude-0/-home-claude/b1a69a06-25b5-5138-9c06-0b7c38cd2931/scratchpad/src3/'
O='/tmp/claude-0/-home-claude/b1a69a06-25b5-5138-9c06-0b7c38cd2931/scratchpad/logos/'
LIGHT='#A6A29B'; DARK='#6E6B66'
jobs=[('bnp-paribas','BNP_Paribas_2000.png',60),('chanel','Chanel-Logo.wine.png',256),('totalenergies','Logo_TotalEnergies.png',256)]
def path(mask):
    cs,_=cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    d=[]
    for c in cs:
        if cv2.contourArea(c)<6: continue
        c=cv2.approxPolyDP(c,0.7,True).reshape(-1,2)
        if len(c)<3: continue
        d.append('M'+' '.join(f'{x},{y}' for x,y in c)+'Z')
    return ''.join(d)
for name,f,T in jobs:
    im=Image.open(U+f).convert('RGBA')
    bg=Image.new('RGBA',im.size,(255,255,255,255)); bg.alpha_composite(im)
    a=np.array(bg.convert('RGB')).astype(float)
    lum=0.3*a[...,0]+0.59*a[...,1]+0.11*a[...,2]
    sat=a.max(-1)-a.min(-1)
    ink=((lum<235)|(sat>40)).astype(np.uint8)
    ys,xs=np.nonzero(ink); y0,y1,x0,x1=ys.min(),ys.max()+1,xs.min(),xs.max()+1
    pad=4
    def crop(m): return np.pad(m[y0:y1,x0:x1],pad)
    ink=crop(ink); dark=crop(((lum<T)&(ink[pad:-pad,pad:-pad]==1 if False else True)).astype(np.uint8)) if False else crop((lum<T).astype(np.uint8))
    dark&=ink
    h=ink.shape[0]; s=480/h
    W=int(round(ink.shape[1]*s)); H=480
    def up(m): 
        r=cv2.resize(m.astype(np.float32),(W,H),interpolation=cv2.INTER_CUBIC)
        return (r>0.5).astype(np.uint8)
    inkU,darkU=up(ink),up(dark)
    parts=[]
    if T<256 and (inkU&~darkU).sum()>50:
        parts.append(f'<path fill="{LIGHT}" fill-rule="evenodd" d="{path(inkU)}"/>')
        parts.append(f'<path fill="{DARK}" fill-rule="evenodd" d="{path(darkU)}"/>')
    else:
        parts.append(f'<path fill="{DARK}" fill-rule="evenodd" d="{path(inkU)}"/>')
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'+''.join(parts)+'</svg>'
    open(O+name+'.svg','w').write(svg); print(name,W,H,len(svg))
