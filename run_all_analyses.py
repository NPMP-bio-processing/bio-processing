from lorenz_attractor import LorenzAttractor
from repressilator import Repressilator
from lorenz96_model import Lorenz96

print("=" * 70)
print("MODELIRANJE ATRAKTORJEV Z NDE")
print("Lorenzov atraktor & Represilator")
print("=" * 70)

# 1. LORENZOV ATRAKTOR
print("\n[1] LORENZOV ATRAKTOR")
print("-" * 70)


lorenz = LorenzAttractor(sigma=10.0, rho=28.0, beta=8.0/3.0)
t, solution = lorenz.solve()

print("Vizualizacija...")
lorenz.plot_3d(solution)
lorenz.plot_time_series(t, solution)

# 2. REPRESILATOR
print("\n[2] REPRESILATOR")
print("-" * 70)

rep = Repressilator(alpha=20.0, n=2.0)
t, solution = rep.solve(t_end=150)

print(f"Simulacija: {len(t)} točk, čas 0-150")
print(f"Gen A: [{solution[:,0].min():.2f}, {solution[:,0].max():.2f}]")
print(f"Gen B: [{solution[:,1].min():.2f}, {solution[:,1].max():.2f}]")
print(f"Gen C: [{solution[:,2].min():.2f}, {solution[:,2].max():.2f}]")

# 3. LORENZ96 MODEL
lorenz96 = Lorenz96(N=5, F=8, T=30.0, dt=0.01)
lorenz96.solve()

print("\n[3] LORENZ-96 MODEL")
print("-" * 70)
print("Vizualizacija...")

lorenz96.plot_3d()
lorenz96.plot_time_series()