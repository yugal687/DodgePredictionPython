from dodgePredictionDataHead import data
from autots import AutoTS
import matplotlib.pyplot as plt


model = AutoTS(forecast_length=2, frequency='infer', ensemble='simple', drop_data_older_than_periods=200)
model = model.fit(data, date_col='Date', value_col='Close', id_col=None)

prediction = model.predict()
forecast = prediction.forecast
print("DogeCoin Price Prediction")
print(forecast)
plt.figure(figsize=(10,4))
plt.title("Dodge Price")
plt.xlabel("Date")
plt.ylabel('Close')
plt.plot(data["Close"])
plt.show(forecast)