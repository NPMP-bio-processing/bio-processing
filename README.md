Github link: https://github.com/NPMP-bio-processing/bio-processing.git

# Modeliranje atraktorjev z NDE v računski biologiji

Osnovna implementacija klasičnih atraktorjev in gensko regulatornih omrežij.

## Struktura projekta

```
lorenz/
├── README.md                  # Dokumentacija
├── requirements.txt    
├── lorenz_attractor.py        # Lorenzov atraktor
├── repressilator.py           # Represilator
└── run_all_analyses.py        # Glavna skripta
```

## Implementirane strukture

### 1. Lorenzov atraktor

Kaotičen sistem:
- dx/dt = σ(y - x)
- dy/dt = x(ρ - z) - y
- dz/dt = xy - βz

**Vizualizacije:**
- 3D trajektorija
- Časovni potek spremenljivk

### 2. Represilator

Trije geni, ki se medsebojno zavirajo:
- dA/dt = α/(1 + C^n) - A
- dB/dt = α/(1 + A^n) - B
- dC/dt = α/(1 + B^n) - C

**Vizualizacije:**
- Oscilacije koncentracij
- Limitni cikel v 3D

## Namestitev

```bash
pip install -r requirements.txt
```

## Uporaba

```bash
# Vse analize
python run_all_analyses.py

# Posamično
python lorenz_attractor.py
python repressilator.py
```

## Primer uporabe

```python
from lorenz_attractor import LorenzAttractor

lorenz = LorenzAttractor()
t, solution = lorenz.solve()
lorenz.plot_3d(solution)
```

## Nadaljnji razvoj

- Analiza občutljivosti na parametre
- Več začetnih pogojev
- Bistabilna stikala
- Bifurkacijska analiza

---
*December 2025*

