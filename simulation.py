import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light (m/s)
epsilon_0 = 8.854e-12  # Vacuum permittivity (F/m)
apple_mass = 0.1  # Mass of the apple (kg)
force_scale = 1e6  # Scale factor to increase the force magnitude

def hologram_pattern(x, y, z, t):
    """
    Calculate the hologram pattern at position (x, y, z) and time t.
    """
    wavelength = 500e-9  # 500 nm (green light)
    k = 2 * np.pi / wavelength  # Wave number
    H = np.exp(1j * k * (x + y + z - c * t)) 
    return H

#H is hologram pattern (a complex exponential function of position and time)

def force(x, y, z, t):
    """
    Calculate the force on the apple at position (x, y, z) and time t due to the hologram pattern.
    """
    I = np.abs(hologram_pattern(x, y, z, t))**2 # I is the intensity of the hologram pattern which is the square of the absolute value of H
    Fx = force_scale * 0.01 * I * np.sin(x) # Calculates the force in the x-direction
    Fy = force_scale * 0.01 * I * np.sin(y) # Calculates the force in the y-direction
    Fz = force_scale * 0.01 * I * np.sin(z)
    
    # Used for debugging - prints the calculated forces
    print(f"Calculated Forces - Fx: {Fx}, Fy: {Fy}, Fz: {Fz}")
    
    return Fx, Fy, Fz

def simulate_motion():

    #Simulate the motion of the apple using holographic forces

    dt = 1e-3  # Time step/discrete intervals in seconds
    t_max = 10  # Total simulation time in seconds

    # Initial conditions starting at 0
    x, y, z = 0.0, 0.0, 0.0
    vx, vy, vz = 0.0, 0.0, 0.0

    t = 0.0
    step = 0

    positions = []
    forces = []

    while t < t_max:
        Fx, Fy, Fz = force(x, y, z, t) #: Calculates forces
        ax, ay, az = Fx / apple_mass, Fy / apple_mass, Fz / apple_mass # Calculate accelerations

        # Debugging: Prints accelerations
        print(f"Step {step}: ax={ax}, ay={ay}, az={az}")

        # Update velocities 
        vx += ax * dt
        vy += ay * dt
        vz += az * dt

        # Update positions
        x += vx * dt
        y += vy * dt
        z += vz * dt

        positions.append((x, y, z))
        forces.append((Fx, Fy, Fz))

        # Debugging - Every 1000 steps, print detailed information about the state

        if step % 1000 == 0:
            H = hologram_pattern(x, y, z, t)
            Intensity = np.abs(H)**2
            print(f"Step {step}: x={x:.2f}, y={y:.2f}, z={z:.2f}, vx={vx:.2f}, vy={vy:.2f}, vz={vz:.2f}, Fx={Fx:.2f}, Fy={Fy:.2f}, Fz={Fz:.2f}, Intensity={Intensity:.2f}, H={H.real:.2f}+{H.imag:.2f}j")

        t += dt
        step += 1

    # Plotting results
    positions = np.array(positions)
    forces = np.array(forces)

    plt.figure(figsize=(10, 8))

    plt.subplot(3, 1, 1)
    plt.plot(positions[:, 0], label='x')
    plt.plot(positions[:, 1], label='y')
    plt.plot(positions[:, 2], label='z')
    plt.xlabel('Time Step')
    plt.ylabel('Position (m)')
    plt.legend()
    plt.title('Position vs. Time Step')

    plt.subplot(3, 1, 2)
    plt.plot(forces[:, 0], label='Fx')
    plt.plot(forces[:, 1], label='Fy')
    plt.plot(forces[:, 2], label='Fz')
    plt.xlabel('Time Step')
    plt.ylabel('Force (N)')
    plt.legend()
    plt.title('Force vs. Time Step')

    plt.subplot(3, 1, 3)
    plt.plot(np.linalg.norm(forces, axis=1), label='|F|')
    plt.xlabel('Time Step')
    plt.ylabel('Force Magnitude (N)')
    plt.legend()
    plt.title('Force Magnitude vs. Time Step')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    simulate_motion()
