### Population Growth & DNA Analysis Functions
## Overview
This project includes four key functions that perform biological and computational tasks:
1. Translating DNA sequences into proteins
2. Simulating logistic population growth with a lag and exponential phase
3. Calculating the time required for a population to reach 80% of its carrying capacity
4. Determining the Hamming distance between two strings

## Features
✔ Converts DNA sequences into protein sequences
✔ Models realistic logistic population growth with randomized phases
✔ Determines the time step for 80% carrying capacity
✔ Computes Hamming distance between two strings

## Functions
1. DNA to Protein Translation
Function: dna_to_protein(dna_sequence)
Converts a DNA sequence into its corresponding protein sequence using a genetic 

2. Logistic Growth Simulation
Function: logistic_growth(P0, r, K, time_steps, lag_phase_range, exp_phase_range)
Simulates logistic population growth with:
Lag phase (population stays constant)
Exponential phase (rapid growth)
Plateau phase (growth slows near carrying capacity)
Returns a list of population values over time.

3. Time to 80% Growth
Function: time_to_80_percent_growth(population, K)
Determines the first time step at which population reaches 80% of K.

4. Hamming Distance Calculation
Function: hamming_distance(str1, str2)
Computes the Hamming distance (the number of character differences) between two strings.

## Requirements
# Dependencies:
1. Python 3.x
2. numpy (for mathematical calculations)
3. pandas (optional for data handling)


