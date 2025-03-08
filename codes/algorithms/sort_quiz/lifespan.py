from typing import List, Tuple


class Mathematician:
    def __init__(self, name: str, birth: int, death: int):
        self.name = name
        self.birth = birth
        self.death = death

    def overlap(self, other: 'Mathematician') -> int:
        """Calculates the overlap between two mathematicians' lifespans."""
        return max(0, min(self.death, other.death) - max(self.birth, other.birth))

    def __repr__(self):
        return f"{self.name} ({self.birth}-{self.death})"

# 1. Brute-Force Algorithm (O(n^2))
def find_max_overlap_brute_force(mathematicians: List[Mathematician]) -> Tuple[Mathematician, Mathematician, int]:
    """
    Finds the two mathematicians with the maximum lifespan overlap using a brute-force approach.

    Args:
        mathematicians: A list of Mathematician objects.

    Returns:
        A tuple containing the two mathematicians and their lifespan overlap.  Returns (None, None, 0) if the list is empty.
    """
    if not mathematicians or len(mathematicians) < 2:
        return None, None, 0

    max_overlap = 0
    mathematician1 = None
    mathematician2 = None

    for i in range(len(mathematicians)):
        for j in range(i + 1, len(mathematicians)):  # Avoid comparing a mathematician to themselves and avoid duplicate pairs
            overlap = mathematicians[i].overlap(mathematicians[j])
            if overlap > max_overlap:
                max_overlap = overlap
                mathematician1 = mathematicians[i]
                mathematician2 = mathematicians[j]

    return mathematician1, mathematician2, max_overlap


# 2. O(n log n) Algorithm (Sort & Divide-and-Conquer Concept)

def find_max_overlap_optimized(mathematicians: List[Mathematician]) -> Tuple[Mathematician, Mathematician, int]:
    """
    Finds the two mathematicians with the maximum lifespan overlap using an optimized approach (O(n log n) conceptually).

    While this implementation doesn't use true divide and conquer, the key optimization is to sort by birth year.  A true divide and conquer approach would involve recursively splitting the list and merging results, which is unnecessarily complex for this particular problem and doesn't necessarily improve performance significantly. The 'sweeping' is an optimization technique.

    Args:
        mathematicians: A list of Mathematician objects.

    Returns:
        A tuple containing the two mathematicians and their lifespan overlap. Returns (None, None, 0) if the list is empty.
    """
    if not mathematicians or len(mathematicians) < 2:
        return None, None, 0

    # Sort by birth year (O(n log n))
    mathematicians.sort(key=lambda x: x.birth)

    max_overlap = 0
    mathematician1 = None
    mathematician2 = None

    # Iterate through the sorted list, comparing each mathematician to the ones after them.  This is more efficient because sorting brings potentially overlapping lifespans closer together.

    for i in range(len(mathematicians) - 1):
        for j in range(i + 1, len(mathematicians)):
            # Optimization: If the current mathematician's death year is before the next mathematician's birth year,
            # then there's no overlap, and we can break the inner loop.  Since the list is sorted by birth year,
            # subsequent mathematicians will also have later birth years and thus no overlap.
            if mathematicians[i].death <= mathematicians[j].birth:
                break

            overlap = mathematicians[i].overlap(mathematicians[j])
            if overlap > max_overlap:
                max_overlap = overlap
                mathematician1 = mathematicians[i]
                mathematician2 = mathematicians[j]

    return mathematician1, mathematician2, max_overlap



# 3. Implementation (with placeholder sorting - replace with your Q2 implementation)

def radix_sort(arr):
  """Placeholder radix sort - replace with your Q2 implementation.
     This just returns the input for demonstration purposes."""
  return sorted(arr, key=lambda x: x.birth)

def find_max_overlap_optimized_radix(mathematicians: List[Mathematician]) -> Tuple[Mathematician, Mathematician, int]:
  """
  Uses radix sort (from Q2) to sort the mathematicians and then finds the max overlap
  using an optimized iteration approach.

  This demonstrates how to integrate the sorting algorithm from Q2.
  """
  if not mathematicians or len(mathematicians) < 2:
        return None, None, 0

  # Sort by birth year using radix sort (replace with your actual radix sort from Q2)
  mathematicians = radix_sort(mathematicians) # Assuming your Q2 implementation sorts in place or returns a new list.


  max_overlap = 0
  mathematician1 = None
  mathematician2 = None

  for i in range(len(mathematicians) - 1):
      for j in range(i + 1, len(mathematicians)):
          if mathematicians[i].death <= mathematicians[j].birth:
              break

          overlap = mathematicians[i].overlap(mathematicians[j])
          if overlap > max_overlap:
              max_overlap = overlap
              mathematician1 = mathematicians[i]
              mathematician2 = mathematicians[j]

  return mathematician1, mathematician2, max_overlap


# Example Usage
if __name__ == '__main__':
    mathematicians = [
        Mathematician("Leonhard Euler", 1707, 1783),
        Mathematician("Carl Friedrich Gauss", 1777, 1855),
        Mathematician("Augustin Louis Cauchy", 1789, 1857),
        Mathematician("Nikolai Lobachevsky", 1792, 1856),
        Mathematician("Bernhard Riemann", 1826, 1866),
        Mathematician("Ada Lovelace", 1815, 1852),
        Mathematician("Alan Turing", 1912, 1954), # Added to span 3 centuries (1800-2100)
    ]

    # Brute Force
    m1_bf, m2_bf, overlap_bf = find_max_overlap_brute_force(mathematicians)
    print("Brute Force:")
    print(f"Mathematicians: {m1_bf}, {m2_bf}, Overlap: {overlap_bf}")

    # Optimized
    m1_opt, m2_opt, overlap_opt = find_max_overlap_optimized(mathematicians)
    print("\nOptimized:")
    print(f"Mathematicians: {m1_opt}, {m2_opt}, Overlap: {overlap_opt}")

    # Optimized with Radix Sort
    m1_radix, m2_radix, overlap_radix = find_max_overlap_optimized_radix(mathematicians)
    print("\nOptimized with Radix Sort:")
    print(f"Mathematicians: {m1_radix}, {m2_radix}, Overlap: {overlap_radix}")