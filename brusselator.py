import tellurium as te
import matplotlib.pyplot as plt


class BrusselatorAttractor:
    """Brusselator - kaotični sistem"""
    
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b
    
    def solve(self, initial_state=[1.0, 1.0], t_end=50, n_points=5000):
        """Reši sistem z Tellurium"""
        x0, y0 = initial_state
        
        model = te.loada(f'''
            model brusselator
                x' = {self.a} + x * x * y - {self.b} * x - x
                y' = {self.b} * x - x * x * y
                
                x = {x0}; y = {y0}
            end
        ''')
        
        result = model.simulate(0, t_end, n_points)
        t = result[:, 0]
        solution = result[:, 1:]
        return t, solution
    
    def plot_3d(self, solution):
        """3D vizualizacija"""
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111)
        ax.plot(solution[:, 0], solution[:, 1], 
                linewidth=0.5, alpha=0.8)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Brusselator atraktor')
        plt.tight_layout()
        plt.show()
    
    def plot_time_series(self, t, solution):
        """Časovni potek"""
        fig, axes = plt.subplots(2, 1, figsize=(10, 6))
        labels = ['X', 'Y']
        for i, (ax, label) in enumerate(zip(axes, labels)):
            ax.plot(t, solution[:, i])
            ax.set_ylabel(label)
            ax.grid(True, alpha=0.3)
        axes[-1].set_xlabel('Čas')
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    print("Lorenzov atraktor - simulacija")
    
    brusselator = BrusselatorAttractor(a=1, b=3)
    t, solution = brusselator.solve(t_end=60)
    
    print(f"Simulirano {len(t)} točk")
    brusselator.plot_3d(solution)
    brusselator.plot_time_series(t, solution)