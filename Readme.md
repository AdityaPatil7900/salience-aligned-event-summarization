# Salience-Aligned Event Construction for Factual Multi-Document Summarization
[Preprocessed, but not truncated, data](https://drive.google.com/open?id=1qZ3zJBv0zrUy4HVWxnx33IsrHGimXLPy) </br>
[Preprocessed, truncated, data](https://drive.google.com/open?id=1qqSnxiaNVEctgiz2g-Wd3a9kwWuwMA07) </br>
[Raw data](https://drive.google.com/open?id=1uDarzpu2HFc-vjXNJCRv2NIHzakpSGOw) (only replaced \n with "NEWLINE_CHAR" and appended "|||||" to the end of each story).  </br>
[Raw data, bad retrievals removed](https://drive.google.com/open?id=1jwBzXBVv8sfnFrlzPnSUBHEEAbpIUnFq) -- Removes documents retrieved with error noticed in [this issue](https://github.com/Alex-Fabbri/Multi-News/issues/11) and removes the "|||||" at the end of each example.  </br>
[Raw data -- zipped](https://drive.google.com/open?id=1vRY2wM6rlOZrf9exGTm5pXj5ExlVwJ0C) </br>
[****Tensorflow datasets****](https://github.com/tensorflow/datasets/blob/master/tensorflow_datasets/summarization/multi_news.py)
This repository contains the official implementation of the preprocessing-based event-centric structuring pipeline described in our conference paper.

## Features
- Temporal segmentation
- SBERT-based semantic clustering
- Source-level balancing
- Structured input construction
- Inference-only LED summarization
- Entity precision & hallucination evaluation

## Reproduction
1. Install requirements
2. Place dataset in data/raw/
3. Run main.py