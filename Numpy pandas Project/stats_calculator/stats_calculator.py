import numpy as np
import pandas as pd


def calculate_stats(data, label="Dataset"):
    data = np.array(data, dtype=float)

    # IQR & Outliers
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    outliers = data[(data < q1 - 1.5 * iqr) | (data > q3 + 1.5 * iqr)]

    # Skewness (manual)
    skew = np.mean(((data - np.mean(data)) / np.std(data)) ** 3)

    if skew > 0.5:
        skew_label = "(right skewed ➡️)"
    elif skew < -0.5:
        skew_label = "(left skewed ⬅️)"
    else:
        skew_label = "(roughly symmetric ↔️)"

    print(f"\n{'='*45}")
    print(f"  📊  {label}")
    print(f"{'='*45}")
    print(f"  Count          : {len(data)}")
    print(f"  Mean           : {np.mean(data):.2f}")
    print(f"  Median         : {np.median(data):.2f}")
    print(f"  Std Deviation  : {np.std(data):.2f}")
    print(f"  Variance       : {np.var(data):.2f}")
    print(f"  Min            : {np.min(data):.2f}")
    print(f"  Max            : {np.max(data):.2f}")
    print(f"  Range          : {np.ptp(data):.2f}")
    print(f"  25th %ile      : {q1:.2f}")
    print(f"  75th %ile      : {q3:.2f}")
    print(f"  IQR            : {iqr:.2f}")
    print(f"  Skewness       : {skew:.2f}  {skew_label}")

    if len(outliers) > 0:
        print(f"  Outliers       : {np.round(outliers, 2)}")
    else:
        print(f"  Outliers       : None found ✅")

    print(f"{'='*45}")

    # Return as dict for future use
    return {
        "label": label,
        "count": len(data),
        "mean": round(float(np.mean(data)), 2),
        "median": round(float(np.median(data)), 2),
        "std_dev": round(float(np.std(data)), 2),
        "variance": round(float(np.var(data)), 2),
        "min": round(float(np.min(data)), 2),
        "max": round(float(np.max(data)), 2),
        "range": round(float(np.ptp(data)), 2),
        "q1": round(float(q1), 2),
        "q3": round(float(q3), 2),
        "iqr": round(float(iqr), 2),
        "skewness": round(float(skew), 2),
        "outlier_count": len(outliers),
    }
