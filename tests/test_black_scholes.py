import black_scholes
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
    # https://personalpages.manchester.ac.uk/staff/paul.johnson-2/pages/blackscholesCalculator.html


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

    # Put-Call Parity: C - P = Se^(-d * T) - K * e^(-r * T)
    assert abs(call_price - put_price - (S*np.exp(-d*T) - K * np.exp(-r * T))) < EPSILON

def test_bs_strike_monotonicity():
    S = 100  # Stock price
    T = 1    # Time to maturity (1 year)
    r = 0.05 # Risk-free rate
    d = 0.02 # Dividend yield
    sigma = 0.2 # Volatility

    K1 = 90
    K2 = 110

    call_price_K1 = black_scholes.call_price(S, K1, T, r, d, sigma)
    call_price_K2 = black_scholes.call_price(S, K2, T, r, d, sigma)

    put_price_K1 = black_scholes.put_price(S, K1, T, r, d, sigma)
    put_price_K2 = black_scholes.put_price(S, K2, T, r, d, sigma)

    assert call_price_K1 > call_price_K2
    assert put_price_K1 < put_price_K2

def test_bs_volatility_monotonicity():
    S = 100  # Stock price
    K = 100  # Strike price
    T = 1    # Time to maturity (1 year)
    r = 0.05 # Risk-free rate
    d = 0.02 # Dividend yield

    sigma1 = 0.2
    sigma2 = 0.3

    call_price_sigma1 = black_scholes.call_price(S, K, T, r, d, sigma1)
    call_price_sigma2 = black_scholes.call_price(S, K, T, r, d, sigma2)

    put_price_sigma1 = black_scholes.put_price(S, K, T, r, d, sigma1)
    put_price_sigma2 = black_scholes.put_price(S, K, T, r, d, sigma2)

    assert call_price_sigma1 < call_price_sigma2
    assert put_price_sigma1 < put_price_sigma2


def test_digital_parity():
    S = 100  # Stock price
    K = 100  # Strike price
    T = 1    # Time to maturity (1 year)
    r = 0.05 # Risk-free rate
    d = 0.02 # Dividend yield
    sigma = 0.2 # Volatility

    digital_call_price = black_scholes.digital_call_price(S, K, T, r, d, sigma)
    digital_put_price = black_scholes.digital_put_price(S, K, T, r, d, sigma) 

    lhs = digital_call_price + digital_put_price
    rhs = np.exp(-r * T)

    assert abs(lhs - rhs) < EPSILON

def test_forward_and_option_parity():
    S = 100  # Stock price
    K = 100  # Strike price
    T = 1    # Time to maturity (1 year)
    r = 0.05 # Risk-free rate
    d = 0.02 # Dividend yield
    sigma = 0.2 # Volatility

    forward_contract_price = black_scholes.forward_contract_price(S, K, T, r, d)
    call_price = black_scholes.call_price(S, K, T, r, d, sigma)
    put_price = black_scholes.put_price(S, K, T, r, d, sigma)

    assert abs(forward_contract_price - (call_price - put_price)) < EPSILON

def test_bs_call_price_convexity_in_strike():
    S = 100  # Stock price
    T = 1    # Time to maturity (1 year)
    r = 0.05 # Risk-free rate
    d = 0.02 # Dividend yield
    sigma = 0.2 # Volatility

    K1 = 90
    K2 = 100
    K3 = 110

    call_price_K1 = black_scholes.call_price(S, K1, T, r, d, sigma)
    call_price_K2 = black_scholes.call_price(S, K2, T, r, d, sigma)
    call_price_K3 = black_scholes.call_price(S, K3, T, r, d, sigma)

    assert call_price_K2 < (call_price_K1 + call_price_K3) / 2
