# Random Password Generator

## This program will generate a random password for you

## Description

This project is a command-line tool for generating random passwords with customizable length and complexity. Users can specify password requirements such as including uppercase letters, lowercase letters, digits, and special characters. The application ensures that the generated passwords are secure and random, making them resistant to brute-force attacks and guessing.

## How to Run

Ensure Python is Installed:
    Check if Python 3 is installed on your system:
    python3 --version

## Set Up the Project

Clone the repository or create the project directory structure:

random-password-generator/
|-- password_generator.py
|-- README.md
|-- launch.json
Place the password_generator.py script in the project directory.

## Run the script

## Open a terminal (integrated terminal in Visual Studio Code or any other terminal application)

``` sh
cd path/to/Random_Password_Generator

```

## Run the script with desired arguments (replace `<length>` with an integer value for password length)

``` sh

python3 password_generator.py --length 12 --uppercase --lowercase --digits --special


```

## Notes

1. Ensure that at least one character type (--uppercase, --lowercase, --digits, --special) is selected when running the script.

2. Adjust the --length parameter to change the length of the generated password.

This README.md file provides clear instructions on setting up and running the Random Password Generator project. It includes details on prerequisites, project setup, running the script, and additional notes for users.
