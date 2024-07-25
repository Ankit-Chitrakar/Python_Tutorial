# Write a program that will convert celsius value to fahrenheit

# °F = (9/5 × °C) + 32.


def change_to_farenhite(deg):
    return (9/5 * deg) + 32

celcius = int(input("Enter deg: "))


print(change_to_farenhite(celcius))