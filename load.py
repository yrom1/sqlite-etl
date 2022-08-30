import pandas as pd
import db

# --- EXTRACT TRANSFORM ---
# df = pd.read_csv("archive.txt", sep=" ", thousands=",")
# df = df.reindex(columns=["date", "key", "value"])
# df.to_csv("archive2.csv", index=False)

# with open("archive2.csv", "r") as f:
#     content = f.readlines()

# with open("archive.csv", "a") as f:
#     f.write("".join(content[1:]))

# --- LOAD ---
data = pd.read_csv("archive.csv").drop_duplicates(["date", "key"]).to_numpy().tolist()
db.insert_data(data)
