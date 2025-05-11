# Minecraft 最佳農場時間分析 / Minecraft Optimal Farm Time Analysis

這個專案分析了 Minecraft 中不同資源的生長和收穫機制，以計算出最佳的採收時間。主要使用二項分布和泊松分布進行建模分析。

This project analyzes the growth and harvesting mechanics of different resources in Minecraft to calculate optimal harvesting times. It primarily uses binomial and Poisson distributions for modeling and analysis.

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/Skywind5487/optimalFarmTimeForMinecraft)

## 📊 目前分析結果 / Current Analysis Results

### 紫水晶 Amethyst

- 最佳採收時間 / Optimal harvesting time: 2h 46m 36s 16tick (199,937 ticks)
- 每小時產量 / Hourly yield: 0.517 shards/hour

### 甘蔗 Sugar Cane

- 最佳採收時間 / Optimal harvesting time: 41m 2s 13tick (49,253 ticks)
- 每小時產量 / Hourly yield: 2.6 sugar canes/hour

## 📚 詳細文檔 / Detailed Documentation

完整的分析和說明請參考 wiki 文件：
For complete analysis and explanation, please refer to the wiki documents:

- [目錄 | index](wiki/index.md)

## 為什麼選擇這些資源？/ Why These Resources?

### 研究對象 / Research Subjects

- 紫水晶 / Amethyst
- 甘蔗 / Sugar Cane

### 選擇原因 / Selection Reasons

1. 生長時間較長 / Long growth time
2. 無法使用骨粉加速 / Cannot be sped up with bone meal
3. 需要精確的計時收割 / Require precise timing for harvesting

## 🛠️ 技術實現 / Technical Implementation

- **語言 / Language**: Python
- **主要套件 / Main Packages**:
  - NumPy: 數值計算 / Numerical computation
  - SciPy: 統計分析 / Statistical analysis

## 📁 專案結構 / Project Structure

```
src/
├── amethyst.py           # 紫水晶分析 / Amethyst analysis
├── sugar_cane.py         # 甘蔗分析 / Sugar cane analysis
└── rate_calculator.py    # 通用計算器 / Generic calculator

wiki/
├── en/                   # 英文文檔 / English documentation
└── zh_tw/               # 中文文檔 / Chinese documentation
```


## 🚀 開始使用 / Getting Started

1. 安裝依賴 / Install dependencies:
use pip

```bash
pip install -r requirements.txt
```

or use uv

```bash
uv venv
uv sync
```

2. 運行分析 / Run analysis:

```bash
python src/amethyst.py    # 分析紫水晶 / Analyze amethyst
python src/sugar_cane.py  # 分析甘蔗 / Analyze sugar cane
```

## 📈 計算原理 / Calculation Principles

本專案使用以下統計模型：
This project uses the following statistical models:

- **二項分布 / Binomial Distribution**: 適用於精確計算 / For exact calculations
- **泊松分布 / Poisson Distribution**: 用於大量樣本近似 / For large sample approximations

## 🔜 未來計劃 / Future Plans

- 補充更多農場範例 / Add more farm designs
- 研究甘蔗的初始值問題(見[doc](wiki/zh_tw/sugar_cane.md#問題)) / Investigate the initial state problem of sugar cane growth(see [doc](wiki/en/sugar_cane.md#problems))
- 研究飛行器返回路徑對產率的影響 / Analyze how return flight paths affect efficiency
- 擴展耕種物品分析 / Expand analysis of farmable items:
    - 傳統作物（小麥、馬鈴薯等）/ Crops (wheat, potatoes, etc.)
    - 菇類植物 / Mushrooms
    - 特殊植物：仙人掌、海帶、竹子、紫頌花、紅樹胎生苗、甜莓叢
        - Special blocks: Cactus, kelp, bamboo, chorus flowers, mangrove propagules, sweet berries
    - 特殊自然方塊：草方塊、海龜蛋、鐘乳石
        -  Natural blocks: grass blocks, turtle eggs, dripstone

## 💡 貢獻 / Contributing

歡迎提供改進建議或提交 Pull Request。
Suggestions for improvements or pull requests are welcome.

## 📄 授權 / License

本專案採用 MIT 授權條款 - 詳見 LICENSE 文件。
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgement

Imango [1.17 Shard Farming: Doing The Crystal Math - YouTube](https://youtu.be/H3bCCANEbbQ?t=502)
Which inspired me to do this, as we obtained very similar results in the end.

My friend @Youhe inspired me to start this project and try modeling it with a binomial distribution.

