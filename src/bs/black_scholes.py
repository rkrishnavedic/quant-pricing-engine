import numpy as np
from scipy.stats import norm # Todo: Implement your own CDF

def _d1(S, K, T, r, d, sigma):
    return (np.log(S/K) + (r - d + (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))

def _d2(S, K, T, r, d, sigma):
    return _d1(S, K, T, r, d, sigma) - sigma * np.sqrt(T)

def call_price(S, K, T, r, d, sigma):
    d1 = _d1(S, K, T, r, d, sigma)
    d2 = _d2(S, K, T, r, d, sigma)
    return (S * np.exp(-d * T) * norm.cdf(d1)) - (K * np.exp(-r * T) * norm.cdf(d2))

def put_price(S, K, T, r, d, sigma):
    d1 = _d1(S, K, T, r, d, sigma)
    d2 = _d2(S, K, T, r, d, sigma)
    return (K * np.exp(-r * T) * norm.cdf(-d2)) - (S * np.exp(-d * T) * norm.cdf(-d1))
