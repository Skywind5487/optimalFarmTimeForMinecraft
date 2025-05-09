# Tick and Chunk

## Tick

Tick is the smallest unit of time in Minecraft.
Generally, the game runs at 20 ticks per second.

## Block

A block is the basic spatial unit in Minecraft, which is a cube.

## Chunk

A chunk is an area composed of blocks from the void to the build height limit, with a horizontal area of 16 × 16 blocks.

### Subchunk

A chunk is vertically divided into several subchunks from bottom to top, each with a height of 16 blocks, making it 16 × 16 × 16.

## Chunk Tick

For this analysis, we only need to know that chunks are loaded when players are nearby and receive a special tag called chunk tick.

## Random Tick

In each chunk that receives a chunk tick, each of its subchunks randomly selects 3 blocks to receive a random tick.

## Average Random Tick Probability

When selecting 3 blocks from $16^3$ blocks, each block has a probability of $\frac{3}{16^3}$ to receive a random tick in one tick.

## Average Random Tick Period

Since this probability is fixed, independent, and has only two outcomes (occur or not occur), it follows a geometric distribution. Therefore, the expected value is:
$$E(x) = \frac{1}{p} = \frac{16^{3}}{3}$$
This means a block receives a random tick once every $\frac{16^{3}}{3}$ ticks on average, approximately 68.27 seconds. For the median value, please refer to the Tick reference below.

## Next Article

next: [amethyst](amethyst.md)

## References

- [Tick – Minecraft Wiki](https://minecraft.wiki/w/Tick#Random_tick)
- [Block - Minecraft Wiki](https://minecraft.wiki/w/Block)
- [Chunk - Minecraft Wiki](https://minecraft.wiki/w/Chunk)
