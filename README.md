# Applied Economics 投稿全流程助手

基于 **Applied Economics**（Taylor & Francis SSCI 期刊）已发表论文萃取的投稿助手 Skill。支持**全文结构重组**和**章节语言改写**双轨工作流。

## 核心能力

```
用户输入
    │
    ▼
┌─────────────────────────────────┐
│ STEP 0: 任务类型自动判断         │
│ 全文投稿 ←→ 章节改写            │
│ → 输出判断结果，用户确认         │
└─────────────────────────────────┘
    │
    ├── 全文投稿
    │   ├── 提取当前章节结构
    │   ├── 匹配 5 种 AE 结构模板
    │   ├── 生成重组大纲 → 用户确认
    │   └── 逐章语言改写（6 维规范）
    │
    └── 章节改写
        ├── RAG 检索 AE 范本
        ├── 读取对应章节规范
        └── 6 维语言改写 → 验收
```

### 5 种 AE 期刊结构模板

| # | 模板 | 章节序列 | 适用场景 |
|---|---|---|---|
| T1 | 完整八章型 | abs→intro→LR→model→data→results→robust→concl | 理论+实证完整论文 |
| T2 | 标准实证型 | abs→intro→data→results→(robust)→concl | **最常见**，LR 嵌入引言 |
| T3 | 模型驱动型 | abs→intro→LR→model→data→concl | 宏观/财政，重理论推导 |
| T4 | 数据简报型 | abs→intro→data→results | 短通讯，数据驱动 |
| T5 | 稳健导向型 | abs→intro→data→results→robust→concl | 因果识别，IV/DiD/RDD |

### 8 章节 × 6 维语言改写

| 维度 | 内容 |
|---|---|
| 结构逻辑 | 章节内标准信息序列 |
| 段落排布 | 段落长度、密度、断点 |
| 开篇/结尾句式 | 高频句式模板 |
| 学术用词 | 高频 trigram、hedging、引用动词 |
| 语态时态 | 主动/被动比例、时态分布 |
| 衔接方式 | 过渡词频次、段落衔接策略 |

### 数据完整性硬约束

- **零虚构**：禁止捏造任何数据、系数、文献、事实
- **可追溯**：所有外来引用必须来自稿件内交叉引用 / RAG 检索 / 用户提供
- **溯源标注**：每个外部信息带 `[Source: ...]` 标签

## 快速安装

```bash
git clone git@github.com:ww11-max/applied-economics-rewrite-skill.git
cd applied-economics-rewrite-skill
python install.py
```

重启 Claude Code 后使用 `/applied-economics-rewrite` 调用。

## 使用示例

```bash
# 全文投稿 — 自动判断为全文，匹配结构模板，生成重组大纲
/applied-economics-rewrite @my_paper.md

# 章节改写 — 自动判断为章节，直接进行语言改写
/applied-economics-rewrite "This study examines the impact of monetary policy..."
/applied-economics-rewrite abstract @my_abstract.txt
```

## 仓库结构

| 目录/文件 | 说明 |
|---|---|
| `skill/SKILL.md` | Claude Code Skill（双轨工作流） |
| `norms/applied_economics_style_skill.md` | 完整规范：结构库 + 8 章 × 6 维 |
| `rag_retriever.py` | RAG 检索器（按章节类型过滤） |
| `data/` | 预构建向量库（FAISS 索引） |
| `install.py` | 一键安装脚本 |

## 支持的章节类型

| 类型 | 标识 |
|---|---|
| 摘要 | `abstract` |
| 引言 | `introduction` |
| 文献综述 | `literature_review` |
| 理论模型 | `theoretical_model` |
| 数据与变量 | `data_and_variables` |
| 实证结果 | `empirical_results` |
| 稳健性检验 | `robustness` |
| 结论 | `conclusion` |

## 依赖

- Python 3.9+
- sentence-transformers
- faiss-cpu
- numpy

`install.py` 自动安装所有依赖。

## 许可

MIT
