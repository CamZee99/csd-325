import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys

def display_menu():
    print("\nWelcome to the Sitka Weather Viewer (2018)")
    print("Please select an option:")
    print("1 - View HIGH temperatures")
    print("2 - View LOW temperatures")
    print("3 - Exit the program")

def read_weather_data(filename):
    """Reads dates, highs, and lows from a CSV file."""
    dates, highs, lows = [], [], []
    try:
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                try:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    high = int(row[5])
                    low = int(row[6])
                except ValueError:
                    print(f"Missing or invalid data for {row[2]}")
                    continue
                else:
                    dates.append(current_date)
                    highs.append(high)
                    lows.append(low)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit()
    return dates, highs, lows

def plot_temperatures(dates, temps, label, color):
    """Plots the given temperatures against dates."""
    plt.figure(figsize=(10,6))
    plt.plot(dates, temps, c=color)
    plt.title(f"Daily {label} Temperatures - 2018", fontsize=20)
    plt.xlabel('', fontsize=14)
    plt.ylabel("Temperature (F)", fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.show()

def main():
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = read_weather_data(filename)

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            plot_temperatures(dates, highs, "High", "red")
        elif choice == '2':
            plot_temperatures(dates, lows, "Low", "blue")
        elif choice == '3':
            print("Thank you for using the Sitka Weather Viewer. Goodbye!")
            sys.exit()
        else:
            print("Invalid selection. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()

# Instructions Are Now Displayed In The Program.
# Reads Weather Data In Next Step.
# Plots High Or Low Temperatures or Will Exit the Program
# Based On User Input.
# Main Program Set To Loop Until User Exits.