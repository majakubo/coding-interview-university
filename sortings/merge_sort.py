def merge_sort(sequence):
    """simple merge sort on additional lists"""
    if len(sequence) > 1:
        middle = len(sequence) // 2
        left = merge_sort(sequence[:middle])
        right = merge_sort(sequence[middle:])
        merged = []
        while left and right:
            if left < right:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        if left:
            merged += left
        if right:
            merged += right

        return merged
    else:
        return sequence

