import random

# Function to simulate UPI Payment
def upi_payment(vpa, amount, merchant_name):
    """
    Simulate a UPI payment process.
    Args:
    - vpa: Virtual Payment Address (UPI ID) of the user.
    - amount: Amount to be paid.
    - merchant_name: Name of the merchant or receiver.

    Returns:
    - transaction_status: A simulated status of the payment.
    """
    print(f"Initiating payment to {merchant_name}...\n")
    print(f"User UPI ID: {vpa}")
    print(f"Amount: ₹{amount}")
    
    # Simulate a payment attempt with a random success/failure
    transaction_id = random.randint(100000, 999999)
    
    # Simulate a random success or failure (80% chance of success)
    transaction_status = "Success" if random.random() < 0.8 else "Failed"
    
    # Display the transaction result
    if transaction_status == "Success":
        print(f"Payment successful! Transaction ID: {transaction_id}")
        print("Thank you for your payment!")
    else:
        print(f"Payment failed. Please try again.")
    
    return {
        "transaction_id": transaction_id,
        "status": transaction_status,
        "amount": amount
    }

# Main function to test UPI Payment
def main():
    print("Welcome to the UPI Payment Simulator!")
    
    # Collect UPI ID, amount, and merchant name
    user_vpa = input("Enter your UPI ID (Virtual Payment Address): ")
    amount = float(input("Enter the amount to be paid (₹): "))
    merchant = input("Enter the merchant name or business name: ")
    
    # Call the UPI payment simulation function
    transaction = upi_payment(user_vpa, amount, merchant)
    
    # Display payment status
    print("\nPayment Status:")
    print(f"Transaction ID: {transaction['transaction_id']}")
    print(f"Status: {transaction['status']}")
    print(f"Amount: ₹{transaction['amount']}")

if __name__ == "__main__":
    main()
