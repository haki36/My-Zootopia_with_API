"""
Zoo JSON Project

This script loads animal data from a JSON file (`animals_data.json`), generates a short
summary for each animal, and injects the generated text into an HTML template by replacing
a placeholder string. The final result is written to a new HTML file.

Data expectations:
- The JSON file contains a list of dictionaries (one dictionary per animal).
- Some fields may be optional or missing.

Output rules for the generated summary:
- Only fields that exist are included.
- Missing fields (e.g., diet, type, locations) are skipped without raising errors.
- If locations are available, only the first location is used.
- Animal blocks are separated by a blank line for readability.

Goal:
- Practice safe access to nested JSON structures (dicts and lists).
- Avoid KeyError and IndexError by checking keys and list length before access.
"""

from dotenv import load_dotenv
load_dotenv()
import json

import os
import requests

BASE = "\t\t\t"
I0 = BASE + "\t"
I1 = BASE + "\t\t"
I2 = BASE + "\t\t\t"
I3 = BASE + "\t\t\t\t"

api_key = os.getenv("API_KEY")

URL_GET = 'https://api.api-ninjas.com/v1/animals'


def fetch_animals_from_api(name: str):
    params = {"name": name}
    headers = {"X-Api-Key": api_key}

    res = requests.get(URL_GET, params=params, headers=headers)
    print("Status:", res.status_code)
    res.raise_for_status()

    return res.json()


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """
    Serialize a single animal dictionary into an HTML <li> card.
    The function builds a small HTML snippet that matches the template structure:
    - Wraps the animal in <li class="cards__item"> ... </li>
    - Adds a title line with the animal name (if present)
    - Adds a <p class="card__text"> block containing optional lines for:
        - diet (from characteristics.diet)
        - type (from characteristics.type)
        - location (first entry from locations)
        - added extra field of animals
    Missing fields are skipped (no placeholder text is inserted).
    Newlines and tab characters are included only to make the generated HTML more readable.
    Args:
        animal_obj (dict): One animal record (a dictionary) possibly containing keys like
            "name", "locations", and "characteristics".
    Returns:
        str: An HTML string representing this animal as a list item.
    """

    output = ''
    output += BASE + '<li class="cards__item">\n'
    if "name" in animal_obj:
        output += I0 + f'<div class="card__title">Name: {animal_obj["name"]}</div>\n'
    output += I0 + '<div class="card__text">\n'
    output += I1 + '<ul>\n'
    if animal_obj.get("characteristics"):
        if animal_obj["characteristics"].get("diet"):
            output += I2 + (f'<li><strong>Diet: </strong>'
                            f'{animal_obj["characteristics"]["diet"]}</li>\n')
        if animal_obj["characteristics"].get("type"):
            output += (I2 + f'<li><strong>Type: </strong>'
                       f'{animal_obj["characteristics"]["type"]}</li>\n')
        if animal_obj["characteristics"].get("lifespan"):
            output += (I2 + f'<li><strong>Lifespan: </strong>'
                       f'{animal_obj["characteristics"]["lifespan"]}</li>\n')
        if animal_obj["characteristics"].get("weight"):
            output += (I2 + f'<li><strong>Weight: </strong>'
                       f'{animal_obj["characteristics"]["weight"]}</li>\n')
        if animal_obj["characteristics"].get("length"):
            output += (I2 + f'<li><strong>Length: </strong>'
                       f'{animal_obj["characteristics"]["length"]}</li>\n')
        if animal_obj["characteristics"].get("skin_type"):
            output += (I2 + f'<li><strong>Skin type: </strong>'
                       f'{animal_obj["characteristics"]["skin_type"]}</li>\n')

    if "locations" in animal_obj and len(animal_obj["locations"]) >= 1:
        output += I2 + f'<li><strong>Location: </strong>{animal_obj["locations"][0]}</li>\n'
    output += I1 + '</ul>\n'
    output += I0 + '</div>\n'
    output += BASE + '</li>\n'

    return output


def get_animal_summary(data_of_animals):
    """
    Build the complete HTML snippet for all animals by concatenating per-animal cards.
    This function loops through a list of animal dictionaries and uses `serialize_animal()`
    to generate one HTML <li> block per animal. The returned string is intended to be
    inserted into an HTML template (e.g., by replacing a placeholder within a <ul>).
    Args:
        data_of_animals (list[dict]): A list of animal records loaded from JSON.
    Returns:
        str: The combined HTML for all animals (multiple <li> blocks).
    """

    output = ''

    for animal in data_of_animals:
        output += serialize_animal(animal)

    return output


def update_html_file(old_html, new_html, old_content, new_content):
    """
    Create a new HTML file by replacing a placeholder string in a template file.
    This function reads `old_html`, replaces all occurrences of `old_content` with
    `new_content`, and writes the result to `new_html`.
    Args:
        old_html (str): Path to the input HTML template file.
        new_html (str): Path to the output HTML file to write.
        old_content (str): Placeholder text to be replaced (e.g., "__REPLACE_ANIMALS_INFO__").
        new_content (str): Replacement text to insert into the template.
    Returns:
        None
    """
    with open(old_html, "r", encoding="utf-8") as handle:
        old_file = handle.read()

        new_file = old_file.replace(old_content, new_content)

    with open(new_html, "w", encoding="utf-8") as f:
        f.write(new_file)


def get_all_skin_of_animal(data_of_animals):
    """
    Collect all available skin_type values from the animals data.
    Animals without a "characteristics" dict or without "skin_type" are ignored.
    Args:
        data_of_animals (list[dict]): List of animal records.
    Returns:
    list[str]: Unique skin_type values found in the dataset.
    """

    summary_skin_type = []
    for hair in data_of_animals:
        if hair.get("characteristics"):
            if hair["characteristics"].get("skin_type"):
                summary_skin_type.append(hair["characteristics"]["skin_type"])
    summary_skin_type = list(set(summary_skin_type))

    return summary_skin_type


def filter_by_skin_type(animals, skin):
    """
    Filter animals by an exact skin_type match (case-insensitive).
    Animals missing "characteristics" or "characteristics.skin_type" are ignored.
    Args:
        animals (list[dict]): List of animal records.
        skin (str): Desired skin_type (e.g. "Hair").
    Returns:
    list[dict]: Animals whose skin_type matches the requested value.
    """

    skin = skin.strip().lower()
    filtered_animals = []

    for animal in animals:
        characteristics = animal.get("characteristics")
        if not characteristics:
            continue
        animal_skin = characteristics.get("skin_type")
        if not animal_skin:
            continue
        if animal_skin.strip().lower() == skin:
            filtered_animals.append(animal)

    return filtered_animals


def user_choice():
    """
    Ask the user for a skin type to filter by.
    Rules:
    - Empty input ("") means: generate HTML for all animals.
    - "exit" or "quit" means: terminate the program.
    - Digits are rejected.
    Returns:
        str: The user's input (lowercased), "" for all animals, or "exit".
    """

    while True:
        choice = input("Enter skin type you are looking for "
                       "or 'exit' for quit: ").strip().lower()

        if choice == "":
            return choice
        if choice.isdigit():
            print("Input cannot be a digit")
            continue
        if choice in ("quit", "exit"):
            return "exit"

        return choice


def main():
    """
    Program entry point.
    - Loads the animals JSON data.
    - Prints all available skin types found in the file.
    - Prompts the user to choose one of the listed skin types (or press Enter for all).
    - Generates an HTML page containing only animals that match the chosen skin type.
      Animals without a skin_type are excluded from filtered results.
    Returns:
        None
    """

    animal_name = input('Enter a name of an animal: ').strip()

    result_animals_data = fetch_animals_from_api(animal_name)

    if not result_animals_data:
        error_html = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
        update_html_file(
            "animals_template.html",
            "animals.html",
            "__REPLACE_ANIMALS_INFO__",
            error_html
        )
        print("Website was successfully generated to the file animals.html.")
        return

    skins = get_all_skin_of_animal(result_animals_data)
    allowed_skins = {s.lower() for s in skins}

    while True:
        print('Empty for all animals or choose / write available skins')
        print('Available skins are: ')
        for skin in skins:
            print(skin)
        print()

        user_input = user_choice().strip().lower()
        if user_input == "exit":
            print("Bye!")
            break
        if user_input == "":
            summary = get_animal_summary(result_animals_data)
            update_html_file(
                "animals_template.html",
                "animals.html",
                "__REPLACE_ANIMALS_INFO__",
                summary)
            print("Website was successfully generated to the file animals.html.")
            break
        if user_input not in allowed_skins:
            print("Please choose one of the available skins")
            continue

        filtered = filter_by_skin_type(result_animals_data, user_input)
        summary = get_animal_summary(filtered)

        update_html_file(
        "animals_template.html",
        "animals.html",
        "__REPLACE_ANIMALS_INFO__",
            summary)
        print("Website was successfully generated to the file animals.html.")
        break


if __name__ == "__main__":
    main()

