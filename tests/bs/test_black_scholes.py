from bs import black_scholes
import numpy as np

EPSILON = 1e-4

def test_bs():
    S = 100  # Stock price
    K = 100  # Strike price
    T = 1    # Time to maturity (1 year)
    r = 0.05 # Risk-free rate
    sigma = 0.2 # Volatility

    call_price = black_scholes.call_price(S, K, T, r, d=0, sigma=sigma)
    put_price = black_scholes.put_price(S, K, T, r, d=0, sigma=sigma)

    assert abs(call_price - 10.45058) < EPSILON
    assert abs(put_price - 5.573526) < EPSILON


def test_bs_with_dividend():
    S = 100  # Stock price
    K = 100  # Strike price
    T = 1    # Time to maturity (1 year)
    r = 0.05 # Risk-free rate
    d = 0.02 # Dividend yield
    sigma = 0.2 # Volatility

    call_price = black_scholes.call_price(S, K, T, r, d, sigma)
    put_price = black_scholes.put_price(S, K, T, r, d, sigma)

    assert abs(call_price - 9.22700) < EPSILON
    assert abs(put_price - 6.33008) < EPSILON

def test_bs_put_call_parity():
    S = 100  # Stock price
    K = 100  # Strike price
    T = 1    # Time to maturity (1 year)
    r = 0.05 # Risk-free rate
    d = 0.02 # Dividend yield
    sigma = 0.2 # Volatility

    call_price = black_scholes.call_price(S, K, T, r, d, sigma)
    put_price = black_scholes.put_price(S, K, T, r, d, sigma)

    # Put-Call Parity: C - P = S - K * e^(-r * T)
    assert abs(call_price - put_price - (S*np.exp(-d*T) - K * np.exp(-r * T))) < EPSILON