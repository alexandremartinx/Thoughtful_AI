import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import Package

def input_package(index):
    while True:
        try:
            print(f"Enter values for package {index}:")
            length = float(input("  Length (cm): "))
            width = float(input("  Width (cm): "))
            height = float(input("  Height (cm): "))
            mass = float(input("  Mass (kg): "))
            if length < 0 or width < 0 or height < 0 or mass < 0:
                print("Values cannot be negative. Please try again.")
                continue
            pkg = Package(width, height, length, mass)  # note order per your class
            print(f"  -> Package {index} created with Length={pkg.length:.2f} cm, Width={pkg.width:.2f} cm, Height={pkg.height:.2f} cm, Mass={pkg.mass:.2f} kg")
            return pkg
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def generate_random_package():
    length = random.uniform(0, 2000)
    width = random.uniform(0, 2000)
    height = random.uniform(0, 2000)
    mass = random.uniform(0, 100)
    pkg = Package(width, height, length, mass)
    print(f"  -> Random package generated with Length={pkg.length:.2f} cm, Width={pkg.width:.2f} cm, Height={pkg.height:.2f} cm, Mass={pkg.mass:.2f} kg")
    return pkg

def print_packages(pkgs):
    print("\nPackage details:")
    for i, pkg in enumerate(pkgs, 1):
        print(f" Package {i}: Length={pkg.length:.2f} cm, Width={pkg.width:.2f} cm, Height={pkg.height:.2f} cm, Mass={pkg.mass:.2f} kg")

def run_test_case(test_number):
    test_cases = {
        1: ("Standard Packages Only", [
            Package(30, 40, 50, 5),
            Package(60, 70, 80, 10),
            Package(90, 100, 110, 18),
        ]),
        2: ("Heavy but Not Bulky", [
            Package(50, 50, 50, 20),
            Package(30, 40, 60, 25),
        ]),
        3: ("Bulky but Not Heavy", [
            Package(150, 100, 100, 10),
            Package(200, 80, 80, 15),
        ]),
        4: ("Rejected Packages (Bulky + Heavy)", [
            Package(200, 200, 200, 25),
            Package(150, 150, 150, 21),
        ]),
        5: ("Edge Conditions", [
            Package(100, 100, 100, 19),
            Package(100, 100, 100, 20),
            Package(149, 149, 149, 19),
            Package(150, 150, 150, 20),
        ]),
        6: ("Zero and Minimal Values", [
            Package(1, 1, 1, 0),
            Package(0, 0, 0, 0),
            Package(10, 10, 10, 1),
        ]),
        7: ("Extremely Large Packages", [
            Package(1000, 1000, 1000, 1000),
            Package(10000, 10000, 10000, 9999),
        ]),
        8: ("Mixed Valid and Invalid Inputs", [
            Package(50, 50, 50, 5),
            Package(200, 50, 50, 10),
            Package(50, 50, 50, 25),
            Package(200, 200, 200, 25),
            Package(150, 150, 150, 21),
            Package(1, 1, 1, 1),
        ]),
    }

    name, default_pkgs = test_cases[test_number]
    print(f"\nRunning Test Case {test_number} – {name}")

    while True:
        choice = input("Choose input method:\n"
                       " 1 - Use predefined values\n"
                       " 2 - Enter your own values\n"
                       " 3 - Generate random packages\n"
                       "Choose (1/2/3): ").strip()

        if choice not in ['1', '2', '3']:
            print("Invalid option. Please choose 1, 2 or 3.")
            continue

        if choice == '1':
            pkgs = default_pkgs
            break

        elif choice == '2':
            pkgs = []
            try:
                n = int(input("How many packages do you want to enter? "))
                if n <= 0:
                    print("Number must be positive.")
                    continue
            except ValueError:
                print("Invalid number.")
                continue
            for i in range(1, n + 1):
                pkgs.append(input_package(i))
            break

        elif choice == '3':
            pkgs = []
            try:
                n = int(input("How many random packages to generate? "))
                if n <= 0:
                    print("Number must be positive.")
                    continue
            except ValueError:
                print("Invalid number.")
                continue
            for _ in range(n):
                pkgs.append(generate_random_package())
            break

    print_packages(pkgs)

    print("\nClassification results:")
    for i, pkg in enumerate(pkgs, 1):
        print(f" Package {i}: {pkg.classify()}")

def main():
    print("Package Classification Test Suite")
    while True:
        print("\nSelect a test case to run:")
        print(" 1 - Standard Packages Only")
        print(" 2 - Heavy but Not Bulky")
        print(" 3 - Bulky but Not Heavy")
        print(" 4 - Rejected Packages (Bulky + Heavy)")
        print(" 5 - Edge Conditions")
        print(" 6 - Zero and Minimal Values")
        print(" 7 - Extremely Large Packages")
        print(" 8 - Mixed Valid and Invalid Inputs")
        print(" 9 - Exit")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == '9':
            print("Exiting. Goodbye!")
            break

        if choice not in [str(i) for i in range(1, 9)]:
            print("Invalid choice. Please select from 1 to 9.")
            continue

        run_test_case(int(choice))


if __name__ == "__main__":
    main()
