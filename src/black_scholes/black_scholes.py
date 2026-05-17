import numpy as np
from scipy.stats import norm # Todo: Implement your own CDF

def _d1(S, K, T, r, d, sigma):
    """
    Calculate d1 used in the Black-Scholes formula.
        S: Stock price
        K: Strike price
        T: Time to maturity
        r: Risk-free rate
        d: Dividend yield
        sigma: Volatility
    Returns:
        d1 value
    """
    return (np.log(S/K) + (r - d + (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))

def _d2(S, K, T, r, d, sigma):
    """
    Calculate d2 used in the Black-Scholes formula.
        S: Stock price
        K: Strike price
        T: Time to maturity
        r: Risk-free rate
        d: Dividend yield
        sigma: Volatility
    Returns:
        d2 value
    """
    return _d1(S, K, T, r, d, sigma) - sigma * np.sqrt(T)

def call_price(S, K, T, r, d, sigma):
    """
    Calculate the price of a European call option using the Black-Scholes formula.
        S: Stock price
        K: Strike price
        T: Time to maturity
        r: Risk-free rate
        d: Dividend yield
        sigma: Volatility
    Returns:
        Price of the call option
    """
    d1 = _d1(S, K, T, r, d, sigma)
    d2 = _d2(S, K, T, r, d, sigma)
    return (S * np.exp(-d * T) * norm.cdf(d1)) - (K * np.exp(-r * T) * norm.cdf(d2))

def put_price(S, K, T, r, d, sigma):
    """
    Calculate the price of a European put option using the Black-Scholes formula.
        S: Stock price
        K: Strike price
        T: Time to maturity
        r: Risk-free rate
        d: Dividend yield
        sigma: Volatility
    Returns:
        Price of the put option
    """
    d1 = _d1(S, K, T, r, d, sigma)
    d2 = _d2(S, K, T, r, d, sigma)
    return (K * np.exp(-r * T) * norm.cdf(-d2)) - (S * np.exp(-d * T) * norm.cdf(-d1))

def zero_coupon_bond_price(N, T, r):
    """
    Calculate the price of a zero-coupon bond.
        N: Face value of the bond
        T: Time to maturity
        r: Risk-free rate
    Returns:        
        Price of the zero-coupon bond
    """
    return N * np.exp(-r * T)

def forward_price(S, T, r, d):
    """
    Calculate the forward price of an asset.
        S: Current stock price
        T: Time to maturity
        r: Risk-free rate
        d: Dividend yield
    Returns:
        Forward price of the asset
    """
    return S * np.exp((r - d) * T)

def forward_contract_price(S, K, T, r, d):
    """
    Calculate the present value of a forward contract.
        S: Current stock price
        K: Strike price
        T: Time to maturity
        r: Risk-free rate
        d: Dividend yield
    Returns:
        Present value of the forward contract
    """
    F = forward_price(S, T, r, d)
    return np.exp(-r * T) * (F-K)

def digital_call_price(S, K, T, r, d, sigma):
    """
    Price of a digital call option using the Black-Scholes model.
        S: Stock price
        K: Strike price
        T: Time to maturity
        r: Risk-free rate
        d: Dividend yield
        sigma: Volatility
    Returns:
        Price of the digital call option
    """
    d2 = _d2(S, K, T, r, d, sigma)
    return np.exp(-r * T) * norm.cdf(d2)

def digital_put_price(S, K, T, r, d, sigma):
    """
    Price of a digital put option using the Black-Scholes model.
        S: Stock price
        K: Strike price
        T: Time to maturity
        r: Risk-free rate
        d: Dividend yield
        sigma: Volatility
    Returns:
        Price of the digital put option
    """
    d2 = _d2(S, K, T, r, d, sigma)
    return np.exp(-r * T) * norm.cdf(-d2)

