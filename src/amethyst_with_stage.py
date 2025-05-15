from rate_calculator import rate_calculator
import numpy as np
from scipy.stats import binom, poisson

STAGE = 3
def amethyst_rate_binom(x: int, p: float) -> float: 
    """二項分布模型計算紫水晶特定階段的生長率
    
    階段說明：
    1 = 小芽 (需要1次成功)
    2 = 中芽 (需要2次成功)
    3 = 大芽 (需要3次成功)
    4 = 晶簇 (需要4次成功)
    
    Args:
        x (int): 等待的 tick 數
        p (float): 每 tick 的生長機率 (1/40960)
    
    Returns:
        float: 每 tick 的期望產出率
    """
    if x <= 0:  # 基本檢查
        return 0.0
    
    # 計算在 x 次嘗試中恰好得到 STAGE 次成功的機率
    expected_growth = binom.pmf(STAGE, int(x), p)
    return expected_growth / x

def amethyst_rate_poisson(x: int, p: float) -> float:
    """泊松分布模型計算紫水晶特定階段的生長率"""
    if x <= 0:
        return 0.0
        
    lambda_val = x * p
    if lambda_val <= 0:
        return 0.0
    
    # 計算在平均值為 lambda 的泊松分布下，恰好發生 STAGE 次的機率
    expected_growth = poisson.pmf(STAGE, lambda_val)
    return expected_growth / x

if __name__ == "__main__":
    print("=== 紫水晶生長階段分析 ===")
    
    # 針對每個階段進行分析
    for stage in range(1, 4):
        STAGE = stage
        print(f"\n--- 第 {stage} 階段分析 ---")
        for i in range(1, 100):
            print(f"i: {i}")
            print(f"amethyst_rate_binom: {amethyst_rate_binom(i, 1/40960)/i}")
            print(f"amethyst_rate_poisson: {amethyst_rate_poisson(i, 1/40960)/i}")
        calc = rate_calculator(
            binomial_func=amethyst_rate_binom,
            poisson_func=amethyst_rate_poisson,
            max_ticks=10**6,
            p=1/40960,
            title=f"紫水晶生長分析 - 第 {stage} 階段",
            rate=10**2,
            search_range=1000,
        )
        calc.show()
        # 儲存圖表
        calc.plot()