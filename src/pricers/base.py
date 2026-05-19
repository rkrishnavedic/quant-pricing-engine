from abc import ABC, abstractmethod

class Pricer(ABC):
    @abstractmethod
    def price(self) -> float:
        """
        Calculate the price of the derivative.
        :return: The price of the derivative
        """
        raise NotImplementedError("Subclasses must implement this method")