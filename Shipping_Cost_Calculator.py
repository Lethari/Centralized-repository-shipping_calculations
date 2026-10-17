# Shipping Cost Calculator - Fixed Version

def calculate_shipping_cost(weight, rate):
    """Calculate shipping cost with validation"""
    if weight <= 0 or rate <= 0:
        raise ValueError("Weight and rate must be positive numbers")
    return weight * rate

def main():
    try:
        weight = float(input("Enter the package weight in kilograms: "))
        rate = float(input("Enter the shipping rate per kilogram: "))
        
        if weight <= 0:
            print("Error: Weight must be greater than 0")
            return
        if rate <= 0:
            print("Error: Rate must be greater than 0")
            return
            
        shipping_cost = calculate_shipping_cost(weight, rate)
        print(f"Shipping Cost: {shipping_cost:.2f} USD")
        
    except ValueError as e:
        print(f"Invalid input: Please enter valid numbers. {e}")

if __name__ == "__main__":
    main()
