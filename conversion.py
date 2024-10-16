# Function to demonstrate various type conversion functions
def demonstrate_type_conversions():
    # Original values
    int_value = 42
    float_value = 3.14
    str_value = "123"
    bool_value = True
    char_code = 65  # ASCII code for 'A'
    
    # Type conversions
    converted_to_int = int(float_value)        # Convert float to int
    converted_to_float = float(str_value)       # Convert string to float
    converted_to_str = str(int_value)           # Convert int to string
    converted_to_bool = bool(0)                 # Convert integer to bool (0 is False)
    converted_to_char = chr(char_code)          # Convert ASCII code to character

    # Displaying results
    print(f"Original float value: {float_value} | Converted to int: {converted_to_int}")
    print(f"Original string value: '{str_value}' | Converted to float: {converted_to_float}")
    print(f"Original int value: {int_value} | Converted to string: '{converted_to_str}'")
    print(f"Original value (0) | Converted to bool: {converted_to_bool}")
    print(f"ASCII code {char_code} | Converted to character: '{converted_to_char}'")

# Run the demonstration
demonstrate_type_conversions()
