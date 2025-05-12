from rate_calculator import rate_calculator
from scipy.stats import binom, poisson

def sugarcane_rate_binom(x: int, p: float) -> float:
    """Binomial distribution model for calculating sugar cane rate rate
    
    The model considers three possible heights:
    - Height 1: 0 drops (when growth count <= 15)
    - Height 2: 1 drop (when 15 < growth count <= 31)
    - Height 3: 2 drops (when growth count > 31)
    
    Args:
        x (int): Number of ticks to wait before harvesting
        p (float): Probability of successful growth tick (3/4096 for sugar cane)
    
    Returns:
        float: Expected rate rate in items per tick
    """
    P0      = binom.cdf(15, int(x), p)    # Height=1, 0 drops
    cdf_31  = binom.cdf(31, int(x), p)    # Intermediate threshold
    P1      = cdf_31 - P0                 # Height=2, 1 drop
    P2      = 1 - cdf_31                  # Height=3, 2 drops
    expected = P1 + 2 * P2                # Expected rate
    return expected / x

def sugarcane_rate_poisson(x: int, p: float) -> float:
    """Poisson distribution model for calculating sugar cane rate rate
    
    Similar to binomial model but uses Poisson approximation:
    - Height 1: 0 drops (x ≤ 15)
    - Height 2: 1 drop (15 < x ≤ 31)
    - Height 3: 2 drops (x > 31)
    
    Args:
        x (int): Number of ticks to wait before harvesting
        p (float): Probability of successful growth tick (3/4096 for sugar cane)
    
    Returns:
        float: Expected rate rate in items per tick
    """
    lam     = x * p                       # λ = np (mean number of events)
    P0      = poisson.cdf(15, lam)        # Height=1, 0 drops
    cdf_31  = poisson.cdf(31, lam)        # Intermediate threshold
    P1      = cdf_31 - P0                 # Height=2, 1 drop
    P2      = 1 - cdf_31                  # Height=3, 2 drops
    expected = P1 + 2 * P2                # Expected rate
    return expected / x

if __name__ == "__main__":
    # Initialize calculator with sugar cane parameters
    calc:rate_calculator = rate_calculator(
        binomial_func=sugarcane_rate_binom,
        poisson_func=sugarcane_rate_poisson,
        max_ticks=10**5,
        p=3/(16**3),  # Sugar cane growth probability (3/4096)
        title="Sugar Cane Growth Rate Analysis"
    )
    
    # Display results and plot
    #calc.save_plot("sugar_cane_growth_rate.png")
    calc.show()
    calc.plot()