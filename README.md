# Applied Economics Rewrite Skill

基于 **Applied Economics**（Taylor & Francis SSCI 期刊）已发表论文萃取的写作规范 Skill，用于将经济学论文初稿改写为 AE 期刊投稿标准。

## 快速安装

```bash
git clone <this-repo-url>
cd applied-economics-rewrite-skill
python install.py
```

安装完成后，重启 Claude Code，使用 `/applied-economics-rewrite` 调用。

## 包含内容

| 目录/文件 | 说明 |
|---|---|
| `skill/SKILL.md` | Claude Code Skill 模板文件 |
| `norms/applied_economics_style_skill.md` | 完整写作规范（7章节×6维度） |
| `rag_retriever.py` | 独立 RAG 检索器 |
| `data/` | 预构建向量库（FAISS 索引） |
| `install.py` | 一键安装脚本 |

## 使用方式

### Claude Code Skill

```
/applied-economics-rewrite abstract "This study examines the impact of..."
/applied-economics-rewrite introduction @my_draft.md
```

Skill 自动：识别章节 → RAG 检索相似范文 → 对照6维规范改写 → 验收。

### 独立 RAG 检索

```bash
python rag_retriever.py --chapter-type introduction --top-k 5 --query "your text"
python rag_retriever.py --stats
```

## 支持的章节类型

| 类型 | 标识 |
|---|---|
| 摘要 | `abstract` |
| 引言 | `introduction` |
| 文献综述 | `literature_review` |
| 理论模型 | `theoretical_model` |
| 数据与变量 | `data_and_variables` |
| 实证结果 | `empirical_results` |
| 稳健性 | `robustness` |
| 结论 | `conclusion` |

## 依赖

- Python 3.9+
- sentence-transformers
- faiss-cpu
- numpy

`install.py` 会自动安装所有依赖。

## 许可

MIT
