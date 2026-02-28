def source_balancing(df):
    balanced = (
        df.sort_values("timestamp")
          .groupby(["cluster_id", "source"])
          .head(1)
    )
    return balanced