import pandas as pd
from src.temporal_segmentation import temporal_segmentation
from src.semantic_clustering import cluster_articles
from src.source_balancing import source_balancing
from src.structured_input import build_structured_input
from src.summarization import generate_summary
from src.evaluation import entity_precision

df = pd.read_csv("data/raw/news.csv")

buckets = temporal_segmentation(df)

for bucket in buckets:
    clustered = cluster_articles(bucket)
    balanced = source_balancing(clustered)

    for cluster_id in balanced["cluster_id"].unique():
        cluster_df = balanced[balanced["cluster_id"] == cluster_id]
        structured_text = build_structured_input(cluster_df)
        summary = generate_summary(structured_text)

        print("\nGenerated Summary:\n", summary)