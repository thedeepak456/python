# ============================================================
#  LESSON 3 — Student Grades CSV Analysis 🎓
#  student_grades.csv ko analyze karo
#  Columns: student_id, name, class, gender, math, science,
#           english, history, computer, total, average,
#           grade, status, class_rank
# ============================================================

import numpy as np
import pandas as pd

print("=" * 56)
print("  LESSON 3 : Student Grades — Har Student ka Report Card")
print("=" * 56)


# ──────────────────────────────────────────────────────────
# 📌 PART 1 : CSV Load karo aur Data dekho
# ──────────────────────────────────────────────────────────

print("\n📌 PART 1 : Data Load karo\n")

# pd.read_csv — CSV file ko DataFrame mein load karta hai
# DataFrame = table jaise structure (rows + columns)
df = pd.read_csv("data/student_grades.csv")

print(f"File load ho gayi!")
print(f"Total students : {df.shape[0]}")     # shape[0] = rows
print(f"Total columns  : {df.shape[1]}")     # shape[1] = columns
print(f"Columns        : {list(df.columns)}")

# Pehli 3 rows dekho — kaisa data hai
print("\nPehli 3 rows (sample):")
print(df.head(3).to_string(index=False))

# Missing values check karo — real data mein hoti hain
print("\nMissing values:")
print(df.isnull().sum())


# ──────────────────────────────────────────────────────────
# 📌 PART 2 : Subject-wise Columns ko NumPy Arrays mein lo
# ──────────────────────────────────────────────────────────

print("\n📌 PART 2 : Subject Arrays Banana\n")

# .values lagao → Pandas column → NumPy array
math     = df["math"].values
science  = df["science"].values
english  = df["english"].values
history  = df["history"].values
computer = df["computer"].values
average  = df["average"].values
total    = df["total"].values

print(f"Math scores sample    : {math[:5]}")
print(f"Science scores sample : {science[:5]}")
print(f"Average sample        : {average[:5]}")


# ──────────────────────────────────────────────────────────
# 📌 PART 3 : Overall Class Statistics
# ──────────────────────────────────────────────────────────

print("\n📌 PART 3 : Overall Class Performance\n")

print(f"Class Average (all students) : {np.mean(average):.2f}")
print(f"Median Average               : {np.median(average):.2f}")
print(f"Std Dev (spread)             : {np.std(average):.2f}")
print(f"Highest Average              : {np.max(average):.2f}")
print(f"Lowest Average               : {np.min(average):.2f}")

# Topper — argmax index deta hai, us index se naam nikalo
topper_idx = np.argmax(average)
bottom_idx = np.argmin(average)
print(f"\n🥇 Topper   : {df['name'].iloc[topper_idx]:<22} Avg: {average[topper_idx]:.2f}")
print(f"📉 Bottom   : {df['name'].iloc[bottom_idx]:<22} Avg: {average[bottom_idx]:.2f}")


# ──────────────────────────────────────────────────────────
# 📌 PART 4 : Subject-wise Class Average Comparison
# ──────────────────────────────────────────────────────────

print("\n📌 PART 4 : Subject-wise Comparison\n")

# Har subject ka mean, std, min, max nikalo
subjects = {
    "Math"    : math,
    "Science" : science,
    "English" : english,
    "History" : history,
    "Computer": computer
}

print(f"  {'Subject':<10} | {'Avg':>6} | {'Median':>7} | {'StdDev':>7} | {'Min':>5} | {'Max':>5}")
print(f"  {'─'*52}")
for subj, arr in subjects.items():
    print(f"  {subj:<10} | {np.mean(arr):>6.2f} | {np.median(arr):>7.2f} | "
          f"{np.std(arr):>7.2f} | {np.min(arr):>5.1f} | {np.max(arr):>5.1f}")

# Best aur worst subject — students kispar zyada acha perform karte hain
avgs = {subj: np.mean(arr) for subj, arr in subjects.items()}
best_subj  = max(avgs, key=avgs.get)
worst_subj = min(avgs, key=avgs.get)
print(f"\n  🏆 Best subject   : {best_subj}   (class avg {avgs[best_subj]:.2f})")
print(f"  ⚠️  Weakest subject: {worst_subj}   (class avg {avgs[worst_subj]:.2f})")
print(f"  💡 Teachers should focus more on {worst_subj}!")


# ──────────────────────────────────────────────────────────
# 📌 PART 5 : Pass / Fail Analysis
# ──────────────────────────────────────────────────────────

print("\n📌 PART 5 : Pass / Fail Analysis\n")

# Boolean masking — condition se True/False array banta hai
# np.sum(True/False array) = True ki count
passed = np.sum(average >= 50)
failed = np.sum(average < 50)
pass_rate = passed / len(average) * 100

print(f"  ✅ Passed (avg >= 50) : {passed} students")
print(f"  ❌ Failed (avg < 50)  : {failed} students")
print(f"  📊 Pass rate          : {pass_rate:.1f}%")

# Failed students ke naam Pandas filtering se
failed_df = df[df["average"] < 50][["name","class","average","grade"]]
if len(failed_df) > 0:
    print(f"\n  ⚠️  Failed students:")
    print(failed_df.to_string(index=False))


# ──────────────────────────────────────────────────────────
# 📌 PART 6 : Grade Distribution
# np.where — array pe if-else lagana
# np.unique — unique values aur unki count ek saath
# ──────────────────────────────────────────────────────────

print("\n📌 PART 6 : Grade Distribution\n")

# CSV mein pehle se grade hai — use karo ya khud assign karo
# Yahan CSV ka grade column use karte hain
grade_col = df["grade"].values

# np.unique — unique grades aur unki frequency
unique_g, counts_g = np.unique(grade_col, return_counts=True)

print(f"  {'Grade':<6} | {'Count':>5} | {'%':>6} | Bar Chart")
print(f"  {'─'*45}")
for g, c in zip(unique_g, counts_g):
    pct = c / len(grade_col) * 100
    bar = "█" * c
    print(f"  {g:<6} | {c:>5} | {pct:>5.1f}% | {bar}")


# ──────────────────────────────────────────────────────────
# 📌 PART 7 : Class-wise Analysis (10A, 10B, 10C, 10D)
# Pandas groupby — class ke hisaab se group karo
# ──────────────────────────────────────────────────────────

print("\n📌 PART 7 : Class-wise Performance (groupby)\n")

# groupby('class') = same class ke saare rows ek group mein
# .agg() = ek saath multiple statistics nikalo
class_stats = df.groupby("class")["average"].agg(
    Students="count",
    Avg_Score="mean",
    Pass_Count=lambda x: (x >= 50).sum(),
).round(2)

# Pass percentage nikalo manually
class_stats["Pass_Pct"] = (class_stats["Pass_Count"] / class_stats["Students"] * 100).round(1)

print(f"  {'Class':<6} | {'Students':>8} | {'Avg Score':>9} | {'Pass %':>7}")
print(f"  {'─'*42}")
for cls, row in class_stats.iterrows():
    print(f"  {cls:<6} | {int(row['Students']):>8} | "
          f"{row['Avg_Score']:>9.2f} | {row['Pass_Pct']:>6.1f}%")

best_class  = class_stats["Avg_Score"].idxmax()
worst_class = class_stats["Avg_Score"].idxmin()
print(f"\n  🏆 Best class    : {best_class}  (avg {class_stats.loc[best_class,'Avg_Score']:.2f})")
print(f"  📉 Needs help    : {worst_class}  (avg {class_stats.loc[worst_class,'Avg_Score']:.2f})")


# ──────────────────────────────────────────────────────────
# 📌 PART 8 : Gender-wise Analysis
# ──────────────────────────────────────────────────────────

print("\n📌 PART 8 : Gender-wise Analysis\n")

gender_stats = df.groupby("gender")["average"].agg(
    Count="count", Mean="mean", Median="median", Std="std"
).round(2)

for gender, row in gender_stats.iterrows():
    print(f"  {gender:<8} — Count: {int(row['Count'])} | "
          f"Avg: {row['Mean']:.2f} | Median: {row['Median']:.2f} | Std: {row['Std']:.2f}")


# ──────────────────────────────────────────────────────────
# 📌 PART 9 : Percentile — Student kahan khada hai?
# ──────────────────────────────────────────────────────────

print("\n📌 PART 9 : Percentile Analysis\n")

p25 = np.percentile(average, 25)
p75 = np.percentile(average, 75)
p90 = np.percentile(average, 90)

print(f"  Bottom 25% average below : {p25:.2f}")
print(f"  Top    25% average above : {p75:.2f}")
print(f"  Top    10% average above : {p90:.2f}  🌟 (Scholarship zone)")

# Scholarship eligible students
scholarship = df[df["average"] >= p90][["name","class","average","grade"]]
print(f"\n  🎖️  Scholarship eligible students (top 10%):")
print(scholarship.to_string(index=False))


# ──────────────────────────────────────────────────────────
# 📌 PART 10 : Outlier Students
# ──────────────────────────────────────────────────────────

print("\n📌 PART 10 : Outlier Students\n")

q1  = np.percentile(average, 25)
q3  = np.percentile(average, 75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

print(f"  Normal range : {lower:.2f} to {upper:.2f}")
outlier_df = df[(df["average"] < lower) | (df["average"] > upper)]
for _, row in outlier_df.iterrows():
    tag = "⭐ Exceptional" if row["average"] > upper else "⚠️  Needs support"
    print(f"  {tag} → {row['name']} | Class {row['class']} | Avg: {row['average']:.2f}")


print("\n✅ Lesson 3 Complete! Ab Lesson 4 → 04_exam_results_analysis.py")
