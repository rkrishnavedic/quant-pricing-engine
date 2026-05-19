from abc import ABC, abstractmethod
import numpy as np

class BaseRNG(ABC):
    @abstractmethod
    def normal(self, size: int) -> np.ndarray:
        """
        Generate standard normal random numbers.
        :param size: Number of random numbers to generate
        :return: Array of standard normal random numbers
        """
        raise NotImplementedError("Subclasses must implement this method")