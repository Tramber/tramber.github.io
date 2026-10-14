# Tramber website — project memory

Website for **Tramber**, Bertrand Langeac's freelance IT company (Cloud Solution Architect + project lead, Paris La Défense). English copy.

## Where things live
- `index.html` — static, self-contained page (deployable as-is). **Source of truth for the shipped site.**
- `design/Main.dc.html` + `design/canvas.json` — Claude Design canvas source (asset URLs there are `/_blob/...` canvas uploads).
  Canvas: https://claude.ai/code/artifact/0d8716e7-3ce3-43ab-83aa-70844dac9def (publish URL https://claude.ai/artifact/2ftRFaNNpQX1FTN2BiXhYA).
  If you edit one, keep the other in sync (index.html = Main.dc.html with `{{accent}}` → `#FFB800` and `/_blob/<id>` → `assets/...`).
- `assets/clients/` grey client logos · `assets/certs/` badges · `assets/illustrations/` network image + paper grain.
- `tools/` — Python used to trace logos/badges to SVG (OpenCV contours, k-means colour layers) and generate the network SVG. Paths inside are from the original workspace; adjust before reuse.
- `tramber-client-logos-grey.zip` — the grey client logos bundle.

## Design system (Swiss editorial)
- Fonts: **Archivo** (400/500/700/900) for type, **JetBrains Mono** for labels (uppercase, letter-spacing .06–.08em).
- Ink `#111111`, paper `#F3F1EC`, muted grey `#6E6B66`, accent **`#FFB800`** (yellow; tweakable).
- 2px black rules between sections; big tight headlines (weight 900, negative tracking); numbered sections `(01)…(05)`.
- Page background = **stepped** gradient (10 flat horizontal bands, warm sand `#F2EBDB` → cool `#CED5E3`) + faint 120px vertical column grid + SVG paper grain. Deliberately *not* a smooth "AI-looking" gradient.
- All logos/badges are **SVG**. Client logos and CNCF badges are **grey**; Golden Kubestronaut, AWS and Azure badges stay in **colour**.

## Page sections (in order)
1. Nav (Services, Approach, About, Certifications, Get in touch)
2. Hero — "Architecture that holds when it matters." + image slot (**still a placeholder**) with "25+ years" strip
3. Black skills band
4. "Trusted by" — two-row marquee (opposite directions, pauses on hover, respects reduced motion) of 12 grey client logos
5. (01) Services — 4 cards · (02) Approach — "Trade-offs, not trends."
6. (03) About — "connecting the dots" illustration: ink-on-paper network with faded edges; Tramber is a peer node (arch · ai · dev · cloud) that binds loosely linked teams — **not** a central sun/star (Bertrand found that pretentious)
7. (04) Certifications — black Golden Kubestronaut card (badge right, 16 grey CNCF badges inside below the text) + full-width AWS→Azure block below (pastel orange→blue, 15° diagonal join, no borders, soft 56px faded edges, badges only on one row, titles "Amazon Web Services" / "Microsoft Azure")
8. (05) Contact — contact@tramber.com, LinkedIn, Malt; "Available for new missions"
9. Footer — giant "tramber." wordmark

## Facts (stated by Bertrand)
- Email contact@tramber.com · LinkedIn linkedin.com/in/bertrandlangeac · Malt malt.fr/profile/bertrandlangeac · Credly credly.com/users/bertrand-langeac
- 25+ years in business-critical architecture. Staff-engineer-type profile: architecture, AI, dev, cloud.
- Domain tramber.com owned since ~1998 (student days) — do **not** present the company as "since 1998".
- Past clients: TotalEnergies, Chanel, Société Générale, BNP Paribas, Banque de France, Coface, Smiths, Veepee, Younited, Derichebourg, L'Oréal, Stago.
- Certifications (badge hover title = "Name (CODE)"):
  - Golden Kubestronaut (all 16 CNCF certs: CKA, CKAD, CKS, KCNA, KCSA, PCA, ICA, CCA, CAPA, CGOA, CBA, OTCA, KCA, CNPA, CNPE, LFCS); also LFCA, Kubestronaut (not shown)
  - AWS: SA Professional (SAP-C02), SA Associate (SAA-C03), SysOps Admin Associate (SOA-C02), Cloud Practitioner (CLF-C01) — versions inferred from Credly issue dates, to confirm
  - Azure: Solutions Architect Expert (AZ-305), Administrator Associate (AZ-104) — Credly shows both **expired Jul 25 2026**; decide whether to keep/label

## Working preferences
- Prefers designed, original visuals over generic/AI-looking effects; iterate in small visual steps.
- Never use a company's logo as a hand-drawn recreation — only official files (traced to SVG).
- When changing the canvas, preserve sections; verify nothing was dropped (a past regex edit deleted sections once).

## Open items
- Hero image (top-right) still a placeholder.
- Confirm AWS exam versions and Azure status.
