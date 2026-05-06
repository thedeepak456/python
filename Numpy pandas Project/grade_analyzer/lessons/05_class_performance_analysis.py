# ============================================================
#  LESSON 5 — Class Performance Analysis 🏫
#  class_performance.csv ko analyze karo
#  Columns: record_id, class, subject, month, year,
#           class_avg, pass_percentage, top_score,
#           lowest_score, total_students
# ============================================================

import numpy as np
import pandas as pd

print("=" * 56)
print("  LESSON 5 : Class Performance — School-wide Insights")
print("=" * 56)


# ──────────────────────────────────────────────────────────
# 📌 PART 1 : Data Load aur Explore
# ──────────────────────────────────────────────────────────

print("\n📌 PART 1 : Data Load karo\n")

df = pd.read_csv("data/class_performance.csv")

print(f"Total records     : {df.shape[0]}")
print(f"Columns           : {list(df.columns)}")
print(f"\nSample data (3 rows):")
print(df.head(3).to_string(index=False))

# Unique values
print(f"\nClasses           : {sorted(df['class'].unique())}")
print(f"Subjects          : {sorted(df['subject'].unique())}")
print(f"Total students/class range: {df['total_students'].min()} to {df['total_students'].max()}")


# ──────────────────────────────────────────────────────────
# 📌 PART 2 : School-wide Overall Statistics
# ──────────────────────────────────────────────────────────

print("\n📌 PART 2 : School-wide Overall Stats\n")

# .values → NumPy array banao
class_avg   = df["class_avg"].values
pass_pct    = df["pass_percentage"].values
top_score   = df["top_score"].values
lowest_score= df["lowest_score"].values
students    = df["total_students"].values

print(f"Overall school avg score : {np.mean(class_avg):.2f}")
print(f"Median class avg         : {np.median(class_avg):.2f}")
print(f"Std Dev                  : {np.std(class_avg):.2f}")
print(f"Best class record avg    : {np.max(class_avg):.2f}")
print(f"Worst class record avg   : {np.min(class_avg):.2f}")

print(f"\nAvg pass percentage  : {np.mean(pass_pct):.2f}%")
print(f"Median pass %        : {np.median(pass_pct):.2f}%")
print(f"Lowest pass % seen   : {np.min(pass_pct):.2f}%  ⚠️")
print(f"Highest pass % seen  : {np.max(pass_pct):.2f}%  ✅")

# Total students covered
print(f"\nTotal students across records : {np.sum(students):,}")
print(f"Avg students per class-subject: {np.mean(students):.1f}")


# ──────────────────────────────────────────────────────────
# 📌 PART 3 : Class-wise Performance Comparison
# groupby('class') — ek class ke saare records group karo
# ──────────────────────────────────────────────────────────

print("\n📌 PART 3 : Class-wise Performance\n")

class_perf = df.groupby("class").agg(
    Records      = ("class_avg",      "count"),
    School_Avg   = ("class_avg",      "mean"),
    Avg_Pass_Pct = ("pass_percentage","mean"),
    Best_Score   = ("top_score",      "max"),
    Worst_Score  = ("lowest_score",   "min")
).round(2)

print(f"  {'Class':<6} | {'Records':>7} | {'Avg Score':>9} | {'Avg Pass%':>9} | {'Best':>5} | {'Worst':>6}")
print(f"  {'─'*58}")
for cls, row in class_perf.iterrows():
    print(f"  {cls:<6} | {int(row['Records']):>7} | "
          f"{row['School_Avg']:>9.2f} | "
          f"{row['Avg_Pass_Pct']:>8.2f}% | "
          f"{row['Best_Score']:>5.1f} | {row['Worst_Score']:>6.1f}")

best_class  = class_perf["School_Avg"].idxmax()
worst_class = class_perf["School_Avg"].idxmin()
print(f"\n  🏆 Best class    : {best_class}  ({class_perf.loc[best_class,'School_Avg']:.2f} avg)")
print(f"  📉 Needs support : {worst_class}  ({class_perf.loc[worst_class,'School_Avg']:.2f} avg)")

# Gap between best and worst — inequality measure
class_avgs_arr = class_perf["School_Avg"].values
gap = np.max(class_avgs_arr) - np.min(class_avgs_arr)
print(f"\n  Gap (best-worst) : {gap:.2f} points")
if gap > 10:
    print(f"  ⚠️  Zyada gap hai! Classes ke beech performance bahut alag hai")
else:
    print(f"  ✅ Classes relatively equal hain — good uniformity!")


# ──────────────────────────────────────────────────────────
# 📌 PART 4 : Subject-wise Analysis (Across all Classes)
# ──────────────────────────────────────────────────────────

print("\n📌 PART 4 : Subject-wise Analysis\n")

subj_perf = df.groupby("subject").agg(
    Avg_Score  = ("class_avg",       "mean"),
    Avg_Pass   = ("pass_percentage", "mean"),
    Top_Score  = ("top_score",       "max"),
    Low_Score  = ("lowest_score",    "min"),
    Records    = ("class_avg",       "count")
).round(2).sort_values("Avg_Score", ascending=False)

print(f"  {'Subject':<10} | {'Avg Score':>9} | {'Avg Pass%':>9} | {'Top':>5} | {'Low':>5}")
print(f"  {'─'*52}")
for subj, row in subj_perf.iterrows():
    print(f"  {subj:<10} | {row['Avg_Score']:>9.2f} | "
          f"{row['Avg_Pass']:>8.2f}% | {row['Top_Score']:>5.1f} | {row['Low_Score']:>5.1f}")

best_subj  = subj_perf["Avg_Score"].idxmax()
worst_subj = subj_perf["Avg_Score"].idxmin()
print(f"\n  🏆 Best subject   : {best_subj}  ({subj_perf.loc[best_subj,'Avg_Score']:.2f})")
print(f"  ⚠️  Weakest subject: {worst_subj}  ({subj_perf.loc[worst_subj,'Avg_Score']:.2f})")
print(f"  💡 School-wide, {worst_subj} needs curriculum improvement!")


# ──────────────────────────────────────────────────────────
# 📌 PART 5 : Class × Subject Heatmap (Pivot Table)
# Pandas pivot_table — 2D grid mein data dikhana
# ──────────────────────────────────────────────────────────

print("\n📌 PART 5 : Class × Subject Performance Grid\n")

# pivot_table — rows = class, columns = subject, values = avg score
pivot = df.pivot_table(
    values="class_avg",
    index="class",
    columns="subject",
    aggfunc="mean"
).round(1)

print("  (Average score — rows = Class, columns = Subject)")
print(f"\n{pivot.to_string()}\n")

# Best class-subject combo — np operations on pivot table
pivot_arr = pivot.values
best_combo_idx = np.unravel_index(np.argmax(pivot_arr), pivot_arr.shape)
worst_combo_idx= np.unravel_index(np.argmin(pivot_arr), pivot_arr.shape)

best_cls  = pivot.index[best_combo_idx[0]]
best_sub  = pivot.columns[best_combo_idx[1]]
worst_cls = pivot.index[worst_combo_idx[0]]
worst_sub = pivot.columns[worst_combo_idx[1]]

print(f"  🏆 Best combo  : {best_cls} + {best_sub}  "
      f"({pivot_arr[best_combo_idx]:.1f})")
print(f"  ⚠️  Worst combo : {worst_cls} + {worst_sub}  "
      f"({pivot_arr[worst_combo_idx]:.1f})")


# ──────────────────────────────────────────────────────────
# 📌 PART 6 : Pass Percentage Distribution
# ──────────────────────────────────────────────────────────

print("\n📌 PART 6 : Pass Percentage Distribution\n")

# Pass percentage ko buckets mein baanto
excellent = np.sum(pass_pct >= 90)
good      = np.sum((pass_pct >= 75) & (pass_pct < 90))
average   = np.sum((pass_pct >= 60) & (pass_pct < 75))
poor      = np.sum((pass_pct >= 40) & (pass_pct < 60))
critical  = np.sum(pass_pct < 40)

total_rec = len(pass_pct)
print(f"  ✅ Excellent (>=90%)  : {excellent:3d} records  ({excellent/total_rec*100:.1f}%)")
print(f"  😊 Good      (75-90%) : {good:3d} records  ({good/total_rec*100:.1f}%)")
print(f"  😐 Average   (60-75%) : {average:3d} records  ({average/total_rec*100:.1f}%)")
print(f"  😟 Poor      (40-60%) : {poor:3d} records  ({poor/total_rec*100:.1f}%)")
print(f"  🚨 Critical  (<40%)   : {critical:3d} records  ({critical/total_rec*100:.1f}%)")

# Critical records — kahan intervention chahiye?
if critical > 0:
    crit_df = df[df["pass_percentage"] < 40][["class","subject","month","class_avg","pass_percentage"]]
    print(f"\n  🚨 Critical cases (immediate attention needed):")
    print(crit_df.to_string(index=False))


# ──────────────────────────────────────────────────────────
# 📌 PART 7 : Top vs Lowest Score Analysis
# Har class mein kitna gap hai best aur worst ke beech?
# ──────────────────────────────────────────────────────────

print("\n📌 PART 7 : Score Range Analysis (Top vs Lowest)\n")

# Score range = top - lowest — kitni inequality hai class mein
score_range = top_score - lowest_score
print(f"Average score range per record : {np.mean(score_range):.2f}")
print(f"Max score range seen           : {np.max(score_range):.2f}  (zyada inequality)")
print(f"Min score range seen           : {np.min(score_range):.2f}  (kam inequality)")

# Records with highest inequality
high_gap_mask = score_range > np.percentile(score_range, 90)
high_gap_df   = df[high_gap_mask][["class","subject","class_avg","top_score","lowest_score"]]
high_gap_df   = high_gap_df.copy()
high_gap_df["gap"] = high_gap_df["top_score"] - high_gap_df["lowest_score"]
high_gap_df = high_gap_df.sort_values("gap", ascending=False)

print(f"\n  📊 Highest inequality cases (top 10%):")
print(high_gap_df.to_string(index=False))
print(f"\n  💡 In these cases, teacher should do differentiated teaching!")


# ──────────────────────────────────────────────────────────
# 📌 PART 8 : Correlation — Pass % aur Avg Score ka relation
# np.corrcoef — do variables ke beech ka linear relationship
# ──────────────────────────────────────────────────────────

print("\n📌 PART 8 : Correlation Analysis\n")

# Agar class ka average zyada hai → pass % bhi zyada hona chahiye
corr_avg_pass = np.corrcoef(class_avg, pass_pct)[0, 1]
corr_avg_top  = np.corrcoef(class_avg, top_score)[0, 1]
corr_avg_low  = np.corrcoef(class_avg, lowest_score)[0, 1]

print(f"  Avg Score ↔ Pass%       : {corr_avg_pass:+.3f}")
print(f"  Avg Score ↔ Top Score   : {corr_avg_top:+.3f}")
print(f"  Avg Score ↔ Lowest Score: {corr_avg_low:+.3f}")

if corr_avg_pass > 0.7:
    print(f"\n  ✅ Strong correlation: Jab class avg zyada → pass % bhi zyada!")
    print(f"     Matlab: Improving average → automatically pass rate badhega!")


# ──────────────────────────────────────────────────────────
# 📌 PART 9 : Outlier Classes/Subjects — kahan attention chahiye?
# ──────────────────────────────────────────────────────────

print("\n📌 PART 9 : Records Needing Immediate Attention\n")

q1_avg = np.percentile(class_avg, 25)
q3_avg = np.percentile(class_avg, 75)
iqr_avg= q3_avg - q1_avg
lower  = q1_avg - 1.5 * iqr_avg

# Critically low average records
critical_df = df[df["class_avg"] < lower].sort_values("class_avg")
print(f"  Records with critically low avg (below {lower:.2f}):")
if len(critical_df) > 0:
    print(critical_df[["class","subject","month","class_avg","pass_percentage"]].to_string(index=False))
else:
    print(f"  Koi critical outlier nahi mila — sab theek hai! ✅")


print("\n✅ Lesson 5 Complete! Ab Lesson 6 → 06_advanced_analysis.py")
