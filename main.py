import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Accelerator dimensions
# -------------------------

R = 5.0          # Radius of the accelerator ring
tube_radius = 0.5  # Thickness of the tube

# -------------------------
# Create the torus
# -------------------------

theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 30)

theta, phi = np.meshgrid(theta, phi)

x = (R + tube_radius * np.cos(phi)) * np.cos(theta)
y = (R + tube_radius * np.cos(phi)) * np.sin(theta)
z = tube_radius * np.sin(phi)

# -------------------------
# Plot
# -------------------------

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(
    x,
    y,
    z,
    alpha=0.5
)

# Particle
# -------------------------
# Particle trajectory
# -------------------------

# -------------------------
# Particle simulation
# -------------------------

particle_theta = 0

# Create the particle
particle, = ax.plot(
    [R],
    [0],
    [0],
    marker="o",
    markersize=8
)

# Number of simulation steps
steps = 500

# How much the particle moves each step
dtheta = 0.04

for step in range(steps):

    # Update particle angle
    particle_theta += dtheta

    # Calculate new position
    particle_x = R * np.cos(particle_theta)
    particle_y = R * np.sin(particle_theta)
    particle_z = 0

    # Move particle
    particle.set_data(
        [particle_x],
        [particle_y]
    )

    particle.set_3d_properties(
        [particle_z]
    )

    # Redraw
    plt.pause(0.01)

plt.show()
# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.set_title("BeamForge")

# Make the axes equal
ax.set_box_aspect([1, 1, 0.3])

plt.show()

