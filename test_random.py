import requests

API_KEY = "78d841b9ea3c40de9fd1607901d31c88"

# response = requests.get(f'https://api.spoonacular.com/recipes/complexSearch?apiKey={API_KEY}'
#                         '&cuisine=Caribbean&number=1&addRecipeInformation=true&instructionsRequired=true')
#
# print(response.json())

result = {
    'results': [
        {
            'summary': 'Trinidad Callaloo Soup could be just the <b>gluten free and dairy free</b> recipe you\'ve been looking for. This main course has <b>508 calories</b>, <b>17g of protein</b>, and <b>42g of fat</b> per serving. For <b>$3.19 per serving</b>, this recipe <b>covers 34%</b> of your daily requirements of vitamins and minerals. This recipe serves 4. <b>Autumn</b> will be even more special with this recipe. This recipe is typical of Central American cuisine. From preparation to the plate, this recipe takes approximately <b>approximately 45 minutes</b>. 1 person were impressed by this recipe. It is brought to you by Foodista. Head to the store and pick up coconut oil, okra, scallions, and a few other things to make it today. With a spoonacular <b>score of 80%</b>, this dish is pretty good. If you like this recipe, take a look at these similar recipes: <a href="https://spoonacular.com/recipes/callaloo-34790">Callaloo</a>, <a href="https://spoonacular.com/recipes/trinidad-spell-470259">Trinidad Spell</a>, and <a href="https://spoonacular.com/recipes/callaloo-stew-34784">Callaloo Stew</a>.',
            'analyzedInstructions': [
                {
                    'name': '',
                    'steps': [
                        {
                            'number': 1,
                            'step': 'Saute onion, okra, salt pork, thyme, garlic, habanero and scallions until the okra and onions brown.',
                            'ingredients': [
                                {
                                    'id': 10165,
                                    'name': 'salt pork',
                                    'localizedName': 'salt pork',
                                    'image': 'pork-belly.jpg'
                                },
                                {
                                    'id': 11291,
                                    'name': 'green onions',
                                    'localizedName': 'green onions',
                                    'image': 'spring-onions.jpg'
                                },
                                {
                                    'id': 10011819,
                                    'name': 'habanero chili',
                                    'localizedName': 'habanero chili',
                                    'image': 'habanero-pepper.jpg'
                                },
                                {
                                    'id': 11215,
                                    'name': 'garlic',
                                    'localizedName': 'garlic',
                                    'image': 'garlic.png'
                                },
                                {
                                    'id': 11282,
                                    'name': 'onion',
                                    'localizedName': 'onion',
                                    'image': 'brown-onion.png'
                                },
                                {
                                    'id': 2049,
                                    'name': 'thyme',
                                    'localizedName': 'thyme',
                                    'image': 'thyme.jpg'
                                },
                                {
                                    'id': 11278,
                                    'name': 'okra',
                                    'localizedName': 'okra',
                                    'image': 'okra.png'
                                }
                            ],
                            'equipment': [

                            ]
                        },
                        {
                            'number': 2,
                            'step': 'Stir in the callaloo with the chicken stock and simmer until the callaloo is tender.',
                            'ingredients': [
                                {
                                    'id': 6172,
                                    'name': 'chicken stock',
                                    'localizedName': 'chicken stock',
                                    'image': 'chicken-broth.png'
                                }
                            ],
                            'equipment': [

                            ]
                        },
                        {
                            'number': 3,
                            'step': 'Puree with a stick blender. Adjust seasoning to taste with salt and pepper.',
                            'ingredients': [
                                {
                                    'id': 1102047,
                                    'name': 'salt and pepper',
                                    'localizedName': 'salt and pepper',
                                    'image': 'salt-and-pepper.jpg'
                                },
                                {
                                    'id': 1042027,
                                    'name': 'seasoning',
                                    'localizedName': 'seasoning',
                                    'image': 'seasoning.png'
                                }
                            ],
                            'equipment': [
                                {
                                    'id': 404726,
                                    'name': 'blender',
                                    'localizedName': 'blender',
                                    'image': 'blender.png'
                                }
                            ]
                        },
                        {
                            'number': 4,
                            'step': 'Stir in coconut milk and crab, then warm gently.',
                            'ingredients': [
                                {
                                    'id': 12118,
                                    'name': 'coconut milk',
                                    'localizedName': 'coconut milk',
                                    'image': 'coconut-milk.png'
                                },
                                {
                                    'id': 15136,
                                    'name': 'crab',
                                    'localizedName': 'crab',
                                    'image': 'crabmeat.jpg'
                                }
                            ],
                            'equipment': [

                            ]
                        },
                        {
                            'number': 5,
                            'step': 'Serve with rice.',
                            'ingredients': [
                                {
                                    'id': 20444,
                                    'name': 'rice',
                                    'localizedName': 'rice',
                                    'image': 'uncooked-white-rice.png'
                                }
                            ],
                            'equipment': [

                            ]
                        }
                    ]
                }
            ],
            'spoonacularSourceUrl': 'https://spoonacular.com/trinidad-callaloo-soup-663822'
        }
    ],
    'offset': 0,
    'number': 1,
    'totalResults': 5
}

# print(result["results"][0]["analyzedInstructions"][0]["steps"][0])

# print("Ingredients Needed: ")
# for i in range(len(result["results"][0]["analyzedInstructions"][0]["steps"])):
#     for x in range(len(result["results"][0]["analyzedInstructions"][0]["steps"][i]["ingredients"])):
#         print(result["results"][0]["analyzedInstructions"][0]["steps"][i]["ingredients"][x]["name"])
#
# print("\nRecipe Instructions: ")
# for i in range(len(result["results"][0]["analyzedInstructions"][0]["steps"])):
#     # print(result["results"][0]["analyzedInstructions"][0]["steps"][i]["number"])
#     # print(result["results"][0]["analyzedInstructions"][0]["steps"][i]["step"])
#     print("Step " +
#           str(result["results"][0]["analyzedInstructions"][0]["steps"][i]["number"]),
#           ": " +
#           result["results"][0]["analyzedInstructions"][0]["steps"][i]["step"]
#           )


# ####################### THIS IS THE RANDOM QUERY # #######################

response = requests.get(f'https://api.spoonacular.com/recipes/random?apiKey={API_KEY}&number=1&tags=thai'
                        f'&instructionsRequired=true')

result2 = response.json()

print(result2)
instructions = ""

print("\nTitle: " + result2["recipes"][0]["title"] + "\n")

print("Instructions: ")  # + str(result2["recipes"][0]["analyzedInstructions"]))
for i in range(len(result2["recipes"][0]["analyzedInstructions"][0]["steps"])):
    instructions += "Step "
    instructions += str(result2["recipes"][0]["analyzedInstructions"][0]["steps"][i]["number"])
    instructions += ": "
    instructions += result2["recipes"][0]["analyzedInstructions"][0]["steps"][i]["step"]
    instructions += "\n"

print(instructions)

ingredients = ""
print("Ingredients Needed: ")
for i in range(len(result2["recipes"][0]["analyzedInstructions"][0]["steps"])):
    for x in range(len(result2["recipes"][0]["analyzedInstructions"][0]["steps"][i]["ingredients"])):
        ingredients += result2["recipes"][0]["analyzedInstructions"][0]["steps"][i]["ingredients"][x]["name"]
        ingredients += "\n"

print(ingredients)
