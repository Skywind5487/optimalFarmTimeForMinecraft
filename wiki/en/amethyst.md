# Minecraft Amethyst Production Rate Analysis

## Summary

Optimal harvesting time: 2 hours 46 minutes 36 seconds 16 ticks (199,937 ticks)
Hourly production rate per budding amethyst block: 0.517 shards

## Background and Mathematical Analysis

Please read [tick_and_chunk](tick_and_chunk.md) first.

### Amethyst Growth Mechanism

In Minecraft, budding amethyst has a chance to attempt growing amethyst buds each tick. The specific conditions are:

- When a budding amethyst receives a redstone tick, there's a 20% chance it will attempt to grow
- During a growth attempt, one direction is randomly chosen from six faces, with a probability of 1/6
- An amethyst cluster requires **4 successful growth stages** from no bud to harvestable
  - Five states: no bud, small bud, medium bud, large bud, cluster
- When mature, breaking yields 2 amethyst shards
  - Machine harvesting: 2 shards
  - Player harvesting with appropriate tools: 4 shards

### Mathematical Model Development

#### Basic Probability Calculation

The probability of successful growth per tick is calculated as follows:

1. Random tick selection probability: $\frac{3}{16^3}$ (3 random ticks / subchunk volume)
2. Growth attempt probability: $20\%$ (grow attempt chance)
3. Direction selection probability: $\frac{1}{6}$ (one of six faces)

Therefore, the total probability is:

```python
p = 3 * (1/16³) * 20% * (1/6) = 1/40960
```

#### Binomial Distribution Model

Since each event has the same probability, is independent, and has only two outcomes, it follows a binomial distribution.

In the implementation, we calculate the production rate using a binomial distribution model. The key concepts are:

1. The probability of k successes in x ticks follows B(x, p)
2. A cluster requires at least 4 successes
3. Each cluster yields 2 shards
4. Production rate is defined as expected yield divided by time
5. Ignoring impossible growth times (e.g., 1, 2, 3, 4 ticks)

Thus, the production rate formula is:

$$
\text{Rate} = \frac{2 \cdot (1 - P(X \leq 3))}{x}
$$

where X ~ B(x, p). Implementation in code:

```python
def binomial_yield(x):
    P_leq_3 = binom.cdf(3, int(x), p)  # P(X ≤ 3)
    expected_fragments = 2 * (1 - P_leq_3)  # Expected shard count
    return expected_fragments / x  # Rate
```

#### Poisson Distribution Model

When x is large and p is small, the binomial distribution can be approximated by a Poisson distribution:

1. λ = xp (expected number of successes)
2. P(X = k) = e^(-λ)λ^k/k!

Implementation:

```python
def poisson_yield(x):
    lambda_val = x * p  # Expected value
    P_leq_3 = poisson.cdf(3, lambda_val)  # P(X ≤ 3)
    expected_fragments = 2 * (1 - P_leq_3)
    return expected_fragments / x
```

## Numerical Analysis Results

### Python Implementation Results

The program found the optimal production rate point:

- Binomial Distribution Model:
  - Maximum rate: 0.000007181 shards/tick
  - Optimal time: 166 minutes 36 seconds 16 ticks (199,937 ticks)
- Poisson Distribution Model:
  - Maximum rate: 0.000007181 shards/tick
  - Optimal time: 166 minutes 36 seconds 16 ticks (199,937 ticks)

Converting to hourly rate:

$$
0.000007181 \cdot 20 \cdot 60 \cdot 60 \approx 0.517 \text{ shards/hour}
$$

## Implementation Details

### Core Parameters

```python
p = 1 / 40960  # Probability of successful growth per tick
max_ticks = 10**6  # Maximum tick range
x_values = np.linspace(1, max_ticks, max_ticks//10**2)
```

### Optimizations

1. Using NumPy's vectorized operations
2. Reducing computation points using linspace
3. Utilizing SciPy's efficient statistical functions
4. Finding extrema using slope and searching nearby discrete points for accuracy

## Conclusions

1. Binomial and Poisson distributions yield nearly identical results, confirming the validity of Poisson approximation when n is large and p is small
2. Optimal waiting time is approximately 166.6 minutes (199,937 ticks)
3. At optimal time, the theoretical maximum production rate per budding amethyst block is about 0.517 shards/hour

## Next Article

next: [sugar_cane](sugar_cane.md)

## References

- [Budding Amethyst – Minecraft Wiki](https://minecraft.wiki/w/Budding_Amethyst/#Usage)
- [Tick – Minecraft Wiki](https://minecraft.wiki/w/Tick#Random_tick)
- [1.17 Shard Farming: Doing The Crystal Math - YouTube](https://youtu.be/H3bCCANEbbQ?t=502)
