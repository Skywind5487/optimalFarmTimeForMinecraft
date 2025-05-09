# Tick and Chunk

## Tick

tick 是 Minecraft 運行時的最小時間單位。
通常來說，遊戲以 20 個 tick 為一秒。

## 方塊 block

方塊是 Minecraft 中的基本空間單位，為一個正立方體。

## 區塊 chunk

區塊是由世界虛空到建築高度上限、水平 16 * 16 的方塊組成的區域。

### 子區塊 subchunk

一個 chunk 由下到上會分成數個高為 16 的 subchunk，即 16 * 16 * 16。

## 區塊刻 chunk tick

在本次推導中，僅需要知道玩家靠近等等方法會載入區塊，並給予區塊一個特殊的標籤，稱為區塊刻。

## 隨機刻 random tick

在每一個接收到區塊刻的區塊中，其每個 subchunk 都會隨機選擇 3 個 方塊得到 random tick。

## 平均隨機刻機率

在 $16^{3}$ 中選 $3$ 個，即每個方塊在一刻內有 $\frac{3}{16^{3}}$ 的機率收到隨機刻。

## 平均隨機刻週期

由於這個這個機率機率固定、每次獨立、只有發生或不發生，符合幾何分布，因此期望值即為 $$E(x) = \frac{1}{p} = \frac{16^{3}}{3}$$
即平均$\frac{16^{3}}{3}$刻會收到隨機刻一次，大約 68.27 秒。中位數可以參見底下的 Tick 參考資料。

# 下一篇
next: [amethyst](amethyst.md)

## 參考資料

- [Tick – Minecraft Wiki](https://minecraft.wiki/w/Tick#Random_tick)
- [Block - Minecraft Wiki](https://minecraft.wiki/w/Block)
- [Chunk - Minecraft Wiki](https://minecraft.wiki/w/Chunk)
