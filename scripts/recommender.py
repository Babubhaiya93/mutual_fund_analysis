import pandas as pd

metrics = pd.read_csv("../data/processed/performance_metrics.csv")

best_fund = metrics.sort_values(
"Sharpe Ratio",
ascending=False
).head(1)

print("Recommended Fund:")
print(best_fund[["fund_name", "Sharpe Ratio"]])
