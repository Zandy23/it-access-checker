def check_user(name, age):
    print(f"Checking {name}...")
    if is_adult(age):
        print(f"Hello {name}, access granted. You are {age}.")
    else:
        print(f"Sorry {name}, you must be 18+. You are {age}.")

def is_adult(age):
    return age >= 18

# Our user list
users = [
    {"name": "Amahle", "age": 20},
    {"name": "Thando", "age": 16},
    {"name": "Lulu", "age": 22}
]

for user in users:
    check_user(user["name"], user["age"])
    print("---")