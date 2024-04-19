import matplotlib.pyplot as plt

# Define the range [0, 1000000) and the constant height
x_range = [0, 16777216]
height = 1 / (x_range[1] - x_range[0])  # Uniform distribution height

# Plot a horizontal line
plt.hlines(y=height, xmin=x_range[0], xmax=x_range[1], color='blue')

# split the range into 3 intervals
x_range_1 = 5592405
x_range_2 = 11184810
x_range_3 = 16777216
mid = 8388608

plt.vlines(x=mid, ymin=0, ymax=0.0000001, color='red', linestyle='--')
plt.vlines(x=x_range_1, ymin=0, ymax=0.0000001, color='red', linestyle='--')
plt.vlines(x=x_range_2, ymin=0, ymax=0.0000001, color='red', linestyle='--')
plt.vlines(x=x_range_3, ymin=0, ymax=0.0000001, color='red', linestyle='--')

plt.text(mid, 0.0000001, "Expected value",ha='center')
plt.text(0, 0, '000000', ha='center')
plt.text(mid, 0, f'{mid:.0f}', ha='center')
plt.text(x_range_1, 0, f'{x_range_1:.0f}', ha='center')
plt.text(x_range_2, 0, f'{x_range_2:.0f}', ha='center')
plt.text(x_range_3-1, 0, f'{x_range_3:.0f}', ha='center')

# Add an arrow from mid to x_range_1 in

plt.annotate('',
             xy=(mid, 0.00000009), xycoords='data',
             xytext=(x_range_1, 0.00000009), textcoords='data',
             arrowprops=dict(arrowstyle="<-",
                             connectionstyle="arc3"),
             )

plt.annotate('',
             xy=(x_range_2, 0.00000009), xycoords='data',
             xytext=(x_range_3, 0.00000009), textcoords='data',
             arrowprops=dict(arrowstyle="<-",
                             connectionstyle="arc3"),
             )

plt.annotate('',
             xy=(0, 0.00000009), xycoords='data',
             xytext=(x_range_1, 0.00000009), textcoords='data',
             arrowprops=dict(arrowstyle="->",
                             connectionstyle="arc3"),
             )

plt.annotate('',
             xy=(mid, 0.00000009), xycoords='data',
             xytext=(x_range_2, 0.00000009), textcoords='data',
             arrowprops=dict(arrowstyle="<-",
                             connectionstyle="arc3"),
             )



# Set labels and title
plt.xlabel('Pin Value')
plt.ylabel('Probability Density')
plt.title('Ideal Distribution')

# Set x-axis limit
plt.xlim(x_range[0], x_range[1])
plt.ylim(0, 0.00000015)

# Display the plot
plt.show()