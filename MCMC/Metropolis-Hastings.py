import numpy as np
import scipy.stats as stats

#sampling from a Gaussian distribution

def metropolis_hastings(target_distribution, initial_state, num_samples, proposal_sd):
    current_state = initial_state
    samples = []

    for _ in range(num_samples):
        proposed_state = np.random.normal(current_state, proposal_sd)

        acceptance_prob = min(1, target_distribution(proposed_state) / target_distribution(current_state))

        if np.random.rand() < acceptance_prob:
            current_state = proposed_state

        samples.append(current_state)

    return np.array(samples)

def target_distribution(x):
    return stats.norm.pdf(x, loc=3, scale=2)


#initial_state of 0, sd of 1
initial_state = 0
num_samples = 10000
proposal_sd = 1.0

samples = metropolis_hastings(target_distribution, initial_state, num_samples, proposal_sd)

import matplotlib.pyplot as plt
plt.hist(samples, bins=50, density=True, alpha=0.5, label='Generated Samples')
x = np.linspace(-5, 10, 1000)
plt.plot(x, target_distribution(x), 'r-', label='True Distribution')
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Metropolis-Hastings Sampling')
plt.legend()
plt.show()