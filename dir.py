# Function to demonstrate dir()
def demonstrate_dir():
    x = [1, 2, 3]  # A list

    print(f"Attributes and methods of the list object x:")
    print(dir(x))

    # You can also use dir() with other types of objects
    y = "Hello"
    print(f"\nAttributes and methods of the string object y:")
    print(dir(y))

    z = 42  # An integer
    print(f"\nAttributes and methods of the integer object z:")
    print(dir(z))

# Run the demonstration
demonstrate_dir()
