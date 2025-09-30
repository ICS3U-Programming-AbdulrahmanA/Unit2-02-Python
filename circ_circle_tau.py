#!/usr/bin/env python3
# Created By: Abdul
# Date: 9/29/2025
# Circumference of a circle

# Import tau from the constants file
from constants import TAU


def main():

    # Ask user for the radius
    radius = float(input("Enter the radius of the circle (in cm): "))

    # Calculate circumference
    circumference = TAU * radius

    # Display the result
    print(f"The circumference of the circle is: {circumference:.2f} cm")


if __name__ == "__main__":
    main()
