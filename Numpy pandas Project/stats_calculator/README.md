# 📊 Statistics Calculator — Python + NumPy + Pandas

A complete teaching project with 6 step-by-step lessons using real-world data.

---

## 📁 Project Structure

```
stats_calculator/
│
├── main.py                     ← Full project run karo
├── stats_calculator.py         ← Core statistics logic
├── README.md
│
├── lessons/                    ← 🎓 Step-by-step lessons
│   ├── 01_numpy_basics.py          Array banana, indexing, masking
│   ├── 02_statistics_basics.py     Mean, Median, Mode, Std Dev, Percentiles
│   ├── 03_student_analysis.py      student_scores.csv ka full analysis
│   ├── 04_weather_analysis.py      weather_data.csv + correlation
│   ├── 05_sales_analysis.py        sales_data.csv + business insights
│   └── 06_numpy_advanced.py        Broadcasting, sorting, reshaping
│
└── data/
    ├── student_scores.csv          100 students (name, subject, score, grade)
    ├── weather_data.csv            100 days (temp, humidity, wind, rainfall)
    ├── sales_data.csv              100 months (revenue, units, city, category)
    └── summary_report.csv          Auto-generated after running main.py
```

---

## ⚙️ Requirements

```bash
pip install numpy pandas
```

---

## ▶️ Lessons ko Order Mein Chalao

```bash
python lessons/01_numpy_basics.py
python lessons/02_statistics_basics.py
python lessons/03_student_analysis.py
python lessons/04_weather_analysis.py
python lessons/05_sales_analysis.py
python lessons/06_numpy_advanced.py
```

## ▶️ Full Project Run Karo

```bash
python main.py
```

---

## 📚 Lesson Summary

| File | Topic | Key Concepts |
|------|-------|-------------|
| `01_numpy_basics.py` | NumPy shuruwat | Arrays, indexing, slicing, boolean masking |
| `02_statistics_basics.py` | Stats fundamentals | Mean, Median, Mode, Std Dev, Percentiles, Outliers |
| `03_student_analysis.py` | Student CSV analysis | groupby, grade distribution, subject-wise avg |
| `04_weather_analysis.py` | Weather CSV analysis | Correlation, moving average, condition counts |
| `05_sales_analysis.py` | Sales CSV analysis | Revenue trends, city/category analysis, spikes |
| `06_numpy_advanced.py` | Advanced NumPy | Broadcasting, fancy indexing, reshape, z-score |

---

## 💡 Hinglish Comments

Saari files mein **Hinglish comments** hain — English + Hindi mix — 
taaki concept asaani se samajh aaye!

Example:
```python
# Yeh ek normal Python list hai
normal_list = [10, 20, 30, 40, 50]

# Isko NumPy array mein convert karo — zyada powerful hota hai
numpy_array = np.array([10, 20, 30, 40, 50])
```

---

## 🚀 Next Steps (After Completing Lessons)

1. **Matplotlib add karo** — histograms, box plots banana
2. **Apna CSV daal ke analyze karo** — koi bhi real data
3. **Linear Regression project** — next level ML
4. **Stock Price Analyzer** — time-series analysis
