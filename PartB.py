import PartA as pA
import sys

# My function runs in linear time relative to the number of tokens in file 1
# Achieving a runtime of O(n) where n is the total tokens counted in file 1
# Constant lookup times (O(1)) are used to count the intersections between
#  both files through hashable data structures
def countIntersection(file1: str, file2: str) -> int:
    freq_1: dict[str, int] = pA.tokenFrequency(pA.tokenize(file1))
    freq_2: dict[str, int] = pA.tokenFrequency(pA.tokenize(file2))
    count = 0

    for token in freq_1:
        count += 1 if token in freq_2 else 0
    
    return count

if __name__ == '__main__':
    f1, f2 = sys.argv[1], sys.argv[2]
    print(countIntersection(f1, f2))