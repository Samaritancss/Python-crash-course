"""
Algorithm to mask a bank account number - hide all digits except the last four
"""

# Method 1: Using slicing and string multiplication
def mask_account_number_v1(account_number):
    """
    Masks bank account number, showing only last 4 digits
    Example: "123456789012" -> "********9012"
    """
    account_str = str(account_number)
    
    # Get the last 4 digits
    last_four = account_str[-4:]
    
    # Create asterisks for the hidden digits
    masked_digits = "*" * (len(account_str) - 4)
    
    # Concatenate masked digits with last four
    masked_account = masked_digits + last_four
    
    return masked_account


# Method 2: Using list comprehension and join
def mask_account_number_v2(account_number):
    """
    Alternative approach using list comprehension
    """
    account_str = str(account_number)
    
    # Mask all but last 4 digits
    masked = "".join(["*" if i < len(account_str) - 4 else digit 
                      for i, digit in enumerate(account_str)])
    
    return masked


# Method 3: Using format strings
def mask_account_number_v3(account_number):
    """
    Using f-string with slicing
    """
    account_str = str(account_number)
    return f"{'*' * (len(account_str) - 4)}{account_str[-4:]}"


# Test the algorithms
if __name__ == "__main__":
    # Test account numbers
    account1 = "123456789012"
    account2 = "987654321"
    account3 = "1111222233334444"
    
    print("=== Bank Account Number Masking ===\n")
    
    print(f"Original Account: {account1}")
    print(f"Method 1: {mask_account_number_v1(account1)}")
    print(f"Method 2: {mask_account_number_v2(account1)}")
    print(f"Method 3: {mask_account_number_v3(account1)}")
    
    print(f"\nOriginal Account: {account2}")
    print(f"Masked: {mask_account_number_v1(account2)}")
    
    print(f"\nOriginal Account: {account3}")
    print(f"Masked: {mask_account_number_v1(account3)}")
    
    # Interactive example
    print("\n=== Interactive Example ===")
    user_account = input("Enter a bank account number: ")
    print(f"Masked Account: {mask_account_number_v1(user_account)}")
