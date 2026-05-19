from .bs_vs_mc import compare_european_call_pricing_methods

# For Black-Scholes vs Monte Carlo convergence experiment
def run_call_convergence_experiment():
    """
    for each path count:
        - run MC pricing
        - compare with BS
        - store metrics
    """
    results = []

    for power in range(10, 20):  # From 2^10 to 2^19 paths

        n_paths = 2 ** power

        # compare BS vs MC
        metrics = compare_european_call_pricing_methods(
            S0=100.0,
            K=100.0,
            T=1.0,
            r=0.05,
            d=0.02,
            sigma=0.2,
            n_paths=n_paths,
            seed=7
        )

        results.append({
            "n_paths": n_paths,
            **metrics
        })

    return results