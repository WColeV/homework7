import sys
import numpy as np
import matplotlib.pyplot as plt

# check if filename argument is provided
if len(sys.argv) < 2:
    print("Please provide a filename argument.")
    sys.exit()

# get filename from command line argument
filename = sys.argv[1]

# read in data from CSV file
data = np.genfromtxt(filename, delimiter=',')

# create heatmap plot
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.title(filename[:-4])

# save plot as PNG file
png_filename = filename[:-4] + ".png"
plt.savefig(png_filename)

# show plot
plt.show()
