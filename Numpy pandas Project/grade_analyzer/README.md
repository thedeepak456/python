# 📊 Grade Analyzer — Python + NumPy + Pandas

A complete teaching project to analyze school grades using real-world data.
Teeno files mein Hinglish comments hain — easy to understand! 🙂

---

## 📁 Project Structure

```
grade_analyzer/
│
├── main.py                        ← Full project run karo (3 tables alag alag)
├── README.md
│
├── lessons/                       ← 🎓 Step-by-step 6 Lessons
│   ├── 01_numpy_basics.py             Arrays, indexing, masking, math ops
│   ├── 02_grade_statistics.py         Mean, Median, Std Dev, Percentiles, Outliers
│   ├── 03_student_grades_analysis.py  student_grades.csv ka full analysis
│   ├── 04_exam_results_analysis.py    exam_results.csv — exam-wise trends
│   ├── 05_class_performance_analysis.py  class_performance.csv — school insights
│   └── 06_advanced_analysis.py        Weighted avg, Z-score, Correlation matrix
│
└── data/
    ├── student_grades.csv         ← 100 students (5 subjects, grade, rank)
    ├── exam_results.csv           ← 100 exams (term, subject, marks, grade)
    ├── class_performance.csv      ← 100 records (class × subject trends)
    └── summary_report.csv         ← Auto-generated after running main.py
```

---

## 📂 Data Files

| File | Rows | Key Columns |
|------|------|-------------|
| `student_grades.csv` | 100 | name, class, gender, math, science, english, history, computer, average, grade |
| `exam_results.csv` | 100 | exam_name, term, subject, max_marks, marks_obtained, percentage, grade, result |
| `class_performance.csv` | 100 | class, subject, month, class_avg, pass_percentage, top_score, lowest_score |

---

## ⚙️ Requirements

```bash
pip install numpy pandas
```

---

## ▶️ Lessons — Order mein chalao

```bash
python lessons/01_numpy_basics.py
python lessons/02_grade_statistics.py
python lessons/03_student_grades_analysis.py
python lessons/04_exam_results_analysis.py
python lessons/05_class_performance_analysis.py
python lessons/06_advanced_analysis.py
```

## ▶️ Full Project

```bash
python main.py
```

---

## 📚 Lesson Summary

| Lesson | File | Topic |
|--------|------|-------|
| 1 | `01_numpy_basics.py` | Arrays, indexing, slicing, boolean masking |
| 2 | `02_grade_statistics.py` | Mean, Median, Std Dev, Percentiles, Outliers, np.where |
| 3 | `03_student_grades_analysis.py` | student_grades.csv full analysis |
| 4 | `04_exam_results_analysis.py` | exam_results.csv — exam/term/subject trends |
| 5 | `05_class_performance_analysis.py` | Pivot table, class vs subject, correlation |
| 6 | `06_advanced_analysis.py` | Weighted avg, Z-score, correlation matrix, rankings |

---

## 🚀 Next Steps

1. **Matplotlib add karo** — bar charts, histograms, heatmaps
2. **Apna CSV daal ke analyze karo** — koi bhi real school data
3. **Next Project**: Stock Price Analyzer → Linear Regression
