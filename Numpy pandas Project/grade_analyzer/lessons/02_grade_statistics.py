# ============================================================
#  LESSON 2 — Grade Statistics (Numbers se insight nikalo! 📊)
#  Mean, Median, Std Dev, Percentiles — Grade Analyzer mein
#  yeh sab functions kaam aate hain
# ============================================================

import numpy as np

print("=" * 56)
print("  LESSON 2 : Grade Statistics — Data Samajhna")
print("=" * 56)


# ──────────────────────────────────────────────────────────
# 📌 PART 1 : Mean — Class ka average nikalna
# ──────────────────────────────────────────────────────────

print("\n📌 PART 1 : Mean (Class Average)\n")

# Ek class ke students ke marks
class_marks = np.array([55, 72, 88, 45, 63, 79, 91, 38, 67, 84,
                         52, 76, 60, 95, 43, 70, 83, 57, 78, 66])
print("Class marks    :", class_marks)

# Mean = Saari values ka sum / total count
class_avg = np.mean(class_marks)
print(f"Class average  : {class_avg:.2f}")

# Manual check — same answer aana chahiye
manual_avg = np.sum(class_marks) / len(class_marks)
print(f"Manual check   : {manual_avg:.2f}  ✅")

print("\n💡 Grade Analyzer mein use:")
print("   → Har subject ka class average nikalna")
print("   → Student ka overall average nikalna")
print("   → Best aur worst performing subject pehchanna")


# ──────────────────────────────────────────────────────────
# 📌 PART 2 : Median — Outlier se safe average
# ──────────────────────────────────────────────────────────

print("\n📌 PART 2 : Median (Middle Value)\n")

marks = np.array([55, 72, 88, 45, 63, 79, 91, 38, 67, 84])
print("Original marks :", marks)
print("Sorted marks   :", np.sort(marks))
print(f"Median         : {np.median(marks):.2f}")
print(f"Mean           : {np.mean(marks):.2f}")

# Ek exceptional student aa gaya — outlier!
marks_with_topper = np.append(marks, [99, 100])
print(f"\nTopper add hua : {marks_with_topper}")
print(f"Mean (changed) : {np.mean(marks_with_topper):.2f}")    # badal gaya
print(f"Median (stable): {np.median(marks_with_topper):.2f}")  # zyada nahi badla

print("\n💡 Kab median use karo?")
print("   → Jab class mein kuch exceptionally high/low scorers ho")
print("   → Scholarship ke liye fair cutoff decide karna ho")


# ──────────────────────────────────────────────────────────
# 📌 PART 3 : Standard Deviation — Marks kitne spread hain?
# ──────────────────────────────────────────────────────────

print("\n📌 PART 3 : Standard Deviation (Spread)\n")

# Do alag sections compare karo
section_A = np.array([68, 70, 72, 69, 71, 73, 70, 68, 72, 71])  # sab similar
section_B = np.array([30, 95, 45, 88, 25, 99, 50, 80, 35, 90])  # bahut fark

print("Section A marks:", section_A)
print("Section B marks:", section_B)

print(f"\nSection A — Avg: {np.mean(section_A):.1f} | Std Dev: {np.std(section_A):.2f}")
print(f"Section B — Avg: {np.mean(section_B):.1f} | Std Dev: {np.std(section_B):.2f}")

print("\n💡 Matlab:")
print("   Section A — Sab students roughly same level par hain")
print("   Section B — Kuch bahut acha kar rahe, kuch struggle kar rahe")
print("   Teacher ko Section B par zyada dhyan dena chahiye! 📌")


# ──────────────────────────────────────────────────────────
# 📌 PART 4 : Percentiles — Student ranking samajhna
# ──────────────────────────────────────────────────────────

print("\n📌 PART 4 : Percentiles (Ranking)\n")

all_marks = np.array([33, 45, 52, 58, 61, 64, 67, 70, 73, 76,
                       79, 82, 84, 87, 89, 91, 93, 95, 97, 99])
print("All marks (sorted):", all_marks)

# Percentile = kitne percent students isse neeche hain
p25 = np.percentile(all_marks, 25)   # 25% students isse neeche
p50 = np.percentile(all_marks, 50)   # median hi hai
p75 = np.percentile(all_marks, 75)   # top 25% ki boundary
p90 = np.percentile(all_marks, 90)   # top 10% ki boundary

print(f"\n25th percentile: {p25:.1f}  (Bottom 25% students isse neeche hain)")
print(f"50th percentile: {p50:.1f}  (Yeh median hai)")
print(f"75th percentile: {p75:.1f}  (Top 25% yahan se upar hain)")
print(f"90th percentile: {p90:.1f}  (Top 10% mein jaane ke liye chahiye 🌟)")

# IQR — middle 50% ka spread
iqr = p75 - p25
print(f"\nIQR (Q3 - Q1)  : {iqr:.1f}  (Middle 50% students ka spread)")


# ──────────────────────────────────────────────────────────
# 📌 PART 5 : Outliers — Exceptional ya Struggling students
# ──────────────────────────────────────────────────────────

print("\n📌 PART 5 : Outlier Detection (IQR Method)\n")

marks = np.array([62, 68, 71, 65, 70, 74, 67, 73, 69, 72,
                  63, 75, 68, 70, 15, 98, 66, 71, 64, 69])
print("Marks          :", marks)

q1  = np.percentile(marks, 25)
q3  = np.percentile(marks, 75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

print(f"\nQ1             : {q1:.1f}")
print(f"Q3             : {q3:.1f}")
print(f"IQR            : {iqr:.1f}")
print(f"Lower boundary : {lower:.1f}")
print(f"Upper boundary : {upper:.1f}")

outliers = marks[(marks < lower) | (marks > upper)]
normal   = marks[(marks >= lower) & (marks <= upper)]

print(f"\nOutliers found : {outliers}")
print(f"Normal range   : {len(normal)} students")

print("\n💡 Grade Analyzer mein use:")
print("   → 15 wala student — bahut struggle kar raha, attention chahiye ⚠️")
print("   → 98 wala student — exceptional, scholarship worthy! ⭐")


# ──────────────────────────────────────────────────────────
# 📌 PART 6 : np.where — Array pe if-else (Grades assign karna)
# Yeh Grade Analyzer ka MOST USED function hai!
# ──────────────────────────────────────────────────────────

print("\n📌 PART 6 : np.where — Grades Assign Karna ⭐\n")

scores = np.array([91, 82, 74, 65, 55, 44, 88, 77, 60, 35])
print("Scores         :", scores)

# np.where(condition, value_if_true, value_if_false)
# Nested → multiple conditions handle karna
grades = np.where(scores >= 90, "A+",
         np.where(scores >= 80, "A",
         np.where(scores >= 70, "B+",
         np.where(scores >= 60, "B",
         np.where(scores >= 50, "C",
         np.where(scores >= 40, "D", "F"))))))

print("Grades         :", grades)

# Pass/Fail
status = np.where(scores >= 40, "Pass", "Fail")
print("Status         :", status)

# Count karo
unique_g, counts_g = np.unique(grades, return_counts=True)
print("\nGrade distribution:")
for g, c in zip(unique_g, counts_g):
    print(f"  Grade {g:<3} : {c} students")


# ──────────────────────────────────────────────────────────
# 📌 PART 7 : np.sort aur np.argsort — Rankings banana
# ──────────────────────────────────────────────────────────

print("\n📌 PART 7 : Sorting aur Rankings\n")

names  = np.array(["Raj","Priya","Aarav","Sneha","Vikram","Ananya","Karan"])
marks2 = np.array([75, 88, 62, 91, 55, 84, 70])

print("Students       :", names)
print("Their marks    :", marks2)

# argsort → sorted order ke indexes deta hai
sort_idx = np.argsort(marks2)[::-1]   # [::-1] = descending (highest pehle)

print("\n🏆 Class Rankings:")
for rank, idx in enumerate(sort_idx, 1):
    medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "  "
    print(f"  Rank {rank} {medal} : {names[idx]:<10} → {marks2[idx]}")


print("\n✅ Lesson 2 Complete! Ab Lesson 3 → 03_student_grades_analysis.py")
