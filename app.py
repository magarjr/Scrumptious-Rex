import PySimpleGUI as sg
import requests
import config

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

cuisine_frame = [
    [sg.Text("Search for a recipe by cuisine:", background_color="#57ADA9")],
    [sg.DropDown(default_value="Select cuisine", values=cuisines, key="cuisine")],
    # [sg.Text("How many recipes do you want to see?")],
    # [sg.DropDown(default_value="", values=[x for x in range(1, 4)])],
    [sg.Button("Submit", key="recipe")]
]

layout = [
    # [sg.Text("SCRUMPTIOUS REX", background_color="#57ADA9", justification="center")],
    [sg.Image("logo.png", subsample=5, expand_x=True, background_color="#57ADA9")],
    [sg.HorizontalSeparator(color="#AD575B")],
    [sg.Button("About", key="about"), sg.Button("Instructions", key="instructions")],
    [sg.Frame("Cuisines: ", cuisine_frame, background_color="#57ADA9", expand_x=False, element_justification="center")]
]

# pad (left, right), (top, bottom)

# Create the window
window = sg.Window("Scrumptious Rex", layout, size=(800, 600), resizable=False, background_color="#57ADA9")


def recipe_window(cuisine_selected):
    response = requests.get(f'https://api.spoonacular.com/recipes/complexSearch?apiKey={config.API_KEY}'
                            f'&cuisine={cuisine_selected}&number=1&addRecipeInformation=true&instructionsRequired=true')

    result = response.json()

    ingredients = "\nRecipe Instructions: \n"
    for i in range(len(result["results"][0]["analyzedInstructions"][0]["steps"])):
        # print(result["results"][0]["analyzedInstructions"][0]["steps"][i]["number"])
        # print(result["results"][0]["analyzedInstructions"][0]["steps"][i]["step"])
        ingredients += "Step "
        ingredients += str(result["results"][0]["analyzedInstructions"][0]["steps"][i]["number"])
        ingredients += ": "
        ingredients += result["results"][0]["analyzedInstructions"][0]["steps"][i]["step"]
        ingredients += "\n"

    print(ingredients)

    rec_layout = [[sg.Multiline(ingredients, size=(50, 30), expand_x=True)]]
    rec_window = sg.Window("", rec_layout, size=(500, 500))
    while True:
        event, values = rec_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

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
            recipe_window(cuisine_selected)

    window.close()


if __name__ == "__main__":
    main()
