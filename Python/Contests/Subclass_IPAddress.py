def identify_ip_subclass(ip_address):
    # Check for empty input
    if not ip_address:
        return "Wrong IP Address"
    
    # Split IP address into parts
    parts = ip_address.split(".")
    
    # Validate that we have exactly 4 parts
    if len(parts) != 4:
        return "Wrong IP Address"
    
    # Check each part to be an integer in the range 0-255
    try:
        parts = [int(part) for part in parts]  # Convert each part to an integer
    except ValueError:
        return "Wrong IP Address"  # Non-integer value found
    
    # Ensure each part is within the range 0-255
    if any(part < 0 or part > 255 for part in parts):
        return "Wrong IP Address"
    
    # Identify the class based on the first part (abc)
    abc = parts[1]  # 'abc' refers to the second part in this IP structure
    
    if 0 <= abc <= 63:
        return "Class L"
    elif 64 <= abc <= 127:
        return "Class M"
    elif 128 <= abc <= 191:
        return "Class N"
    elif 192 <= abc <= 255:
        return "Class P"
    
    return "Wrong IP Address"  # Fallback case

# Test cases
inval = input()
print(identify_ip_subclass(inval))
