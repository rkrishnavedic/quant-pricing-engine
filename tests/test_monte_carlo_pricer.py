from models import GeometricBrownianMotion
from pricers import MonteCarloPricer
from options import EuropeanCallOption
from black_scholes import black_scholes
from random_numbers import NumpyRNG


def test_mc_call_price_matches_black_scholes():
    # Market parameters
    S0 = 100.0
    K = 100.0
    T = 1.0
    r = 0.05
    d = 0.02
    sigma = 0.2

    # Monte Carlo setup
    n_paths = 100_000
    rng = NumpyRNG(seed=7) # For reproducibility

    # Create model
    model = GeometricBrownianMotion(
        S0=S0,
        r=r,
        d=d,
        sigma=sigma,
        rng=rng
    )

    # Create option
    option = EuropeanCallOption(strike=K)

    # Create pricer
    pricer = MonteCarloPricer(model)

    # Monte Carlo estimate
    mc_result = pricer.price(
        option=option,
        T=T,
        n_paths=n_paths,
        r=r
    )

    mc_price = mc_result["price"]
    std_error = mc_result["std_error"]

    # Analytical BS price
    bs_price = black_scholes.call_price(
        S=S0,
        K=K,
        T=T,
        r=r,
        d=d,
        sigma=sigma
    )

    # Statistical validation
    assert abs(mc_price - bs_price) < 3 * std_error # # Approximate 3-sigma statistical tolerance