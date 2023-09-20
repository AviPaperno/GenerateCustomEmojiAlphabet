from letter_generator import generate_all_alphabet
from emoji import add_emoji_alphabet
from constants import alphabet

api_id = None
api_hash = ""
session_name = "my_account"

if __name__ == "__main__":
    font = "Kablammo"
    generate_all_alphabet(f"fonts/{font}.ttf", alphabet, color=(255, 87, 51))
    add_emoji_alphabet(font, api_id, api_hash, session_name)
