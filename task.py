userfruits = int(input("How many is your favorite fruits: "))
listfruits = []

for i in range(userfruits):
    fruits = input("Enter fruits: ") 
    listfruits.append(fruits)

    if fruits == "apple":
        print("HAPPY EATING!")
    elif fruits == "banana":
            break

print(listfruits)