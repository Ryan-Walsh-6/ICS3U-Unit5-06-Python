#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: January 2021
# this program rounds a number to the decimal places entered by the user


def decimal_converter(adder, decimal_places_from_user):
    # calculates volume

    # process & output
    adder[0] = (adder[0] * 10 ** decimal_places_from_user)
    adder[0] = adder[0] + 0.5
    adder[0] = int(adder[0])
    adder[0] = (adder[0] / 10 ** decimal_places_from_user)


def main():
    # this program rounds a number to the decimal places entered by the user

    adder = []
    while True:
        try:
            decimal_from_user = input("Enter the number you want to round:")
            decimal_from_user = float(decimal_from_user)
            decimal_places_from_user = input("Enter how many decimal places"
                                             " you want to round by:")
            print("\n", end="")
            decimal_places_from_user = int(decimal_places_from_user)
            if decimal_places_from_user < 0:
                print("The amount of decimal places must be above 0")
                print("\n", end="")
            else:
                break
        except Exception:
            print("Please enter a valid number.")
            print("\n", end="")

    adder.append(decimal_from_user)
    # call function
    decimal_converter(adder, decimal_places_from_user)

    print("The rounded number is {0}".format(adder[0]))


if __name__ == "__main__":
    main()
