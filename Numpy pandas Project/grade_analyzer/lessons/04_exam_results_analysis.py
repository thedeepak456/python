# ============================================================
#  LESSON 4 — Exam Results Analysis 📝
#  exam_results.csv ko analyze karo
#  Columns: exam_id, student_id, exam_name, term, subject,
#           max_marks, marks_obtained, percentage, grade, result
# ============================================================

import numpy as np
import pandas as pd

print("=" * 56)
print("  LESSON 4 : Exam Results — Performance Deep Dive")
print("=" * 56)


# ──────────────────────────────────────────────────────────
# 📌 PART 1 : Data Load aur Overview
# ──────────────────────────────────────────────────────────

print("\n📌 PART 1 : Data Load karo\n")

df = pd.read_csv("data/exam_results.csv")

print(f"Total exam records : {df.shape[0]}")
print(f"Columns            : {list(df.columns)}")
print(f"\nPehli 3 rows:")
print(df.head(3).to_string(index=False))

# Unique values dekho — kitne types ke exams hain
print(f"\nExam types     : {df['exam_name'].unique()}")
print(f"Subjects       : {df['subject'].unique()}")
print(f"Terms          : {df['term'].unique()}")
print(f"Max marks used : {np.sort(df['max_marks'].unique())}")


# ──────────────────────────────────────────────────────────
# 📌 PART 2 : Percentage aur Marks Statistics
# ──────────────────────────────────────────────────────────

print("\n📌 PART 2 : Overall Performance Statistics\n")

# .values = NumPy array mein convert karo
percentage   = df["percentage"].values
marks_obt    = df["marks_obtained"].values
max_marks    = df["max_marks"].values

print(f"Avg percentage   : {np.mean(percentage):.2f}%")
print(f"Median %         : {np.median(percentage):.2f}%")
print(f"Std Dev          : {np.std(percentage):.2f}%")
print(f"Highest %        : {np.max(percentage):.2f}%")
print(f"Lowest %         : {np.min(percentage):.2f}%")

# Kitne exams mein 100 max marks the vs 50 vs 80
print(f"\nMax 100 wale exams : {np.sum(max_marks == 100)}")
print(f"Max  80 wale exams : {np.sum(max_marks == 80)}")
print(f"Max  50 wale exams : {np.sum(max_marks == 50)}")


# ──────────────────────────────────────────────────────────
# 📌 PART 3 : Pass / Fail Rate
# ──────────────────────────────────────────────────────────

print("\n📌 PART 3 : Pass / Fail Analysis\n")

# Boolean masking se count karo
total_exams = len(df)
passed_exams = np.sum(percentage >= 40)    # 40% se upar = pass
failed_exams = np.sum(percentage < 40)

print(f"Total exam entries : {total_exams}")
print(f"✅ Passed          : {passed_exams}  ({passed_exams/total_exams*100:.1f}%)")
print(f"❌ Failed          : {failed_exams}  ({failed_exams/total_exams*100:.1f}%)")

# Pandas value_counts — result column mein har value kitni baar hai
print(f"\nResult distribution (Pandas value_counts):")
print(df["result"].value_counts())


# ──────────────────────────────────────────────────────────
# 📌 PART 4 : Grade Distribution (A+ to F)
# ──────────────────────────────────────────────────────────

print("\n📌 PART 4 : Grade Distribution\n")

# np.unique = unique grades aur unki count
grade_col = df["grade"].values
unique_g, counts_g = np.unique(grade_col, return_counts=True)

# Sorted dekho — A+ pehle, F aakhri mein
grade_order = ["A+","A","B+","B","C","D","F"]
print(f"  {'Grade':<5} | {'Count':>5} | {'%':>6} | Bar")
print(f"  {'─'*40}")
for g in grade_order:
    if g in unique_g:
        idx = np.where(unique_g == g)[0][0]
        c   = counts_g[idx]
        pct = c / len(grade_col) * 100
        bar = "█" * c
        print(f"  {g:<5} | {c:>5} | {pct:>5.1f}% | {bar}")


# ──────────────────────────────────────────────────────────
# 📌 PART 5 : Subject-wise Performance
# groupby('subject') — subject ke hisaab se group karo
# ──────────────────────────────────────────────────────────

print("\n📌 PART 5 : Subject-wise Performance\n")

# groupby = same subject ke saare exams ek group mein
subj_stats = df.groupby("subject")["percentage"].agg(
    Count="count",
    Avg_Pct="mean",
    Pass_Rate=lambda x: (x >= 40).mean() * 100,
    Top_Score="max"
).round(2)

subj_stats = subj_stats.sort_values("Avg_Pct", ascending=False)

print(f"  {'Subject':<10} | {'Exams':>5} | {'Avg %':>6} | {'Pass%':>6} | {'Top':>5}")
print(f"  {'─'*48}")
for subj, row in subj_stats.iterrows():
    print(f"  {subj:<10} | {int(row['Count']):>5} | "
          f"{row['Avg_Pct']:>6.2f} | {row['Pass_Rate']:>5.1f}% | {row['Top_Score']:>5.1f}%")

best_subj  = subj_stats["Avg_Pct"].idxmax()
worst_subj = subj_stats["Avg_Pct"].idxmin()
print(f"\n  🏆 Best subject   : {best_subj}  (avg {subj_stats.loc[best_subj,'Avg_Pct']:.1f}%)")
print(f"  ⚠️  Weakest subject: {worst_subj}  (avg {subj_stats.loc[worst_subj,'Avg_Pct']:.1f}%)")


# ──────────────────────────────────────────────────────────
# 📌 PART 6 : Exam Type Analysis (Unit Test vs Final)
# ──────────────────────────────────────────────────────────

print("\n📌 PART 6 : Exam Type Comparison\n")

exam_stats = df.groupby("exam_name")["percentage"].agg(
    Count="count", Avg="mean", Pass_Rate=lambda x: (x >= 40).mean() * 100
).round(2)

print(f"  {'Exam Type':<15} | {'Count':>5} | {'Avg %':>6} | {'Pass%':>7}")
print(f"  {'─'*48}")
for exam, row in exam_stats.iterrows():
    print(f"  {exam:<15} | {int(row['Count']):>5} | {row['Avg']:>6.2f} | {row['Pass_Rate']:>6.1f}%")

print("\n  💡 Insight:")
print("  Final exam mein performance alag hoti hai Unit Tests se?")
print("  Agar Final mein avg zyada hai → students zyada seriously lete hain! 📚")


# ──────────────────────────────────────────────────────────
# 📌 PART 7 : Term-wise Analysis (Term 1, 2, 3)
# ──────────────────────────────────────────────────────────

print("\n📌 PART 7 : Term-wise Performance Trend\n")

term_stats = df.groupby("term")["percentage"].agg(
    Count="count", Avg="mean", Median="median"
).round(2)

for term, row in term_stats.iterrows():
    print(f"  {term:<8} — Avg: {row['Avg']:.2f}%  Median: {row['Median']:.2f}%  "
          f"  ({int(row['Count'])} exams)")

# Kya students term ke saath improve kar rahe hain?
term_avgs = term_stats["Avg"].values
if len(term_avgs) >= 2:
    if term_avgs[-1] > term_avgs[0]:
        print(f"\n  📈 Students improve kar rahe hain term ke saath! Great!")
    else:
        print(f"\n  📉 Performance decline ho rahi hai — remedial action needed!")


# ──────────────────────────────────────────────────────────
# 📌 PART 8 : Percentile Distribution
# ──────────────────────────────────────────────────────────

print("\n📌 PART 8 : Percentile Distribution\n")

p25 = np.percentile(percentage, 25)
p50 = np.percentile(percentage, 50)
p75 = np.percentile(percentage, 75)
p90 = np.percentile(percentage, 90)

print(f"  25th percentile (P25) : {p25:.2f}%  → 25% exams isse neeche hain")
print(f"  50th percentile (P50) : {p50:.2f}%  → Median score")
print(f"  75th percentile (P75) : {p75:.2f}%  → Top 25% boundary")
print(f"  90th percentile (P90) : {p90:.2f}%  → Excellent zone 🌟")

# Excellent performers
excellent = df[df["percentage"] >= p90][["student_id","exam_name","subject","percentage","grade"]]
print(f"\n  🌟 Top 10% exam performances:")
print(excellent.to_string(index=False))


# ──────────────────────────────────────────────────────────
# 📌 PART 9 : Outlier Exam Scores
# ──────────────────────────────────────────────────────────

print("\n📌 PART 9 : Outlier Detection\n")

q1  = np.percentile(percentage, 25)
q3  = np.percentile(percentage, 75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

print(f"  Normal range : {lower:.1f}% to {upper:.1f}%")

low_outliers  = df[df["percentage"] < lower]
high_outliers = df[df["percentage"] > upper]

print(f"\n  ⚠️  Very low scores ({len(low_outliers)} found):")
if len(low_outliers) > 0:
    print(low_outliers[["student_id","subject","percentage","result"]].to_string(index=False))

print(f"\n  ⭐ Exceptional scores ({len(high_outliers)} found):")
if len(high_outliers) > 0:
    print(high_outliers[["student_id","subject","percentage","grade"]].to_string(index=False))


print("\n✅ Lesson 4 Complete! Ab Lesson 5 → 05_class_performance_analysis.py")
