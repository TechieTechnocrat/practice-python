def containsNearbyDuplicate(arr, k):
    index_map = {}  # Dictionary to store last seen index of each number
    for i, num in enumerate(arr):  # Loop through each element
        print(f"Checking {num} at index {i}, index_map: {index_map}")  # Debug print
        if num in index_map and i - index_map[num] <= k:
            return True  # Found a duplicate within k distance
        index_map[num] = i  # Update last seen index
    return False

arr = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(arr, k))