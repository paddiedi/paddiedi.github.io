import json, os

filters_path = os.path.join(os.path.dirname(__file__), 'settings', 'filters.json')
settings_path = os.path.join(os.path.dirname(__file__), 'settings', 'settings.json')
filters = None
settings = None
# Haetaan tiedot tiedostoista yms.

with open(filters_path, "r", encoding="utf-8") as file:
    filters = json.load(file)
with open(settings_path, "r", encoding="utf-8") as file:
    settings = json.load(file)
# Poistaa oman filtterin
filters.pop(settings["HOME"])