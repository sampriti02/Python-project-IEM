import matplotlib.pyplot as plt
import numpy as np

batchName = np.array([0, 1, 2, 3])
averagePercentage = np.array([3, 8, 1, 10])

plt.xlabel("Batch Name")
plt.ylabel("Average Percentage")
plt.title('Line Plot')

plt.plot(batchName,averagePercentage, c = '#4CAF50', linewidth = '8')
plt.show()
