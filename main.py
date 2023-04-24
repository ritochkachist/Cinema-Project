# Margarita Chistiakova
# 11/1/2022
# Additional project 10

print("Welcome to our cinema! We have a lot of new movies that you can watch!")
movies = ["Black Adam", "Ticket to Paradise", "Prey for the Devil", "Halloween Ends", "Smile", "Call Jane", "The Bad Guys"]
for movie in movies:
  print(f"The movie: {movie}")

movie_price = 0

choice = input("What movie would you like to watch?\n")
if choice == "Black Adam":
  print("The price for the ticket for this movie is $10")
  movie_price = movie_price + 10
elif choice == "Ticket to Paradise":
  print("The price for the ticket for this movie is $12")
  movie_price = movie_price + 12
elif choice == "Prey for the Devil":
  print("The price for the ticket for this movie is $15")
  movie_price = movie_price + 15
elif choice == "Halloween Ends":
  print("The price for the ticket for this movie is $8")
  movie_price = movie_price + 8
elif choice == "Smile":
  print("The price for the ticket for this movie is $15")
  movie_price = movie_price + 15
elif choice == "Call Jane":
  print("The price for the ticket for this movie is $7")
  movie_price = movie_price + 7
elif choice == "The Bad Guys":
  print("The price for the ticket for this movie is $10")
  movie_price = movie_price + 10
else:
  print("This movie is not broadcasted in our theatre at the moment")

input()

print("We also have a wide variety of snacks and drinks!")
snacks = ['Chips', 'Popcorn', 'Candy', 'Pizza slices', 'Nuts']
for snack in snacks:
  print(f"We have {snack}")

snack_price = 0

choice2 = input("What snacks do you wanna buy?\n")
if choice2 == 'Chips':
  print("The cost of this snack is $2")
  snack_price += 2
elif choice2 == 'Popcorn':
  print("The cost of this snack is $1.50")
  snack_price = snack_price + 1.50
elif choice2 == 'Candy':
  print("The cost of this snack is $1")
  snack_price = snack_price + 1
elif choice2 == 'Pizza slices':
  print("The cost of this snack is $1.50 per piece")
  snack_price = snack_price + 1.50
elif choice2 == 'Nuts':
  print("The cost of this snack is $1.25")
  snack_price = snack_price + 1.25
elif choice2 == 'None':
  print("Okay! What about drinks?")

input()

drink_price = 0
print("As for beverages,")
drinks = ['Water', 'Soda', 'Juice', 'Iced Tea', 'Coffee']
for drink in drinks:
  print(f"We have {drink}")

choice4 = input("What have you chosen?\n")
if choice4 == 'Water':
  print("The cost of this drink is $1")
  drink_price += 1
elif choice4 == 'Soda':
  print("The cost of this drink is $1.50")
  drink_price += 1.50
elif choice4 == 'Juice':
  print("The cost of this drink is $1.75")
  drink_price += 1.75
elif choice4 == 'Iced Tea':
  print("The cost of this drink is $2")
  drink_price = drink_price + 2
elif choice4 == 'Coffee':
  print("The cost of this drink is $2.20")
  drink_price = drink_price + 2.20

input()

total = movie_price + snack_price + drink_price

print(f"So, you would like to watch {choice}, eat {choice2}, and drink {choice4}, which came out to a total of ${total}")

input()

print("Thank you for choosing our cinema! Enjoy the film!")