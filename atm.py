balance = 10000
transactions = []

def show_menu():
  print("\nthis is a virtual ATM!")
  print("1. View Transaction History")
  print("2. Withdraw Cash")
  print("3. Deposit Cash")
  # Placeholder for transfer (not implemented in this example)
  print("4. Transfer Money (Not Implemented)")
  print("5. Quit")

def view_history():
  if not transactions:
    print("There are no transactions to display.")
  else:
    print("\nTransaction History:")
    for transaction in transactions:
      print(transaction)

def withdraw_cash():
  global balance
  amount = float(input("Enter amount to withdraw: "))
  if amount > balance:
    print("Insufficient balance")
  else:
    balance -= amount
    transactions.append(f"Withdrew: ${amount:.2f}")
    print(f"${amount:.2f} withdrawn. New balance: ${balance:.2f}")

def deposit_cash():
  global balance
  amount = float(input("Enter amount to deposit: "))
  balance += amount
  transactions.append(f"Deposited: ${amount:.2f}")
  print(f"${amount:.2f} deposited. New balance: ${balance:.2f}")

def main():
  while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
      view_history()
    elif choice == '2':
      withdraw_cash()
    elif choice == '3':
      deposit_cash()
    elif choice == '4':
      print("Transfer not yet available.")
    elif choice == '5':
      print("Thank you for using the ATM.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
