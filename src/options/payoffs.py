from abc import ABC, abstractmethod
import numpy as np

class Option(ABC):
    """
    Abstract base class for option payoff definitions.
    """

    @abstractmethod
    def payoff(self, S_T: float | np.ndarray) -> float | np.ndarray:
        pass


class EuropeanCallOption(Option):

    def __init__(self, strike: float):
        self.strike = strike

    def payoff(self, S_T: float | np.ndarray) -> float | np.ndarray:
        return np.maximum(S_T - self.strike, 0.0)


class EuropeanPutOption(Option):
    def __init__(self, strike: float):
        self.strike = strike

    def payoff(self, S_T: float | np.ndarray) -> float | np.ndarray:
        return np.maximum(self.strike - S_T, 0.0)


class EuropeanDigitalCallOption(Option):
    def __init__(self, strike: float, payout: float = 1.0):
        self.strike = strike
        self.payout = payout

    def payoff(self, S_T: float | np.ndarray) -> float | np.ndarray:
        return self.payout * np.where(S_T > self.strike, 1.0, 0.0)


class EuropeanDigitalPutOption(Option):
    def __init__(self, strike: float, payout: float = 1.0):
        self.strike = strike
        self.payout = payout

    def payoff(self, S_T: float | np.ndarray) -> float | np.ndarray:
        return self.payout * np.where(S_T < self.strike, 1.0, 0.0)