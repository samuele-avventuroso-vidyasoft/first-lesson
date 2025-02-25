age_people = {
    "Alice": 30,
    "Bob": 25,
    "Carla": 28
}

print(f"Alice's age is: {age_people['Alice']}")

age_people["Dario"] = 32
age_people["Bob"] = 26

for name, age in age_people.items():
    print(f"{name} is {age} years old.")

del age_people["Carla"]

if "Carla" in age_people:
    print("Carla is present in the dictionary.")
else:
    print("Carla is not present in the dictionary")
    
if "Dario" in age_people:
    print("Dario is present in the dictionary.")
else:
    print("Dario is not present in the dictionary")
