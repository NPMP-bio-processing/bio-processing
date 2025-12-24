from __future__ import annotations

import numpy as np
import tellurium as te
import matplotlib.pyplot as plt


def build_antimony(N: int, F: float, x0: np.ndarray) -> str:
    if x0 is None:
        x0 = F * np.ones(N)

    species_decl = ", ".join(f"x{i}={float(x0[i-1])}" for i in range(1, N + 1))
    ant = f"model Lorenz96\n  // species and initial values\n  species {species_decl}\n  const F = {float(F)}\n\n"

    for i in range(1, N + 1):
        ip1 = (i % N) + 1  # i+1
        im1 = (i - 2) % N + 1  # i-1
        im2 = (i - 3) % N + 1  # i-2
        # Lorenz-96: dx_i/dt = (x_{i+1} - x_{i-2}) * x_{i-1} - x_i + F
        expr = f"(x{ip1} - x{im2}) * x{im1} - x{i} + F"
        ant += f"  x{i}' = {expr}\n"

    ant += "end"
    return ant


class Lorenz96:
    """Lorenz-96 model"""

    def __init__(self, N: int = 5, F: float = 8.0, T: float = 30.0, dt: float = 0.01, x0: np.ndarray | None = None):
        if (N < 4):
            raise ValueError("N must be at least 4 for Lorenz-96 model")
        
        self.N = int(N)
        self.F = float(F)
        self.T = float(T)
        self.dt = float(dt)
        self.t_points = int(np.ceil(self.T / self.dt)) + 1

        if x0 is None:
            x0 = self.F * np.ones(self.N)
            x0[0] += 0.01
        self.x0 = np.asarray(x0, dtype=float)

        self._antimony = build_antimony(self.N, self.F, self.x0)
        self.rr = None
        self.result = None
        self.time = None
        self.states = None

    def solve(self):
        """Run the simulation and store the results on the instance."""
        self.rr = te.loada(self._antimony)
        self.result = self.rr.simulate(0, self.T, self.t_points)
        self.time = self.result[:, 0]
        self.states = self.result[:, 1 : self.N + 1]
        return self.result

    def plot_3d(self, ax=None, show: bool = True):
        """3D visualization"""
        if self.result is None:
            raise RuntimeError("Call solve() before plotting")

        created_fig = False
        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(projection="3d")
            created_fig = True

        ax.plot(self.states[:, 0], self.states[:, 1], self.states[:, 2], lw=0.7)
        ax.set_xlabel("$X$")
        ax.set_ylabel("$Y$")
        ax.set_zlabel("$Z$")
        ax.set_title(f"Lorenz-96 model (N={self.N}, F={self.F})")
        if show and created_fig:
            plt.tight_layout()
            plt.show()

    def plot_time_series(self, indices: list[int] | None = None):
        """Time series"""
        if self.result is None:
            raise RuntimeError("Call solve() before plotting")

        if indices is None:
            indices = list(range(1, self.N + 1))

        # convert 1-based to 0-based
        idx0 = [i - 1 for i in indices]

        fig, axes = plt.subplots(3, 1, figsize=(10, 6))
        labels = ['X', 'Y', 'Z']

        for i, (ax, label) in enumerate(zip(axes, labels)):
            ax.plot(self.time, self.states[:, i])
            ax.set_ylabel(label)
            ax.grid(True, alpha=0.3)

        axes[-1].set_xlabel('Čas')
        
        plt.tight_layout()
        plt.show()


def main():
    sim = Lorenz96(N=5, F=8, T=30.0, dt=0.01)
    sim.solve()

    sim.plot_3d()
    sim.plot_time_series()


if __name__ == "__main__":
    main()
