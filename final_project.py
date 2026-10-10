def is_adult(age):
    return age >= 18

def check_user(name, age):
    print(f"Checking {name}... age {age}")
    if is_adult(age):
        print(f"  -> Access GRANTED for {name}")
    else:
        print(f"  -> Access DENIED for {name} - Must be 18+")
    print("---")

# User database
users = [
    {"name": "Amahle", "age": 20},
    {"name": "Thando", "age": 16},
    {"name": "Lulu", "age": 22},
    {"name": "Zama", "age": 17},
    {"name": "Sipho", "age": 30}
]

print("=== IT ACCESS CHECKER STARTING ===")

# LOOP through every user
for user in users:
    check_user(user["name"], user["age"])

print("=== All users checked! ===")