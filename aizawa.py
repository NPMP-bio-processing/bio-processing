import tellurium as te
import matplotlib.pyplot as plt
from tqdm import tqdm
import random


class AizawaAttractor:
    """Brusselator - kaotični sistem"""
    
    def __init__(self, a=0.92, b=0.7, c=0.67, d=3.5, e=0.25, f=0.1, gridx=5, gridy=5):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.gridx = gridx
        self.gridy = gridy
    
    def solve(self, initial_state=[0.1, 0.0, 0.0], t_end=50, n_points=2000):
        """Reši sistem z Tellurium"""
        x0, y0, z0 = initial_state
        
        
        # model.integrator = 'gillespie'
        # model.integrator.seed = 1234
        solutions = []
        ts = []
        for r in tqdm(range(self.gridx * self.gridy)):
            x0, y0, z0 = initial_state
            # x0 += (r//self.gridy) * 0.2
            # y0 += (r%self.gridy) * 0.2
            model = te.loada(f'''
            model aizawa
                x' = (z - b)*x - d*y
                y' = d*x + (z - b)*y
                z' = c + a*z - z*z*z/3 - x*x + f*z*x*x*x
                
                a = {self.a}; b = {self.b}; c = {self.c}; d = {self.d}; e = {self.e}; f = {self.f};
                x = {x0}; y = {y0}; z = {z0};
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
        ax = fig.add_subplot(111, projection='3d')
        #print(solutions.shape)
        # colors = [((1 - i/len(solutions[0]))**2,0.5, (i/len(solutions[0]))**0.5) for i in range(len(solutions[0])) ]
        for solution in solutions:
            #print(type(solutions))
            ax.scatter(solution[:, 0], solution[:, 2], solution[:, 1], 
                    linewidth=0.5, s=1, alpha=0.3, color="tab:blue")
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Aizawa atraktor')
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
    print("Aizawa atraktor - simulacija")
    
    brusselator = AizawaAttractor(gridx=1, gridy=1)
    ts, solutions = brusselator.solve(t_end=1000, n_points=200000)
    
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