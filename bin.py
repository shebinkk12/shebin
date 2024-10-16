# Function to demonstrate bin(), oct(), and hex()
def demonstrate_number_systems():
    x = 255  # Example integer

    binary_representation = bin(x)  # Convert to binary
    octal_representation = oct(x)    # Convert to octal
    hexadecimal_representation = hex(x)  # Convert to hexadecimal

    # Displaying results
    print(f"The binary representation of {x} is: {binary_representation}")
    print(f"The octal representation of {x} is: {octal_representation}")
    print(f"The hexadecimal representation of {x} is: {hexadecimal_representation}")

# Run the demonstration
demonstrate_number_systems()
