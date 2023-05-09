import numpy as np
N = 13000 # Number of observations
counter = 0# Counter to keep track of how many observations fall within the range (-1, 1)
for i in np.random.normal(size=N):# Generate N random numbers from a standard normal distribution and count how many fall within the range (-1, 1)
    if i > -1 and i < 1:
        counter += 1
percentage = (counter / N)*100# Calculate the percentage of observations that fall within the range (-1, 1)
print(percentage)