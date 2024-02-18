import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns


with open("events.json.txt", "r") as file:
  data = json.load(file)
  df = pd.DataFrame(data["events"])


plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="signature")

plt.title("Распределение типов событий безопасности")
plt.xticks(rotation=90)
plt.show()
