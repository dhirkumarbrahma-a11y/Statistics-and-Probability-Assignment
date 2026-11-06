"""
Statistics & Probability - Session 1
Topic: Measures of Central Tendency & Sampling Concepts
Simulated Zomato Order Amount Analysis
"""

import numpy as np
import pandas as pd
from scipy import stats

# 1. 20 Simulated Zomato Order Amounts (in INR)
order_amounts = [
    250, 420, 150, 320, 680, 250, 850, 490, 310, 720,
    540, 250, 890, 630, 180, 350, 420, 950, 510, 480
]

df = pd.DataFrame({"Order_Amount": order_amounts})

# 2. Measures of Central Tendency (Population of 20 orders)
pop_mean = np.mean(order_amounts)
pop_median = np.median(order_amounts)
pop_mode = stats.mode(order_amounts, keepdims=True).mode[0]

# 3. Sample of First 5 Orders
sample_5 = order_amounts[:5]
sample_mean = np.mean(sample_5)
diff = sample_mean - pop_mean

print("=== Task 1 & 2: Full Dataset (Population of 20 Orders) ===")
print("Order Values:", order_amounts)
print(f"Mean (AVERAGE):   ₹{pop_mean:.2f}")
print(f"Median (MEDIAN): ₹{pop_median:.2f}")
print(f"Mode (MODE):     ₹{pop_mode:.2f}")

print("\n=== Task 3: Sample (First 5 Orders) ===")
print("Sample Values:", sample_5)
print(f"Sample Mean:     ₹{sample_mean:.2f}")
print(f"Population Mean: ₹{pop_mean:.2f}")
print(f"Difference (Sample - Population): ₹{diff:.2f}")
