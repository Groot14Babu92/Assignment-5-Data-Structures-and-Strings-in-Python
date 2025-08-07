# Create a list of numbers from 1 to 10
ls = [i + 1 for i in range(10)]

# Extract the first five elements
extracted = ls[:5]

# Reverse the extracted elements
reversed_extracted = extracted[::-1]

# Print both lists
print("Extracted list:", extracted)
print("Reversed list:", reversed_extracted)