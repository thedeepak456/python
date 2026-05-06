# ============================================================
#  LESSON 1 — NumPy Basics (Grade Analyzer ke liye foundation)
#  Yahan seekhoge: Arrays, Indexing, Masking, Math Operations
#  Yeh sab Grade Analyzer mein use hoga — dhyan se padho! 🎯
# ============================================================

import numpy as np

print("=" * 56)
print("  LESSON 1 : NumPy Basics — Shuruwat karte hain! 🚀")
print("=" * 56)


# ──────────────────────────────────────────────────────────
# 📌 PART 1 : Array kya hota hai?
# Python list aur NumPy array mein kya fark hai?
# ──────────────────────────────────────────────────────────

print("\n📌 PART 1 : List vs NumPy Array\n")

# Normal Python list — sirf data store karta hai
marks_list = [45, 78, 62, 89, 55, 71, 83, 47, 66, 74]
print("Python list    :", marks_list)

# NumPy array — data + fast math operations dono
marks_array = np.array([45, 78, 62, 89, 55, 71, 83, 47, 66, 74])
print("NumPy array    :", marks_array)

# Fark dekho — list * 2 repeat karta hai, array multiply karta hai!
print("\nList * 2       :", marks_list * 2)    # ❌ yeh repeat karta hai
print("Array * 2      :", marks_array * 2)   # ✅ yeh multiply karta hai

# Grade Analyzer mein hum percentage nikalte hain — array se easy hai
out_of_100 = marks_array   # ye pehle se 100 mein se hai
print("\nPercentage     :", (marks_array / 100 * 100))  # same, sirf concept ke liye


# ──────────────────────────────────────────────────────────
# 📌 PART 2 : Array banane ke tarike
# Grade Analyzer mein alag alag tariko se arrays banenge
# ──────────────────────────────────────────────────────────

print("\n📌 PART 2 : Array Banane ke Tarike\n")

# Direct values deke — student scores
scores = np.array([72, 85, 61, 90, 44, 78, 55, 88, 63, 76])
print("Direct array   :", scores)

# np.zeros — placeholder jab abhi data nahi hai
empty_scores = np.zeros(5)
print("Zeros array    :", empty_scores)

# np.ones — sabko ek weight dene ke liye
weights = np.ones(5)
print("Ones array     :", weights)

# np.arange — student IDs banane ke liye
student_ids = np.arange(1, 11)   # 1 se 10 tak
print("Student IDs    :", student_ids)

# np.linspace — equal steps mein marks ranges
grade_thresholds = np.linspace(0, 100, 6)  # 6 equal points
print("Grade thresholds:", grade_thresholds)

# np.random — practice data banana
random_marks = np.random.randint(30, 100, size=10)
print("Random marks   :", random_marks)


# ──────────────────────────────────────────────────────────
# 📌 PART 3 : Array ki properties jaanna
# Pehle array ko samjho, phir use karo
# ──────────────────────────────────────────────────────────

print("\n📌 PART 3 : Array ki Properties\n")

class_scores = np.array([55, 78, 45, 91, 63, 72, 88, 34, 67, 80,
                          59, 74, 82, 49, 76, 93, 61, 70, 85, 57])
print("Class scores   :", class_scores)

# Shape — rows aur columns kitne hain
print("Shape          :", class_scores.shape)   # (20,) = 1D, 20 elements

# Size — total elements kitne hain
print("Total students :", class_scores.size)

# Dtype — kaunsa data type hai
print("Data type      :", class_scores.dtype)

# Min, Max directly
print("Highest score  :", np.max(class_scores))
print("Lowest score   :", np.min(class_scores))


# ──────────────────────────────────────────────────────────
# 📌 PART 4 : Indexing — specific element nikalna
# Grade Analyzer mein specific student ka data chahiye hota hai
# ──────────────────────────────────────────────────────────

print("\n📌 PART 4 : Indexing\n")

scores = np.array([72, 85, 61, 90, 44, 78, 55, 88, 63, 76])
print("Scores         :", scores)
print("Index numbers  :", np.arange(len(scores)))

# Pehla element — index 0 se shuru hota hai Python mein
print("\n1st student    :", scores[0])

# Aakhri element — negative index se
print("Last student   :", scores[-1])

# Kuch elements — slicing [start:stop] (stop exclude hota hai)
print("Index 2 to 4   :", scores[2:5])     # index 2, 3, 4

# Pehle 3 students
print("Top 3 listed   :", scores[:3])

# Aakhri 3 students
print("Last 3 listed  :", scores[-3:])


# ──────────────────────────────────────────────────────────
# 📌 PART 5 : Boolean Masking — Condition lagake filter karna
# Yeh Grade Analyzer ka sabse important concept hai!
# Pass/Fail, Grade A/B/C sab yahi se karte hain
# ──────────────────────────────────────────────────────────

print("\n📌 PART 5 : Boolean Masking (Filter Karna) ⭐\n")

marks = np.array([72, 85, 61, 90, 44, 78, 55, 88, 63, 76])
print("All marks      :", marks)

# Condition lagao — har element ke liye True/False banta hai
pass_mask = marks >= 60
print("Pass mask      :", pass_mask)     # True = pass, False = fail

# Mask se sirf pass wale lo
passed = marks[pass_mask]
print("Passed marks   :", passed)

# Ek line mein bhi likh sakte ho
failed = marks[marks < 60]
print("Failed marks   :", failed)

# Count karna
print(f"\nTotal students : {len(marks)}")
print(f"Passed         : {np.sum(marks >= 60)}")   # True=1, False=0
print(f"Failed         : {np.sum(marks < 60)}")

# Grade A — 80 se zyada
grade_a = marks[marks >= 80]
print(f"Grade A (>=80) : {grade_a}")


# ──────────────────────────────────────────────────────────
# 📌 PART 6 : Math Operations — Calculations karna
# Grade Analyzer mein yeh sab use hoga — weighted avg etc.
# ──────────────────────────────────────────────────────────

print("\n📌 PART 6 : Math Operations\n")

math_marks    = np.array([70, 85, 55, 90, 65])
science_marks = np.array([80, 75, 60, 85, 70])

print("Math marks     :", math_marks)
print("Science marks  :", science_marks)

# Dono subjects ka total
total = math_marks + science_marks
print("\nTotal (M+S)    :", total)

# Average nikalna
average = total / 2
print("Average        :", average)

# Percentage increase — science ne math se kitna acha kiya
diff = science_marks - math_marks
print("Science - Math :", diff)

# Sabka mean — class average
print("\nClass avg Math :", np.mean(math_marks).round(2))
print("Class avg Sci  :", np.mean(science_marks).round(2))


print("\n✅ Lesson 1 Complete! Ab Lesson 2 → 02_grade_statistics.py")
