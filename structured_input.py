def build_structured_input(cluster_df):
    cluster_df = cluster_df.sort_values("timestamp")
    structured_text = ""

    for _, row in cluster_df.iterrows():
        structured_text += row["headline"] + "\n"
        structured_text += row["body"] + "\n\n"

    return structured_text.strip()