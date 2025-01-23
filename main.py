# Display a welcome message
print("Thank you for choosing Python Pizza Deliveries!")

# Initialize the bill variable to track the total price
bill = 0

# Prompt the user to choose a pizza size (S, M, or L)
size = str(input("What size pizza do you want? (S, M or L)"))

# Price calculations based on the pizza size
if size == "S":
  bill = bill + 15  # Small pizza costs $15
  add_pepperoni = bool(input("Do you want pepperoni? Y or N"))
  if add_pepperoni == "Y":
    bill = bill + 2  # Add $2 for pepperoni
  extra_cheese = input("Do you want extra cheese? Y or N")
  if extra_cheese == "Y":
    bill = bill + 1  # Add $1 for extra cheese

elif size == "M":
  bill = bill + 20  # Medium pizza costs $20
  add_pepperoni = input("Do you want pepperoni? Y or N")
  if add_pepperoni == "Y":
    bill = bill + 3  # Add $3 for pepperoni
  extra_cheese = input("Do you want extra cheese Y or N?")
  if extra_cheese == "Y":
    bill = bill + 1  # Add $1 for extra cheese

else:
  bill = bill + 25  # Large pizza costs $25
  add_pepperoni = input("Do you want pepperoni? Y or N")
  if add_pepperoni == "Y":
    bill = bill + 3  # Add $3 for pepperoni
  extra_cheese = input("Do you want extra cheese? Y or N")
  if extra_cheese == "Y":
    bill = bill + 1  # Add $1 for extra cheese

# Display the final bill to the user
print(f"Your final bill is ${bill}")
