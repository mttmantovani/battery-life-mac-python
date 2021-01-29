import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data.csv", index_col="Date")
df.index = pd.to_datetime(df.index, infer_datetime_format=True)
df["ExpDate"] = pd.to_datetime(df.ExpDate, infer_datetime_format=True).values.astype(
    np.int64
)
df = df.groupby(by="Date").mean()
df.ExpDate = pd.to_datetime(df.ExpDate, infer_datetime_format=True)

exp_date_plot = plt.figure()
ax = exp_date_plot.add_subplot()
ax.plot(df.index, df["ExpDate"], marker="o", color="ForestGreen", lw=2)
exp_date_plot.autofmt_xdate()
exp_date_plot.canvas.set_window_title("Expected date to reach 1000 cycles")

cycles_plot = plt.figure()
ax2 = cycles_plot.add_subplot()
ax2.plot(df.index, df["Cycles"], marker="o", lw=2)
cycles_plot.autofmt_xdate()
cycles_plot.canvas.set_window_title("Battery cycles")

capacity_plot = plt.figure()
ax3 = capacity_plot.add_subplot()
ax3.plot(df.index, df["FullCapacity"], marker="o", lw=2, color="red")
capacity_plot.autofmt_xdate()
capacity_plot.canvas.set_window_title("Full capacity (mAh)")

plt.show()
