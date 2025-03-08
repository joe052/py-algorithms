def counting_sort(arr, base, digit):
    """
    Sorts an array based on a specific digit using counting sort.

    Args:
        arr: The array to sort.
        base: The base of the number system.
        digit: The digit position to sort by (0 for least significant, 1 for next, etc.).

    Returns:
        The sorted array.
    """
    n = len(arr)
    count = [0] * base  # Initialize count array
    output = [0] * n   # Output array

    # Count occurrences of each digit at the specified position
    for i in range(n):
        index = (arr[i] // (base ** digit)) % base
        count[index] += 1

    # Modify count array to store the position of each digit in the output array
    for i in range(1, base):
        count[i] += count[i - 1]

    # Build the output array (stable sort)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // (base ** digit)) % base
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output


def radix_sort(arr, base, filename):
    """
    Sorts an array using radix sort.

    Args:
        arr: The array to sort.
        base: The base of the number system.
        filename: The name of the output file.
    """
    max_val = max(arr)
    num_digits = 0
    while max_val > 0:
        max_val //= base
        num_digits += 1

    with open(filename, "w") as f:
        for digit in range(num_digits):
            arr = counting_sort(arr, base, digit)
            f.write(" ".join(map(str, arr)) + "\n")
            if digit < num_digits - 1:
                f.write("\n") # Separate passes by a blank line


if __name__ == "__main__":
    # Get input from the user
    base = int(input("Enter the base: "))
    numbers = list(map(int, input("Enter the numbers to sort (separated by spaces): ").split()))
    filename = "radix_sort_output.txt"

    # Perform radix sort and write the output to the file
    radix_sort(numbers, base, filename)

    print(f"Radix sort completed.  Output written to {filename}")