# Function to simulate cmp() in Python 3
def cmp(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

# Function to demonstrate the custom cmp function
def demonstrate_cmp():
    x = 10
    y = 20
    z = 10

    print(f"Comparing {x} and {y}: {cmp(x, y)}")  # Expected output: -1
    print(f"Comparing {y} and {x}: {cmp(y, x)}")  # Expected output: 1
    print(f"Comparing {x} and {z}: {cmp(x, z)}")  # Expected output: 0

# Run the demonstration
demonstrate_cmp()
