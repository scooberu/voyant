# Voyant Coding Exercise

# Dependencies

I have made use of a few external libraries to complete this challenge. To install all dependencies on a Linux/UNIX system, execute the following command in the root directory for this project:

`pip install -r requirements.txt`

## Common Passwords Check

To execute this script, run `src/password_check \[STRING\]`, where `\[STRING\]` is potentially a commonly used password. The script will print a message indicating whether the password is one of the list of the 1000 most commonly used passwords according to a list file which is configurable within the script, but defaults to the file supplied in the exercise instructions.

## Weather
*Note*: Before running the weather.py script, you must first set the environment variable OWM\_API\_KEY to a valid OpenWeatherMap API key. I have provided a key for the purposes of evaluating my solution. On a Linux/UNIX/macOS system, you can set this environment variable using the following command in your shell:

`export OWM_API_KEY='d94aa5248e7ecf2be851189a6e3ad9af'`

Afterwards, the program may be executed by running `src/weather \[ZIP\]`, where `\[ZIP\]` is a valid 5-digit US ZIP code.


