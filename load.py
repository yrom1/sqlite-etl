import pandas as pd

df = pd.read_csv("archive.txt", sep=" ")
df = df.reindex(columns=["date", "key", "value"])
df.to_csv("archive2.csv", index=False)
