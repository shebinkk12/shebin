# Function to demonstrate type()
def demonstrate_type():
    x = 42                # Integer
    y = 3.14             # Float
    z = "Hello, World!"  # String
    a = [1, 2, 3]        # List
    b = (4, 5, 6)        # Tuple
    c = {'key': 'value'} # Dictionary

    print(f"The type of {x} is: {type(x)}")
    print(f"The type of {y} is: {type(y)}")
    print(f"The type of '{z}' is: {type(z)}")
    print(f"The type of {a} is: {type(a)}")
    print(f"The type of {b} is: {type(b)}")
    print(f"The type of {c} is: {type(c)}")

# Run the demonstration
demonstrate_type()
