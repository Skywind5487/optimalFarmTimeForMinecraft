# Minecraft 紫水晶產率分析

## 先說結果

最佳採收時間為: 2 小時 46 分 36 秒 16 刻（199937 ticks）
每個紫水晶芽床方塊每小時產量(產率)為: 0.517 個碎片

## 問題背景與數學推導

請先閱讀[tick_and_chunk](tick_and_chunk.md)

### 紫水晶生長機制

在 Minecraft 中，紫水晶芽床（budding amethyst）有機會在每 tick 嘗試生長紫水晶芽（bud）。具體條件如下：


- 紫水晶芽床若收到 redstone tick，有 20% 的機率會進行一次 grow 嘗試
- grow 嘗試時，從六個面中隨機選擇一個方向生成芽，機率為1/6
- 紫水晶從完全沒有長芽，到可以被收穫，需要經過 **4 次成功成長**
  - 無芽、小芽、中芽、大芽、晶簇五種狀態
- 成熟後破壞會掉落 2 個紫水晶碎片
  - 機器採收: 2個
  - 玩家以合適工具採收: 4個

### 數學模型建立

#### 基礎機率計算

每次 tick 成功成長的機率計算過程：

1. 隨機tick選中機率：$\frac{3}{16^3}$ (3個隨機tick / 子區塊體積)
2. 成長嘗試機率：$20\%$ (grow嘗試機率)
3. 方向選擇機率：$\frac{1}{6}$ (六個面選一個)

因此總機率為：

```python
p = 3 * (1/16³) * 20% * (1/6) = 1/40960
```

#### 二項分布模型

由於每次發生的機率相同、獨立、只有發生與不發生兩種選擇，因此符合二項分布。

於是，在程式實作中，我們使用二項分布模型計算產率。關鍵思路是：

1. 在x個tick中，成功k次的機率符合二項分布 B(x, p)
2. 要形成晶簇需要至少4次成功
3. 每個晶簇產出2個碎片
4. 產率定義為期望產量除以時間
5. 不計算絕對長不出來的時間，忽略(如1, 2, 3, 4 tick)

因此產率公式為：

$$
\text{產率} = \frac{2 \cdot (1 - P(X \leq 3))}{x}
$$

其中 X ~ B(x, p)。在代碼中的實現：

```python
def binomial_yield(x):
    P_leq_3 = binom.cdf(3, int(x), p)  # P(X ≤ 3)
    expected_fragments = 2 * (1 - P_leq_3)  # 期望碎片數
    return expected_fragments / x  # 產率
```

#### 泊松分布模型

當 x 很大且 p 很小時，二項分布可以用泊松分布近似。在這種情況下：

1. λ = xp（期望成功次數）
2. P(X = k) = e^(-λ)λ^k/k!

程式實作：

```python
def poisson_yield(x):
    lambda_val = x * p  # 期望值
    P_leq_3 = poisson.cdf(3, lambda_val)  # P(X ≤ 3)
    expected_fragments = 2 * (1 - P_leq_3)
    return expected_fragments / x
```

## 數值分析結果

### Python程式實作結果

程式使用數值方法找到了最佳產率時間點：

- 二項分布模型：
  - 最大產率：0.000007181 碎片/tick
  - 最佳時間：166 分 36 秒 16 刻（199937 ticks）
- 泊松分布模型：
  - 最大產率：0.000007181 碎片/tick
  - 最佳時間：166 分 36 秒 16 刻（199937 ticks）

轉換為每小時產率：

$$
0.000007181 \cdot 20 \cdot 60 \cdot 60 \approx 0.517 \text{ 碎片/小時}
$$

## 程式實作細節

### 核心參數設定

```python
p = 1 / 40960  # 每 tick 成功成長的機率
max_ticks = 10**6  # 最大 tick 數範圍
x_values = np.linspace(1, max_ticks, max_ticks//10**2)
```

### 優化

1. 使用 NumPy 的向量化操作
2. 採用 linspace 減少計算點數
3. 利用 SciPy 的高效統計函數
4. 以斜率取極值，並在其附近區間搜索離散點確保準確性

## 結論

1. 二項分布和泊松分布給出幾乎完全相同的結果，證實了在 n 大 p 小時泊松近似的有效性
2. 最佳等待時間約為 166.6 分鐘（199937 ticks）
3. 在最佳時間點，每個紫水晶芽床點位的理論最大產率約為 0.517 碎片/小時

## 下一篇

next: [sugar_cane](sugar_cane.md)

## 參考資料

- [Budding Amethyst – Minecraft Wiki](https://minecraft.wiki/w/Budding_Amethyst/#Usage)
- [Tick – Minecraft Wiki](https://minecraft.wiki/w/Tick#Random_tick)
- [1.17 Shard Farming: Doing The Crystal Math - YouTube](https://youtu.be/H3bCCANEbbQ?t=502)
