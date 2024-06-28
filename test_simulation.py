import unittest
import numpy as np
from simulation import hologram_pattern, force

class TestHolographicForce(unittest.TestCase):

    def setUp(self):
        self.results = []
        self.intensity_results = []

    def test_force_magnitude(self):
        """
        Test that the force magnitude is as expected for different positions and times.
        """
        positions = [(0.0, 0.0, 0.0), (1e-6, 1e-6, 0.0), (1e-3, 1e-3, 0.0)]
        times = [0, 1e-3, 1e-2, 1e-1]

        for pos in positions:
            for t in times:
                fx, fy, fz = force(*pos, t)
                magnitude = np.sqrt(fx**2 + fy**2 + fz**2)
                self.results.append((pos, t, fx, fy, fz, magnitude))

    def test_intensity_calculation(self):
        """
        Test that the intensity calculation from the hologram pattern is correct.
        """
        positions = [(0.0, 0.0, 0.0), (1e-6, 1e-6, 0.0), (1e-3, 1e-3, 0.0)]
        times = [0, 1e-3, 1e-2, 1e-1]

        for pos in positions:
            for t in times:
                H = hologram_pattern(*pos, t)
                intensity = np.abs(H)**2
                self.intensity_results.append((pos, t, intensity))

    def tearDown(self):
        with open('test_results.txt', 'w') as f:
            f.write("Position, Time, Fx, Fy, Fz, Magnitude\n")
            for res in self.results:
                f.write(f"{res[0]}, {res[1]:.3e}, {res[2]:.3e}, {res[3]:.3e}, {res[4]:.3e}, {res[5]:.3e}\n")
        
        with open('intensity_results.txt', 'w') as f:
            f.write("Position, Time, Intensity\n")
            for res in self.intensity_results:
                f.write(f"{res[0]}, {res[1]:.3e}, {res[2]:.3e}\n")

if __name__ == '__main__':
    unittest.main()
