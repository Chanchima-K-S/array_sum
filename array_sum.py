# Initialize the list
arr = []

# Read the number of elements
n = int(input("Enter how many elements you have to add: "))

# Read and append elements to this list
for i in range(n):
    x = int(input("Enter the element: "))  # Convert input to integer
    arr.append(x)
    
print("Array:", arr)

# Read the target number
target = int(input("Enter target number: "))

# Function to find two elements that sum to the target
def find_two_sum(arr, target):
    num_dict = {}
    for index, num in enumerate(arr):
        diff = target - num
        if diff in num_dict:
            return [num_dict[diff], index]
        num_dict[num] = index
    return None

# Find the two sum
result = find_two_sum(arr, target)

# Print the result
if result:
    print(f"The indices of the two numbers that add up to {target} are {result}")
else:
    print("No results found.")
