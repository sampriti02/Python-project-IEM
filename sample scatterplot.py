import matplotlib.pyplot as plt

# for Python programming
marks = [95, 73]
batches = [1, 2]
 
plt.xlabel("Marks")
plt.ylabel("Batches")
plt.title('Scatter Plot')
# for Physics
plt.scatter(marks, batches, c='green')
 
# second data point
marks = [65, 78, 34, 95]
batches = [1, 2, 3, 4]
 
# depict second scatted plot
plt.scatter(marks, batches, c='red')
 
# depict illustration
plt.show()
