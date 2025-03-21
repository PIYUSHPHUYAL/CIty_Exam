def count_inversions(arr):
    # Helper function to perform merge sort and count inversions
    def merge_sort(array):
        # Base case: if the array has 1 or no elements, it's already sorted
        if len(array) <= 1:
            return array, 0

        # Split the array into two halves
        middle = len(array) // 2
        left_half, left_inv = merge_sort(array[:middle])
        right_half, right_inv = merge_sort(array[middle:])

        # Merge the sorted halves and count cross-inversions
        merged_array, cross_inv = merge_and_count(left_half, right_half)

        # Total inversions = left + right + cross
        total_inversions = left_inv + right_inv + cross_inv
        return merged_array, total_inversions

    # This function merges two sorted arrays and counts the inversions
    def merge_and_count(left, right):
        i = j = 0  # Pointers for left and right arrays
        merged = []
        inversions = 0

        # Merge while comparing elements from both arrays
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                # All remaining elements in left are greater than right[j]
                inversions += len(left) - i

        # Append any remaining elements (no more inversions here)
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, inversions

    # Start the recursive merge sort and inversion count
    _, total = merge_sort(arr)
    return total


# Example usage
numbers = [2, 4, 1, 3, 5]
result = count_inversions(numbers)
print("Total number of inversions:", result)
