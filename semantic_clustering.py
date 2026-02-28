from sentence_transformers import SentenceTransformer
from sklearn.cluster import DBSCAN
import numpy as np

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def cluster_articles(df, eps=0.25):
    texts = (df["headline"] + " " + df["body"]).tolist()
    embeddings = model.encode(texts, convert_to_numpy=True)

    clustering = DBSCAN(eps=eps, min_samples=2, metric="cosine").fit(embeddings)
    df["cluster_id"] = clustering.labels_

    return df