from random import randint

print("Welcome to guessing game!")


def main():
    print("Enter a Number: ")
    number = randint(1, 10)
    limit = 3
    while True:
        n = int(input())
        if n == number:
            print("You win!")
            break
        elif limit == 0:
            print(f"Game over! The number was {number}")
            print("Do you want to play again? (y/n)")
            choice = input()
            if choice == "y":
                main()
            else:
                break
        elif n < number:
            print("Too low!")
            limit -= 1
            print(f"Remaining tries: {limit}")
            continue
        elif n > number:
            print("Too high!")
            limit -= 1
            print(f"Remaining tries: {limit}")
            continue
        else:
            print("Try again!")
            limit -= 1
            continue


main()
