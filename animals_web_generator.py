import json

def load_data(file_path):
    """
    Lädt Daten aus einer JSON-Datei.

    Params:
        file_path (str): Der Pfad zur JSON-Datei.

    Returns:
        dict or list: Der Inhalt der JSON-Datei.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """
    Erzeugt einen HTML-Listen-Eintrag (<li>) für ein einzelnes Tier.

    Die Funktion extrahiert Name, Diät, Standort und Typ des Tieres und formatiert
    diese Informationen in eine HTML-Kartenstruktur.

    Params:
        animal (dict): Ein Dictionary, das die Daten eines Tieres enthält (erwartet Keys wie 'name', 'locations' und 'characteristics').

    Returns:
        str: Der fertig formatierte HTML-String für den Tier-Eintrag.
    """

    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    location = animal.get("locations")
    animal_type = animal.get("characteristics", {}).get("type")

    output = ''
    output += '<li class ="cards__item">'
    output += f'<div class="card__title">{name}</div>'
    output += '<p class="card__text">'
    output += f"<strong>Diet:</strong> {diet}<br/>"
    output += f"<strong>Location:</strong> {location[0]}<br/>"
    if animal_type:
        output += f"<strong>Type:</strong> {animal_type}<br/>"
    output += '</p>'
    output += '</li>'
    return output


def main():
    """
    Die Hauptfunktion des Programms.

    Sie lädt die Tierdaten, liest eine HTML-Vorlage, generiert die HTML-Listen
    aller Tiere und ersetzt einen Platzhalter in der Vorlage, um die finale
    'animals.html'-Datei zu erzeugen.
    """
    animals_data = load_data('animals_data.json')
    html_data = ''

    with open('animals_template.html', "r") as handle:
        template = handle.read()

    html_data += '<ul class="cards">'

    for animal in animals_data:
        html_data += serialize_animal(animal)
    html_data += '</ul>'


    with open("animals.html", "w") as output:
        output.write(template.replace("__REPLACE_ANIMALS_INFO__", html_data))

if __name__ == "__main__":
    main()