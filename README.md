# 📄 AI 文档生成检测工具

本项目致力于构建一个高准确率的 AI 文档生成识别系统，支持快速检测文本是否由大语言模型（LLM）生成，适用于风控审核、内容把关、模型更换检测等业务场景。

---

## 🚀 项目特性

* ✅ **支持多种检测策略**（BERT、BERTScore、LLM 语义比对）
* ⚡ **检测速度快**（100 条 Case 最快 1 分钟完成）
* 🎯 **高准确率**（离线评估达 97.8%，线上灰度达 94.7%）
* 📊 **语义+风格双维度分析**
* 🔁 **可用于模型切换监控与误报率巡检**

---

## 📦 安装与环境依赖

```bash
# 建议使用 Python 3.9+
conda create -n ai-detector python=3.9
conda activate ai-detector

# 安装依赖
pip install -r requirements.txt
```

依赖项（部分）：

* `transformers`（用于加载 BERT、LLM）
* `bert-score`（用于快速语义比对）
* `openai` or `vllm`（用于调用 LLM）
* `pandas` / `numpy` / `tqdm`（数据处理和进度显示）

---

## ⚙️ 快速开始

### 1. 离线检测（语义+风格）

```bash
python detect_offline.py --input data/test_cases.json --output result.json
```

### 2. 使用大模型进行一致性分析

```bash
python detect_with_llm.py --prompt_template prompt.txt --input data/test_cases.json
```

### 3. 查看评估结果

结果 JSON 样例如：

```json
{
  "分析": "核心一致但缺乏细节，表达略有不同",
  "等价程度": 2,
  "语言风格": 1
}
```

---

## 📊 精度表现

| 模型策略      | 准确率   | 执行速度（100 条） |
| --------- | ----- | ----------- |
| BERTScore | 70.0% | 1min        |
| LLM（一致性）  | 97.8% | 5min35s     |
| LLM（线上灰度） | 94.7% | -           |

---

## 📁 项目结构

```
.
├── data/                  # 数据集存放目录
│   └── test_cases.json
├── detect_offline.py     # 离线检测主程序（BERTScore）
├── detect_with_llm.py    # 基于LLM一致性分析主程序
├── prompt.txt            # Prompt 模板
├── requirements.txt      # 依赖包列表
└── README.md
```

---

## 🧪 数据与评估集

* 离线构建：100 条测试样本（50 正确 / 50 错误）
* 线上巡检：覆盖常见问题、上下文缺失、模型切换等场景
* 数据链接请联系维护者获取（企业内部表格）

---

## 📌 注意事项

* 语言模型输出会受到温度、采样策略和 Prompt 模板影响，请固定配置以保证可复现性。
* LLM 请求建议使用批处理，提高吞吐效率。
* 如用于线上巡检，请考虑误报率容忍范围。

---

## 🤝 贡献指南

欢迎提交 PR 或 issue，我们期待以下方面的协作：

* 更丰富的 Prompt 模板优化
* 引入轻量模型加速检测
* 多语言支持（如英文、日文检测）

---

## 📮 联系我们

* 项目负责人：[lingxianghu](neulingxianghu@gmail.com)

---
