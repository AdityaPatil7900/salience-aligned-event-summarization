import pandas as pd

def temporal_segmentation(df, time_window_days=2):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')

    buckets = []
    current_bucket = []
    start_time = df.iloc[0]['timestamp']

    for _, row in df.iterrows():
        if (row['timestamp'] - start_time).days <= time_window_days:
            current_bucket.append(row)
        else:
            buckets.append(pd.DataFrame(current_bucket))
            current_bucket = [row]
            start_time = row['timestamp']

    if current_bucket:
        buckets.append(pd.DataFrame(current_bucket))

    return buckets