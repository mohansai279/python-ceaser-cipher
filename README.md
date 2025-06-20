# python-ceaser-cipher
The Caesar Cipher program is a classic cryptography tool that encrypts and decrypts messages by shifting letters in the alphabet. Users can interactively input messages and a shift key, with the program running until they choose to exit.
# Caesar Cipher

## Project Overview

This program is a classic cryptography tool that implements the Caesar cipher. It allows a user to either encrypt a message (making it unreadable) or decrypt a coded message by shifting each letter of the alphabet by a specified number of places. The program is interactive, running in a loop until the user decides to exit.

Run the program using Python:

```bash
python 4.Caesar_cipher.py
```

Follow the prompts to either encrypt or decrypt a message by providing the desired text and the numerical shift key. Type 'no' when prompted if you wish to exit the program.

## Detailed Logic Breakdown

### Step 1: Establishing the Foundation: The Alphabet

- **Code**: `alphabet = ['a', 'b', 'c', ..., 'z']`
- **Purpose**: The entire logic of the cipher relies on having a defined, ordered sequence of characters to shift.
- **In-Depth**: An alphabet list is declared globally. This list acts as the fundamental reference for all encryption and decryption operations. Using a list is ideal because each letter has a specific index (position number), from 'a' at index 0 to 'z' at index 25. This makes it easy to find a letter's position and calculate its new, shifted position.

### Step 2: The Encryption Engine (encryption function)

- **Purpose**: This function takes a readable message (plain text) and a numerical key, transforming it into a secret message (cipher text).
- **In-Depth Logic**:
  - **Initialization**: An empty string `cipher_text = ""` is created. This variable will be built up, character by character, to form the final encrypted message.
  - **Character-by-Character Processing**: The function iterates through every single character in the input `plain_text`.
    - **Handling Alphabetic Characters**:
      - It first checks if the character exists in the alphabet list. This is crucial to avoid errors with spaces, numbers, or symbols.
      - If it's a letter, it finds its numerical position using `position = alphabet.index(char)`.
      - The core of the cipher is this calculation: `new_position = (position + shift_key) % 26`. The `+ shift_key` moves the letter down the alphabet. The modulo operator (`% 26`) ensures the shifting "wraps around." For example, if 'y' (position 24) is shifted by 3, the new position would be 27. `27 % 26` results in 1, which corresponds to 'b'. This elegant solution handles all wrap-around cases seamlessly.
      - The new character is retrieved from the alphabet (`alphabet[new_position]`) and appended to `cipher_text`.
    - **Handling Non-Alphabetic Characters**: If the character is not in the alphabet (e.g., a space, "!", or "5"), it appends the character unchanged to `cipher_text`, preserving the message's structure.
  - **Final Output**: Once the loop is complete, the final `cipher_text` is printed.

### Step 3: The Decryption Engine (decryption function)

- **Purpose**: This is the inverse of the encryption function. It takes a coded message and the original key to revert it back to readable plain text.
- **In-Depth Logic**: The process is a mirror image of encryption. The only fundamental difference is in the position calculation: `new_position = (position - shift_key) % 26`. By subtracting the shift key, it reverses the encryption process, moving letters back to their original positions. The modulo operator (`%`) continues to handle wrap-around, but in the opposite direction (e.g., from 'a' back to 'z').

### Step 4: The Interactive User Interface (The Main Loop)

- **Purpose**: This section acts as the program's control center, managing user interaction and calling the appropriate functions.
- **In-Depth Logic**:
  - A `while not wanna_end` loop keeps the program running continuously.
  - **User Choices**: Inside the loop, it prompts the user for three pieces of information:
    - The desired action (encrypt or decrypt).
    - The message (text).
    - The numerical shift key (shift).
  - **Conditional Execution**: An `if/elif` statement directs the program's flow. If the user types "encrypt", it calls `encryption()`. If they type "decrypt", it calls `decryption()`.
  - **Continuation Logic**: After an operation, it asks the user to type 'Yes' if they want to continue. If the user types "no", the `wanna_end` flag is set to True, gracefully ending the program with a "bye" message.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
