import numpy as np
from Q2 import radixsort

# Brute-Force Algorithm
def brute_force_max_overlap(M):
    n = len(M)
    max_overlap = 0
    result = None
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            start = max(M[i][1], M[j][1])
            end = min(M[i][2], M[j][2])
            overlap = max(0, end - start)
            if overlap > max_overlap:
                max_overlap = overlap
                result = (M[i][0], M[j][0], max_overlap)
    return result

# Divide-and-conquer Algorithm
def find_max_crossing_overlap(M, low, mid, high):
    left_index = mid
    max_death_left = M[mid][2]
    for i in range(mid, low - 1, -1):
        # need to choose M[i] with latest death to maximize overlap
        if M[i][2] > max_death_left:
            max_death_left = M[i][2]
            left_index = i
    
    right_index = mid + 1
    min_birth_right = M[mid + 1][1]
    for j in range(mid + 1, high + 1):
        # need to choose M[j] with earliest birth to maximize overlap
        if M[j][1] < min_birth_right:
            min_birth_right = M[j][1]
            right_index = j
    start = max(M[left_index][1], M[right_index][1])
    end = min(M[left_index][2], M[right_index][2])
    cross_overlap = max(0, end - start) # take 0 if cross_overlap < 0
    return (left_index, right_index, cross_overlap)

def find_max_overlap(M, low, high):
    if low == high:
        return (low, low, 0) # base case: only 1 element
    if high - low == 2:
        start = max(M[low][1], M[high][1])
        end = min(M[low][2], M[high][2])
        overlap = max(0, end - start) # take 0 if overlap < 0
        return (low, high, overlap)

    mid = (low + high) // 2

    # overlap in the left half
    (left_low, left_high, left_overlap) = find_max_overlap(M, low, mid)

    # overlap in the right half
    (right_low, right_high, right_overlap) = find_max_overlap(M, mid + 1, high)

    # overlap that crosses the midpiunt
    (cross_low, cross_high, cross_overlap) = find_max_crossing_overlap(M, low, mid, high)

    # take the best one between them
    if left_overlap >= right_overlap and left_overlap >= cross_overlap:
        return (left_low, left_high, left_overlap)
    elif right_overlap >= left_overlap and right_overlap >= cross_overlap:
        return (right_low, right_high, right_overlap)
    else:
        return (cross_low, cross_high, cross_overlap)

# List of mathematicians as (name, birth year, death year)
M = [
    ("Leonhard Euler", 1707, 1783),
    ("Carl Friedrich Gauss", 1777, 1855),
    ("Augustin-Louis Cauchy", 1789, 1857),
    ("Nikolai Lobachevsky", 1792, 1856),
    ("Bernhard Riemann", 1826, 1866)
]

birth_years = [m[1] for m in M]

# sort the birth years using radix sort
sorted_birth_years = radixsort(birth_years, 10)

# dictionary to map birth years to mathematicians
year_to_math = {m[1]: m for m in M}

# retrieve mathematicians in sorted order
sorted_M = [year_to_math[year] for year in sorted_birth_years]

print("Brute force algorithm result:")
brute_result = brute_force_max_overlap(sorted_M)
print(brute_result)

print("\nDivide-and-Conquer algorithm result:")
divide_result = find_max_overlap(sorted_M, 0, len(sorted_M) - 1)
print((sorted_M[divide_result[0]][0], sorted_M[divide_result[1]][0], divide_result[2]))