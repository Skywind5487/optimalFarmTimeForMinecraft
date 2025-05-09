from rate_calculator import rate_calculator
import numpy as np
from scipy.stats import binom, poisson

def amethyst_yield_binom(x: int, p: float) -> float:
    """Binomial distribution model for calculating amethyst shard yield rate
    
    The model assumes:
    - Small buds grow to medium buds with probability p per tick
    - Medium buds grow to large buds with same probability
    - Large buds grow to clusters with same probability
    - Clusters drop 2 shards when broken
    
    Args:
        x (int): Number of ticks to wait before harvesting
        p (float): Probability of successful growth tick (1/40960 for amethyst)
    
    Returns:
        float: Expected yield rate in shards per tick
    """
    P_leq_3 = binom.cdf(3, int(x), p)     # Probability of ≤3 growth events
    expected_fragments = 2 * (1 - P_leq_3) # Expected number of shards
    return expected_fragments / x

def amethyst_yield_poisson(x: int, p: float) -> float:
    """Poisson distribution model for calculating amethyst shard yield rate
    
    Similar to binomial model but uses Poisson approximation:
    - Assumes rare events (growth) over many trials
    - Uses λ = np as the mean number of events
    
    Args:
        x (int): Number of ticks to wait before harvesting
        p (float): Probability of successful growth tick (1/40960 for amethyst)
    
    Returns:
        float: Expected yield rate in shards per tick
    """
    lambda_val = x * p                     # Mean number of growth events
    P_leq_3 = poisson.cdf(3, lambda_val)  # Probability of ≤3 events
    expected_fragments = 2 * (1 - P_leq_3) # Expected number of shards
    return expected_fragments / x

if __name__ == "__main__":
    # Initialize calculator with amethyst parameters
    calc = rate_calculator(
        binomial_func=amethyst_yield_binom,
        poisson_func=amethyst_yield_poisson,
        max_ticks=10**6,
        p=1/40960,  # Amethyst bud growth probability
        title="Amethyst Growth Rate Analysis"
    )
    
    # Display results and plot
    calc.show()
    calc.plot()