from abc import ABC, abstractmethod


class Option(ABC):
    """
    Abstract base class for option payoff definitions.
    """

    @abstractmethod
    def payoff(self, S_T: float) -> float:
        pass


class EuropeanCallOption(Option):

    def __init__(self, strike: float):
        self.strike = strike

    def payoff(self, S_T: float) -> float:
        return max(S_T - self.strike, 0.0)


class EuropeanPutOption(Option):
    def __init__(self, strike: float):
        self.strike = strike

    def payoff(self, S_T: float) -> float:
        return max(self.strike - S_T, 0.0)


class EuropeanDigitalCallOption(Option):
    def __init__(self, strike: float, payout: float = 1.0):
        self.strike = strike
        self.payout = payout

    def payoff(self, S_T: float) -> float:
        return self.payout if S_T > self.strike else 0.0


class EuropeanDigitalPutOption(Option):
    def __init__(self, strike: float, payout: float = 1.0):
        self.strike = strike
        self.payout = payout

    def payoff(self, S_T: float) -> float:
        return self.payout if S_T < self.strike else 0.0