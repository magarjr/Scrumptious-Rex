import PySimpleGUI as sg
import requests
import config

testing = True

cuisines = [
    "African",
    "American",
    "British",
    "Cajun",
    "Caribbean",
    "Chinese",
    "Eastern European",
    "European",
    "French",
    "German",
    "Greek",
    "Indian",
    "Irish",
    "Italian",
    "Japanese",
    "Jewish",
    "Korean",
    "Latin American",
    "Mediterranean",
    "Mexican",
    "Middle Eastern",
    "Nordic",
    "Southern",
    "Spanish",
    "Thai",
    "Vietnamese"
]

diets = [
    "Gluten Free",
    "Ketogenic",
    "Vegetarian",
    "Lacto-Vegetarian",
    "Ovo-Vegetarian",
    "Vegan",
    "Pescetarian",
    "Paleo",
    "Primal",
    "Low FODMAP",
    "Whole30"
]

cuisine_frame = [
    # [sg.Text("Search for a recipe by cuisine:", background_color="#57ADA9")],
    [sg.DropDown(default_value="Select Cuisine", values=cuisines, key="cuisine")],
    # [sg.Text("How many recipes do you want to see?")],
    # [sg.DropDown(default_value="", values=[x for x in range(1, 4)])],
    [sg.Button("Get Recipe", key="recipe")]
]

diet_frame = [
    [sg.DropDown(default_value="Select Diet", values=diets, key="diet")],
    [sg.Button("Get Recipe", key="diet_recipe")]
]

layout = [
    # [sg.Text("SCRUMPTIOUS REX", background_color="#57ADA9", justification="center")],
    [sg.Image("logo.png", subsample=5, expand_x=True, background_color="#57ADA9")],
    [sg.HorizontalSeparator(color="#AD575B")],
    [sg.Button("About", key="about"), sg.Button("Instructions", key="instructions")],
    [sg.Frame("Search for a recipe by Cuisine:",
              cuisine_frame,
              background_color="#57ADA9",
              expand_x=True,
              element_justification="center",
              font="Any 14 bold"
              )],
    [sg.Frame("Search for a recipe by Diet:",
              diet_frame,
              background_color="#57ADA9",
              expand_x=True,
              element_justification="center",
              font="Any 14 bold"
              )]
]

# pad (left, right), (top, bottom)

# Create the window
window = sg.Window("Scrumptious Rex", layout, size=(350, 600), resizable=False, background_color="#57ADA9")


def recipe_window(cuisine_selected, presses):
    if not testing:
        response = requests.get(f'https://api.spoonacular.com/recipes/complexSearch?apiKey={config.API_KEY}'
                            f'&cuisine={cuisine_selected}&number=1&addRecipeInformation=true&instructionsRequired=true'
                            f'&offset={presses}')

    result = response.json()
    print(result)

    instructions = "Recipe Instructions: \n\n"
    for i in range(len(result["results"][0]["analyzedInstructions"][0]["steps"])):
        instructions += "Step "
        instructions += str(result["results"][0]["analyzedInstructions"][0]["steps"][i]["number"])
        instructions += ": "
        instructions += result["results"][0]["analyzedInstructions"][0]["steps"][i]["step"]
        instructions += "\n"

    # print(instructions)

    ingredients = "Ingredients Needed: \n\n"
    for i in range(len(result["results"][0]["analyzedInstructions"][0]["steps"])):
        for x in range(len(result["results"][0]["analyzedInstructions"][0]["steps"][i]["ingredients"])):
            ingredients += result["results"][0]["analyzedInstructions"][0]["steps"][i]["ingredients"][x]["name"]
            ingredients += "\n"

    title = result["results"][0]["title"]

    rec_layout = [
        [sg.Multiline(ingredients, size=(50, 18), expand_x=True, disabled=True)],
        [sg.Multiline(instructions, size=(50, 18), expand_x=True, disabled=True)],
        [sg.Button(f"View another {cuisine_selected} recipe", key="another")]
    ]
    rec_window = sg.Window(f"{title}", rec_layout, size=(500, 500), background_color="#57ADA9")
    while True:
        event, values = rec_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "another":
            # cuisine_selected = values["cuisine"]
            rec_window.close()
            presses += 1
            recipe_window(cuisine_selected, presses)

    rec_window.close()


def instructions_window():
    inst_layout = [[sg.Multiline("Bulleted instructions here")]]
    inst_window = sg.Window("Instructions", inst_layout, size=(400, 300))
    while True:
        event, values = inst_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    inst_window.close()


def open_about_window():
    about_layout = [[sg.Text("Some text about the features")]]
    about_window = sg.Window("About", about_layout, size=(400, 300))
    while True:
        event, values = about_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    about_window.close()


def main():
    presses = 0
    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            print("Program closed.")
            break
        if event == "about":
            open_about_window()
        if event == "instructions":
            instructions_window()
        if event == "recipe":
            cuisine_selected = values["cuisine"]
            recipe_window(cuisine_selected, presses)
            presses += 1

    window.close()


if __name__ == "__main__":
    main()
