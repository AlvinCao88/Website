import numpy as np
import matplotlib.pyplot as plt

# Your data
data = [6, 7, 8, 9]

# Calculate mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

# Generate data points for the normal distribution
x = np.linspace(min(data), max(data), 100)
y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev)**2)

# Plot the bell curve
plt.plot(x, y, label='Bell Curve')

# Overlay the histogram for comparison
# plt.hist(data, bins=range(min(data), max(data) + 1), density=True, alpha=0.5, edgecolor='black', label='Histogram')

# Add labels and title
plt.title('Bell Curve and Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Density/Frequency')
plt.legend()

# Show the plot
plt.show()
