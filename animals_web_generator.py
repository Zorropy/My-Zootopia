import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def serialize_animal(animal):
    name = animal.get("name")
    if name:
        print(f"Name: {name}")
    diet = animal.get("characteristics", {}).get("diet")
    if diet:
        print(f"Diet: {diet}")
    location = animal.get("locations")
    if location:
        print(f"Location: {location[0]}")
    animal_type = animal.get("characteristics", {}).get("type")
    if animal_type:
        print(f"Type: {animal_type}")








def main():
    animals_data = load_data('animals_data.json')
    for animal in animals_data:
        serialize_animal(animal)
        print()

if __name__ == "__main__":
    main()

