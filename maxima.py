def find_maxima(arr):
    """Returns the positions of the maximum values in the array
    arr.

    Example:
    find_maxima([]) → []
    find_maxima([1, 2, 1]) → [1]
    find_maxima([2, 0, 0, -2, 2]) → [0, 4]
    """
    ans = []
    N = len(arr)
    for i in range(N):
        if (arr[i] > arr[i-1] and
            (i >= N or arr[i] > arr[i+1])):
            ans.append(i)
    return ans
