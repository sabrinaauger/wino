import pandas as pd

def load_region():
    # Load your dataset (adjust the path and format accordingly)
    dataset_path = '~/code/sabrinaauger/wino/raw_data/winemag-data-130k-v2.csv'
    wine_regions_df = pd.read_csv(dataset_path)
    return wine_regions_df
