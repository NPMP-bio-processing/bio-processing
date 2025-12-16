from lorenz_attractor import LorenzAttractor
from repressilator import Repressilator


print("=" * 70)
print("MODELIRANJE ATRAKTORJEV Z NDE")
print("Lorenzov atraktor & Represilator")
print("=" * 70)

# 1. LORENZOV ATRAKTOR
print("\n[1] LORENZOV ATRAKTOR")
print("-" * 70)


lorenz = LorenzAttractor(sigma=10.0, rho=28.0, beta=8.0/3.0)
t, solution = lorenz.solve()

print(f"Simulacija: {len(t)} točk, čas 0-50")
print(f"Območja: X=[{solution[:,0].min():.1f}, {solution[:,0].max():.1f}], "
      f"Y=[{solution[:,1].min():.1f}, {solution[:,1].max():.1f}], "
      f"Z=[{solution[:,2].min():.1f}, {solution[:,2].max():.1f}]")

print("Vizualizacija...")
lorenz.plot_3d(solution)
lorenz.plot_time_series(t, solution)

# 2. REPRESILATOR
print("\n[2] REPRESILATOR")
print("-" * 70)


rep = Repressilator(alpha=20.0, n=2.0)
t, solution = rep.solve(t_end=150)

print(f"Simulacija: {len(t)} točk, čas 0-150")
print("Vizualizacija...")
rep.plot_time_series(t, solution)
rep.plot_3d(solution)