# ============================================================
#  LESSON 6 — NumPy Advanced Concepts ⚡
#  Broadcasting, Fancy Indexing, Sorting, Reshaping —
#  yeh sab real world mein bahut kaam aata hai!
# ============================================================

import numpy as np
import pandas as pd

print("=" * 55)
print("  LESSON 6 : NumPy Advanced — Pro Level Tricks")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# 📌 PART 1 : Broadcasting — Loop ke bina math karo
# (Yeh NumPy ki superpower hai!)
# ──────────────────────────────────────────────────────────

print("\n📌 PART 1 : Broadcasting 📡\n")

print("💡 Broadcasting kya hai?")
print("   Alag size ke arrays par seedha math karna")
print("   Loop likhne ki zaroorat nahi!\n")

# Example: Har student ke marks mein 5 bonus marks add karo
marks = np.array([45, 67, 89, 23, 56, 78, 90, 34])
print(f"Original marks   : {marks}")

# Python loop se karna
bonus_loop = []
for m in marks:
    bonus_loop.append(m + 5)
print(f"Loop se +5       : {bonus_loop}")

# NumPy broadcasting se — ek line mein!
bonus_numpy = marks + 5
print(f"NumPy se +5      : {bonus_numpy}")
print("(Dono same result! Lekin NumPy zyada fast aur clean hai ✅)")

# Har mark ko percentage mein convert karo (max 100 maan ke)
percentage = (marks / 100) * 100
print(f"\nPercentage       : {percentage}")

# 2D array broadcasting
print("\n--- 2D Broadcasting Example ---")
# Ek 2D array — 3 students, 4 subjects ke marks
student_marks = np.array([
    [70, 85, 60, 90],   # Student 1
    [55, 78, 82, 65],   # Student 2
    [90, 45, 73, 88],   # Student 3
])
print(f"Student marks (3x4):\n{student_marks}")

# Har subject ka bonus alag hai
subject_bonus = np.array([5, 10, 3, 7])
print(f"Subject bonus    : {subject_bonus}")

# Broadcasting — NumPy automatically har row mein bonus add karta hai
boosted = student_marks + subject_bonus
print(f"After bonus:\n{boosted}")


# ──────────────────────────────────────────────────────────
# 📌 PART 2 : Sorting aur argsort
# argsort = index milta hai, sort nahi hota
# ──────────────────────────────────────────────────────────

print("\n📌 PART 2 : Sorting aur argsort 📋\n")

scores = np.array([67, 45, 89, 23, 78, 56, 91, 34, 62, 80])
names  = ["Raj", "Priya", "Aarav", "Sneha", "Vikram",
          "Ananya", "Karan", "Meera", "Arjun", "Divya"]

print(f"Scores           : {scores}")

# np.sort — sorted array deta hai
sorted_scores = np.sort(scores)
print(f"Sorted scores    : {sorted_scores}")

# np.argsort — index deta hai ki kahan jaana chahiye
sort_idx = np.argsort(scores)
print(f"Sort indices     : {sort_idx}")

# Is index se names ko bhi sort kar sakte ho!
names_arr     = np.array(names)
sorted_names  = names_arr[sort_idx]
print(f"Sorted names     : {sorted_names}")

# Ranking list banana — ascending order mein
print("\n📊 Ranking (Lowest to Highest):")
for rank, (name, score) in enumerate(zip(sorted_names, sorted_scores), 1):
    print(f"   Rank {rank:2d}: {name:<10} → {score}")

# Top 3 kaise nikalen? — last 3 elements (already sorted)
top3_idx   = np.argsort(scores)[-3:][::-1]  # reverse karo — highest pehle
print("\n🏆 Top 3 Students:")
for i, idx in enumerate(top3_idx, 1):
    print(f"   #{i}: {names[idx]} — {scores[idx]}")


# ──────────────────────────────────────────────────────────
# 📌 PART 3 : Reshaping — Array ki shape badalna
# ──────────────────────────────────────────────────────────

print("\n📌 PART 3 : Reshaping Arrays 🔄\n")

# 12 elements wala flat array
flat = np.arange(1, 13)
print(f"Flat array       : {flat}")
print(f"Shape            : {flat.shape}")

# 3 rows, 4 columns mein reshape karo
matrix_3x4 = flat.reshape(3, 4)
print(f"\nReshaped to 3x4:\n{matrix_3x4}")
print(f"Shape            : {matrix_3x4.shape}")

# 4 rows, 3 columns
matrix_4x3 = flat.reshape(4, 3)
print(f"\nReshaped to 4x3:\n{matrix_4x3}")

# -1 use karo — NumPy khud calculate kar lega
auto_reshape = flat.reshape(2, -1)   # 2 rows, columns NumPy decide karega
print(f"\nReshape(2, -1):\n{auto_reshape}")

# Wapas flat karna — ravel
back_flat = matrix_3x4.ravel()
print(f"\nWapas flat       : {back_flat}")


# ──────────────────────────────────────────────────────────
# 📌 PART 4 : Fancy Indexing — Multiple elements ek saath nikalna
# ──────────────────────────────────────────────────────────

print("\n📌 PART 4 : Fancy Indexing 🎯\n")

data = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
print(f"Data array       : {data}")

# Normal indexing — ek element
print(f"Index 3          : {data[3]}")

# Fancy indexing — multiple elements ek saath
indices = [1, 3, 5, 7]   # in indexes pe value chahiye
selected = data[indices]
print(f"Fancy index [1,3,5,7]: {selected}")

# Boolean + Fancy — condition se specific index
even_mask = np.arange(len(data)) % 2 == 0   # even indexes
print(f"Even index values: {data[even_mask]}")

# Real world use: Specific students ke marks nikalna
all_scores = np.array([45, 67, 89, 23, 56, 78, 90, 34, 61, 72])
# Students 2, 5, 8 ke marks chahiye (0-indexed: 1, 4, 7)
specific = all_scores[[1, 4, 7]]
print(f"\nSpecific students' scores: {specific}")


# ──────────────────────────────────────────────────────────
# 📌 PART 5 : np.where — Array pe if-else
# ──────────────────────────────────────────────────────────

print("\n📌 PART 5 : np.where — Array pe If-Else ⚡\n")

scores = np.array([45, 78, 62, 89, 55, 71, 83, 47, 66, 74])
print(f"Scores           : {scores}")

# Simple if-else — pass ya fail
result = np.where(scores >= 50, "PASS", "FAIL")
print(f"Pass/Fail        : {result}")

# Multiple conditions — grades
grades = np.where(scores >= 90, "A",
         np.where(scores >= 75, "B",
         np.where(scores >= 60, "C",
         np.where(scores >= 50, "D", "F"))))
print(f"Grades           : {grades}")

# Values replace karna — outliers ko clip karo
clipped = np.where(scores > 80, 80, scores)   # 80 se zyada ho toh 80 kar do
print(f"Clipped at 80    : {clipped}")

print("\n💡 np.where ka real use:")
print("   → Fraud detection: amount > threshold → 'Suspicious'")
print("   → Weather: temp > 35 → 'Heatwave' warning")
print("   → Sales: revenue > target → 'Achieved' badge")


# ──────────────────────────────────────────────────────────
# 📌 PART 6 : Aggregation Functions — Summary nikalna
# ──────────────────────────────────────────────────────────

print("\n📌 PART 6 : Aggregation Functions Summary 📊\n")

data = np.array([23, 45, 67, 89, 12, 56, 78, 34, 90, 11,
                 55, 76, 43, 28, 92, 61, 38, 84, 47, 69])

print(f"Data array (20 elements):")
print(f"  {data}\n")

print(f"  np.sum()            : {np.sum(data)}")
print(f"  np.mean()           : {np.mean(data):.2f}")
print(f"  np.median()         : {np.median(data):.2f}")
print(f"  np.std()            : {np.std(data):.2f}")
print(f"  np.var()            : {np.var(data):.2f}")
print(f"  np.min()            : {np.min(data)}")
print(f"  np.max()            : {np.max(data)}")
print(f"  np.ptp() (range)    : {np.ptp(data)}")
print(f"  np.argmin()         : index {np.argmin(data)} (value={data[np.argmin(data)]})")
print(f"  np.argmax()         : index {np.argmax(data)} (value={data[np.argmax(data)]})")
print(f"  np.cumsum()[:5]     : {np.cumsum(data)[:5]}")   # running total
print(f"  np.percentile(25)   : {np.percentile(data, 25)}")
print(f"  np.percentile(75)   : {np.percentile(data, 75)}")
print(f"  np.unique() count   : {len(np.unique(data))} unique values")


# ──────────────────────────────────────────────────────────
# 📌 PART 7 : Real Data pe Apply Karo — CSV se
# ──────────────────────────────────────────────────────────

print("\n📌 PART 7 : Sab kuch Real Data pe Apply Karo\n")

df = pd.read_csv("data/sales_data.csv")
revenue = df["revenue_inr"].values

print("Sales Data pe Advanced NumPy:")
print(f"  Cumulative Revenue (first 5 months):")
cumrev = np.cumsum(revenue)
for i in range(5):
    print(f"    Month {i+1}: ₹{cumrev[i]:,.0f}")

# Percent change month over month
pct_change = np.diff(revenue) / revenue[:-1] * 100
print(f"\n  Month-over-month % change (first 5):")
for i in range(5):
    arrow = "📈" if pct_change[i] > 0 else "📉"
    print(f"    Month {i+1}→{i+2}: {pct_change[i]:+.1f}% {arrow}")

# Z-score normalization — machine learning mein use hota hai
z_scores = (revenue - np.mean(revenue)) / np.std(revenue)
print(f"\n  Z-score (normalized) first 5 months:")
for i in range(5):
    print(f"    Month {i+1}: {z_scores[i]:+.2f}  "
          f"({'above' if z_scores[i] > 0 else 'below'} average)")


print("\n" + "=" * 55)
print("  🎓 CONGRATULATIONS! Saari 6 lessons complete!")
print("  Ab tum ek real Statistics Calculator bana sakte ho!")
print("=" * 55)
print("\n  Next Steps:")
print("  1. main.py run karo — full project dekhne ke liye")
print("  2. Data mein changes karo aur output observe karo")
print("  3. Apna naya dataset CSV mein daal ke analyze karo")
print("  4. Matplotlib add karo — graphs banana seekho! 📈")
