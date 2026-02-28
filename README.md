# Salience-Aligned-Event-Construction-for-Factual-Multi-Document-Summarization

# Salience-Aligned Event Construction for Factual Multi-Document Summarization

Official implementation of the conference paper:

**"Salience-Aligned Event Construction for Factual Multi-Document Summarization"**

---

## 📌 Overview

Long-context transformer models enable multi-document summarization but often generate factually inconsistent summaries when multiple sources describe evolving events. Naive concatenation of documents increases redundancy, temporal drift, and unsupported entity generation.

This repository implements an **event-centric preprocessing pipeline** that improves factual consistency in an inference-only setting without modifying pretrained model parameters.

The pipeline includes:

- Temporal segmentation
- Semantic clustering using Sentence-BERT
- Source-level balancing
- Structured event representation
- Inference-only long-context summarization (LED)
- Entity precision and hallucination rate evaluation

---

## 🏗️ Repository Structure
event-centric-summarization/
│
├── data/
│ ├── raw/ # Raw news articles
│ ├── processed/ # Clustered and structured data
│
├── src/
│ ├── temporal_segmentation.py
│ ├── semantic_clustering.py
│ ├── source_balancing.py
│ ├── structured_input.py
│ ├── summarization.py
│ ├── evaluation.py
│
├── configs/
│ └── config.yaml
│
├── requirements.txt
├── main.py
└── README.md


---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/event-centric-summarization.git
cd event-centric-summarization
pip install -r requirements.txt

Install spaCy model:

python -m spacy download en_core_web_sm
📂 Dataset

Place your dataset inside:

data/raw/news.csv

Expected columns:

headline

body

timestamp

source

reference_summary

If using a public dataset, ensure preprocessing matches the paper setup.

🚀 Running the Pipeline
python main.py

This will:

Perform temporal segmentation

Apply semantic clustering (DBSCAN)

Apply source-level balancing

Construct structured event input

Generate summaries using LED (inference-only)

Compute entity precision and hallucination rate

🧠 Method Summary

The proposed method operates entirely as a preprocessing layer before encoding.

Instead of naive document concatenation:

Articles are segmented into temporal windows.

Semantic clustering groups event-coherent articles.

Source-level balancing prevents dominance from high-frequency publishers.

Structured event inputs are passed to a pretrained long-context transformer.

No model fine-tuning or parameter updates are performed.

📈 Reproducibility

All experiments are conducted under inference-only settings.

Default configuration:

Embedding model: sentence-transformers/all-MiniLM-L6-v2

Clustering algorithm: DBSCAN (cosine distance)

Long-context model: allenai/led-base-16384

Beam width: 4

Max input length: 8192 tokens

Hyperparameters can be modified in configs/config.yaml.

🔍 Computational Complexity

Let N denote the number of articles within a temporal bucket:

Embedding computation: O(N)

Clustering (worst-case): O(N²)

Source balancing: O(N)

Structured concatenation: O(N)

Temporal segmentation reduces bucket size, keeping clustering tractable.

📄 License

This repository is released for academic research purposes only.

News datasets may be subject to copyright restrictions. Please ensure compliance with dataset licensing terms.

📬 Contact

For questions regarding the implementation or research collaboration:

Aditya Patil
Department of Artificial Intelligence and Data Science
Savitribai Phule Pune University
