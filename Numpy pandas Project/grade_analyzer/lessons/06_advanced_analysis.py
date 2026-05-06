# ============================================================
#  LESSON 6 — Advanced Analysis (Pro Level Techniques! ⚡)
#  Broadcasting, argsort rankings, weighted averages,
#  z-score, correlation matrix — sab teeno tables milake
# ============================================================

import numpy as np
import pandas as pd

print("=" * 56)
print("  LESSON 6 : Advanced Analysis — Teeno Tables Milake")
print("=" * 56)


# Teeno tables ek baar mein load kar lo
df_students = pd.read_csv("data/student_grades.csv")
df_exams    = pd.read_csv("data/exam_results.csv")
df_class    = pd.read_csv("data/class_performance.csv")

print(f"\nTables loaded:")
print(f"  student_grades.csv    : {len(df_students)} rows")
print(f"  exam_results.csv      : {len(df_exams)} rows")
print(f"  class_performance.csv : {len(df_class)} rows")


# ──────────────────────────────────────────────────────────
# 📌 PART 1 : Weighted Average — Subjects ko alag weight dena
# Real schools mein kuch subjects zyada important hote hain
# ──────────────────────────────────────────────────────────

print("\n📌 PART 1 : Weighted Average (Importance ke hisaab se)\n")

math     = df_students["math"].values
science  = df_students["science"].values
english  = df_students["english"].values
history  = df_students["history"].values
computer = df_students["computer"].values

# Normal average — sab subjects equal
normal_avg = (math + science + english + history + computer) / 5
print("Normal avg (first 5)   :", np.round(normal_avg[:5], 2))

# Weighted average — Math aur Science zyada important
# Weights: Math=30%, Sci=25%, Eng=20%, Hist=10%, Comp=15%
weights = np.array([0.30, 0.25, 0.20, 0.10, 0.15])

# np.column_stack — alag alag arrays ko ek 2D array mein dalo
all_marks = np.column_stack([math, science, english, history, computer])
print("All marks shape        :", all_marks.shape)  # (100, 5)

# Broadcasting — har row ke marks ko weights se multiply karo
weighted_avg = np.dot(all_marks, weights)  # matrix multiplication
print("Weighted avg (first 5) :", np.round(weighted_avg[:5], 2))

# Difference dekho
diff = weighted_avg - normal_avg
print("\nTop 5 students jahan difference zyada hai:")
top_diff_idx = np.argsort(np.abs(diff))[-5:][::-1]
for idx in top_diff_idx:
    print(f"  {df_students['name'].iloc[idx]:<22} | "
          f"Normal: {normal_avg[idx]:.2f} | Weighted: {weighted_avg[idx]:.2f} | "
          f"Diff: {diff[idx]:+.2f}")


# ──────────────────────────────────────────────────────────
# 📌 PART 2 : Z-Score Normalization
# Alag subjects ke marks compare karna mushkil hota hai
# Z-score se sab same scale par aa jaate hain
# ──────────────────────────────────────────────────────────

print("\n📌 PART 2 : Z-Score Normalization (Fair Comparison)\n")

print("💡 Z-score kya hai?")
print("   Z = (score - mean) / std_dev")
print("   Positive Z = average se upar, Negative = neeche")
print("   Different subjects ko same scale par compare kar sakte ho!\n")

# Math ka z-score — kaun relatively zyada/kam achha hai
math_mean = np.mean(math)
math_std  = np.std(math)
math_z    = (math - math_mean) / math_std

# English ka z-score
eng_mean  = np.mean(english)
eng_std   = np.std(english)
english_z = (english - eng_mean) / eng_std

print("First 5 students — Z-score comparison:")
print(f"  {'Name':<22} | {'Math':>5} | {'Math Z':>7} | {'Eng':>5} | {'Eng Z':>7}")
print(f"  {'─'*55}")
for i in range(5):
    name = df_students["name"].iloc[i]
    print(f"  {name:<22} | {math[i]:>5.1f} | {math_z[i]:>+7.2f} | "
          f"{english[i]:>5.1f} | {english_z[i]:>+7.2f}")

print("\n💡 Matlab: +1.5 Z = average se 1.5 standard deviation upar")
print("   Z-score se fair comparison hota hai regardless of subject difficulty")


# ──────────────────────────────────────────────────────────
# 📌 PART 3 : np.argsort — Proper Rankings banana
# ──────────────────────────────────────────────────────────

print("\n📌 PART 3 : School Rankings (argsort)\n")

average = df_students["average"].values
names   = df_students["name"].values

# np.argsort → sorted order ke indexes deta hai (ascending by default)
# [::-1] = reverse karo taaki highest pehle aaye
rank_idx = np.argsort(average)[::-1]

print("🏆 Top 10 Students (School Rank):")
print(f"  {'Rank':<5} | {'Name':<22} | {'Class':<5} | {'Avg':>6} | {'Grade':<5}")
print(f"  {'─'*52}")
for rank, idx in enumerate(rank_idx[:10], 1):
    medal = "🥇" if rank==1 else "🥈" if rank==2 else "🥉" if rank==3 else f"#{rank:<2}"
    print(f"  {medal:<5} | {names[idx]:<22} | "
          f"{df_students['class'].iloc[idx]:<5} | "
          f"{average[idx]:>6.2f} | {df_students['grade'].iloc[idx]:<5}")

print("\n📉 Bottom 5 Students (Need Support):")
print(f"  {'Rank':<5} | {'Name':<22} | {'Class':<5} | {'Avg':>6} | {'Grade':<5}")
print(f"  {'─'*52}")
total = len(average)
for rank, idx in enumerate(rank_idx[-5:][::-1], 1):
    print(f"  {total-rank+1:<5} | {names[idx]:<22} | "
          f"{df_students['class'].iloc[idx]:<5} | "
          f"{average[idx]:>6.2f} | {df_students['grade'].iloc[idx]:<5}")


# ──────────────────────────────────────────────────────────
# 📌 PART 4 : Correlation Matrix — Subjects aapas mein kitne related hain?
# ──────────────────────────────────────────────────────────

print("\n📌 PART 4 : Subject Correlation Matrix\n")

print("💡 Agar Math aur Science mein strong correlation hai,")
print("   matlab jo Math mein acha woh Science mein bhi acha hoga!\n")

# Sab subjects ek 2D array mein
all_subjects = np.column_stack([math, science, english, history, computer])
subj_names   = ["Math","Science","English","History","Computer"]

# np.corrcoef — full correlation matrix
corr_matrix = np.corrcoef(all_subjects.T)

# Print as table
print(f"  {'':>10}", end="")
for name in subj_names:
    print(f"  {name[:4]:>6}", end="")
print()
print(f"  {'─'*50}")

for i, row_name in enumerate(subj_names):
    print(f"  {row_name:<10}", end="")
    for j in range(len(subj_names)):
        val = corr_matrix[i, j]
        print(f"  {val:>6.2f}", end="")
    print()

# Strongest correlation (excluding self-correlation of 1.0)
np.fill_diagonal(corr_matrix, 0)   # diagonal ko 0 kar do
max_corr_idx = np.unravel_index(np.argmax(corr_matrix), corr_matrix.shape)
print(f"\n  Strongest pair: {subj_names[max_corr_idx[0]]} ↔ {subj_names[max_corr_idx[1]]}")
print(f"  Correlation   : {corr_matrix[max_corr_idx]:.3f}")


# ──────────────────────────────────────────────────────────
# 📌 PART 5 : Broadcasting — Class mein curved grading
# Teacher ne decide kiya — sab marks mein 5% add karo
# Lekin sirf unhe jo fail hain (50 se kam)
# ──────────────────────────────────────────────────────────

print("\n📌 PART 5 : Curve/Bonus Marks (Broadcasting)\n")

print("💡 Scenario: School ne decide kiya —")
print("   Jo students fail hain, unhe 5 bonus marks do (max 100 tak)")

avg_copy = average.copy()   # original change na ho

# Sirf fail students mein +5 add karo
fail_mask      = avg_copy < 50
avg_copy[fail_mask] = np.minimum(avg_copy[fail_mask] + 5, 100)

# Kitne students ab pass hue?
before_pass = np.sum(average >= 50)
after_pass  = np.sum(avg_copy >= 50)
newly_passed= after_pass - before_pass

print(f"\n  Before bonus — Pass: {before_pass}")
print(f"  After  bonus — Pass: {after_pass}")
print(f"  Newly passed        : {newly_passed} students! 🎉")

# Dikhao kaunse students newly pass hue
newly_pass_mask = (average < 50) & (avg_copy >= 50)
if np.any(newly_pass_mask):
    print("\n  Students who crossed pass mark after bonus:")
    for idx in np.where(newly_pass_mask)[0]:
        print(f"    {names[idx]:<22} | "
              f"Before: {average[idx]:.2f} → After: {avg_copy[idx]:.2f}")


# ──────────────────────────────────────────────────────────
# 📌 PART 6 : Cumulative Distribution — Marks ka pattern
# np.sort + counting → kitne percent students kahan tak hain
# ──────────────────────────────────────────────────────────

print("\n📌 PART 6 : Cumulative Distribution\n")

sorted_avg = np.sort(average)
total_st   = len(sorted_avg)

# Kuch thresholds par kitne students aate hain
thresholds = [40, 50, 60, 70, 75, 80, 90]
print(f"  Score Threshold | Students Below | % of Class")
print(f"  {'─'*45}")
for thresh in thresholds:
    count = np.sum(sorted_avg < thresh)
    pct   = count / total_st * 100
    bar   = "█" * int(pct / 5)
    print(f"  < {thresh:<14} | {count:>14} | {pct:>5.1f}%  {bar}")


# ──────────────────────────────────────────────────────────
# 📌 PART 7 : Final School Report — Teeno tables combine
# ──────────────────────────────────────────────────────────

print("\n📌 PART 7 : Final School Report (All 3 Tables)\n")

print("╔══════════════════════════════════════════════════════╗")
print("║           📋 SCHOOL ANNUAL REPORT SUMMARY           ║")
print("╚══════════════════════════════════════════════════════╝")

# From Table 1 — Student Grades
avg_arr = df_students["average"].values
print(f"""
  🎓 STUDENT PERFORMANCE (student_grades.csv)
  ─────────────────────────────────────────────
  Total students     : {len(df_students)}
  School average     : {np.mean(avg_arr):.2f}
  Pass rate          : {np.sum(avg_arr >= 50)/len(avg_arr)*100:.1f}%
  Grade A students   : {(df_students['grade'] == 'A').sum()}
  Scholarship (top10%): {np.sum(avg_arr >= np.percentile(avg_arr, 90))} students

  📝 EXAM ANALYSIS (exam_results.csv)
  ─────────────────────────────────────────────
  Total exams        : {len(df_exams)}
  Avg % score        : {np.mean(df_exams['percentage'].values):.2f}%
  Pass rate          : {(df_exams['result'] == 'Pass').sum()/len(df_exams)*100:.1f}%
  Subjects covered   : {df_exams['subject'].nunique()}

  🏫 CLASS PERFORMANCE (class_performance.csv)
  ─────────────────────────────────────────────
  Records analyzed   : {len(df_class)}
  School avg score   : {np.mean(df_class['class_avg'].values):.2f}
  Avg pass %         : {np.mean(df_class['pass_percentage'].values):.2f}%
  Best class         : {df_class.groupby('class')['class_avg'].mean().idxmax()}
  Best subject       : {df_class.groupby('subject')['class_avg'].mean().idxmax()}
""")

print("=" * 56)
print("  🎉 LESSON 6 COMPLETE!")
print("  Congratulations! Grade Analyzer ke saare concepts seekh liye! 🏆")
print("=" * 56)
print("\n  Ab main.py run karo → python main.py")
