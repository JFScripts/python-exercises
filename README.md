# python-exercises

In this repository I will put my exercises from "CS50's Introduction to Programming with Python"

## Problem Set 0

* **Indoor Voice**
  WRITING IN ALL CAPS IS LIKE YELLING. Best to use your “indoor voice” sometimes, writing entirely in lowercase.
  In a file called `indoor.py`, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged.

* **Playback Speed**
  Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down.
  In a file called `playback.py`, implement a program that prompts the user for input and then outputs that same input, replacing each space with `...` (three periods).

* **Making Faces**
  Before there were emoji, there were emoticons, whereby text like `:)` was a happy face and text like `:(` was a sad face.
  In a file called `faces.py`, implement a function `convert` that accepts a `str` as input and returns that same input with any `:)` converted to 🙂 and any `:(` converted to 🙁. Then implement a `main` function that prompts the user, calls `convert`, and prints the result. Be sure to call `main` at the bottom of your file.

* **Einstein**
  Implement the mass–energy equivalence formula E = mc².
  In a file called `einstein.py`, prompt the user for mass as an integer (in kilograms) and output the equivalent number of Joules as an integer, assuming the speed of light is 300000000 m/s.

* **Tip Calculator**
  In the United States, it’s customary to leave a tip for your server after dining, typically 15% or more of your meal’s cost.
  In a file called `tip.py`, implement a program that prompts the user for the cost of a meal as a number and outputs how much to tip (15% of the cost), formatted to two decimal places.

## Problem Set 1

* **Deep Thought**
  In `deep.py`, prompt the user for the answer to the Great Question of Life, the Universe and Everything, outputting `Yes` if the input is `42` or (case-insensitively) `forty-two` or `forty two`; otherwise output `No`.

* **Home Federal Savings Bank**
  In `bank.py`, prompt the user for a greeting. If it starts with “hello”, output `$0`; if it starts with “h” (but not “hello”), output `$20`; otherwise output `$100`. Ignore leading whitespace and treat input case-insensitively.

* **File Extensions**
  In `extensions.py`, prompt the user for a filename and output its media type based on its extension (`.gif`, `.jpg`, `.jpeg`, `.png`, `.pdf`, `.txt`, `.zip`); otherwise output `application/octet-stream`.

* **Math Interpreter**
  In `interpreter.py`, prompt the user for an expression formatted as `x y z` (e.g., `1 + 1`) and output the result as a float with one decimal place. Assume `x` and `z` are integers and `y` is one of `+`, `-`, `*`, `/`.

* **Meal Time**
  In `meal.py`, implement `convert(time: str) -> float` that converts a 24-hour time (e.g., `7:30`) to hours as a float (e.g., `7.5`). In `main`, prompt for a time and output `breakfast time` if between 7:00–8:00, `lunch time` if between 12:00–13:00, `dinner time` if between 18:00–19:00; otherwise output nothing.

## Problem Set 2

* **camelCase**
  In `camel.py`, prompt the user for a variable name in camelCase and output the corresponding snake\_case version.

* **Coke Machine**
  In `coke.py`, simulate a machine that sells a Coke for 50 cents. Prompt the user to insert coins (25, 10, or 5 cents) until at least 50 cents is inserted; then output the change owed.

* **Just setting up my twttr**
  In `twttr.py`, prompt the user for text and output it with all vowels (A, E, I, O, U) removed (case-insensitively).

* **Vanity Plates**
  In `plates.py`, prompt the user for a vanity plate and output `Valid` if it:

  1. Starts with at least two letters,
  2. Has 2–6 characters,
  3. Has numbers only at the end (and the first number is not `0`),
  4. Contains no periods, spaces, or punctuation;
     otherwise output `Invalid`.

* **Nutrition Facts**
  In `nutrition.py`, prompt the user for a fruit (case-insensitively) and output the number of calories in one portion, per the FDA’s poster for the 20 most frequently consumed raw fruits.

## Problem Set 3

* **Fuel Gauge**
  In `fuel.py`, prompt the user for a fraction `X/Y`. If `X` and `Y` are integers, `0 < X ≤ Y`, and `Y ≠ 0`, output the tank’s fullness as a percentage (rounded to the nearest integer). If the result is ≤ 1%, output `E`; if ≥ 99%, output `F`. Otherwise, prompt again (handling `ValueError` and `ZeroDivisionError`).

* **Taqueria**
  In `taqueria.py`, given a `dict` menu of items to prices, prompt the user for items (case-insensitive) until Control‑D. After each valid item, output the total cost so far, formatted as `$x.xx`.

* **Grocery List**
  In `grocery.py`, prompt the user for grocery items until Control‑D. Then print each item in uppercase, sorted alphabetically, prefixed by the count of how many times it was entered (case-insensitive).

* **Outdated**
  In `outdated.py`, prompt the user for a date in `M/D/YYYY` or `Month D, YYYY` format (Month as full name). If valid (assuming all months ≤ 31 days), output it in ISO 8601 `YYYY-MM-DD` format; otherwise prompt again
