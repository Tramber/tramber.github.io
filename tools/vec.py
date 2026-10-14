import cv2, numpy as np, glob, os, sys
from PIL import Image
SRC='credly_hi/'; OUT='badges_svg/'; os.makedirs(OUT,exist_ok=True)
COLOR={'golden-kubestronaut','azure-administrator','azure-solutions-architect'} | {os.path.basename(f)[:-5] for f in glob.glob(SRC+'aws-*.webp')}
GREYS=['#5A5752','#77746F','#94918B','#B2AFA9','#D0CDC6','#F1EFEA']
def paths(mask):
    cs,_=cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    d=[]
    for c in cs:
        if cv2.contourArea(c)<12: continue
        c=cv2.approxPolyDP(c,0.9,True).reshape(-1,2)
        if len(c)<3: continue
        d.append('M'+' '.join(f'{x/2:.1f},{y/2:.1f}' for x,y in c)+'Z')
    return ''.join(d)
def hexc(c): return '#%02X%02X%02X'%tuple(int(v) for v in c)
for f in sorted(glob.glob(SRC+'*.webp')):
    name=os.path.basename(f)[:-5]
    im=Image.open(f).convert('RGBA'); w,h=im.size
    im=im.resize((w*2,h*2),Image.LANCZOS)
    a=np.array(im); alpha=a[...,3]; rgb=a[...,:3].astype(np.float32)
    op=alpha>127
    wh=((rgb.min(-1)>232)|(~op)).astype(np.uint8)
    n,cc=cv2.connectedComponents(wh)
    border=set(np.unique(np.concatenate([cc[0],cc[-1],cc[:,0],cc[:,-1]])))
    bgm=np.isin(cc,list(border))&(wh==1)
    op=op&~bgm
    color=name in COLOR
    K=6 if color else 4
    feats=rgb[op] if color else (0.3*rgb[...,0]+0.59*rgb[...,1]+0.11*rgb[...,2])[op][:,None]
    crit=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,30,1.0)
    _,lab,cent=cv2.kmeans(feats.astype(np.float32),K,None,crit,3,cv2.KMEANS_PP_CENTERS)
    L=np.full(alpha.shape,255,np.uint8); L[op]=lab.ravel().astype(np.uint8)
    L=cv2.medianBlur(L,5)
    lum=(cent@np.array([0.3,0.59,0.11])) if color else cent[:,0]
    order=np.argsort(-np.bincount(L[op].ravel(),minlength=K)[:K])  # biggest first
    if color: fills={k:hexc(cent[k]) for k in range(K)}
    else:
        rank=np.argsort(np.argsort(lum))  # 0 darkest
        ramp=[GREYS[int(round(r*(len(GREYS)-1)/(K-1)))] for r in range(K)]
        fills={k:ramp[rank[k]] for k in range(K)}
    base=(cv2.medianBlur(op.astype(np.uint8)*255,5)>127).astype(np.uint8)
    parts=[f'<path fill="{fills[order[0]]}" fill-rule="evenodd" d="{paths(base)}"/>']
    ker=np.ones((3,3),np.uint8)
    for k in order[1:]:
        m=((L==k)&(base==1)).astype(np.uint8)
        if m.sum()<30: continue
        m=cv2.dilate(m,ker,1)&base
        parts.append(f'<path fill="{fills[k]}" fill-rule="evenodd" d="{paths(m)}"/>')
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'+''.join(parts)+'</svg>'
    open(OUT+name+'.svg','w').write(svg); print(name, len(svg)//1024,'KB')
