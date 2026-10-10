def is_adult(age):
    return age >= 18

print("=== INTERACTIVE IT ACCESS CHECKER ===")
print("Type 'exit' for name to quit")
print("")

while True:
    name = input("Enter name: ")
    
    if name.lower() == "exit":
        print("Goodbye! Checker closed.")
        break
    
    age_text = input(f"Enter age for {name}: ")
    
    # Convert text to number
    try:
        age = int(age_text)
    except:
        print("Please enter a number for age!")
        print("---")
        continue

    if is_adult(age):
        print(f"-> Access GRANTED for {name}, age {age}")
    else:
        print(f"-> Access DENIED for {name}, age {age} - Must be 18+")
    
    print("---")