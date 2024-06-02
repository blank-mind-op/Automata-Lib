import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
width, height = 50, 50
days = 600
P = 0.15
pa = 0.05
T1 = 20
T2 = 10
u = 0.5
T3 = 14
k = 0.02
q = 0.6

# State constants
S, I, Ia, C, R, H, D = 0, 1, 2, 3, 4, 5, 6

# Initialize grid
grid = np.zeros((width, height), dtype=int)
initial_infected = 10
infected_indices = np.random.choice(width * height, initial_infected, replace=False)
grid.flat[infected_indices] = I

# Function to get neighbors
def get_neighbors(x, y):
    neighbors = [(i, j) for i in range(x-1, x+2) for j in range(y-1, y+2) if 0 <= i < width and 0 <= j < height and (i, j) != (x, y)]
    return neighbors

# Simplified r_values and immunity arrays
r_values = np.random.uniform(0, 1, (width, height))
immunity = np.random.uniform(0, 1, (width, height))

# Function to calculate probability
def calculate_probability(grid, x, y, r_values, immunity):
    neighbors = get_neighbors(x, y)
    total_probability = 0

    for nx, ny in neighbors:
        distance_factor = 1 if (nx == x or ny == y) else 1 / np.sqrt(2)
        infectivity = np.sqrt(r_values[nx, ny])
        susceptibility = 1 - immunity[x, y]
        P_ij_mn = infectivity * susceptibility
        total_probability += distance_factor * P_ij_mn

    probability = total_probability / len(neighbors)
    return probability

# Function to update grid
def update_grid(grid, r_values, immunity):
    new_grid = grid.copy()
    for x in range(width):
        for y in range(height):
            if grid[x, y] == S:
                if np.random.rand() < q:
                    continue
                for nx, ny in get_neighbors(x, y):
                    if grid[nx, ny] in [I, Ia, C]:
                        P_ij = calculate_probability(grid, x, y, r_values, immunity)
                        if np.random.rand() < P_ij:
                            new_grid[x, y] = I if np.random.rand() > pa else Ia
                            break
            elif grid[x, y] == I:
                if np.random.rand() < 1 / T1:
                    new_grid[x, y] = C
            elif grid[x, y] == C:
                if np.random.rand() < u:
                    new_grid[x, y] = H
                elif np.random.rand() < 1 / T2:
                    new_grid[x, y] = R
            elif grid[x, y] == H:
                if np.random.rand() < k:
                    new_grid[x, y] = D
                elif np.random.rand() < 1 / T3:
                    new_grid[x, y] = R
    return new_grid

# Initialize data storage for the simulation
grids = [grid]
counts = {S: [], I: [], Ia: [], C: [], R: [], H: [], D: []}

# Run the simulation
for day in range(days):
    grid = update_grid(grid, r_values, immunity)
    grids.append(grid)
    counts[S].append(np.sum(grid == S))
    counts[I].append(np.sum(grid == I))
    counts[Ia].append(np.sum(grid == Ia))
    counts[C].append(np.sum(grid == C))
    counts[R].append(np.sum(grid == R))
    counts[H].append(np.sum(grid == H))
    counts[D].append(np.sum(grid == D))

# Set up the figure for plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12), gridspec_kw={'height_ratios': [3, 1]})

cmap = plt.colormaps.get_cmap('plasma')
im = ax1.imshow(grids[0], cmap=cmap, vmin=0, vmax=6)
cbar = fig.colorbar(im, ax=ax1, ticks=np.arange(7))
cbar.ax.set_yticklabels(['Susceptible', 'Infected', 'Asymptomatic', 'Confirmed', 'Recovered', 'Hospitalized', 'Deceased'])

ax2.set_xlim(0, days)
ax2.set_ylim(0, width * height)
lines = {state: ax2.plot([], [], label=label)[0] for state, label in zip(
    [S, I, Ia, C, R, H, D],
    ['Susceptible', 'Infected', 'Asymptomatic', 'Confirmed', 'Recovered', 'Hospitalized', 'Deceased']
)}

ax2.legend()

# Update function for the animation
def update(frame):
    im.set_data(grids[frame])
    ax1.set_title(f'Day {frame}')
    for state, line in lines.items():
        line.set_data(range(frame + 1), counts[state][:frame + 1])
    return [im] + list(lines.values())

# Create the animation
anim = FuncAnimation(fig, update, frames=range(days), interval=200, repeat=False)

# Display the animation
plt.show()
