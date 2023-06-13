def converter(type_peso, dollar_value):
    try:
        pesos = int(input(f'How much {type_peso} pesos do you have? => '))
        assert pesos > 0, "The amount of pesos must be a positive integer"
        dollars = pesos / dollar_value
        print(f'You have $ {round(dollars, 2)} dollars')
    except ValueError:
        print("Invalid input. Please enter a valid integer")
    except AssertionError as ve:
        print(ve)

def run():
    menu = """
    Welcome to the currency converter
    
    1 - Colombian pesos
    2 - Argentine pesos
    3 - Mexican pesso

    Choose an option (1,2,3) =>  """

    try:
        option = int(input(menu))
        assert option in [1,2,3],"Invalid option, enter 1,2 or 3"
    except ValueError:
        print("Invalid input. Please enter a valid integer")
        return
    except AssertionError as ve:
        print(ve)
        return

    if option == 1:
        converter("Colombian", 4500)
    elif option == 2:
        converter("Argentine", 235)
    elif option == 3:
        converter("Mexican", 25)
    else:
        print("That option is not available")


if __name__ == '__main__':
    run()
