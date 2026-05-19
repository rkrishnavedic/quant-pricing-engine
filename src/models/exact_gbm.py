from random_numbers import NumpyRNG
import numpy as np

class GeometricBrownianMotion:
    """
    Exact GBM terminal value simulator under risk-neutral dynamics.
    """

    def __init__(self, S0, r, d, sigma, rng=None):
        # Todo: Add validation for input parameters
        self.S0 = S0
        self.r = r
        self.d = d
        self.sigma = sigma
        self.rng = rng if rng is not None else NumpyRNG()

    def simulate_terminal(self, T, n_paths):
        """
        Simulate terminal stock prices S_T.
        """
        Z = self.rng.normal(size=n_paths)
        drift = (self.r - self.d - 0.5 * self.sigma ** 2) * T
        diffusion = self.sigma * np.sqrt(T) * Z
        return self.S0 * np.exp(drift + diffusion)