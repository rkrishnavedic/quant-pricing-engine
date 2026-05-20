import numpy as np
from random_numbers import NumpyRNG


class PathGeometricBrownianMotion:
    """
    Euler-discretized GBM path simulator under risk-neutral dynamics.
    """
    def __init__(self, S0, r, d, sigma, rng=None):
        # Todo: Add validation for input parameters
        self.S0 = S0
        self.r = r
        self.d = d
        self.sigma = sigma
        self.rng = rng if rng is not None else NumpyRNG()

    def simulate_paths(self, T, n_steps, n_paths):
        """
        Simulate GBM paths using Euler discretization.

        Returns:
            np.ndarray of shape (n_paths, n_steps + 1)
        """
        dt = T / n_steps
        Z = self.rng.normal(size=(n_paths, n_steps))
        paths = np.zeros((n_paths, n_steps + 1))
        paths[:, 0] = self.S0
        for t in range(n_steps):
            paths[:, t + 1] = (
                paths[:, t]
                + (self.r - self.d) * paths[:, t] * dt
                + self.sigma * paths[:, t] * np.sqrt(dt) * Z[:, t]
            )
        return paths

    def simulate_terminal(self, T, n_steps, n_paths):
        """
        Simulate terminal prices S_T using Euler paths.
        """
        paths = self.simulate_paths(T, n_steps, n_paths)
        return paths[:, -1]