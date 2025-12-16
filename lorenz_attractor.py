import tellurium as te
import matplotlib.pyplot as plt


class LorenzAttractor:
    """Lorenzov atraktor - kaotični sistem"""
    
    def __init__(self, sigma=10.0, rho=28.0, beta=8.0/3.0):
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
    
    def solve(self, initial_state=[1.0, 1.0, 1.0], t_end=50, n_points=5000):
        """Reši sistem z Tellurium"""
        x0, y0, z0 = initial_state
        
        model = te.loada(f'''
            model lorenz
                x' = {self.sigma} * (y - x)
                y' = x * ({self.rho} - z) - y
                z' = x * y - {self.beta} * z
                
                x = {x0}; y = {y0}; z = {z0}
            end
        ''')
        
        result = model.simulate(0, t_end, n_points)
        t = result[:, 0]
        solution = result[:, 1:]
        return t, solution
    
    def plot_3d(self, solution):
        """3D vizualizacija"""
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(solution[:, 0], solution[:, 1], solution[:, 2], 
                linewidth=0.5, alpha=0.8)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Lorenzov atraktor')
        plt.tight_layout()
        plt.show()
    
    def plot_time_series(self, t, solution):
        """Časovni potek"""
        fig, axes = plt.subplots(3, 1, figsize=(10, 6))
        labels = ['X', 'Y', 'Z']
        for i, (ax, label) in enumerate(zip(axes, labels)):
            ax.plot(t, solution[:, i])
            ax.set_ylabel(label)
            ax.grid(True, alpha=0.3)
        axes[-1].set_xlabel('Čas')
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    print("Lorenzov atraktor - simulacija")
    
    lorenz = LorenzAttractor()
    t, solution = lorenz.solve()
    
    print(f"Simulirano {len(t)} točk")
    lorenz.plot_3d(solution)
    lorenz.plot_time_series(t, solution)
