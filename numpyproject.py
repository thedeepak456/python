# =========================================================
# Employee Data Analysis Project
# =========================================================

# NumPy library import kar rahe hain
import numpy as np


# =========================================================
# DATASET SETUP
# =========================================================

# Same random data har baar generate hoga
np.random.seed(42)

# Total employees
n = 100


# ---------------------------------------------------------
# Basic Employee Information
# ---------------------------------------------------------

# Employee IDs : 1 se 100 tak
employee_id = np.arange(1, 101)

# Random age : 22 se 59 ke beech
age = np.random.randint(22, 60, n)

# Experience : 0 se 29 years
experience = np.random.randint(0, 30, n)


# ---------------------------------------------------------
# Quarterly Sales Data
# uniform() = decimal random numbers
# round(...,2) = 2 decimal places
# ---------------------------------------------------------

sales_q1 = np.round(
    np.random.uniform(5000, 50000, n),
    2
)

sales_q2 = np.round(
    np.random.uniform(5000, 50000, n),
    2
)

sales_q3 = np.round(
    np.random.uniform(5000, 50000, n),
    2
)

sales_q4 = np.round(
    np.random.uniform(5000, 50000, n),
    2
)


# ---------------------------------------------------------
# Salary & Target
# ---------------------------------------------------------

# Salary : 30k se 120k tak
salary = np.round(
    np.random.uniform(30000, 120000, n),
    2
)

# Sales target
target = np.round(
    np.random.uniform(40000, 160000, n),
    2
)


# ---------------------------------------------------------
# Random Category Data
# choice() = given list me se random value choose karta hai
# ---------------------------------------------------------

# Region assign
region = np.random.choice(
    ['North', 'South', 'East', 'West'],
    n
)

# Gender assign
gender = np.random.choice(
    ['M', 'F'],
    n
)

# Department assign
department = np.random.choice(
    ['Tech', 'Sales', 'HR', 'Finance'],
    n
)


# ---------------------------------------------------------
# Employee Rating
# 1 se 5 tak
# ---------------------------------------------------------

rating = np.random.randint(1, 6, n)


# ---------------------------------------------------------
# Bonus Calculation
#
# Agar rating >= 4 :
#     15% bonus
#
# Warna :
#     5% bonus
# ---------------------------------------------------------

bonus = np.where(
    rating >= 4,
    salary * 0.15,
    salary * 0.05
)


# ---------------------------------------------------------
# Total Yearly Sales
# Sabhi quarters ka total
# ---------------------------------------------------------

total_sales = (
    sales_q1 +
    sales_q2 +
    sales_q3 +
    sales_q4
)


# =========================================================
# SECTION A — Descriptive Statistics
# =========================================================

print("=" * 60)
print("SECTION A — Descriptive Statistics")
print("=" * 60)


# ---------------------------------------------------------
# A-i. Mean, Median, Standard Deviation
# ---------------------------------------------------------

print("\nA-i. Mean, Median, Std Dev of total_sales:")

# Average sales
print(f"     Mean   : {np.mean(total_sales):.2f}")

# Middle value
print(f"     Median : {np.median(total_sales):.2f}")

# Data kitna spread hai
print(f"     Std Dev: {np.std(total_sales):.2f}")


# ---------------------------------------------------------
# A-ii. Minimum, Maximum, Range
# ---------------------------------------------------------

print("\nA-ii. Min, Max, Range of salary:")

print(f"     Min   : {np.min(salary):.2f}")

print(f"     Max   : {np.max(salary):.2f}")

# Range = max - min
print(f"     Range : {np.max(salary) - np.min(salary):.2f}")


# ---------------------------------------------------------
# A-iii. Percentiles
# ---------------------------------------------------------

print("\nA-iii. Percentiles of total_sales:")

print(f"     25th : {np.percentile(total_sales, 25):.2f}")

print(f"     50th : {np.percentile(total_sales, 50):.2f}")

print(f"     75th : {np.percentile(total_sales, 75):.2f}")


# ---------------------------------------------------------
# A-iv. Variance
# ---------------------------------------------------------

print("\nA-iv. Variance:")

print(f"     Salary Variance: {np.var(salary):.2f}")

print(f"     Bonus  Variance: {np.var(bonus):.2f}")


# =========================================================
# SECTION B — Filtering & Conditional Analysis
# =========================================================

print("\n" + "=" * 60)
print("SECTION B — Filtering & Conditional Analysis")
print("=" * 60)


# ---------------------------------------------------------
# B-i. Employees who achieved target
# ---------------------------------------------------------

print("\nB-i. Employees who exceeded their target:")

# Jinka sales target se zyada hai
exceeded = employee_id[total_sales > target]

print(f"     Count           : {len(exceeded)}")

print(f"     Employee IDs    : {exceeded}")


# ---------------------------------------------------------
# B-ii. Employees with rating 5
# ---------------------------------------------------------

print("\nB-ii. Employees with rating == 5:")

# Mask = True/False filter
mask_r5 = rating == 5

print(f"     Count    : {np.sum(mask_r5)}")

print(f"     Salaries : {salary[mask_r5]}")

print(f"     Bonuses  : {bonus[mask_r5]}")


# ---------------------------------------------------------
# B-iii. North region + experience > 10
# ---------------------------------------------------------

print("\nB-iii. North region & experience > 10:")

mask_north_exp = (
    (region == 'North') &
    (experience > 10)
)

print(f"     Count       : {np.sum(mask_north_exp)}")

print(f"     Employee IDs: {employee_id[mask_north_exp]}")


# ---------------------------------------------------------
# B-iv. Above Average Salary
# ---------------------------------------------------------

print("\nB-iv. Employees earning above average salary:")

# Average salary
avg_salary = np.mean(salary)

# Kitne employees average se zyada kama rahe hain
above_avg = np.sum(salary > avg_salary)

print(f"     Average Salary : {avg_salary:.2f}")

print(f"     Count Above Avg: {above_avg}")


# =========================================================
# SECTION C — Aggregation & Grouping
# =========================================================

print("\n" + "=" * 60)
print("SECTION C — Aggregation & Grouping")
print("=" * 60)


# ---------------------------------------------------------
# C-i. Average sales per region
# ---------------------------------------------------------

print("\nC-i. Average total_sales per region:")

for r in ['North', 'South', 'East', 'West']:

    # Particular region ka average
    avg = np.mean(total_sales[region == r])

    print(f"     {r:6s}: {avg:.2f}")


# ---------------------------------------------------------
# C-ii. Department with highest average salary
# ---------------------------------------------------------

print("\nC-ii. Department with highest average salary:")

depts = ['Tech', 'Sales', 'HR', 'Finance']

# Har department ki average salary
dept_avgs = [
    np.mean(salary[department == d])
    for d in depts
]

# Highest salary wala department
best_dept = depts[np.argmax(dept_avgs)]

print(f"     Best Department: {best_dept} ({np.max(dept_avgs):.2f})")


# ---------------------------------------------------------
# C-iii. Total bonus paid
# ---------------------------------------------------------

print("\nC-iii. Total bonus paid:")

print(f"     Total Bonus: {np.sum(bonus):.2f}")


# ---------------------------------------------------------
# C-iv. Average age per rating
# ---------------------------------------------------------

print("\nC-iv. Average age per rating:")

for r in range(1, 6):

    avg_age = np.mean(age[rating == r])

    print(f"     Rating {r}: avg age = {avg_age:.1f}")


# =========================================================
# SECTION D — Correlation & Relationship
# =========================================================

print("\n" + "=" * 60)
print("SECTION D — Correlation & Relationship")
print("=" * 60)


# ---------------------------------------------------------
# D-i. Correlation : experience vs total_sales
# ---------------------------------------------------------

print("\nD-i. Correlation — experience vs total_sales:")

corr_exp_sales = np.corrcoef(
    experience,
    total_sales
)[0, 1]

print(f"     Correlation: {corr_exp_sales:.4f}")


# ---------------------------------------------------------
# D-ii. Correlation : age vs salary
# ---------------------------------------------------------

print("\nD-ii. Correlation — age vs salary:")

corr_age_sal = np.corrcoef(
    age,
    salary
)[0, 1]

print(f"     Correlation: {corr_age_sal:.4f}")


# ---------------------------------------------------------
# D-iii. Covariance : salary vs bonus
# ---------------------------------------------------------

print("\nD-iii. Covariance — salary vs bonus:")

cov_sal_bonus = np.cov(
    salary,
    bonus
)[0, 1]

print(f"     Covariance: {cov_sal_bonus:.2f}")


# ---------------------------------------------------------
# D-iv. Best Quarter
# ---------------------------------------------------------

print("\nD-iv. Quarter with highest average sales:")

quarters = [
    sales_q1,
    sales_q2,
    sales_q3,
    sales_q4
]

# Har quarter ka average
q_avgs = [np.mean(q) for q in quarters]

# Highest average wala quarter
best_q = np.argmax(q_avgs) + 1

print(f"     Best Quarter: Q{best_q} (avg = {np.max(q_avgs):.2f})")

for i, avg in enumerate(q_avgs):

    print(f"     Q{i+1}: {avg:.2f}")


# =========================================================
# SECTION E — Outlier & Z-Score Detection
# =========================================================

print("\n" + "=" * 60)
print("SECTION E — Outlier & Z-Score Detection")
print("=" * 60)


# ---------------------------------------------------------
# E-i. Z-score & Outliers
# ---------------------------------------------------------

print("\nE-i. Z-scores of total_sales (outliers where |Z| > 2):")

# Z-score formula
z_scores = (
    (total_sales - np.mean(total_sales))
    / np.std(total_sales)
)

# Outlier IDs
outlier_ids = employee_id[np.abs(z_scores) > 2]

print(f"     Outlier count       : {len(outlier_ids)}")

print(f"     Outlier Employee IDs: {outlier_ids}")


# ---------------------------------------------------------
# E-ii. Very High Salary Employees
# ---------------------------------------------------------

print("\nE-ii. Salary > 2 std devs above mean:")

sal_mean = np.mean(salary)

sal_std = np.std(salary)

# High salary employees
high_sal = employee_id[
    salary > sal_mean + 2 * sal_std
]

print(f"     Threshold    : {sal_mean + 2 * sal_std:.2f}")

print(f"     Count        : {len(high_sal)}")

print(f"     Employee IDs : {high_sal}")


# ---------------------------------------------------------
# E-iii. Replace Outliers with Median
# ---------------------------------------------------------

print("\nE-iii. Replace outlier total_sales with median:")

# Median value
med_sales = np.median(total_sales)

# Outliers ko median se replace karna
cleaned_sales = np.where(
    np.abs(z_scores) > 2,
    med_sales,
    total_sales
)

print(f"     Median value used : {med_sales:.2f}")

print(f"     Values replaced   : {len(outlier_ids)}")

print(f"     New mean          : {np.mean(cleaned_sales):.2f}")


# =========================================================
# SECTION F — Ranking & Sorting
# =========================================================

print("\n" + "=" * 60)
print("SECTION F — Ranking & Sorting")
print("=" * 60)


# ---------------------------------------------------------
# F-i. Top 10 employees by sales
# ---------------------------------------------------------

print("\nF-i. Top 10 employees by total_sales:")

# argsort() = sorting indexes deta hai
top10_idx = np.argsort(total_sales)[::-1][:10]

print(f"     Employee IDs : {employee_id[top10_idx]}")

print(f"     Total Sales  : {np.round(total_sales[top10_idx], 2)}")


# ---------------------------------------------------------
# F-ii. Bottom 5 salaries
# ---------------------------------------------------------

print("\nF-ii. Bottom 5 employees by salary:")

bot5_idx = np.argsort(salary)[:5]

print(f"     Employee IDs : {employee_id[bot5_idx]}")

print(f"     Salaries     : {np.round(salary[bot5_idx], 2)}")


# ---------------------------------------------------------
# F-iii. Highest bonus employee
# ---------------------------------------------------------

print("\nF-iii. Employee with highest bonus:")

max_bonus_idx = np.argmax(bonus)

print(f"     Employee ID  : {employee_id[max_bonus_idx]}")

print(f"     Bonus Amount : {bonus[max_bonus_idx]:.2f}")


# =========================================================
# Program Complete
# =========================================================

print("\n" + "=" * 60)
print("All sections complete!")
print("=" * 60)