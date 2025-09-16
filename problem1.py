def gdc_recursive(a,b):
    """Recursive function to compute GDC (Eucledian algorithm)."""
    if b == 0:
        return a
    return gdc_recursive(b, a % b)

def lcm_recursive(a, b):
    """Recursive function to compute LCM (Eucledian algorithm)."""
    return abs(a * b) // gdc_recursive(a, b)

while True:
    try:
        x = int(input("Enter a value for x: "))
        y = int(input("Enter a value for y: "))
        if x <=  0 or y <= 0:
            print("Error: Please enter a positive integer only(no zero or negative values).")
            continue

        lcm = lcm_recursive(x, y)
        print(f"The LCM of {x} and {y} is = {lcm}")
        break

    except ValueError:
        print("Invalid input! Please enter integer only.")
