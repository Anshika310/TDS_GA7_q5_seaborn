# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Email in comment
# 23f2004584@ds.study.iitm.ac.in

# Set professional styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic monthly revenue data for 3 customer segments over a year
months = pd.date_range(start="2024-01-01", periods=12, freq="M").strftime('%b')
segments = ["Premium", "Standard", "Budget"]

np.random.seed(42)
data = {
    "Month": np.tile(months, len(segments)),
    "Segment": np.repeat(segments, len(months)),
    "Revenue": np.concatenate([
        np.random.normal(loc=120000, scale=10000, size=12) + np.linspace(0, 15000, 12),  # Premium
        np.random.normal(loc=80000, scale=8000, size=12) + np.linspace(0, 10000, 12),    # Standard
        np.random.normal(loc=40000, scale=5000, size=12) + np.linspace(0, 5000, 12),     # Budget
    ])
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(8, 8))  # 8x8 inches → 512x512 pixels @ 64 dpi

sns.lineplot(data=df, x="Month", y="Revenue", hue="Segment", marker="o",
             palette="Set2", linewidth=2.5)

plt.title("Monthly Revenue Trend by Customer Segment (2024)", fontsize=18)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Revenue (USD)", fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

# Save figure as PNG 512x512 px
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
plt.close()
