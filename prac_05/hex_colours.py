NAME_TO_CODE = {'aquamarine4': '#458b74', 'asparagus': '#87a96b', 'blueviolet': '#8a2be2', 'cardinal': '#c41e3a',
                'glossygrape': '#ab92b3', 'harlequin': '#3fff00', 'khaki': '#f0e68c', 'mandarin': '#f37a48',
                'mediumorchid': '#ba55d3', 'olivine': '#9ab973', 'zomp': '#39a78e'}

colour_choice = input("Colour? ").lower()
while colour_choice != "":
    while colour_choice not in NAME_TO_CODE:
        print("Invalid Choice")
        colour_choice = input("Colour? ").lower()
    print(f"The hexadecimal code for {colour_choice} is {NAME_TO_CODE[colour_choice]}")
    colour_choice = input("Colour? ").lower()
