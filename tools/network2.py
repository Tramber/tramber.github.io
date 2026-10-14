import random, math
random.seed(11)
W,H=640,560; ME=(292,300)
INK='#141413'; DIM='#8E8A82'; ACC='#E3A200'
clusters=[('Business',(120,150)),('Product',(330,95)),('Data',(540,140)),('Ops',(560,360)),('Security',(400,450)),('Delivery',(140,420))]
pts=[]
for i,(n,(cx,cy)) in enumerate(clusters):
    for k in range(11):
        a=random.uniform(0,2*math.pi); r=random.uniform(8,70)
        pts.append([cx+r*math.cos(a),cy+r*math.sin(a),i])
while len(pts)<170:
    x,y=random.uniform(20,W-20),random.uniform(20,H-20)
    if math.dist((x,y),ME)<55: continue
    pts.append([x,y,None])
o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
# weak links
for i,(x,y,c) in enumerate(pts):
    d=sorted((math.dist((x,y),(u,v)),j) for j,(u,v,_) in enumerate(pts) if j!=i)
    for dist,j in d[:2]:
        if j<i or dist>80: continue
        dash=' stroke-dasharray="2 4"' if random.random()<0.5 else ''
        o.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{pts[j][0]:.1f}" y2="{pts[j][1]:.1f}" stroke="{DIM}" stroke-opacity="0.45" stroke-width="0.8"{dash}/>')
# my bindings: one entry node per cluster; the entry then binds its neighbours
bound=[];entries=[]
for i in range(len(clusters)):
    mem=sorted([p for p in pts if p[2]==i],key=lambda p:math.dist(p[:2],ME))
    e=mem[0]; entries.append(e); bound.append(e)
    near=sorted(mem[1:],key=lambda p:math.dist(p[:2],e[:2]))[:4]
    for p in near:
        bound.append(p)
        o.append(f'<line x1="{e[0]:.1f}" y1="{e[1]:.1f}" x2="{p[0]:.1f}" y2="{p[1]:.1f}" stroke="{INK}" stroke-opacity="0.75" stroke-width="1"/>')
for e in entries:
    o.append(f'<line x1="{ME[0]}" y1="{ME[1]}" x2="{e[0]:.1f}" y2="{e[1]:.1f}" stroke="{INK}" stroke-width="1.6"/>')
# a few cross-cluster bridges between entries, made possible by me
for a,b in [(0,1),(2,3),(4,5)]:
    A,B=entries[a],entries[b]
    o.append(f'<line x1="{A[0]:.1f}" y1="{A[1]:.1f}" x2="{B[0]:.1f}" y2="{B[1]:.1f}" stroke="{INK}" stroke-opacity="0.5" stroke-width="0.9" stroke-dasharray="6 3"/>')
# dots
for p in pts:
    if p in bound: continue
    o.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{random.choice([2,2.4,2.8,3.2])}" fill="{DIM}" fill-opacity="{random.uniform(0.45,0.75):.2f}"/>')
for p in bound:
    o.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{4.5 if p in entries else 3.2}" fill="{INK}"/>')
# me: same family as others, just more connected
o.append(f'<circle cx="{ME[0]}" cy="{ME[1]}" r="11" fill="none" stroke="{ACC}" stroke-width="3"/><circle cx="{ME[0]}" cy="{ME[1]}" r="6" fill="{INK}"/>')
F='font-family="JetBrains Mono, ui-monospace, monospace"'
o.append(f'<text x="{ME[0]+18}" y="{ME[1]+30}" {F} font-size="12" font-weight="700" letter-spacing="1" stroke="#E6E2DA" stroke-width="5" paint-order="stroke" fill="{INK}">TRAMBER</text>')
o.append(f'<text x="{ME[0]+18}" y="{ME[1]+45}" {F} font-size="10.5" letter-spacing="0.5" stroke="#E6E2DA" stroke-width="5" paint-order="stroke" fill="{INK}">arch · ai · dev · cloud</text>')
for n,(cx,cy) in clusters:
    o.append(f'<text x="{cx}" y="{cy-78 if cy<ME[1] else cy+86}" text-anchor="middle" {F} font-size="11" letter-spacing="1.2" fill="{DIM}">{n.upper()}</text>')
o.append('</svg>')
open('network2.svg','w').write(''.join(o))
open('net2.html','w').write('<body style="margin:0;background:#E6E2DA"><div style="width:640px;-webkit-mask-image:radial-gradient(ellipse 72% 70% at 50% 50%,#000 55%,transparent 100%);mask-image:radial-gradient(ellipse 72% 70% at 50% 50%,#000 55%,transparent 100%)"><img src="network2.svg" style="width:640px;display:block"></div></body>')
