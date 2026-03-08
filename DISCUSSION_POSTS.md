# Discussion Post 1: Initial Post (Game Design)

For this activity, I designed a simple text-based adventure game called **"The Lost Temple Adventure."**

## Game Concept
The player is an explorer searching for treasure. They make decisions at key points in the story, and each choice leads to a different outcome. The game uses:
- **Conditional statements** (`if`, `elif`, `else`) to branch the story
- **User input handling** with `input()`
- **Input validation** through a helper function so users must enter valid choices
- **Basic game loop** so the player can replay without restarting the script

## Python Code
```python
def get_choice(prompt, valid_choices):
    """Prompt until the user enters a valid choice."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please enter one of: {', '.join(valid_choices)}")


def play_game():
    print("\n=== The Lost Temple Adventure ===")
    print("You are an explorer searching for a hidden treasure.")

    name = input("What is your name, adventurer? ").strip()
    if not name:
        name = "Explorer"

    print(f"\nWelcome, {name}!")
    print("You stand at the entrance of a dark jungle.")

    path = get_choice(
        "Do you go left toward the river or right into the cave? (left/right): ",
        {"left", "right"},
    )

    if path == "left":
        print("\nYou walk toward the river and see a weak bridge.")
        bridge = get_choice(
            "Do you cross the bridge or follow the riverbank? (cross/follow): ",
            {"cross", "follow"},
        )

        if bridge == "cross":
            print("\nThe bridge breaks, but you grab a vine and swing to safety!")
            print("You find an ancient chest full of gold. You win!")
        else:
            print("\nYou follow the river and find fresh footprints.")
            print("A friendly guide appears and helps you find the hidden temple. You win!")

    else:
        print("\nInside the cave, you hear a low growl.")
        action = get_choice(
            "Do you run away or light a torch? (run/torch): ",
            {"run", "torch"},
        )

        if action == "run":
            print("\nYou safely escape, but the treasure remains hidden. Game over.")
        else:
            print("\nWith the torch lit, you discover a sleeping jaguar and quietly sneak past.")
            print("Behind it is the temple treasure room. You win!")


def main():
    while True:
        play_game()
        again = get_choice("\nPlay again? (yes/no): ", {"yes", "no"})
        if again == "no":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
```

## Reflection
This project helped me understand how conditionals can create multiple story paths and how important input validation is for user experience. If I expand this game later, I would add inventory items and more scenes.

---

# Discussion Post 2: Peer Response (Example)

Hi [Classmate Name],

I really enjoyed your game idea and the way you used branching decisions to keep the player engaged. Your use of conditional statements was clear, and I liked how each choice had a different outcome.

One thing I especially noticed was your input handling—it makes the game feel smoother when users can only enter valid options. That’s a great design choice for beginner-friendly games.

A possible enhancement could be adding a replay loop so players can try different paths without rerunning the script manually. You could also include a scoring system to track successful decisions.

Overall, your design is creative and demonstrates the core Python concepts from this lesson very well.
