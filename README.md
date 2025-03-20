# Character Counter

A Python program that uses regular expressions (regex) to count specific types of characters in a user-entered sentence. It categorizes characters into lowercase vowels, uppercase vowels, lowercase consonants, uppercase consonants, and numbers, then displays the counts.

## Features
- Counts lowercase vowels (e.g., 'a', 'e', 'i', 'o', 'u').
- Counts uppercase vowels (e.g., 'A', 'E', 'I', 'O', 'U').
- Counts lowercase consonants (e.g., 'b', 'c', 'd', etc.).
- Counts uppercase consonants (e.g., 'B', 'C', 'D', etc.).
- Counts numbers (e.g., '0', '1', '2', etc.).
- Allows the user to quit by typing 'q'.
- Handles empty input with a prompt to enter text.

## How It Works
1. The program prompts the user to enter a sentence.
2. It uses regex patterns to count the specified character types.
3. The counts are stored in a dictionary and displayed to the user.
4. The program runs in a loop, allowing multiple inputs until the user types 'q' to quit.

## Requirements
- Python 3.x
- The `re` module (included in Python's standard library)

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/character-counter.git
