# ============================================================
#  LESSON 1 — NumPy Basics (Shuruwat karte hain! 🚀)
#  Yeh file beginners ke liye hai — ek ek cheez samjhayenge
# ============================================================

import numpy as np

print("=" * 55)
print("  LESSON 1 : NumPy Basics — Array banana aur samajhna")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# 📌 PART 1 : Array kya hota hai?
# Normal Python list vs NumPy array ka fark samjho
# ──────────────────────────────────────────────────────────

print("\n📌 PART 1 : List vs NumPy Array\n")

# Yeh ek normal Python list hai
normal_list = [10, 20, 30, 40, 50]
print("Normal Python List :", normal_list)

# Isko NumPy array mein convert karo — zyada powerful hota hai
numpy_array = np.array([10, 20, 30, 40, 50])
print("NumPy Array        :", numpy_array)

# Fark kya hai? — NumPy array pe math seedha hota hai!
# List mein 2x karna mushkil, array mein ek line mein!
print("List * 2 (galat)   :", normal_list * 2)   # yeh repeat karta hai!
print("Array * 2 (sahi)   :", numpy_array * 2)   # yeh sahi multiply karta hai!


# ──────────────────────────────────────────────────────────
# 📌 PART 2 : Array banane ke tarike
# ──────────────────────────────────────────────────────────

print("\n📌 PART 2 : Array banane ke alag alag tarike\n")

# Directly values deke array banana
arr1 = np.array([1, 2, 3, 4, 5])
print("Direct array       :", arr1)

# 0 se 9 tak ka array — range ki tarah
arr2 = np.arange(0, 10)
print("0 se 9 tak         :", arr2)

# Sirf zeros wala array — placeholder ki tarah use hota hai
arr3 = np.zeros(5)
print("Zeros wala array   :", arr3)

# Sirf ones wala array
arr4 = np.ones(5)
print("Ones wala array    :", arr4)

# 0 se 1 ke beech mein 5 equally spaced numbers
arr5 = np.linspace(0, 1, 5)
print("Linspace 0 to 1    :", arr5)

# Random numbers — 1 se 100 ke beech mein 5 numbers
arr6 = np.random.randint(1, 100, size=5)
print("5 Random numbers   :", arr6)


# ──────────────────────────────────────────────────────────
# 📌 PART 3 : Array ki properties
# ──────────────────────────────────────────────────────────

print("\n📌 PART 3 : Array ke baare mein info nikalna\n")

sample = np.array([15, 28, 33, 47, 52, 61, 74, 88, 91, 100])
print("Hamaara Array      :", sample)

# Kitne elements hain array mein
print("Kitne elements hai :", sample.size)       # ya len(sample)

# Array ka shape kya hai (rows, columns)
print("Shape              :", sample.shape)

# Kaunsa data type hai
print("Data type          :", sample.dtype)

# Sabse bada aur chota value
print("Sabse bada (Max)   :", np.max(sample))
print("Sabse chota (Min)  :", np.min(sample))


# ──────────────────────────────────────────────────────────
# 📌 PART 4 : Indexing — Element kaise nikaalte hain?
# ──────────────────────────────────────────────────────────

print("\n📌 PART 4 : Indexing — Element nikalna\n")

marks = np.array([45, 67, 89, 23, 56, 78, 90, 34, 61, 72])
print("Marks array        :", marks)

# Pehla element (index 0 se shuru hota hai)
print("Pehla mark         :", marks[0])

# Aakhri element (negative index)
print("Aakhri mark        :", marks[-1])

# Slice — index 2 se 5 tak (5 exclude)
print("Index 2 to 4       :", marks[2:5])

# Pehle 3 elements
print("Pehle 3 marks      :", marks[:3])

# Aakhri 3 elements
print("Aakhri 3 marks     :", marks[-3:])


# ──────────────────────────────────────────────────────────
# 📌 PART 5 : Boolean Masking — Condition lagana
# (Yeh bahut important hai! Real world mein zyada use hota hai)
# ──────────────────────────────────────────────────────────

print("\n📌 PART 5 : Boolean Masking — Condition se filter karna\n")

scores = np.array([45, 67, 89, 23, 56, 78, 90, 34, 61, 72])
print("Scores             :", scores)

# 50 se zyada marks wale students
pass_mask   = scores >= 50
print("Pass/Fail (True/False):", pass_mask)

# Sirf pass students ke marks
passed = scores[pass_mask]
print("Pass wale marks    :", passed)

# Directly bhi likh sakte ho ek line mein
failed = scores[scores < 50]
print("Fail wale marks    :", failed)

print(f"\nTotal students     : {len(scores)}")
print(f"Pass students      : {np.sum(scores >= 50)}")
print(f"Fail students      : {np.sum(scores < 50)}")


# ──────────────────────────────────────────────────────────
# 📌 PART 6 : Basic Math Operations
# ──────────────────────────────────────────────────────────

print("\n📌 PART 6 : Math Operations\n")

a = np.array([10, 20, 30, 40, 50])
b = np.array([1,  2,  3,  4,  5])

print("a                  :", a)
print("b                  :", b)
print("a + b              :", a + b)       # jod
print("a - b              :", a - b)       # ghatao
print("a * b              :", a * b)       # gunna
print("a / b              :", a / b)       # bhag
print("a ** 2             :", a ** 2)      # square
print("sqrt(a)            :", np.sqrt(a))  # square root


print("\n✅ Lesson 1 Complete! Ab Lesson 2 dekho → 02_statistics_basics.py")
