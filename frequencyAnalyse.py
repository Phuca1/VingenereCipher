import numpy as np

THEORETICAL_FREQUENCIES = [12.7, 9.06, 8.17, 7.51, 6.97, 6.75, 6.33, 6.09, 5.99, 4.25, 4.02, 2.78, 2.76,
                           2.41, 2.36, 2.23, 2.01, 1.97, 1.93, 1.49, 0.99, 0.77, 0.15, 0.15, 0.09, 0.07]

ALPHABET_SORTED_BY_FREQUENCY = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u',
                                'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

a = dict(zip(ALPHABET_SORTED_BY_FREQUENCY,THEORETICAL_FREQUENCIES))
sorted_a = sorted(a.items(), key=lambda x: x[0])
print(sorted_a)
