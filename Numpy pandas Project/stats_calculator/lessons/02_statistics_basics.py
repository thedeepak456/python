# ============================================================
#  LESSON 2 — Statistics Basics (Numbers se secrets nikalo! 🔍)
#  Mean, Median, Mode, Std Dev — sab kuch yahan hai
# ============================================================

import numpy as np

print("=" * 55)
print("  LESSON 2 : Statistics Basics — Data ko samajhna")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# 📌 PART 1 : Mean (Average) — Sabka average nikalna
# ──────────────────────────────────────────────────────────

print("\n📌 PART 1 : Mean (Average)\n")

# Ek class ke 10 students ke marks
marks = np.array([45, 78, 62, 89, 55, 71, 83, 47, 66, 74])
print("Students ke marks  :", marks)

# Mean = Saari values ka total / total count
# Jaise 10 logo ki salary add karo aur 10 se divide karo
mean_value = np.mean(marks)
print(f"Mean (Average)     : {mean_value:.2f}")

# Manual tarike se bhi nikal sakte ho — samajhne ke liye
manual_mean = np.sum(marks) / len(marks)
print(f"Manual Mean check  : {manual_mean:.2f}")

print("\n💡 Mean kab use karo?")
print("   Jab data mein koi bahut bada/chota outlier na ho")
print("   Example: Class ka average score nikalna")


# ──────────────────────────────────────────────────────────
# 📌 PART 2 : Median — Beech ka value
# ──────────────────────────────────────────────────────────

print("\n📌 PART 2 : Median (Middle Value)\n")

# Median = Sorted data ka beech wala number
# Mean se better hota hai jab outliers ho
marks_sorted = np.sort(marks)
print("Sorted marks       :", marks_sorted)

median_value = np.median(marks)
print(f"Median             : {median_value:.2f}")

# Outlier ka asar dekho!
marks_with_outlier = np.append(marks, [2, 3])  # do bahut kam marks add karo
print(f"\nOutlier ke saath   : {marks_with_outlier}")
print(f"Mean (outlier ke saath)   : {np.mean(marks_with_outlier):.2f}")    # badal gaya!
print(f"Median (outlier ke saath) : {np.median(marks_with_outlier):.2f}")  # zyada nahi badla

print("\n💡 Median kab use karo?")
print("   Jab data mein outliers ho — jaise salary data mein")
print("   Example: India ki median salary (billionaires se affect nahi hoti)")


# ──────────────────────────────────────────────────────────
# 📌 PART 3 : Mode — Sabse zyada bar aane wala number
# ──────────────────────────────────────────────────────────

print("\n📌 PART 3 : Mode (Most Frequent Value)\n")

# NumPy mein direct mode nahi hai — iska trick use karo
exam_grades = np.array([85, 72, 85, 90, 72, 85, 68, 72, 85, 90])
print("Exam grades        :", exam_grades)

# np.unique se unique values aur unki frequency nikalo
values, counts = np.unique(exam_grades, return_counts=True)
print("Unique values      :", values)
print("Unki frequency     :", counts)

# Sabse zyada bar aane wala — mode
mode_value = values[np.argmax(counts)]
print(f"Mode               : {mode_value}  ({np.max(counts)} baar aaya)")

print("\n💡 Mode kab use karo?")
print("   Categories mein — jaise kaunsa subject sabse popular hai")
print("   Example: Sabse zyada bikne wala product")


# ──────────────────────────────────────────────────────────
# 📌 PART 4 : Variance aur Standard Deviation
# Data kitna spread hai — yeh batata hai
# ──────────────────────────────────────────────────────────

print("\n📌 PART 4 : Variance & Standard Deviation (Spread)\n")

# Do alag classes ke marks compare karo
class_A = np.array([70, 71, 69, 72, 70, 68, 73, 70, 71, 69])  # sab similar
class_B = np.array([40, 95, 55, 88, 30, 99, 45, 80, 62, 75])  # bahut different

print("Class A marks      :", class_A)
print("Class B marks      :", class_B)

# Variance = Average of squared differences from mean
# Std Dev = Variance ka square root
print(f"\nClass A — Mean: {np.mean(class_A):.1f}  |  Std Dev: {np.std(class_A):.2f}")
print(f"Class B — Mean: {np.mean(class_B):.1f}  |  Std Dev: {np.std(class_B):.2f}")

print("\n💡 Matlab:")
print("   Class A std dev kam → sab students similar level par hain")
print("   Class B std dev zyada → kuch bahut achhe, kuch bahut bure")


# ──────────────────────────────────────────────────────────
# 📌 PART 5 : Percentiles — Top X% mein kahan ho?
# ──────────────────────────────────────────────────────────

print("\n📌 PART 5 : Percentiles (Ranking)\n")

scores = np.array([45, 78, 62, 89, 55, 71, 83, 47, 66, 74,
                   58, 91, 63, 82, 50, 77, 88, 43, 69, 75])
print(f"Total students     : {len(scores)}")
print(f"All scores         : {np.sort(scores)}")

# 25th percentile = 25% students isse neeche hain
p25 = np.percentile(scores, 25)
p50 = np.percentile(scores, 50)   # yeh median hi hai!
p75 = np.percentile(scores, 75)
p90 = np.percentile(scores, 90)

print(f"\n25th Percentile    : {p25:.1f}  → 25% students isse neeche")
print(f"50th Percentile    : {p50:.1f}  → Yeh median hai!")
print(f"75th Percentile    : {p75:.1f}  → 75% students isse neeche")
print(f"90th Percentile    : {p90:.1f}  → Top 10% mein jaane ke liye chahiye")

# IQR = Interquartile Range = Q3 - Q1
iqr = p75 - p25
print(f"\nIQR (Q3 - Q1)      : {iqr:.1f}  (middle 50% data ka spread)")


# ──────────────────────────────────────────────────────────
# 📌 PART 6 : Outliers detect karna
# IQR method se — data science mein bahut use hota hai
# ──────────────────────────────────────────────────────────

print("\n📌 PART 6 : Outliers Detect Karna (IQR Method)\n")

data = np.array([52, 61, 73, 68, 55, 77, 64, 58, 70, 66,
                 62, 75, 59, 71, 63, 2, 99, 65, 69, 57])

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

# Lower aur upper boundary set karo
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print(f"Data               : {np.sort(data)}")
print(f"Q1                 : {q1:.1f}")
print(f"Q3                 : {q3:.1f}")
print(f"IQR                : {iqr:.1f}")
print(f"Lower boundary     : {lower_bound:.1f}")
print(f"Upper boundary     : {upper_bound:.1f}")

# Outliers = jo boundary ke bahar hain
outliers = data[(data < lower_bound) | (data > upper_bound)]
normal   = data[(data >= lower_bound) & (data <= upper_bound)]

print(f"\nOutliers           : {outliers}  ← Yeh suspicious hain!")
print(f"Normal data count  : {len(normal)}")

print("\n💡 Real world use:")
print("   Fraud detection mein — koi transaction bahut badi/choti ho")
print("   Quality control mein — defective products pakadna")


print("\n✅ Lesson 2 Complete! Ab Lesson 3 dekho → 03_student_analysis.py")
