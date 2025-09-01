# Password Manager
#### Description:    A command-line password management tool that securely stores and encrypts user passwords using Fernet encryption from Python's cryptography library.

## Features
- Secure encryption of all stored passwords
- Basic master password protection
- Add new password entries
- View stored passwords
- Delete existing accounts/passwords
- Automatic key generation
- Storage in encrypted format

    ### File Functions
- `project.py`: Main application file containing all program logic, contains key generation (pytest removes key.key and password.txt)
- `test_project.py`: Test file containing pytest unit tests
- `key.key`: Auto Generated encryption key file
- `password.txt`: Auto generated Encrypted password storage file

    ### Core functions
- `add_key()`: Handles encryption key generation and retrieval
- `view()`: Decrypts and displays stored passwords
- `add()`: Encrypts and stores new passwords
- `delete()`: Manages password entry removal
- `main()`: Controls program flow and user interaction

    ### Design choices
1. Master Password being included - This was one I debated a bit. On one hand there was no real usability of it functionality wise but for the sake of having something cool and gimmicky I opted to keep it in. Initially I wanted to make it very secure but I realised it would be alot more complicated than previously thought.
2. Simple print outputs - This is somewhat of a characteristics in my projects. In my opinion the less writing in the terminal the better.
3. File storage - Plain text files used for simplicity, though a database would be better for production.

## Testing
The project includes pytest unit tests that verify:
- Key generation and retrieval
- Password viewing functionality
- New password addition
- File handling operations

This was in my opinion the most frustrating part of the project.
With each fix another 2 issues showed up and using solutions I had never touched before definitely pushed me to the limits.
A prevalent issue was key generation not working after pytest, however after some tinkering to my main project this somehow vanished ;/

RUN : 'pytest test_project.py -v'

## Future Improvements
1. Implement proper user authentication
2. Add password strength checking / password generator feature
3. Convert to database storage
4. Stronger password encryption than Fernet

## This has been CS50P!!!!

