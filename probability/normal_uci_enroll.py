import numpy as np
import matplotlib.pyplot as plt

# Define the elements and their respective bell-shaped probabilities
elements = [2, 3, 4, 5, 6]
probabilities = [0.02, 0.22, 0.52, 0.22, 0.02]  # Bell-shaped distribution

# Function to generate random samples based on the given probabilities
def generate_samples(n):
    samples = np.random.choice(elements, size=n, p=probabilities)
    return samples

# Generate 1000 samples as an example
samples = generate_samples(1000)
plt.hist(samples, bins=10)
plt.show()
print("Mean:", np.mean(samples))