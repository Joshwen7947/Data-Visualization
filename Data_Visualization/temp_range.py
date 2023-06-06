import csv
import matplotlib.pyplot as plt
from datetime import datetime
# 
filename = "death_valley.csv"
with open(filename) as file:
    reader = csv.reader(file)
    header = next(reader)
    

    date, highs, lows = [],[], []
    for row in reader:
        current = datetime.strptime(row[2],"%Y-%m-%d")
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current}")
        else:
            highs.append(high)
            date.append(current)
            lows.append(low)
    print(highs)
    print(lows)
    

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(date,highs, c="red", linewidth=1)
ax.plot(date,lows,c="blue", linewidth=1)

plt.fill_between(date,highs,lows, facecolor="blue",alpha=0.3)

title = "Death Valley 2018"
ax.set_title(title,fontsize=24)
ax.set_xlabel("Time", fontsize=18)
fig.autofmt_xdate()
ax.set_ylabel("Temp",fontsize=18)

plt.show()