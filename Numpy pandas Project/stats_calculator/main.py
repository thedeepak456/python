import numpy as np
import pandas as pd
from stats_calculator import calculate_stats

print("\n🚀 Statistics Calculator — Real World Data Analysis")
print("=" * 45)

# ─────────────────────────────────────────
# 📚 Dataset 1 — Student Exam Scores
# ─────────────────────────────────────────
df1 = pd.read_csv("data/student_scores.csv")
scores = df1["score"].values
result1 = calculate_stats(scores, label="Student Exam Scores")

# Extra insight with NumPy
above_pass = np.sum(scores >= 50)
below_pass = np.sum(scores < 50)
print(f"  ✅ Passed (>=50)  : {above_pass} students")
print(f"  ❌ Failed (<50)   : {below_pass} students")

grade_labels = np.where(scores >= 90, "A",
               np.where(scores >= 75, "B",
               np.where(scores >= 60, "C",
               np.where(scores >= 50, "D", "F"))))

unique, counts = np.unique(grade_labels, return_counts=True)
print(f"\n  Grade Distribution:")
for g, c in zip(unique, counts):
    print(f"    Grade {g} : {c} students")


# ─────────────────────────────────────────
# 🌤️ Dataset 2 — Daily Weather Temperatures
# ─────────────────────────────────────────
df2 = pd.read_csv("data/weather_data.csv")
temps = df2["temp_celsius"].values
humidity = df2["humidity_percent"].values

result2 = calculate_stats(temps, label="Daily Temperature (°C)")

# Extra insight
print(f"  🔥 Days above 23°C : {np.sum(temps > 23)}")
print(f"  🥶 Days below 17°C : {np.sum(temps < 17)}")
print(f"  💧 Avg Humidity    : {np.mean(humidity):.1f}%")

# Correlation between temp & humidity
correlation = np.corrcoef(temps, humidity)[0, 1]
print(f"  📉 Temp↔Humidity Correlation: {correlation:.2f}")


# ─────────────────────────────────────────
# 💰 Dataset 3 — Monthly Sales Revenue
# ─────────────────────────────────────────
df3 = pd.read_csv("data/sales_data.csv")
revenue = df3["revenue_inr"].values
units = df3["units_sold"].values

result3 = calculate_stats(revenue, label="Monthly Sales Revenue (₹)")

# Extra insight
total_revenue = np.sum(revenue)
avg_per_unit = np.mean(revenue / units)
best_month_idx = np.argmax(revenue)
worst_month_idx = np.argmin(revenue)

print(f"  💵 Total Revenue   : ₹{total_revenue:,.0f}")
print(f"  📦 Avg Revenue/Unit: ₹{avg_per_unit:.2f}")
print(f"  🏆 Best Month      : {df3['month'].iloc[best_month_idx]} (₹{revenue[best_month_idx]:,.0f})")
print(f"  📉 Worst Month     : {df3['month'].iloc[worst_month_idx]} (₹{revenue[worst_month_idx]:,.0f})")

# Category-wise revenue using Pandas groupby
print(f"\n  📂 Revenue by Category:")
cat_summary = df3.groupby("category")["revenue_inr"].sum()
for cat, rev in cat_summary.items():
    print(f"    {cat:<15}: ₹{rev:,.0f}")


# ─────────────────────────────────────────
# 📋 Export All Results to Summary CSV
# ─────────────────────────────────────────
summary_df = pd.DataFrame([result1, result2, result3])
summary_df.to_csv("data/summary_report.csv", index=False)
print(f"\n\n📁 Summary report saved → data/summary_report.csv ✅")
print("=" * 45)
