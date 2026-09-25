# Python Program to Calculate Z-Bus Matrix
# Zbus = inverse of Ybus

import numpy as np

print("========================================")
print("        Z-BUS MATRIX CALCULATOR")
print("========================================")

# Number of buses
n = int(input("Enter the number of buses: "))

print("\nEnter the Y-Bus matrix elements:")

# Create Y-bus matrix
Ybus = np.zeros((n, n), dtype=complex)

for i in range(n):
    for j in range(n):
        real = float(input(f"Real part of Y[{i+1},{j+1}]: "))
        imag = float(input(f"Imaginary part of Y[{i+1},{j+1}]: "))
        Ybus[i, j] = complex(real, imag)

# Check whether Ybus is invertible
if np.linalg.det(Ybus) == 0:
    print("\nY-Bus matrix is singular.")
    print("Z-Bus matrix cannot be calculated.")
else:
    # Calculate Z-bus
    Zbus = np.linalg.inv(Ybus)

    print("\n------------- Y-BUS MATRIX -------------")
    print(Ybus)

    print("\n------------- Z-BUS MATRIX -------------")
    
    for i in range(n):
        for j in range(n):
            print(
                f"Z[{i+1},{j+1}] = "
                f"{Zbus[i, j].real:.4f} "
                f"+ j{Zbus[i, j].imag:.4f} ohm"
            )

    print("-----------------------------------------")
