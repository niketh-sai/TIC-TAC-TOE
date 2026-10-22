"""
Sound Effects Generator
Generates basic beep sounds for the game using Python's standard library
Run this script to create basic sound effects if needed
"""

import winsound
import time


def play_click():
    """Play a short click sound"""
    winsound.Beep(1000, 100)


def play_move():
    """Play a move placement sound"""
    winsound.Beep(800, 150)


def play_win():
    """Play a victory sound"""
    for _ in range(3):
        winsound.Beep(1200, 200)
        time.sleep(0.1)


def play_draw():
    """Play a draw notification sound"""
    winsound.Beep(600, 300)


if __name__ == "__main__":
    print("Sound Effects Generator")
    print("======================")
    print("\nThis script demonstrates basic sound effects using Windows API.")
    print("Note: This only works on Windows systems.")
    print("\nTo test sounds:")
    print("1. click - Short click sound")
    print("2. move - Move placement sound")
    print("3. win - Victory sound")
    print("4. draw - Draw notification sound")
    print("5. all - Test all sounds")
    print("6. exit - Exit")
    
    while True:
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == "1":
            print("Playing click sound...")
            play_click()
        elif choice == "2":
            print("Playing move sound...")
            play_move()
        elif choice == "3":
            print("Playing win sound...")
            play_win()
        elif choice == "4":
            print("Playing draw sound...")
            play_draw()
        elif choice == "5":
            print("Playing all sounds...")
            play_click()
            time.sleep(0.5)
            play_move()
            time.sleep(0.5)
            play_win()
            time.sleep(0.5)
            play_draw()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1-6.")
