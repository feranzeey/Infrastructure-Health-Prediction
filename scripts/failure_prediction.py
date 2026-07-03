import pandas as pd

df = pd.read_csv("../data/infrastructure_metrics.csv")

print("\nHistorical Failures\n")

print(df)

risk = df[df["CPU"] > 80]

print("\nPredicted High Risk Days\n")

print(risk)
