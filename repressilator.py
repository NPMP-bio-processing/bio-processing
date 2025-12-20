import tellurium as te
import matplotlib.pyplot as plt

class Repressilator:
    """Model represilatorja - oscilatorni genetski sistem"""
    def __init__(self, alpha=20.0, n=2.0):
        self.alpha = alpha  # Stopnja transkripcije
        self.n = n          # Hillov koeficient
    
    def solve(self, initial_state=[0.1, 0.1, 0.1], t_end=100, n_points=5000):
        """Reši sistem z Tellurium (Antimony)"""
        A0, B0, C0 = initial_state
        
        model = te.loada(f'''
            model repressilator
                A' = {self.alpha} / (1 + C^{self.n}) - A
                B' = {self.alpha} / (1 + A^{self.n}) - B
                C' = {self.alpha} / (1 + B^{self.n}) - C
                
                A = {A0}; B = {B0}; C = {C0}
            end
        ''')
        
        result = model.simulate(0, t_end, n_points)
        t = result[:, 0]
        solution = result[:, 1:]
        return t, solution
    
    def plot_time_series(self, t, solution):
        """Časovni potek genov"""
        fig, ax = plt.subplots(figsize=(10, 5))
        labels = ['Gen A', 'Gen B', 'Gen C']
        for i, label in enumerate(labels):
            ax.plot(t, solution[:, i], label=label, linewidth=1.5)
        ax.set_xlabel('Čas')
        ax.set_ylabel('Koncentracija')
        ax.set_title('Represilator - Oscilacije')
        ax.legend()
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    
    def plot_3d(self, solution):
        """3D fazni prostor"""
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(solution[:, 0], solution[:, 1], solution[:, 2], 
                linewidth=0.7, alpha=0.8)
        ax.set_xlabel('Gen A')
        ax.set_ylabel('Gen B')
        ax.set_zlabel('Gen C')
        ax.set_title('Represilator - Limitni cikel')
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    print("Represilator - simulacija")
    
    rep = Repressilator(alpha=20.0, n=3.0)
    t, solution = rep.solve(initial_state=[1, 2, 3], t_end=150)
    
    print(f"Simulirano {len(t)} točk")
    rep.plot_time_series(t, solution)
    rep.plot_3d(solution)
