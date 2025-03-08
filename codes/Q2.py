import numpy as np

# Sorting algorithms

def countingsort(A, b, digit_place):
    n = len(A)
    B = [0 for x in range(n)] # output list

    C = [0 for x in range(b)] # auxillary list for storing the frequency of each digit
    
    for num in A:
        num_at_position = num // (b ** digit_place)  # remove rightmost digit until we reach the one required
        digit = num_at_position % b  # extract the required digit
        C[digit] = C[digit] + 1 # find frequency of each digit
    
    for i in range (1, b):
        C[i] = C[i] + C[i - 1] # C[i] stores the number of elements <= i in A

    # copy A to B, from last element to first element of A
    for j in range(n - 1, -1, -1):
        num = A[j] # reset num after every iteration for correct digit extraction
        num_at_position = num // (b ** digit_place)  # remove rightmost digits
        digit = num_at_position % b  # extract the required digit
        B[C[digit] - 1] = A[j] # place A[j] in sorted position
        C[digit] = C[digit] - 1 # to handle duplicate values

    return B

def radixsort(A, b):
    max_num = max(A)
    d = 0
    num = max_num
    # find the number of digits d in base b
    if num == 0:
        d = 1
    else:
        while num > 0:
            d = d + 1
            num = num // b
    
    output_file = f"sort_base{b}.txt"
    with open(output_file, "a") as file:
        for i in range(d):
            A = countingsort(A, b, i)
            converted_A = [np.base_repr(x, base=b) for x in A]
            formatted_A = " ".join(converted_A)
            file.write(f"Pass {i + 1}:  {formatted_A}\n\n")

    return A

# Main
if __name__ == "__main__":
    b = int(input("Enter the base: "))
    A = [int(x, b) for x in input("Enter numbers separated by space: ").split()]
    sorted_A = radixsort(A, b)