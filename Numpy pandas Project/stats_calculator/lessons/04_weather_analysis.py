# ============================================================
#  LESSON 4 — Weather Data Analysis 🌤️
#  weather_data.csv analyze karo — temperature, humidity,
#  correlation, aur patterns dhundho
# ============================================================

import numpy as np
import pandas as pd

print("=" * 55)
print("  LESSON 4 : Weather Data Analysis")
print("=" * 55)


# ──────────────────────────────────────────────────────────
# 📌 PART 1 : Data Load aur Explore Karna
# ──────────────────────────────────────────────────────────

print("\n📌 PART 1 : Data Load Karna\n")

df = pd.read_csv("data/weather_data.csv")

print("Pehli 5 rows:")
print(df.head())
print(f"\nTotal rows         : {df.shape[0]}")
print(f"Total columns      : {df.shape[1]}")
print(f"Date range         : {df['date'].iloc[0]}  to  {df['date'].iloc[-1]}")

# Missing values check karo — real world data mein hoti hain
print(f"\nMissing values:")
print(df.isnull().sum())


# ──────────────────────────────────────────────────────────
# 📌 PART 2 : Temperature Analysis
# ──────────────────────────────────────────────────────────

print("\n📌 PART 2 : Temperature Analysis 🌡️\n")

# .values lagao — NumPy array mil jaata hai
temp = df["temp_celsius"].values

print(f"  Average Temp     : {np.mean(temp):.2f}°C")
print(f"  Median Temp      : {np.median(temp):.2f}°C")
print(f"  Std Dev          : {np.std(temp):.2f}°C")
print(f"  Hottest Day      : {np.max(temp):.1f}°C  (Day {np.argmax(temp) + 1})")
print(f"  Coldest Day      : {np.min(temp):.1f}°C  (Day {np.argmin(temp) + 1})")

# Temperature ko categories mein baanto
hot_days    = np.sum(temp > 28)   # 28 se zyada
warm_days   = np.sum((temp >= 20) & (temp <= 28))
cool_days   = np.sum(temp < 20)   # 20 se kam

print(f"\n  🔥 Hot days (>28°C)    : {hot_days}")
print(f"  😊 Warm days (20-28°C) : {warm_days}")
print(f"  🥶 Cool days (<20°C)   : {cool_days}")

# Percentage nikalo — broadcasting use karo
print(f"\n  Hot days %     : {hot_days / len(temp) * 100:.1f}%")
print(f"  Warm days %    : {warm_days / len(temp) * 100:.1f}%")
print(f"  Cool days %    : {cool_days / len(temp) * 100:.1f}%")


# ──────────────────────────────────────────────────────────
# 📌 PART 3 : Humidity Analysis
# ──────────────────────────────────────────────────────────

print("\n📌 PART 3 : Humidity Analysis 💧\n")

humidity = df["humidity_percent"].values

print(f"  Average Humidity : {np.mean(humidity):.1f}%")
print(f"  Min Humidity     : {np.min(humidity):.1f}%")
print(f"  Max Humidity     : {np.max(humidity):.1f}%")

# Barish wale din — humidity 75% se zyada
high_humidity_days = np.sum(humidity > 75)
dry_days           = np.sum(humidity < 50)
print(f"\n  Humid days (>75%)  : {high_humidity_days}  (Rain ho sakti hai)")
print(f"  Dry days (<50%)    : {dry_days}  (Dry weather)")

# Percentiles
p25_h = np.percentile(humidity, 25)
p75_h = np.percentile(humidity, 75)
print(f"\n  25th percentile humidity : {p25_h:.1f}%")
print(f"  75th percentile humidity : {p75_h:.1f}%")


# ──────────────────────────────────────────────────────────
# 📌 PART 4 : Correlation — Do cheezein milke kaise chalti hain?
# np.corrcoef — bahut important concept hai!
# ──────────────────────────────────────────────────────────

print("\n📌 PART 4 : Correlation Analysis 📊\n")

print("💡 Correlation kya hota hai?")
print("   +1  → Dono saath badhte hain (jaise age aur experience)")
print("    0  → Koi relation nahi")
print("   -1  → Ek badhta hai, doosra ghatta hai")
print()

# Temperature aur Humidity ka relation
corr_temp_humidity = np.corrcoef(temp, humidity)[0, 1]
print(f"  Temp ↔ Humidity Correlation   : {corr_temp_humidity:.3f}")
if corr_temp_humidity < -0.5:
    print("  → Matlab: Jab temperature badhta hai, humidity kam hoti hai! 🔥💨")
elif corr_temp_humidity > 0.5:
    print("  → Matlab: Temperature aur humidity saath badhte hain!")
else:
    print("  → Matlab: Temperature aur humidity mein zyada relation nahi")

# Temperature aur Rainfall ka relation
rainfall = df["rainfall_mm"].values
corr_temp_rain = np.corrcoef(temp, rainfall)[0, 1]
print(f"\n  Temp ↔ Rainfall Correlation    : {corr_temp_rain:.3f}")

# Humidity aur Rainfall ka relation
corr_humidity_rain = np.corrcoef(humidity, rainfall)[0, 1]
print(f"  Humidity ↔ Rainfall Correlation: {corr_humidity_rain:.3f}")
if corr_humidity_rain > 0.5:
    print("  → Matlab: Jab humidity zyada hoti hai tab barish zyada hoti hai! ✅")


# ──────────────────────────────────────────────────────────
# 📌 PART 5 : Moving Average — Trend dekhna
# Yeh stock market mein bhi use hota hai!
# ──────────────────────────────────────────────────────────

print("\n📌 PART 5 : Moving Average (7-Day) 📈\n")

# np.convolve se moving average nikalte hain
# window = 7 matlab 7 din ka average
window = 7
weights = np.ones(window) / window   # har din ko equal weight dete hain

# 'valid' mode = sirf wahan jahan poora window fit ho
moving_avg = np.convolve(temp, weights, mode='valid')

print(f"  Original temp array length : {len(temp)}")
print(f"  Moving avg array length    : {len(moving_avg)}")
print(f"  (Difference = window - 1 = {window - 1})")

print(f"\n  Pehle 7 din ka raw avg    : {np.mean(temp[:7]):.2f}°C")
print(f"  7-day moving avg (day 7)  : {moving_avg[0]:.2f}°C")
print("  (Same hona chahiye! ✅)")

print(f"\n  Overall trend:")
print(f"  Pehle 10 din avg  : {np.mean(moving_avg[:10]):.2f}°C")
print(f"  Aakhri 10 din avg : {np.mean(moving_avg[-10:]):.2f}°C")
if np.mean(moving_avg[-10:]) > np.mean(moving_avg[:10]):
    print("  → Temperature increase ho raha hai (garmi aa rahi hai! 🌞)")
else:
    print("  → Temperature decrease ho raha hai (thand aa rahi hai! ❄️)")


# ──────────────────────────────────────────────────────────
# 📌 PART 6 : Weather Conditions — Pandas value_counts
# ──────────────────────────────────────────────────────────

print("\n📌 PART 6 : Weather Conditions Distribution 🌈\n")

# value_counts — har category kitni baar aayi
condition_counts = df["condition"].value_counts()
print("  Condition        | Count | %")
print("  " + "-" * 40)
for condition, count in condition_counts.items():
    pct  = count / len(df) * 100
    bar  = "█" * int(pct / 2)
    print(f"  {condition:<16} |  {count:3d}  | {pct:5.1f}% {bar}")


# ──────────────────────────────────────────────────────────
# 📌 PART 7 : Wind Speed Analysis
# ──────────────────────────────────────────────────────────

print("\n📌 PART 7 : Wind Speed Analysis 💨\n")

wind = df["wind_speed_kmh"].values

print(f"  Average Wind     : {np.mean(wind):.1f} km/h")
print(f"  Max Wind Speed   : {np.max(wind):.1f} km/h  (Day {np.argmax(wind) + 1})")
print(f"  Min Wind Speed   : {np.min(wind):.1f} km/h")

# Windy days classify karo
calm_days  = np.sum(wind < 10)
breezy     = np.sum((wind >= 10) & (wind < 25))
windy_days = np.sum(wind >= 25)

print(f"\n  Calm days (<10)  : {calm_days}")
print(f"  Breezy (10-25)   : {breezy}")
print(f"  Windy (>25)      : {windy_days}")


# ──────────────────────────────────────────────────────────
# 📌 PART 8 : Day-wise Summary — Best aur Worst Day
# ──────────────────────────────────────────────────────────

print("\n📌 PART 8 : Notable Days 🗓️\n")

# Best day = high temp, low humidity, low wind
best_day_idx   = np.argmax(temp)   # hottest
rainiest_idx   = np.argmax(rainfall)

print(f"  🔥 Hottest Day :")
print(f"     Date: {df['date'].iloc[best_day_idx]}  |  "
      f"Temp: {temp[best_day_idx]:.1f}°C  |  "
      f"Condition: {df['condition'].iloc[best_day_idx]}")

print(f"\n  🌧️ Most Rainfall Day:")
print(f"     Date: {df['date'].iloc[rainiest_idx]}  |  "
      f"Rainfall: {rainfall[rainiest_idx]:.1f}mm  |  "
      f"Humidity: {humidity[rainiest_idx]:.1f}%")


print("\n✅ Lesson 4 Complete! Ab Lesson 5 dekho → 05_sales_analysis.py")
