# Donald Nwolisa
# python programme numbers to words claude ai
# 05/12/2024

def convert_number_to_words(n):
    # Define word mappings for numbers
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", 
            "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion"]

    def convert_hundreds(n):
        """Helper function to convert numbers less than 1000 into words."""
        if n == 0:
            return ""
        elif n < 20:
            return ones[n]
        elif n < 100:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
        else:
            return ones[n // 100] + " Hundred" + (" " + convert_hundreds(n % 100) if n % 100 != 0 else "")
    
    # Handle zero
    if n == 0:
        return "Zero"
    
    # Handle negative numbers
    if n < 0:
        return "Negative " + convert_number_to_words(-n)
    
    # Split number into chunks of 3 digits (e.g., 1,000 = [1, 0])
    parts = []
    chunk_index = 0
    while n > 0:
        if n % 1000 != 0:
            parts.append(convert_hundreds(n % 1000) + (" " + thousands[chunk_index] if thousands[chunk_index] else ""))
        n //= 1000
        chunk_index += 1
    
    # Combine all parts
    return ' '.join(reversed(parts)).strip()

def convert_decimal_to_words(n):
    """Convert decimal numbers (e.g., 123.45) into words."""
    integer_part = int(n)
    decimal_part = round(n - integer_part, 2)
    
    # Convert the integer part
    integer_in_words = convert_number_to_words(integer_part)
    
    # Convert the decimal part
    decimal_in_words = ""
    if decimal_part > 0:
        decimal_in_words = " point " + " ".join([ones[int(digit)] for digit in str(int(decimal_part * 100))])
    
    return integer_in_words + decimal_in_words


# Test the function
number = float(input("Enter a number: "))
print(f"The number {number} in words is: {convert_decimal_to_words(number)}")
