import math
import pprint
import random
from statistics import mean, stdev

pp = pprint.PrettyPrinter()

# Set seed to generate predictable data
random.seed(500)

# Generate 5 rows x 5 columns
data = [[random.randint(0, math.pow(2, y)) for y in range(5)] for x in range(5)]

print("Row view:")
pp.pprint(data)
# Demonstration of Data Transformation

# Build column view
columns = {i: [row[i] for row in data] for i in range(len(data[0]))}

print("\nColumn view:")
pp.pprint(columns)

# Print basic statistics
print("\nStats:")
for x in sorted(columns):
    print("Column %d, min=%.2f, max=%.2f, mean=%.2f, stdev=%.2f" % 
          (x, min(columns[x]), max(columns[x]), mean(columns[x]), stdev(columns[x])))