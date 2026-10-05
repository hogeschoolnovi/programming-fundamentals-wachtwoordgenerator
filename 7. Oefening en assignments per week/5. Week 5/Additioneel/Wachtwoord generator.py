import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+-=[]{};:,.<>?"
numbers = "0123456789"

amount_letters = int(input("Hoeveel letters wil je in je wachtwoord? "))
amount_symbols = int(input("Hoeveel symbolen wil je in je wachtwoord? "))
amount_numbers = int(input("Hoeveel nummers wil je in je wachtwoord? "))

password = ""

for i in range(amount_letters):
    password += random.choice(letters)

for i in range(amount_symbols):
    password += random.choice(symbols)

for i in range(amount_numbers):
    password += random.choice(numbers)

print("Je wachtwoord is:", password)