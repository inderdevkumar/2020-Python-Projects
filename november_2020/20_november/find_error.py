import time
import numpy as np

# Algorithm 1 finds median in O(n log n) time
def find_median(a, n):
    # First we sort the array
    sorted(a)

    # check for even case
    if n % 2 != 0:
        return float(a[n // 2])

    return float((a[int((n - 1) / 2)] +
                  a[int(n / 2)]) / 2.0)

# Algorithm number 2 finds median in O(n) time
def median_of_medians(A, i):

    # divide A into sublists of len 5
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]
    medians = [sorted(sublists[index])[len(sublists[index]) // 2] for index in range(len(sublists)-2)]
    print(len(medians))
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        # the pivot is the median of the medians
        pivot = median_of_medians(medians, len(medians)/2)

    # partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return median_of_medians(low, i)
    elif i > k:
        return median_of_medians(high, i-k-1)
    else:  # pivot = k
        return pivot


def main():
    n = 1000
    a = np.random.randint(1, 101, n)
    n = len(a)
    start_time = time.time()
    print("Median =", find_median(a, n))
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print(median_of_medians(a, 0))  # should be 1
    print("--- %s seconds ---" % (time.time() - start_time))
    #print(median_of_medians(A, 7))  # should be 99
    #print(median_of_medians(B, 4))  # should be 5


if __name__ == "__main__":
    main()
