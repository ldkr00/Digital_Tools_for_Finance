import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

#url = "https://raw.githubusercontent.com/ipozdeev/it-skills-for-research/master/data/coding-environment-exercise.csv"
#data = pd.read_csv(url)
path = "data/coding-environment-exercise.csv"
data = pd.read_csv(path)
date = data.date
value = data.value

def main(x,y):
    plt.rc('font', size=12) 
    plt.figure(figsize=(10,6), tight_layout=True)
    plt.plot(x, y, linewidth=2)
    plt.xticks(np.arange(0, len(date) + 1, 2))
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Evolution of Unknown')
    plt.show()

if __name__ == '__main__':
    main(date, value)


