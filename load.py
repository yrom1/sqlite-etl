import pandas as pd

df = pd.read_csv("archive.txt", sep=" ")
df = df.reindex(columns=["date", "key", "value"])
df.to_csv("archive2.csv", index=False)

with open("archive2.csv", "r") as f:
    content = f.readlines()

with open("archive.csv", "a") as f:
    f.write("".join(content[1:]))
