import tellurium as te
import matplotlib.pyplot as plt
from tqdm import tqdm
import random


class BrusselatorAttractor:
    """Brusselator - kaotični sistem"""
    
    def __init__(self, a=1, b=1, gridx=5, gridy=5):
        self.a = a
        self.b = b
        self.gridx = gridx
        self.gridy = gridy
    
    def solve(self, initial_state=[1.0, 1.0], t_end=50, n_points=2000):
        """Reši sistem z Tellurium"""
        x0, y0 = initial_state
        
        
        # model.integrator = 'gillespie'
        # model.integrator.seed = 1234
        solutions = []
        ts = []
        for r in tqdm(range(self.gridx * self.gridy)):
            x0, y0 = initial_state
            x0 += (r//self.gridy) * 0.2
            y0 += (r%self.gridy) * 0.2
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
            solutions.append(solution)
            ts.append(t)
        return ts, solutions
    
    def plot_3d(self, solutions):
        """3D vizualizacija"""
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111)
        #print(solutions.shape)
        # colors = [((1 - i/len(solutions[0]))**2,0.5, (i/len(solutions[0]))**0.5) for i in range(len(solutions[0])) ]
        for solution in solutions:
            #print(type(solutions))
            ax.plot(solution[:, 0], solution[:, 1], 
                    linewidth=0.5, alpha=0.3, color="tab:blue")
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
    print("Brusselator atraktor - simulacija")
    
    brusselator = BrusselatorAttractor(a=1, b=3, gridx=10, gridy=16)
    ts, solutions = brusselator.solve(t_end=20, initial_state=[0.5, 1.0], n_points=500)
    
    print(f"Simulirano {len(ts)} točk")
    brusselator.plot_3d(solutions)
    brusselator.plot_time_series(ts[0], solutions[0])

#     r = te.loada ('''

#     $Xo -> S1; Xo
#     S1 -> S2; k1*S3
#     S2 -> S3; k2*S1
#     S3 -> S1; k3*S2
      

#     k1 = 0.1; k2 = 0.1; k3 = 0.1
#     Xo = 1;
#     S1 = 10; S2 = 5; S3 = 1
    

# ''')

# m = r.simulate (0, 80, 50)
# r.plot()