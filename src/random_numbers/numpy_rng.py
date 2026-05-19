from .base import BaseRNG
import numpy as np

class NumpyRNG(BaseRNG):
    def __init__(self, seed: int = None):
        self._rng = np.random.default_rng(seed)

    def normal(self, size: int) -> np.ndarray:
        return self._rng.standard_normal(size=size)