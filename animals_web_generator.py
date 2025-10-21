import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)




def serialize_animal(animal):
    output = ''
    name = animal.get("name")
    if name:
        output += f"Name: {name}\n"
    diet = animal.get("characteristics", {}).get("diet")
    if diet:
        output += f"Diet: {diet}\n"
    location = animal.get("locations")
    if location:
        output += f"Location: {location[0]}\n"
    animal_type = animal.get("characteristics", {}).get("type")
    if animal_type:
        output += f"Type: {animal_type}\n"
    output += "\n"
    return output



def main():
    animals_data = load_data('animals_data.json')
    html_data = ''

    with open("animals_template.html", "r") as handle:
        template = handle.read()
    for animal in animals_data:
        html_data += serialize_animal(animal)
    print(html_data)
    with open("animals.html", "w") as output:
        output.write(template.replace("__REPLACE_ANIMALS_INFO__", html_data))


if __name__ == "__main__":
    main()

