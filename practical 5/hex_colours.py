# Hex Colours

COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                  "Alizarin crimson": "#e32636", "Amaranth": "#e52b50",
                  "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "Apricot": "#fbceb1",
                  "Aqua": "#00ffff"}

print(COLOUR_TO_CODE)

colour_name = input("Enter Colour name: ").title()  # using title() to capitalize first letter of each word
while colour_name != "":
    if colour_name in COLOUR_TO_CODE:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    else:
        print("Invalid Colour name")
    colour_name = input("Enter Colour name: ").title()

for colour_name, code in COLOUR_TO_CODE.items():  # iterating over key-value pairs
    print("{}: {}".format(colour_name, code))  # formatting output string
