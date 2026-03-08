def play_round():
    choice = input("Choose a location to explore (forest/cave/beach): ").strip().lower()

    if choice == "forest":
        print("You step into the forest and discover glowing mushrooms under ancient trees.")
    elif choice == "cave":
        print("You enter the cave and find crystal walls sparkling in the darkness.")
    elif choice == "beach":
        print("You walk along the beach and uncover a message bottle in the sand.")
    else:
        print("Invalid choice. Please choose forest, cave, or beach.")


def main():
    print("Welcome to the Adventure Game!")

    while True:
        play_round()
        again = input("Would you like to explore another location? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
