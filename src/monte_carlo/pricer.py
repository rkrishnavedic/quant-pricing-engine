from random_numbers import NumpyRNG
import numpy as np

class MonteCarloPricer:
    def __init__(self, model):
        self.model = model
    
    def price(self, option, T, n_paths, r):
        """
        Price an option using Monte Carlo simulation.
            option: An instance of an Option subclass
            T: Time to maturity
            n_paths: Number of Monte Carlo paths to simulate
            r: Risk-free rate
        Returns:
            Estimated option price
        """
        # Simulate terminal stock prices
        S_T = self.model.simulate_terminal(T, n_paths)
        
        # Calculate payoffs for each path
        payoffs = option.payoff(S_T)
        
        # Discount payoffs back to present value
        discounted_payoffs = payoffs * np.exp(-r * T)

        # Calculate the Monte Carlo price as the average of discounted payoffs
        price = np.mean(discounted_payoffs)

        # Calculate standard error
        variance = np.var(discounted_payoffs, ddof=1)  # Sample variance, ddof=1 for unbiased estimator
        std_error = np.sqrt(variance / n_paths)
        
        return {
            'price': price,
            'std_error': std_error,
            'variance': variance
        }
