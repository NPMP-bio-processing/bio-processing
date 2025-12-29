import tellurium as te
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap


class ThomasAttractor:
    """Thomas' cyclically symmetric strange attractor."""

    def __init__(self, b=0.208186):
        self.b = float(b)

    def solve(self, initial_state=(0.1, 0.11, 0.09), t_end=500.0, n_points=50000):
        """Simulate the Thomas attractor via Tellurium.
        
        For dense visualization matching Wikipedia, use long simulation times
        (500+ time units) with many points (50,000+) to fully explore the attractor.
        """
        x0, y0, z0 = initial_state
        model = te.loada(f'''
            model thomas
                b = {self.b}

                x' = sin((y-cy)) - b * (x-cx)
                y' = sin((z-cz)) - b * (y-cy)
                z' = sin((x-cx)) - b * (z-cz)

                cx = 2
                cy = 2
                cz = 2

                x = {x0} + cx
                y = {y0} + cy
                z = {z0} + cz

            end
        ''')
        result = model.simulate(0, t_end, n_points)
        t = result[:, 0]
        solution = result[:, 1:]
        return t, solution

    def plot_3d(self, solution, figsize=(12, 10)):
        """3D visualization with gradient coloring based on trajectory progression."""
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111, projection='3d')
        
        # Create custom colormap: yellow -> orange -> red -> purple -> blue
        colors = ['#FFFF00', '#FFA500', '#FF4500', '#8B008B', '#00008B']
        n_bins = 256
        cmap = LinearSegmentedColormap.from_list('thomas', colors, N=n_bins)
        
        # Create line segments for gradient coloring
        points = solution
        n_points = len(points)
        
        # Create segments
        segments = []
        for i in range(n_points - 1):
            segment = [points[i], points[i + 1]]
            segments.append(segment)
        
        # Create colors based on position in trajectory
        colors_array = np.linspace(0, 1, n_points - 1)
        
        # Plot using scatter with gradient for dense, filled appearance
        # Higher point density creates the characteristic "filled" look of the attractor
        scatter = ax.scatter(solution[:, 0], solution[:, 1], solution[:, 2], 
                           c=np.arange(len(solution)), 
                           cmap=cmap, 
                           s=1.0,  # Slightly larger points for better visibility
                           alpha=0.5,
                           linewidths=0,
                           edgecolors='none')
        
        # Set labels and title
        ax.set_xlabel('X', fontsize=10)
        ax.set_ylabel('Y', fontsize=10)
        ax.set_zlabel('Z', fontsize=10)
        ax.set_title("Thomas' Cyclically Symmetric Attractor", fontsize=14, pad=20)
        
        # Set viewing angle similar to reference image
        ax.view_init(elev=20, azim=45)
        
        # Make grid more subtle
        ax.grid(True, alpha=0.2, linestyle='--', linewidth=0.5)
        
        # Set background color
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        
        plt.tight_layout()
        plt.show()

    def plot_time_series(self, t, solution, figsize=(12, 6)):
        """Plot time series of x, y, z components."""
        fig, axes = plt.subplots(3, 1, figsize=figsize)
        labels = ['X', 'Y', 'Z']
        colors = ['#FF4500', '#8B008B', '#00008B']
        
        for i, (ax, label, color) in enumerate(zip(axes, labels, colors)):
            ax.plot(t, solution[:, i], color=color, linewidth=0.8, alpha=0.8)
            ax.set_ylabel(label, fontsize=11)
            ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
            
        axes[-1].set_xlabel('Time', fontsize=11)
        axes[0].set_title("Thomas Attractor - Time Series", fontsize=12)
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    print("Thomas' cyclically symmetric attractor")
    print("=" * 50)
    
    # Create attractor with chaotic parameter value
    thomas = ThomasAttractor(b=0.208186)
    
    # Simulate with many points over long time for dense, filled attractor
    print(f"Simulating with b = {thomas.b} (chaotic regime)")
    print("This may take 30-60 seconds...")
    t, sol = thomas.solve(initial_state=(0.1, 0.0, 0.0), t_end=500.0, n_points=50000)
    
    print(f"Simulated {len(t)} points")
    print(f"X range: [{sol[:, 0].min():.3f}, {sol[:, 0].max():.3f}]")
    print(f"Y range: [{sol[:, 1].min():.3f}, {sol[:, 1].max():.3f}]")
    print(f"Z range: [{sol[:, 2].min():.3f}, {sol[:, 2].max():.3f}]")
    print("=" * 50)
    
    # Plot 3D visualization with gradient
    thomas.plot_3d(sol)
    
    # Plot time series
    thomas.plot_time_series(t, sol)