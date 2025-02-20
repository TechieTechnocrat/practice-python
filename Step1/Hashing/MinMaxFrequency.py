def analyze_frequencies(numbers):
    # Creating frequency dictionary manually
    freq_map = {}
    for num in numbers:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    # Finding min and max frequency
    min_freq = min(freq_map.values())
    max_freq = max(freq_map.values())
    
    # Finding numbers corresponding to min and max frequency
    min_freq_numbers = [num for num, freq in freq_map.items() if freq == min_freq]
    max_freq_numbers = [num for num, freq in freq_map.items() if freq == max_freq]
    
    # Finding min and max number in the list
    min_number = min(numbers)
    max_number = max(numbers)
    
    return {
        "min_frequency": min_freq,
        "max_frequency": max_freq,
        "min_frequency_numbers": min_freq_numbers,
        "max_frequency_numbers": max_freq_numbers,
        "min_number": min_number,
        "max_number": max_number
    }

# Example usage
numbers = [4, 1, 2, 2, 3, 4, 4, 5, 1, 1, 6]
result = analyze_frequencies(numbers)
print(result)
