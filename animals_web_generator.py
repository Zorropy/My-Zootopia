import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)




def serialize_animal(animal):

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
    output += f"<strong>Type:</strong> {animal_type}<br/>"
    output += '</p>'
    output += '</li>'
    return output



def main():
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
