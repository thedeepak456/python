# ============================================================
#  LESSON 3 — Student Data Analysis 🎓
#  student_scores.csv ko NumPy + Pandas se analyze karo
#  Real CSV file padhna, filter karna, insights nikalna
# ============================================================

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

# Pehli 5 rows dekho — hamesha pehle data dekho!
print("Pehli 5 rows (df.head()):")
print(df.head())

# Total rows aur columns kitne hain
print(f"\nTotal students     : {df.shape[0]}")  # rows
print(f"Total columns      : {df.shape[1]}")   # columns

# Column names kya hain
print(f"Columns            : {list(df.columns)}")

# Data types kya hain har column ka
print("\nData Types:")
print(df.dtypes)


# ──────────────────────────────────────────────────────────
# 📌 PART 2 : Pandas se NumPy Array mein convert karna
# NumPy math ke liye, Pandas data laane ke liye
# ──────────────────────────────────────────────────────────

print("\n📌 PART 2 : Pandas → NumPy Conversion\n")

# .values lagao — Pandas column ko NumPy array mein badlo
scores = df["score"].values
print("Scores array type  :", type(scores))
print("Pehle 10 scores    :", scores[:10])
print("Total scores       :", len(scores))


# ──────────────────────────────────────────────────────────
# 📌 PART 3 : Basic Statistics — Class ka report card
# ──────────────────────────────────────────────────────────

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


# ──────────────────────────────────────────────────────────
# 📌 PART 4 : Pass / Fail Analysis
# ──────────────────────────────────────────────────────────

print("\n📌 PART 4 : Pass / Fail Analysis\n")

# Boolean masking — 50 se zyada = pass
pass_mask = scores >= 50
fail_mask = scores < 50

passed_count = np.sum(pass_mask)   # True = 1, False = 0 isliye sum karo
failed_count = np.sum(fail_mask)

print(f"  ✅ Pass Students : {passed_count}")
print(f"  ❌ Fail Students : {failed_count}")
print(f"  📊 Pass Rate     : {passed_count / len(scores) * 100:.1f}%")

# Failed students ke naam nikalo — Pandas filtering
failed_df = df[df["score"] < 50]
print(f"\n  Failed Students List:")
for _, row in failed_df.iterrows():
    print(f"    → {row['name']} | {row['subject']} | Score: {row['score']:.1f}")


# ──────────────────────────────────────────────────────────
# 📌 PART 5 : Grade Distribution
# np.where — ek tarah ka if-else for arrays
# ──────────────────────────────────────────────────────────

print("\n📌 PART 5 : Grade Distribution\n")

# np.where(condition, value_if_true, value_if_false)
# Nested np.where = agar pehla fail ho toh agle pe jao
grades = np.where(scores >= 90, "A",
         np.where(scores >= 75, "B",
         np.where(scores >= 60, "C",
         np.where(scores >= 50, "D", "F"))))

# np.unique se count karo
unique_grades, grade_counts = np.unique(grades, return_counts=True)

print("  Grade | Count | Bar")
print("  " + "-" * 35)
for g, c in zip(unique_grades, grade_counts):
    bar = "█" * c   # visual bar chart
    print(f"    {g}   |  {c:3d}  | {bar}")


# ──────────────────────────────────────────────────────────
# 📌 PART 6 : Subject-wise Analysis — Pandas groupby
# Groupby = ek jaisi cheezein ek group mein rakhna
# ──────────────────────────────────────────────────────────

print("\n📌 PART 6 : Subject-wise Analysis (Pandas groupby)\n")

# groupby = subject ke hisaab se group karo, phir average nikalo
subject_avg = df.groupby("subject")["score"].mean().round(2)
subject_min = df.groupby("subject")["score"].min()
subject_max = df.groupby("subject")["score"].max()
subject_count = df.groupby("subject")["score"].count()

print(f"  {'Subject':<12} | {'Count':>5} | {'Avg':>6} | {'Min':>5} | {'Max':>5}")
print("  " + "-" * 45)
for subj in subject_avg.index:
    print(f"  {subj:<12} | {subject_count[subj]:>5} | "
          f"{subject_avg[subj]:>6.1f} | {subject_min[subj]:>5.1f} | {subject_max[subj]:>5.1f}")

# Best aur worst subject
best_subject  = subject_avg.idxmax()
worst_subject = subject_avg.idxmin()
print(f"\n  🏆 Best Subject  : {best_subject} (avg {subject_avg[best_subject]:.1f})")
print(f"  📉 Worst Subject : {worst_subject} (avg {subject_avg[worst_subject]:.1f})")


# ──────────────────────────────────────────────────────────
# 📌 PART 7 : Percentile Ranking — Student kahan khada hai?
# ──────────────────────────────────────────────────────────

print("\n📌 PART 7 : Score Percentile Ranges\n")

p25 = np.percentile(scores, 25)
p50 = np.percentile(scores, 50)
p75 = np.percentile(scores, 75)
p90 = np.percentile(scores, 90)

print(f"  Bottom 25% students score below : {p25:.1f}")
print(f"  Median score (50th %ile)         : {p50:.1f}")
print(f"  Top 25% students score above     : {p75:.1f}")
print(f"  Top 10% students score above     : {p90:.1f}")

# Koi specific student kahan hai?
student_name  = df["name"].iloc[0]
student_score = scores[0]
percentile_rank = np.sum(scores <= student_score) / len(scores) * 100
print(f"\n  Example: {student_name} ka score {student_score:.1f}")
print(f"  Woh top {100 - percentile_rank:.0f}% mein hai! 🎯")


# ──────────────────────────────────────────────────────────
# 📌 PART 8 : Outlier Students
# ──────────────────────────────────────────────────────────

print("\n📌 PART 8 : Outlier Students (Exceptional ya Struggling)\n")

q1 = np.percentile(scores, 25)
q3 = np.percentile(scores, 75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outlier_mask = (scores < lower) | (scores > upper)
outlier_df   = df[outlier_mask]

if len(outlier_df) > 0:
    print(f"  Boundary: {lower:.1f} to {upper:.1f}")
    print(f"  {len(outlier_df)} exceptional students mile:")
    for _, row in outlier_df.iterrows():
        tag = "⭐ Exceptionally good" if row["score"] > upper else "⚠️ Needs help"
        print(f"    → {row['name']} | Score: {row['score']:.1f} | {tag}")
else:
    print("  Koi outlier student nahi mila!")


print("\n✅ Lesson 3 Complete! Ab Lesson 4 dekho → 04_weather_analysis.py")
