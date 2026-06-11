import pandas as pd
import numpy as np

df = pd.read_csv("../data/processed/clean_nav_data.csv")

df["date"] = pd.to_datetime(df["date"], dayfirst=True, format="mixed")
df = df.sort_values(["fund_name", "date"])

df["daily_return"] = df.groupby("fund_name")["nav"].pct_change()

results = []

for fund in df["fund_name"].unique():
temp = df[df["fund_name"] == fund]

```
start_nav = temp["nav"].iloc[0]
end_nav = temp["nav"].iloc[-1]

years = (temp["date"].max() - temp["date"].min()).days / 365

cagr = ((end_nav / start_nav) ** (1 / years) - 1) if years > 0 else np.nan

volatility = temp["daily_return"].std() * np.sqrt(252)

sharpe = ((temp["daily_return"].mean() * 252) - 0.05) / volatility if volatility and volatility > 0 else np.nan

results.append([fund, cagr, volatility, sharpe])
```

metrics = pd.DataFrame(
results,
columns=["fund_name", "CAGR", "Volatility", "Sharpe Ratio"]
)

metrics.to_csv("../data/processed/performance_metrics.csv", index=False)

print("Performance metrics saved successfully")
