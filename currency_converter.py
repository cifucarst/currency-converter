def converter(type_peso, dollar_value):
    pesos = int(input(f'How much {type_peso} pesos do you have? => '))
    dollars = pesos / dollar_value
    print(f'You have $ {round(dollars, 2)} dollars')

def run():
    menu = """
    Welcome to the currency converter
    
    1 - Colombian pesos
    2 - Argentine pesos
    3 - Mexican pesso

    Choose an option (1,2,3) =>  """

    option = int(input(menu))

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