from operator import length_hint

print(type("Jackson"))
print(type(123))
print(type(3.14))
print(type(True))


# Minha solução:
print("Number of letters in your name: " + str(len(input("Enter your name"))))

# Solução da Angela (mais legível):
# name_of_the_user  = input("Enter your name")
# length_of_the_name = len(name_of_the_user )
# print("Number of letters in your name: " + str(length_of_the_name))

name_of_the_user = input("What is your name?")
length_of_the_name = len(name_of_the_user)
print("Number of letters in your name: " + str(length_of_the_name))