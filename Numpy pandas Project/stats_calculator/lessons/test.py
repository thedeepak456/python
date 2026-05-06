import numpy as np
import pandas as pd

print("=" * 55)
print("  LESSON 3 : Student Data Analysis")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# 📌 PART 1 : CSV File Padhna — Pandas se
# ──────────────────────────────────────────────────────────

print("\n📌 PART 1 : CSV File Load Karna\n")

# pd.read_csv() — CSV file ko Pandas DataFrame mein load karta hai
# DataFrame = Excel sheet ki tarah hota hai (rows + columns)
df = pd.read_csv(r"C:\Users\Deepak Rastogi\Documents\python\Numpy pandas Project\stats_calculator\data\student_scores.csv")

# # Pehli 5 rows dekho — hamesha pehle data dekho!
# print("Pehli 5 rows (df.head()):")
# print(df.tail())

# Total rows aur columns kitne hain
# print(f"\nTotal students     : {df.shape}")  # rows
# print(f"Total columns      : {df.shape[1]}")   # columns
# print(f"{df.info()}")
# Column names kya hain
# print(f"Columns            : {list(df.columns)}")

# # Data types kya hain har column ka
# print("\nData Types:")
# print(df.dtypes)


# # ──────────────────────────────────────────────────────────
# # 📌 PART 2 : Pandas se NumPy Array mein convert karna
# # NumPy math ke liye, Pandas data laane ke liye
# # ──────────────────────────────────────────────────────────

# print("\n📌 PART 2 : Pandas → NumPy Conversion\n")

# # .values lagao — Pandas column ko NumPy array mein badlo
scores = df["score"].values
# print("Scores array type  :", type(scores))
# print("Pehle 10 scores    :", scores[-10:])
# print("Total scores       :", len(scores))



print("\n📌 PART 3 : Class ka Overall Statistics\n")

print(f"  Class Average    : {np.mean(scores):.2f}")
print(f"  Median Score     : {np.median(scores):.2f}")
print(f"  Std Deviation    : {np.std(scores):.2f}")
print(f"  Highest Score    : {np.max(scores):.1f}")
print(f"  Lowest Score     : {np.min(scores):.1f}")
print(f"  Score Range      : {np.ptp(scores):.1f}")

# Topper kaun hai? — argmax se index milta hai
topper_idx   = np.argmax(scores)
bottom_idx   = np.argmin(scores)
print(f"\n  🏆 Topper        : {df['name'].iloc[topper_idx]} ({scores[topper_idx]:.1f})")
print(f"  📉 Lowest Scorer : {df['name'].iloc[bottom_idx]} ({scores[bottom_idx]:.1f})")

