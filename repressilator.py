import tellurium as te


class Repressilator:
    """Model represilatorja - oscilatorni genetski sistem"""
    def __init__(self, alpha=1.0, n=2.0):
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


if __name__ == "__main__":
    print("Represilator - simulacija")
    
    rep = Repressilator(alpha=20.0, n=2.0)
    t, solution = rep.solve(t_end=150)
    
    print(f"Simulirano {len(t)} točk")
    print(f"Gen A: [{solution[:,0].min():.2f}, {solution[:,0].max():.2f}]")
    print(f"Gen B: [{solution[:,1].min():.2f}, {solution[:,1].max():.2f}]")
    print(f"Gen C: [{solution[:,2].min():.2f}, {solution[:,2].max():.2f}]")
