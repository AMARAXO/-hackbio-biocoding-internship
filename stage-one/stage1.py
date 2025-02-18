# Change DNA to Protein

def dna_to_protein(dna_sequence):
    genetic_code = {
        "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
        "TAA": "*", "TAG": "*", "TGA": "*"
    }
    protein = ""  # Initialize protein string
    for i in range(0, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i+3]  # Extracts 3 nucleotides at a time
        amino_acid = genetic_code.get(codon, "?")

        if amino_acid == "*":  # STOP codon
            break  # Stops translation at STOP codon

        protein += amino_acid  # Adds amino acid to protein string
    
    return protein  # Function must return the result, not just print it

# Calling the function and printing the result
print(dna_to_protein("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"))

#Stimulating Logistic Population Growth
import numpy as np  # Ensure NumPy is imported
import pandas as pd  # For data manipulation (if needed)

def logistic_growth(P0, r, K, time_steps, lag_phase_range=(3, 10), exp_phase_range=(5, 15)):
    lag_phase = np.random.randint(*lag_phase_range)  # Random lag phase duration
    exp_phase = np.random.randint(*exp_phase_range)  # Random exponential phase duration
    population = []  # List to store population values

    for t in range(time_steps):
        if t < lag_phase:
            P_t = P0  # Population stays constant during lag phase
        elif t < lag_phase + exp_phase:
            P_t = P0 * np.exp(r * (t - lag_phase))  # Exponential growth phase
        else:
            P_t = K / (1 + ((K - P0) / P0) * np.exp(-r * (t - lag_phase - exp_phase)))  # Logistic growth

        population.append(min(P_t, K))  # Ensure population never exceeds carrying capacity

    return population  # Return the list of population values

# Test the function
pop_growth = logistic_growth(10, 0.2, 1000, 50)
print(pop_growth)  # This should print a list of population values over time

#time to reach 80% of maximum growth
import numpy as np  # For mathematical calculations
import pandas as pd  # For data manipulation

def logistic_growth(P0, r, K, time_steps, lag_phase_range=(3, 10), exp_phase_range=(5, 15)):
    lag_phase = np.random.randint(*lag_phase_range)
    exp_phase = np.random.randint(*exp_phase_range)
    population = []  # List to store population values

    for t in range(time_steps):
        if t < lag_phase:
            P_t = P0  # Population stays the same (lag phase)
        elif t < lag_phase + exp_phase:
            P_t = P0 * np.exp(r * (t - lag_phase))  # Exponential growth
        else:
            P_t = K / (1 + ((K - P0) / P0) * np.exp(-r * (t - lag_phase - exp_phase)))  # Logistic growth
        population.append(min(P_t, K))  # Ensure population never exceeds K
    
    return population  # RETURN the population list

# Generate the population growth data
pop_growth = logistic_growth(10, 0.2, 1000, 50)

# Function to determine time to 80% of carrying capacity (K)
def time_to_80_percent_growth(population, K):
    threshold = 0.8 * K  # Calculate 80% of K
    for t, P_t in enumerate(population):  # Iterate through population values
        if P_t >= threshold:
            return t  # Return the first time step where it reaches 80%
    return None  # If population never reaches 80%, return None

# Calculate time to 80% of max population (1000)
time_to_80 = time_to_80_percent_growth(pop_growth, 1000)

# Print the result
print(time_to_80)  # Should print an integer if 80% of K is reached

#Hamming Disance with Slack and Twitter Usernames
def hamming_distance(str1, str2):
    max_len = max(len(str1), len(str2))
    str1 = str1.ljust(max_len, "_")  # Pad with underscores
    str2 = str2.ljust(max_len, "_")
    return sum(1 for a, b in zip(str1, str2) if a != b)
print(hamming_distance("Amara", "Amaraxo"))

#link to Github: https://github.com/AMARAXO/-hackbio-biocoding-internship

