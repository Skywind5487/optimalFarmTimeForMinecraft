# Minecraft 最佳農場時間分析 / Minecraft Optimal Farm Time Analysis

這個專案分析了 Minecraft 中不同資源的生長和收穫機制，以計算出最佳的採收時間。主要使用二項分布和泊松分布進行建模分析。

This project analyzes the growth and harvesting mechanics of different resources in Minecraft to calculate optimal harvesting times. It primarily uses binomial and Poisson distributions for modeling and analysis.

## 📊 目前分析結果 / Current Analysis Results

### 紫水晶 Amethyst

- 最佳採收時間 / Optimal harvesting time: 2h 46m 36s 16t (199,937 ticks)
- 每小時產量 / Hourly yield: 0.517 shards/hour

### 甘蔗 Sugar Cane

- 最佳採收時間 / Optimal harvesting time: 41m 2s 13t (49,253 ticks)
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
```bash
pip install -r requirements.txt
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

- 補充更多農場範例 / Add more farm examples
- 研究飛行器來回對產率的影響 / Study the impact of return flight paths on rates
- 分析更多可耕種物品 / Analyze more farmable items:
  - 作物 / Crops
  - 蘑菇 / Mushrooms
  - 仙人掌、海帶、竹子等 / Cacti, kelp, bamboo, etc.
  - 草方塊 / Grass blocks
  - 海龜蛋 / Turtle eggs
  - 鐘乳石 / Pointed dripstone

## 💡 貢獻 / Contributing

歡迎提供改進建議或提交 Pull Request。
Suggestions for improvements or pull requests are welcome.

## 📄 授權 / License

本專案採用 MIT 授權條款 - 詳見 LICENSE 文件。
This project is licensed under the MIT License - see the LICENSE file for details.