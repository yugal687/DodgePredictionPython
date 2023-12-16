
from dodgePredictionDataHead import data
from dodgePredictionDataHead import plt


data.dropna()
plt.figure(figsize=(10,4))
plt.title("Dodge Price")
plt.xlabel("Date")
plt.ylabel('Close')
plt.plot(data["Close"])
plt.show()
