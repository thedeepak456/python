# ============================================================
#  LESSON 5 — Sales Data Analysis 💰
#  sales_data.csv analyze karo — revenue, categories,
#  cities, trends, aur business insights nikalo
# ============================================================

import numpy as np
import pandas as pd

print("=" * 55)
print("  LESSON 5 : Sales Data Analysis")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# 📌 PART 1 : Data Load aur Quick Overview
# ──────────────────────────────────────────────────────────

print("\n📌 PART 1 : Data Load aur Overview\n")

df = pd.read_csv("data/sales_data.csv")

print("Pehli 5 rows:")
print(df.head())
print(f"\nTotal records      : {df.shape[0]}")
print(f"Columns            : {list(df.columns)}")

# Basic Pandas describe — quick summary
print("\nPandas .describe() — Quick Stats:")
print(df[["revenue_inr", "units_sold", "profit_margin_pct"]].describe().round(2))


# ──────────────────────────────────────────────────────────
# 📌 PART 2 : Revenue ka Overall Analysis
# ──────────────────────────────────────────────────────────

print("\n📌 PART 2 : Revenue Overview 💵\n")

revenue = df["revenue_inr"].values  # NumPy array bana lo

total_revenue = np.sum(revenue)
avg_revenue   = np.mean(revenue)
median_rev    = np.median(revenue)

print(f"  Total Revenue    : ₹{total_revenue:,.0f}")
print(f"  Average Revenue  : ₹{avg_revenue:,.0f}")
print(f"  Median Revenue   : ₹{median_rev:,.0f}")

# Agar mean > median toh data right-skewed hai
# Matlab kuch months mein bahut zyada sale hoti hai
if avg_revenue > median_rev:
    diff = ((avg_revenue - median_rev) / median_rev) * 100
    print(f"\n  ⚠️  Mean > Median ({diff:.1f}% difference)")
    print(f"  Matlab: Kuch months mein SPIKE aayi — data right-skewed hai!")
    print(f"  (Festival season ki wajah se hota hai usually 🎉)")


# ──────────────────────────────────────────────────────────
# 📌 PART 3 : High Revenue vs Low Revenue Months
# ──────────────────────────────────────────────────────────

print("\n📌 PART 3 : High vs Low Revenue Months\n")

# Median se upar aur neeche wale months
high_months = np.sum(revenue > median_rev)
low_months  = np.sum(revenue <= median_rev)
print(f"  Median se upar months  : {high_months}")
print(f"  Median se neeche months: {low_months}")

# Top 10% revenue wale months — np.percentile use karo
p90 = np.percentile(revenue, 90)
top_months_mask = revenue >= p90
top_months_df   = df[top_months_mask]

print(f"\n  Top 10% revenue months (above ₹{p90:,.0f}):")
print(f"  {'Month':<12} | {'Year'} | {'City':<12} | {'Revenue':>12}")
print(f"  {'-'*50}")
for _, row in top_months_df.iterrows():
    print(f"  {row['month']:<12} | {row['year']} | "
          f"{row['city']:<12} | ₹{row['revenue_inr']:>10,.0f}")


# ──────────────────────────────────────────────────────────
# 📌 PART 4 : Category-wise Analysis — Pandas groupby
# ──────────────────────────────────────────────────────────

print("\n📌 PART 4 : Category-wise Revenue 📦\n")

# groupby ka magic — category ke hisaab se group karo
cat_revenue = df.groupby("category")["revenue_inr"].agg(
    total="sum",
    average="mean",
    count="count"
).round(0)

# Sort karo descending order mein — sabse zyada revenue pehle
cat_revenue = cat_revenue.sort_values("total", ascending=False)

print(f"  {'Category':<14} | {'Count':>5} | {'Total Revenue':>14} | {'Avg/Month':>12}")
print(f"  {'-'*58}")
for cat, row in cat_revenue.iterrows():
    print(f"  {cat:<14} | {int(row['count']):>5} | "
          f"₹{row['total']:>12,.0f} | ₹{row['average']:>10,.0f}")

# Best category
best_cat  = cat_revenue.index[0]
worst_cat = cat_revenue.index[-1]
print(f"\n  🏆 Best Category  : {best_cat}")
print(f"  📉 Worst Category : {worst_cat}")

# Category revenue as percentage of total
print(f"\n  Revenue % by category:")
for cat, row in cat_revenue.iterrows():
    pct = row["total"] / total_revenue * 100
    bar = "█" * int(pct / 2)
    print(f"  {cat:<14} : {pct:5.1f}% {bar}")


# ──────────────────────────────────────────────────────────
# 📌 PART 5 : City-wise Analysis
# ──────────────────────────────────────────────────────────

print("\n📌 PART 5 : City-wise Performance 🏙️\n")

city_stats = df.groupby("city")["revenue_inr"].agg(
    total="sum",
    average="mean",
    count="count"
).sort_values("total", ascending=False)

print(f"  {'City':<12} | {'Months':>6} | {'Total Revenue':>14} | {'Avg/Month':>12}")
print(f"  {'-'*54}")
for city, row in city_stats.iterrows():
    print(f"  {city:<12} | {int(row['count']):>6} | "
          f"₹{row['total']:>12,.0f} | ₹{row['average']:>10,.0f}")

# NumPy se city revenues ka array banakar statistics nikalo
city_totals = city_stats["total"].values
print(f"\n  City revenue std dev : ₹{np.std(city_totals):,.0f}")
print(f"  (Zyada std dev → cities mein bahut inequality hai)")


# ──────────────────────────────────────────────────────────
# 📌 PART 6 : Month-wise Trend — Seasonal Pattern
# ──────────────────────────────────────────────────────────

print("\n📌 PART 6 : Monthly Revenue Trend 📅\n")

month_order = ["January","February","March","April","May","June",
               "July","August","September","October","November","December"]

# Months ko order mein rakhne ke liye Categorical use karo
df["month"] = pd.Categorical(df["month"], categories=month_order, ordered=True)
monthly_avg = df.groupby("month")["revenue_inr"].mean().round(0)

print("  Month          | Avg Revenue   | Trend")
print("  " + "-" * 45)
overall_avg = np.mean(revenue)
for month, avg in monthly_avg.items():
    trend = "📈 HIGH" if avg > overall_avg * 1.3 else \
            "📉 LOW"  if avg < overall_avg * 0.7 else "➡️ NORMAL"
    print(f"  {month:<14} | ₹{avg:>10,.0f}  | {trend}")


# ──────────────────────────────────────────────────────────
# 📌 PART 7 : Profit Margin Analysis
# ──────────────────────────────────────────────────────────

print("\n📌 PART 7 : Profit Margin Analysis 📊\n")

profit = df["profit_margin_pct"].values

print(f"  Average Margin   : {np.mean(profit):.2f}%")
print(f"  Highest Margin   : {np.max(profit):.2f}%")
print(f"  Lowest Margin    : {np.min(profit):.2f}%")
print(f"  Std Dev          : {np.std(profit):.2f}%")

# High profit wale records
high_profit_mask = profit > np.percentile(profit, 75)
high_profit_df   = df[high_profit_mask]

# Kaunsi category mein profit zyada hai
print(f"\n  Category-wise avg profit margin:")
cat_profit = df.groupby("category")["profit_margin_pct"].mean().sort_values(ascending=False)
for cat, margin in cat_profit.items():
    print(f"    {cat:<14} : {margin:.1f}%")


# ──────────────────────────────────────────────────────────
# 📌 PART 8 : Outlier Revenue Months — Festive Spikes
# ──────────────────────────────────────────────────────────

print("\n📌 PART 8 : Outlier Detection — Festive Sale Spikes 🎉\n")

q1 = np.percentile(revenue, 25)
q3 = np.percentile(revenue, 75)
iqr = q3 - q1
upper_bound = q3 + 1.5 * iqr
lower_bound = q1 - 1.5 * iqr

print(f"  Normal revenue range: ₹{lower_bound:,.0f}  to  ₹{upper_bound:,.0f}")

spike_mask = revenue > upper_bound
spike_df   = df[spike_mask]
print(f"\n  {len(spike_df)} exceptional revenue months (spikes):")
for _, row in spike_df.iterrows():
    extra = ((row["revenue_inr"] - avg_revenue) / avg_revenue) * 100
    print(f"    🎉 {row['month']} {row['year']} | {row['city']} | "
          f"{row['category']} | ₹{row['revenue_inr']:,.0f}  "
          f"(+{extra:.0f}% above avg)")


# ──────────────────────────────────────────────────────────
# 📌 PART 9 : Units Sold vs Revenue Correlation
# ──────────────────────────────────────────────────────────

print("\n📌 PART 9 : Units Sold ↔ Revenue Correlation\n")

units = df["units_sold"].values
corr = np.corrcoef(units, revenue)[0, 1]
print(f"  Correlation: {corr:.3f}")
if corr > 0.7:
    print("  ✅ Strong positive — zyada units becho, zyada revenue")
elif corr > 0.3:
    print("  ➡️ Moderate — kuch relation hai")
else:
    print("  ⚠️ Weak — revenue sirf units par depend nahi karta")

# Revenue per unit
rev_per_unit = revenue / units
print(f"\n  Avg Revenue per unit   : ₹{np.mean(rev_per_unit):.2f}")
print(f"  Max Revenue per unit   : ₹{np.max(rev_per_unit):.2f}")
print(f"  Min Revenue per unit   : ₹{np.min(rev_per_unit):.2f}")


print("\n✅ Lesson 5 Complete! Ab Lesson 6 dekho → 06_numpy_advanced.py")
