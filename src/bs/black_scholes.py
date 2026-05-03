import numpy as np
from scipy.stats import norm # Todo: Implement your own CDF

class BlackScholes:
    def __init__(self, S, K, T, r, sigma):
        self.S = S  # Stock price
        self.K = K  # Strike price
        self.T = T  # Time to maturity
        self.r = r  # Risk-free rate
        self.sigma = sigma  # Volatility

    @property
    def d1(self):
        return (np.log(self.S/self.K) + (self.r + (self.sigma ** 2) / 2) * self.T) / (self.sigma * np.sqrt(self.T))
    
    @property
    def d2(self):
        return self.d1 - self.sigma * np.sqrt(self.T)

    def call_price(self):
        return (self.S * norm.cdf(self.d1)) - (self.K * (np.exp(-self.r * self.T)) * norm.cdf(self.d2))

    def put_price(self):
        return (self.K * (np.exp(-self.r * self.T)) * norm.cdf(-self.d2)) - (self.S * norm.cdf(-self.d1))