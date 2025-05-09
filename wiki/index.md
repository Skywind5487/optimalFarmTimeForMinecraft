# Minecraft 農場最佳化分析 / Minecraft Farm Optimization Analysis

這個專案分析了 Minecraft 中不同作物和資源的最佳採收時間。
This project analyzes the optimal harvesting time for different crops and resources in Minecraft.

## 目錄 / Table of Contents

### 基礎概念 / Basic Concepts

- [Tick and Chunk (英文)](en/tick_and_chunk.md)
- [Tick and Chunk (中文)](zh_tw/tick_and_chunk.md)

### 資源分析 / Resource Analysis

#### 紫水晶 / Amethyst

- [Amethyst Analysis (英文)](en/amethyst.md)
- [紫水晶分析 (中文)](zh_tw/amethyst.md)

#### 甘蔗 / Sugar Cane

- [Sugar Cane Analysis (英文)](en/sugar_cane.md)
- [甘蔗分析 (中文)](zh_tw/sugar_cane.md)

## 閱讀順序 / Reading Order

1. Tick and Chunk（基礎概念 / Basic concepts）
2. 紫水晶分析 / Amethyst Analysis
3. 甘蔗分析 / Sugar Cane Analysis

## 主要結論 / Key Findings

### 紫水晶 / Amethyst

- 最佳採收時間 / Optimal harvesting time: 2h 46m 36s 16t (199,937 ticks)
- 每小時產量 / Hourly yield: 0.517 shards/hour

### 甘蔗 / Sugar Cane

- 最佳採收時間 / Optimal harvesting time: 41m 2s 13t (49,253 ticks)
- 每小時產量 / Hourly yield: 2.6 sugar canes/hour

## 程式碼 / Source Code

所有分析都使用 Python 實現，源代碼位於 `src/` 目錄下：
All analyses are implemented in Python, with source code located in the `src/` directory:

- `rate_class.py`: 通用產率計算器 / Generic rate calculator
- `amethyst.py`: 紫水晶分析 / Amethyst analysis
- `sugar_cane.py`: 甘蔗分析 / Sugar cane analysis