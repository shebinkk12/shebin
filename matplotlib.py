import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a line plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line Graph')

# Add titles and labels
plt.title("Sample Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Add a legend
plt.legend()

# Show the grid
plt.grid()

# Display the plot
plt.show()
