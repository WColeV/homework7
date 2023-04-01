import sys
import numpy as np
import matplotlib.pyplot as plt

# check if filename arguments are provided
if len(sys.argv) < 2:
    print("Please provide at least one filename argument.")
    sys.exit()

# create empty arrays to store data
all_data = []
all_heights = []

# read in data from CSV files and store in arrays
for filename in sys.argv[1:]:
    data = np.genfromtxt(filename, delimiter=',')
    height = np.mean(data, axis=1)
    all_data.append(data)
    all_heights.append(height)

# create overall average surface plot
mean_data = np.mean(all_data, axis=0)
plt.imshow(mean_data, cmap='hot', interpolation='nearest')
plt.title("Mean Surface")
plt.savefig("mean_surface.png")
plt.show()

# create average height plot with individual file curves
plt.figure()
plt.title("Height Comparison")
plt.xlabel("Vertical Axis")
plt.ylabel("Height")
plt.ylim([0, np.max(all_heights)])
plt.plot(np.mean(all_heights, axis=0), label="Overall Average")
for i in range(len(sys.argv)-1):
    plt.plot(all_heights[i], alpha=0.3, label=sys.argv[i+1][:-4])
plt.legend()
plt.savefig("surface_compare.png")
plt.show()
