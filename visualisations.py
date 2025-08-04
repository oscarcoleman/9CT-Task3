# display bar graph for each region, with each country showing their primary and high school scores side-by-side
# display world bar graph that compares the regional averages

import numpy as np
import matplotlib.pyplot as plt

# ----- TEMPLATE -----

labels = ['A', 'B', 'C', 'D']
values1 = [10, 15, 20, 25]
values2 = [12, 18, 22, 28]

x = np.arange(len(labels))  # the label locations
width = 0.35  # width of the bars

fig, ax = plt.subplots()
ax.bar(x - width/2, values1, width, label='Group 1')
ax.bar(x + width/2, values2, width, label='Group 2')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Values')
ax.set_title('Grouped Bar Chart')
ax.legend()
plt.show()

# ----- TEMPLATE -----

# Scandanavia Graph

labels = ['']