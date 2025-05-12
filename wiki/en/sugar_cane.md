# Minecraft Sugar Cane Production Rate Analysis

## Summary

Optimal harvesting time: 41 minutes 2 seconds 13 ticks (49,253 ticks)
Hourly production rate per sugar cane position: 2.6 sugar canes

## Background and Mathematical Analysis

Please read [tick_and_chunk](tick_and_chunk.md) first.

### Sugar Cane Growth Mechanism

In Minecraft, sugar cane growth has the following characteristics:

1. Each sugar cane has a chance to attempt growth every tick, but only the top sugar cane can grow
2. A single sugar cane position can grow up to three blocks high
3. Different heights yield different amounts when harvested:
   - 1 block high: no harvest (preserve)
   - 2 blocks high: harvest 1
   - 3 blocks high: harvest 2

### Mathematical Model Development

Since the probability of receiving a random tick at the top is the same as at the bottom, we can simplify the problem to counting successful ticks at the bottom.

#### Basic Probability Calculation

Random tick selection probability: $\frac{3}{16^3}$ (3 random ticks / subchunk volume), defined as one success.

Therefore, the total probability is:

```python
p = 3 / (16³)
```

#### Binomial Distribution Model

Since each event has the same probability, is independent, and has only two outcomes, it follows a binomial distribution. In implementation:

1. Define probabilities for different heights:
    - P0: Probability of staying 1 block high (0-15 successes)
        - Harvest = 0
    - P1: Probability of reaching 2 blocks high (16-31 successes)
        - Harvest = 1
    - P2: Probability of reaching 3 blocks high (32+ successes)
        - Harvest = 2

2. Calculate expected yield:
   ```python
   expected_yield = P1 * 1 + P2 * 2
   ```

3. Calculate production rate:
   ```python
   rate = expected_yield / time
   ```

#### Poisson Distribution Model

When x is large and p is small, the binomial distribution can be approximated by a Poisson distribution:

1. λ = xp (expected number of successes)
2. Use the same logic to calculate P0, P1, P2
3. Calculation method same as binomial distribution

## Numerical Analysis Results

### Python Implementation Results

The program found the optimal production rate point:

- Binomial Distribution Model:
  - Maximum rate: 0.000036 sugar cane/tick
  - Optimal time: 41 minutes 2 seconds 13 ticks (49,253 ticks)
- Poisson Distribution Model:
  - Maximum rate: 0.000036 sugar cane/tick
  - Optimal time: 41 minutes 2 seconds 13 ticks (49,253 ticks)

Converting to hourly rate:

```
0.000036 * 20 * 60 * 60 ≈ 2.6 sugar canes/hour
```

## Implementation Details

### Core Parameters

```python
p = 3 / (16 ** 3)  # Probability of successful growth per tick
max_ticks = 10**5   # Maximum time range
```

## Problems
We treat x times as one cycle and assume it starts counting from the beginning each time. This works for amethyst but not for sugar cane.
Because we don't break the bottom block of the sugar cane, which means the previous growth state might be preserved. This makes our calculation incorrect.

## Conclusions

1. Binomial and Poisson distributions yield identical results
2. Optimal waiting time is approximately 41 minutes (49,253 ticks)
3. At optimal time, the theoretical maximum production rate per sugar cane position is about 2.6 per hour
4. Compared to amethyst, sugar cane grows much faster (amethyst is about 0.517 per hour)

## Previous Article

previous: [amethyst](amethyst.md)

## References

- [Sugar Cane – Minecraft Wiki](https://minecraft.wiki/w/Sugar_Cane)
- [Tick – Minecraft Wiki](https://minecraft.wiki/w/Tick#Random_tick)
