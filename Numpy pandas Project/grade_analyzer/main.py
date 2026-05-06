# ============================================================
#  MAIN.PY — Grade Analyzer 📊🎓
#  Teen alag CSV files ko alag alag analyze kiya gaya hai
#
#  TABLE 1 → student_grades.csv    (Students ka report card)
#  TABLE 2 → exam_results.csv      (Exam-wise performance)
#  TABLE 3 → class_performance.csv (Class aur subject trends)
#
#  Hinglish comments se samjhana aasaan hoga 🙂
# ============================================================

import numpy as np
import pandas as pd

# ──────────────────────────────────────────────────────────
# Helper Function — Kisi bhi NumPy array ka stats print karo
# Yeh function teeno tables mein baar baar use hoga
# ──────────────────────────────────────────────────────────
def print_stats(data, label):
    """Kisi bhi numeric array ka poora stats summary print karta hai."""
    data = np.array(data, dtype=float)

    # Q1, Q3, IQR — outlier detection ke liye
    q1  = np.percentile(data, 25)
    q3  = np.percentile(data, 75)
    iqr = q3 - q1

    # IQR boundaries ke bahar wale = outliers
    lower    = q1 - 1.5 * iqr
    upper    = q3 + 1.5 * iqr
    outliers = data[(data < lower) | (data > upper)]

    # Skewness — data kis taraf jhuka hai?
    skew = np.mean(((data - np.mean(data)) / np.std(data)) ** 3)
    if   skew >  0.5: skew_msg = "Right skewed  (kuch bahut badi values hain)"
    elif skew < -0.5: skew_msg = "Left skewed   (kuch bahut choti values hain)"
    else:             skew_msg = "Symmetric     (data evenly distributed hai)"

    print(f"\n  {'─'*52}")
    print(f"  📊  {label}")
    print(f"  {'─'*52}")
    print(f"  Count (kitne records)    : {len(data)}")
    print(f"  Mean  (average)          : {np.mean(data):.2f}")
    print(f"  Median (beech ki value)  : {np.median(data):.2f}")
    print(f"  Std Dev (kitna spread)   : {np.std(data):.2f}")
    print(f"  Variance                 : {np.var(data):.2f}")
    print(f"  Min (sabse chota)        : {np.min(data):.2f}")
    print(f"  Max (sabse bada)         : {np.max(data):.2f}")
    print(f"  Range (Max - Min)        : {np.ptp(data):.2f}")
    print(f"  25th Percentile (Q1)     : {q1:.2f}")
    print(f"  75th Percentile (Q3)     : {q3:.2f}")
    print(f"  IQR  (Q3 - Q1)          : {iqr:.2f}")
    print(f"  Skewness                 : {skew:.2f}  ({skew_msg})")
    if len(outliers) > 0:
        print(f"  Outliers ({len(outliers):2d} mile)         : {np.round(outliers, 1)}")
    else:
        print(f"  Outliers                 : Koi nahi ✅")
    print(f"  {'─'*52}")

    return {
        "label": label, "count": len(data),
        "mean": round(float(np.mean(data)), 2),
        "median": round(float(np.median(data)), 2),
        "std_dev": round(float(np.std(data)), 2),
        "min": round(float(np.min(data)), 2),
        "max": round(float(np.max(data)), 2),
        "outlier_count": len(outliers)
    }


# ==============================================================
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#   TABLE 1 — STUDENT GRADES ANALYSIS
#   File: data/student_grades.csv
#   Columns: student_id, name, class, gender,
#            math, science, english, history, computer,
#            total, average, grade, status, class_rank
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ==============================================================

print("\n")
print("╔══════════════════════════════════════════════════════╗")
print("║       TABLE 1 : STUDENT GRADES ANALYSIS  🎓         ║")
print("╚══════════════════════════════════════════════════════╝")

# ── Step 1: CSV load karo ───────────────────────────────────
# pd.read_csv() — CSV file ko Pandas DataFrame mein load karta hai
# DataFrame = table jaise structure jisme rows aur columns hain
df_st = pd.read_csv("data/student_grades.csv")

print(f"\n📂 File loaded successfully!")
print(f"   Total students  : {df_st.shape[0]}")
print(f"   Total columns   : {df_st.shape[1]}")
print(f"   Columns         : {list(df_st.columns)}")

print("\n👁️  Sample (first 3 rows):")
print(df_st.head(3).to_string(index=False))

# ── Step 2: NumPy Arrays banao ───────────────────────────────
# .values lagane se Pandas Series → NumPy array ban jaata hai
# NumPy arrays par math operations fast aur easy hoti hain
math     = df_st["math"].values
science  = df_st["science"].values
english  = df_st["english"].values
history  = df_st["history"].values
computer = df_st["computer"].values
average  = df_st["average"].values
total    = df_st["total"].values

# ── Step 3: Average Score Statistics ────────────────────────
print("\n📊 OVERALL AVERAGE SCORE STATS:")
res_avg = print_stats(average, "Student Overall Average Score")

# ── Step 4: Subject-wise Statistics ─────────────────────────
# Har subject ka alag analysis — kahan students struggle kar rahe hain?
print("\n📚 SUBJECT-WISE STATISTICS:")
subjects = {
    "Math"    : math,
    "Science" : science,
    "English" : english,
    "History" : history,
    "Computer": computer
}

print(f"\n   {'Subject':<10} | {'Avg':>6} | {'Median':>7} | {'Std Dev':>7} | "
      f"{'Min':>5} | {'Max':>5} | {'Pass%':>6}")
print(f"   {'─'*60}")
for subj, arr in subjects.items():
    pass_pct = np.sum(arr >= 50) / len(arr) * 100
    print(f"   {subj:<10} | {np.mean(arr):>6.2f} | {np.median(arr):>7.2f} | "
          f"{np.std(arr):>7.2f} | {np.min(arr):>5.1f} | {np.max(arr):>5.1f} | {pass_pct:>5.1f}%")

# Best aur weakest subject dhundho
avg_by_subj = {s: np.mean(a) for s, a in subjects.items()}
best_subj   = max(avg_by_subj, key=avg_by_subj.get)
worst_subj  = min(avg_by_subj, key=avg_by_subj.get)
print(f"\n   🏆 Best subject    : {best_subj}  (class avg {avg_by_subj[best_subj]:.2f})")
print(f"   ⚠️  Weakest subject : {worst_subj}  (class avg {avg_by_subj[worst_subj]:.2f})")
print(f"   💡 Teachers should focus extra attention on {worst_subj}!")

# ── Step 5: Pass / Fail ──────────────────────────────────────
# Boolean masking — condition se True/False array banta hai
# np.sum(True/False) = True ki total count
print("\n✅ PASS / FAIL BREAKDOWN:")
passed    = np.sum(average >= 50)
failed    = np.sum(average < 50)
pass_rate = passed / len(average) * 100
print(f"   ✅ Passed (avg >= 50) : {passed} students")
print(f"   ❌ Failed (avg < 50)  : {failed} students")
print(f"   📊 Pass rate          : {pass_rate:.1f}%")

failed_df = df_st[df_st["average"] < 50][["name","class","average","grade"]]
if len(failed_df) > 0:
    print(f"\n   ⚠️  Failed students:")
    print(failed_df.to_string(index=False))

# ── Step 6: Grade Distribution ───────────────────────────────
# np.unique — unique values aur unki count ek saath nikalti hai
print("\n📋 GRADE DISTRIBUTION:")
grades     = df_st["grade"].values
u_grades, g_counts = np.unique(grades, return_counts=True)
print(f"   {'Grade':<6} | {'Count':>5} | {'%':>6} | Bar")
print(f"   {'─'*42}")
for g, c in zip(u_grades, g_counts):
    pct = c / len(grades) * 100
    print(f"   {g:<6} | {c:>5} | {pct:>5.1f}% | {'█' * c}")

# ── Step 7: Topper aur Bottom ────────────────────────────────
# np.argmax → index of maximum value
# np.argmin → index of minimum value
print("\n🏆 TOP & BOTTOM PERFORMERS:")
top10_pct  = np.percentile(average, 90)
topper_idx = np.argmax(average)
bottom_idx = np.argmin(average)
print(f"   🥇 School Topper : {df_st['name'].iloc[topper_idx]:<22} Avg: {average[topper_idx]:.2f}")
print(f"   📉 Needs Support : {df_st['name'].iloc[bottom_idx]:<22} Avg: {average[bottom_idx]:.2f}")

# Top 5 rankings — np.argsort sort ke indexes deta hai
print(f"\n   Top 5 Students:")
rank_idx = np.argsort(average)[::-1]   # descending order
for rank, idx in enumerate(rank_idx[:5], 1):
    medal = ["🥇","🥈","🥉","4️⃣ ","5️⃣ "][rank-1]
    print(f"   {medal} {df_st['name'].iloc[idx]:<22} | "
          f"Class {df_st['class'].iloc[idx]} | Avg: {average[idx]:.2f} | "
          f"Grade: {df_st['grade'].iloc[idx]}")

# ── Step 8: Class-wise Analysis ─────────────────────────────
# groupby('class') — same class ke saare rows ek group mein
# .agg() — ek saath multiple calculations karo
print("\n🏫 CLASS-WISE PERFORMANCE:")
class_stats = df_st.groupby("class")["average"].agg(
    Students="count", Avg="mean",
    Pass=lambda x: (x >= 50).sum()
).round(2)
class_stats["Pass%"] = (class_stats["Pass"] / class_stats["Students"] * 100).round(1)

print(f"\n   {'Class':<6} | {'Students':>8} | {'Avg Score':>9} | {'Pass%':>7}")
print(f"   {'─'*40}")
for cls, row in class_stats.iterrows():
    print(f"   {cls:<6} | {int(row['Students']):>8} | "
          f"{row['Avg']:>9.2f} | {row['Pass%']:>6.1f}%")
print(f"\n   🏆 Best class : {class_stats['Avg'].idxmax()}")
print(f"   📉 Needs help : {class_stats['Avg'].idxmin()}")

# ── Step 9: Gender Analysis ──────────────────────────────────
print("\n👫 GENDER-WISE ANALYSIS:")
gender_g = df_st.groupby("gender")["average"].agg(Count="count", Mean="mean", Median="median").round(2)
for g, row in gender_g.iterrows():
    print(f"   {g:<8} — Students: {int(row['Count'])} | Avg: {row['Mean']:.2f} | Median: {row['Median']:.2f}")

# ── Step 10: Scholarship Students ────────────────────────────
# np.percentile — 90th percentile se upar wale top 10% hain
print("\n🎖️  SCHOLARSHIP ELIGIBLE (Top 10%):")
p90 = np.percentile(average, 90)
scholarship_df = df_st[df_st["average"] >= p90][["name","class","average","grade"]]
print(f"   Threshold (90th pct) : {p90:.2f}")
print(scholarship_df.to_string(index=False))

# ── Step 11: Outlier Students ────────────────────────────────
# IQR method — boundary se bahar wale outliers hain
print("\n🔍 OUTLIER STUDENTS:")
q1  = np.percentile(average, 25)
q3  = np.percentile(average, 75)
iqr = q3 - q1
lb  = q1 - 1.5 * iqr
ub  = q3 + 1.5 * iqr
print(f"   Normal range: {lb:.2f} to {ub:.2f}")
out_df = df_st[(df_st["average"] < lb) | (df_st["average"] > ub)]
for _, row in out_df.iterrows():
    tag = "⭐ Exceptional" if row["average"] > ub else "⚠️  Needs help"
    print(f"   {tag} → {row['name']}  | Avg: {row['average']:.2f}")

print("\n✅ TABLE 1 COMPLETE!\n")
print("=" * 56)


# ==============================================================
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#   TABLE 2 — EXAM RESULTS ANALYSIS
#   File: data/exam_results.csv
#   Columns: exam_id, student_id, exam_name, term, subject,
#            max_marks, marks_obtained, percentage, grade, result
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ==============================================================

print("\n")
print("╔══════════════════════════════════════════════════════╗")
print("║       TABLE 2 : EXAM RESULTS ANALYSIS  📝           ║")
print("╚══════════════════════════════════════════════════════╝")

# ── Step 1: CSV Load ─────────────────────────────────────────
df_ex = pd.read_csv("data/exam_results.csv")

print(f"\n📂 File loaded!")
print(f"   Total exam records : {df_ex.shape[0]}")
print(f"   Columns            : {list(df_ex.columns)}")

print("\n👁️  Sample (first 3 rows):")
print(df_ex.head(3).to_string(index=False))

# Unique values — kitne types ke exams aur subjects hain
print(f"\n   Exam types : {list(df_ex['exam_name'].unique())}")
print(f"   Terms      : {list(df_ex['term'].unique())}")
print(f"   Subjects   : {list(df_ex['subject'].unique())}")

# ── Step 2: NumPy arrays ─────────────────────────────────────
percentage  = df_ex["percentage"].values
marks_obt   = df_ex["marks_obtained"].values
max_marks   = df_ex["max_marks"].values

# ── Step 3: Core Percentage Stats ────────────────────────────
print("\n📊 PERCENTAGE SCORE STATISTICS:")
res_pct = print_stats(percentage, "Exam Percentage Scores")

# ── Step 4: Pass / Fail ──────────────────────────────────────
# Boolean masking — condition lagake count karo
print("\n✅ PASS / FAIL ANALYSIS:")
total_ex = len(df_ex)
passed_ex = np.sum(percentage >= 40)   # 40% se upar = pass
failed_ex = np.sum(percentage < 40)
print(f"   Total exams    : {total_ex}")
print(f"   ✅ Passed       : {passed_ex}  ({passed_ex/total_ex*100:.1f}%)")
print(f"   ❌ Failed       : {failed_ex}  ({failed_ex/total_ex*100:.1f}%)")

# ── Step 5: Grade Distribution ───────────────────────────────
# np.unique = unique grades aur unki count
print("\n📋 GRADE DISTRIBUTION (A+ to F):")
grade_vals = df_ex["grade"].values
u_g, c_g   = np.unique(grade_vals, return_counts=True)
grade_order = ["A+","A","B+","B","C","D","F"]
print(f"   {'Grade':<5} | {'Count':>5} | {'%':>6} | Bar")
print(f"   {'─'*38}")
for g in grade_order:
    if g in u_g:
        c   = c_g[list(u_g).index(g)]
        pct = c / len(grade_vals) * 100
        print(f"   {g:<5} | {c:>5} | {pct:>5.1f}% | {'█' * c}")

# ── Step 6: Subject-wise Performance ─────────────────────────
# groupby('subject') — same subject ke saare exam records group karo
print("\n📚 SUBJECT-WISE EXAM PERFORMANCE:")
subj_ex = df_ex.groupby("subject")["percentage"].agg(
    Count="count", Avg="mean",
    Pass_Rate=lambda x: (x >= 40).mean() * 100,
    Best="max", Lowest="min"
).round(2).sort_values("Avg", ascending=False)

print(f"\n   {'Subject':<10} | {'Exams':>5} | {'Avg%':>6} | {'Pass%':>6} | {'Best':>5} | {'Low':>5}")
print(f"   {'─'*52}")
for subj, row in subj_ex.iterrows():
    print(f"   {subj:<10} | {int(row['Count']):>5} | {row['Avg']:>6.2f} | "
          f"{row['Pass_Rate']:>5.1f}% | {row['Best']:>5.1f} | {row['Lowest']:>5.1f}")
print(f"\n   🏆 Best subject   : {subj_ex['Avg'].idxmax()}")
print(f"   ⚠️  Weakest subject: {subj_ex['Avg'].idxmin()}")

# ── Step 7: Exam Type Comparison ─────────────────────────────
# Unit Test vs Mid Term vs Final Exam — kismein students zyada score karte hain?
print("\n📝 EXAM TYPE COMPARISON:")
exam_type_stats = df_ex.groupby("exam_name")["percentage"].agg(
    Count="count", Avg="mean",
    Pass_Rate=lambda x: (x >= 40).mean() * 100
).round(2)

print(f"\n   {'Exam Type':<16} | {'Count':>5} | {'Avg%':>6} | {'Pass%':>7}")
print(f"   {'─'*48}")
for exam, row in exam_type_stats.iterrows():
    print(f"   {exam:<16} | {int(row['Count']):>5} | {row['Avg']:>6.2f} | {row['Pass_Rate']:>6.1f}%")

# ── Step 8: Term-wise Trend ──────────────────────────────────
# Kya students term ke saath improve kar rahe hain?
print("\n📈 TERM-WISE PERFORMANCE TREND:")
term_stats = df_ex.groupby("term")["percentage"].agg(
    Count="count", Avg="mean", Pass_Rate=lambda x: (x >= 40).mean() * 100
).round(2)

for term, row in term_stats.iterrows():
    bar = "█" * int(row["Avg"] / 5)
    print(f"   {term:<8} : Avg {row['Avg']:>5.2f}% | Pass {row['Pass_Rate']:>5.1f}% | {bar}")

# Trend direction
term_avgs = term_stats["Avg"].values
if len(term_avgs) >= 2 and term_avgs[-1] > term_avgs[0]:
    print(f"\n   📈 Students improve kar rahe hain! Great progress! ✅")
else:
    print(f"\n   📉 Performance trend down — remedial classes needed!")

# ── Step 9: Max Marks Distribution ───────────────────────────
# Kitne exams 50/80/100 mein se the?
print("\n📏 MAX MARKS DISTRIBUTION:")
max_vals, max_counts = np.unique(max_marks, return_counts=True)
for mv, mc in zip(max_vals, max_counts):
    pct = mc / total_ex * 100
    print(f"   Out of {int(mv):>3}  : {mc:3d} exams  ({pct:5.1f}%)")

# ── Step 10: Top Performances ────────────────────────────────
# np.argsort — sort ke indexes deta hai
print("\n🌟 TOP 5 EXAM PERFORMANCES:")
top5_idx = np.argsort(percentage)[-5:][::-1]
print(f"   {'S.ID':>4} | {'Exam Type':<16} | {'Subject':<10} | {'%':>6} | Grade")
print(f"   {'─'*52}")
for idx in top5_idx:
    row = df_ex.iloc[idx]
    print(f"   {row['student_id']:>4} | {row['exam_name']:<16} | "
          f"{row['subject']:<10} | {row['percentage']:>6.2f} | {row['grade']}")

# ── Step 11: Percentile Insights ─────────────────────────────
print("\n📈 PERCENTILE INSIGHTS:")
print(f"   P25 (bottom 25%) : {np.percentile(percentage, 25):.2f}%")
print(f"   P50 (median)     : {np.percentile(percentage, 50):.2f}%")
print(f"   P75 (top 25%)    : {np.percentile(percentage, 75):.2f}%")
print(f"   P90 (top 10%)    : {np.percentile(percentage, 90):.2f}%  🌟")

print("\n✅ TABLE 2 COMPLETE!\n")
print("=" * 56)


# ==============================================================
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#   TABLE 3 — CLASS PERFORMANCE ANALYSIS
#   File: data/class_performance.csv
#   Columns: record_id, class, subject, month, year,
#            class_avg, pass_percentage, top_score,
#            lowest_score, total_students
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ==============================================================

print("\n")
print("╔══════════════════════════════════════════════════════╗")
print("║     TABLE 3 : CLASS PERFORMANCE ANALYSIS  🏫        ║")
print("╚══════════════════════════════════════════════════════╝")

# ── Step 1: CSV Load ─────────────────────────────────────────
df_cl = pd.read_csv("data/class_performance.csv")

print(f"\n📂 File loaded!")
print(f"   Total records   : {df_cl.shape[0]}")
print(f"   Columns         : {list(df_cl.columns)}")
print(f"   Classes         : {sorted(df_cl['class'].unique())}")
print(f"   Subjects        : {sorted(df_cl['subject'].unique())}")

print("\n👁️  Sample (first 3 rows):")
print(df_cl.head(3).to_string(index=False))

# ── Step 2: NumPy Arrays ─────────────────────────────────────
class_avg    = df_cl["class_avg"].values
pass_pct     = df_cl["pass_percentage"].values
top_score    = df_cl["top_score"].values
lowest_score = df_cl["lowest_score"].values
students_cnt = df_cl["total_students"].values

# ── Step 3: School-wide Overall Stats ────────────────────────
print("\n📊 SCHOOL-WIDE OVERALL STATISTICS:")
res_cls   = print_stats(class_avg, "Class Average Scores")
res_pass  = print_stats(pass_pct,  "Pass Percentage (%)")

# ── Step 4: Class-wise Comparison ────────────────────────────
# groupby — same class ke saare records group karo phir aggregate karo
print("\n🏫 CLASS-WISE PERFORMANCE:")
cls_perf = df_cl.groupby("class").agg(
    Records      = ("class_avg",       "count"),
    Avg_Score    = ("class_avg",       "mean"),
    Avg_Pass_Pct = ("pass_percentage", "mean"),
    Best_Score   = ("top_score",       "max"),
    Worst_Score  = ("lowest_score",    "min")
).round(2)

print(f"\n   {'Class':<6} | {'Records':>7} | {'Avg Score':>9} | {'Avg Pass%':>9} | {'Best':>5} | {'Worst':>6}")
print(f"   {'─'*58}")
for cls, row in cls_perf.iterrows():
    print(f"   {cls:<6} | {int(row['Records']):>7} | "
          f"{row['Avg_Score']:>9.2f} | "
          f"{row['Avg_Pass_Pct']:>8.2f}% | "
          f"{row['Best_Score']:>5.1f} | {row['Worst_Score']:>6.1f}")

best_cls  = cls_perf["Avg_Score"].idxmax()
worst_cls = cls_perf["Avg_Score"].idxmin()
gap       = cls_perf["Avg_Score"].max() - cls_perf["Avg_Score"].min()
print(f"\n   🏆 Best class    : {best_cls}  ({cls_perf.loc[best_cls,'Avg_Score']:.2f})")
print(f"   📉 Needs support : {worst_cls}  ({cls_perf.loc[worst_cls,'Avg_Score']:.2f})")
print(f"   📐 Gap (best-worst): {gap:.2f} points")
if gap > 10:
    print(f"   ⚠️  Gap is large — classes need equal resources!")
else:
    print(f"   ✅ Classes are relatively balanced — good!")

# ── Step 5: Subject-wise Performance ─────────────────────────
print("\n📚 SUBJECT-WISE PERFORMANCE (Across all classes):")
subj_perf = df_cl.groupby("subject").agg(
    Avg_Score = ("class_avg",       "mean"),
    Avg_Pass  = ("pass_percentage", "mean"),
    Best      = ("top_score",       "max"),
    Worst     = ("lowest_score",    "min")
).round(2).sort_values("Avg_Score", ascending=False)

print(f"\n   {'Subject':<10} | {'Avg Score':>9} | {'Avg Pass%':>9} | {'Best':>5} | {'Worst':>6}")
print(f"   {'─'*52}")
for subj, row in subj_perf.iterrows():
    print(f"   {subj:<10} | {row['Avg_Score']:>9.2f} | "
          f"{row['Avg_Pass']:>8.2f}% | {row['Best']:>5.1f} | {row['Worst']:>6.1f}")

print(f"\n   🏆 Best subject   : {subj_perf['Avg_Score'].idxmax()}")
print(f"   ⚠️  Weakest subject: {subj_perf['Avg_Score'].idxmin()}")

# ── Step 6: Pivot Table — Class x Subject Grid ───────────────
# Pandas pivot_table — 2D matrix mein data dikhana
# Rows = class, columns = subject, values = avg score
print("\n📊 CLASS × SUBJECT PERFORMANCE GRID:")
pivot = df_cl.pivot_table(
    values="class_avg", index="class",
    columns="subject", aggfunc="mean"
).round(1)
print(f"\n{pivot.to_string()}\n")

# Best aur worst class-subject combo
pivot_arr = pivot.values
best_i, best_j   = np.unravel_index(np.argmax(pivot_arr), pivot_arr.shape)
worst_i, worst_j = np.unravel_index(np.argmin(pivot_arr), pivot_arr.shape)
print(f"   🏆 Best combo  : {pivot.index[best_i]} + {pivot.columns[best_j]}  "
      f"({pivot_arr[best_i,best_j]:.1f})")
print(f"   ⚠️  Worst combo : {pivot.index[worst_i]} + {pivot.columns[worst_j]}  "
      f"({pivot_arr[worst_i,worst_j]:.1f})")

# ── Step 7: Pass Percentage Distribution ─────────────────────
print("\n📈 PASS PERCENTAGE DISTRIBUTION:")
exc  = np.sum(pass_pct >= 90)
good = np.sum((pass_pct >= 75) & (pass_pct < 90))
avg2 = np.sum((pass_pct >= 60) & (pass_pct < 75))
poor = np.sum((pass_pct >= 40) & (pass_pct < 60))
crit = np.sum(pass_pct < 40)
tot  = len(pass_pct)

print(f"   ✅ Excellent (>=90%) : {exc:3d}  ({exc/tot*100:.1f}%)")
print(f"   😊 Good      (75-90%): {good:3d}  ({good/tot*100:.1f}%)")
print(f"   😐 Average   (60-75%): {avg2:3d}  ({avg2/tot*100:.1f}%)")
print(f"   😟 Poor      (40-60%): {poor:3d}  ({poor/tot*100:.1f}%)")
print(f"   🚨 Critical  (<40%)  : {crit:3d}  ({crit/tot*100:.1f}%)")

# Critical cases dikhao — kahan immediate action chahiye
if crit > 0:
    crit_df = df_cl[df_cl["pass_percentage"] < 40][
        ["class","subject","month","class_avg","pass_percentage"]]
    print(f"\n   🚨 CRITICAL CASES (immediate intervention needed):")
    print(crit_df.to_string(index=False))

# ── Step 8: Score Range — Inequality Measure ─────────────────
# Score range = top - lowest — class mein kitna fark hai?
print("\n📐 SCORE RANGE ANALYSIS (Inequality):")
score_range = top_score - lowest_score
print(f"   Average range per record : {np.mean(score_range):.2f}")
print(f"   Max range seen           : {np.max(score_range):.2f}  (high inequality)")
print(f"   Min range seen           : {np.min(score_range):.2f}  (low inequality)")

# ── Step 9: Correlation ──────────────────────────────────────
# np.corrcoef — do variables ke beech ka linear relationship
print("\n🔗 CORRELATION ANALYSIS:")
corr_ap = np.corrcoef(class_avg, pass_pct)[0, 1]
corr_at = np.corrcoef(class_avg, top_score)[0, 1]
corr_al = np.corrcoef(class_avg, lowest_score)[0, 1]

print(f"   Avg Score ↔ Pass%        : {corr_ap:+.3f}  "
      f"({'Strong ✅' if corr_ap > 0.7 else 'Moderate'})")
print(f"   Avg Score ↔ Top Score    : {corr_at:+.3f}")
print(f"   Avg Score ↔ Lowest Score : {corr_al:+.3f}")

if corr_ap > 0.7:
    print(f"\n   💡 Insight: Class average improve karo → Pass rate apne aap badhega!")

# ── Step 10: Outlier Records ─────────────────────────────────
print("\n🔍 OUTLIER RECORDS (IQR Method):")
q1_c  = np.percentile(class_avg, 25)
q3_c  = np.percentile(class_avg, 75)
iqr_c = q3_c - q1_c
lb_c  = q1_c - 1.5 * iqr_c
ub_c  = q3_c + 1.5 * iqr_c

print(f"   Normal range: {lb_c:.2f} to {ub_c:.2f}")
out_cl = df_cl[(df_cl["class_avg"] < lb_c) | (df_cl["class_avg"] > ub_c)]
for _, row in out_cl.iterrows():
    tag = "⭐ Exceptional" if row["class_avg"] > ub_c else "⚠️  Needs help"
    print(f"   {tag} : Class {row['class']} | {row['subject']} | "
          f"Avg: {row['class_avg']:.2f} | Pass: {row['pass_percentage']:.1f}%")

print("\n✅ TABLE 3 COMPLETE!\n")
print("=" * 56)


# ==============================================================
#   FINAL SUMMARY — Teeno tables ka combined report
# ==============================================================

print("\n")
print("╔══════════════════════════════════════════════════════╗")
print("║      📋 FINAL SUMMARY — TEENO TABLES KA REPORT      ║")
print("╚══════════════════════════════════════════════════════╝")

avg_arr   = df_st["average"].values
pct_arr   = df_ex["percentage"].values
cavg_arr  = df_cl["class_avg"].values
grade_arr = df_st["grade"].values

print(f"""
  🎓 TABLE 1 — STUDENT GRADES (student_grades.csv)
  ─────────────────────────────────────────────────
  Total students      : {len(df_st)}
  School avg score    : {np.mean(avg_arr):.2f}
  Pass rate           : {np.sum(avg_arr>=50)/len(avg_arr)*100:.1f}%
  Grade A students    : {np.sum(grade_arr == 'A')}
  Scholarship eligible: {np.sum(avg_arr >= np.percentile(avg_arr,90))} students
  Best subject        : {max({s: np.mean(df_st[s].values) for s in ['math','science','english','history','computer']}, key=lambda x: np.mean(df_st[x].values)).capitalize()}

  📝 TABLE 2 — EXAM RESULTS (exam_results.csv)
  ─────────────────────────────────────────────────
  Total exam records  : {len(df_ex)}
  Avg % scored        : {np.mean(pct_arr):.2f}%
  Overall pass rate   : {np.sum(pct_arr>=40)/len(pct_arr)*100:.1f}%
  Exams with A+ grade : {np.sum(df_ex['grade'].values == 'A+')}
  Subjects analyzed   : {df_ex['subject'].nunique()}

  🏫 TABLE 3 — CLASS PERFORMANCE (class_performance.csv)
  ─────────────────────────────────────────────────
  Records analyzed    : {len(df_cl)}
  School avg score    : {np.mean(cavg_arr):.2f}
  Avg pass percentage : {np.mean(pass_pct):.2f}%
  Best performing cls : {cls_perf['Avg_Score'].idxmax()}
  Best subject        : {subj_perf['Avg_Score'].idxmax()}
  Critical records    : {np.sum(pass_pct < 40)}
""")

# Save summary CSV — baad mein reference ke liye
summary = pd.DataFrame([res_avg, res_pct, res_cls, res_pass])
summary.to_csv("data/summary_report.csv", index=False)
print("  📁 Summary saved → data/summary_report.csv ✅")
print("=" * 56)
print("  🎉 GRADE ANALYZER — POORA ANALYSIS COMPLETE!")
print("     Teen tables successfully alag alag analyze ho gayi!")
print("=" * 56)
