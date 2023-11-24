from datasets import list_datasets
from datasets import load_dataset
import pandas as pd


all_datasets = list_datasets()

print(f"There are {len(all_datasets)} datasets currently available on the Hub")
print(f"The first 10 are: {all_datasets[:10]}")

emotions = load_dataset("emotion")

emotions.set_format(type="pandas")

df = emotions["train"][:]
df.head()

