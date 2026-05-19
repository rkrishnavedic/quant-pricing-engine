from pricers import MonteCarloPricer
from black_scholes import black_scholes
from models import GeometricBrownianMotion
from options import EuropeanCallOption
import numpy as np
from random_numbers import NumpyRNG


def compare_european_call_pricing_methods(S0, K, T, r, d, sigma, n_paths=100_000, seed=7):
    option = EuropeanCallOption(strike=K)

    # Analytical BS price
    bs_price = black_scholes.call_price(S=S0, K=K, T=T, r=r, d=d, sigma=sigma)

    # Monte Carlo setup
    rng = NumpyRNG(seed=seed) # For reproducibility
    model = GeometricBrownianMotion(
        S0=S0,
        r=r,
        d=d,
        sigma=sigma,
        rng=rng
    )
    mc_pricer = MonteCarloPricer(model)
    mc_result = mc_pricer.price(
        option=option,
        T=T,
        n_paths=n_paths,
        r=r
    )
    mc_price = mc_result["price"]
    mc_std_error = mc_result["std_error"]

    return {
        "bs_price": bs_price,
        "mc_price": mc_price,
        "mc_std_error": mc_std_error,
        "abs_error": abs(bs_price - mc_price)
    }
