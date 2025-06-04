def countdown(bottles):
    while bottles > 0:
        if bottles == 1:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, 0 bottle(s) of beer on the wall.\n")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.\n")
        bottles -= 1

def main():
    try:
        count = int(input("Enter number of bottles:"))
        countdown(count)
        print("Time to buy more bottles of beer.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
