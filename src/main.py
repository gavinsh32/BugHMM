# main.py

import os
import random
import numpy

# Read in each sequence from data file and form dataset
dataset = []
with open('../data/data.txt') as file:
    dataset = [line.rstrip() for line in file]

# Display dataset
# for gene in dataset: print(f'[{gene}]\n')

emmission_frequencies = [[0 for _ in range(26)] for _ in range(26)]

background_frequencies = {}

counter = 0

# Record background frequencies
for _ in range(50):
    # Pick two random genes
    gene = random.choice(dataset)
    other = random.choice(dataset)
    if gene != other:
        for i in range(len(gene)):
            counter += 1
            a = gene[i]
            if a not in background_frequencies:
                background_frequencies[a] = 1
            else:
                background_frequencies[a] += 1

print(background_frequencies.sort())
print(counter)

def main():
    pass

if __name__ == '__main__':
    main()