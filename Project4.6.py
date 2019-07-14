class Pizza:
    def __init__(self, size = "Small", crust = "Thin", sauce = "None", topping = "no topping", topping_2 = "no topping", topping_3 = "no topping", done = "not done", number = "1"):
        self.size = size
        self.crust = crust
        self.sauce = sauce
        self.topping = topping
        self.topping_2 = topping_2
        self.topping_3 = topping_3
        self.done = done
        self.number = number

    def display_pizza(self):
        return self.size + ", " + self.crust + ", " + self.sauce + ", " + self.topping + ", " + self.topping_2 + ", " + self.topping_3 + ", " + self.done + ", " + self.number

def welcome_input():
    print("Welcome to Pie in the Sky Pizza Shoppe!")
    print("(O)rder a pizza")
    print("(F)inish an order")
    print("(D)isplay un-finished orders")
    print("(E)xit")
    user_input = input()
    user_input = user_input.lower()
    while user_input != "o" and user_input != "f" and user_input != "d" and user_input != "e":
        print("Type an O, F, D, or E")
        print("Welcome to Pie in the Sky Pizza Shoppe!")
        print("(O)rder a pizza")
        print("(F)inish an order")
        print("(D)isplay un-finished orders")
        print("(E)xit")
        user_input = input()
        user_input = user_input.lower()
    return user_input

def size_pizza():
    size_input = input("What size pizza do you want? (S)mall, (M)edium, or (L)arge ")
    size_input = size_input.lower()
    while size_input != "s" and size_input != "m" and size_input != "l":
        print("That is not a size we have. Try again")
        size_input = input("What size pizza do you want? (S)mall, (M)edium, or (L)arge ")
        size_input = size_input.lower()
    if size_input == "s" and "S":
        size_input = "Small"
        return size_input
    elif size_input == "m" and "M":
        size_input = "Medium"
        return size_input
    elif size_input == "l" and "L":
        size_input = "Large"
        return size_input
    else:
        print("nope thats not an option")

def crust_pizza():
    crust_input = input("What curst do you want? (H)and-tossed, (T)hin, (C)heese Stuffed or (D)eep Dish ")
    crust_input = crust_input.lower()
    while crust_input != "h" and crust_input != "t" and crust_input != "c" and crust_input != "d":
        print("That is not a curst we have. Try again")
        crust_input = input("What curst do you want? (H)and-tossed, (T)hin, (C)heese Stuffed or (D)eep Dish ")
        crust_input = crust_input.lower()
    if crust_input == "h" and "H":
        crust_input = "Hand-tossed"
        return crust_input
    elif crust_input == "t" and "T":
        crust_input = "Thin"
        return crust_input
    elif crust_input == "c" and "C":
        crust_input = "Cheese Stuffed"
        return crust_input
    elif crust_input == "d" and "D":
        crust_input = "Deep Dish"
        return crust_input
    else:
        print("thats not a crust")

def sauce_pizza():
    sauce_input = input("How much sauce do you want? (N)one, (E)xtra, or (L)ight ")
    sauce_input = sauce_input.lower()
    while sauce_input != "n" and sauce_input != "e" and sauce_input != "l":
        print("That is not a level of sauce we have. Try again")
        sauce_input = input("How much sauce do you want? (N)one, (E)xtra, or (L)ight ")
        sauce_input = sauce_input.lower()
    if sauce_input == "n" and "N":
        sauce_input = "None"
        return sauce_input
    elif sauce_input == "e" and "E":
        sauce_input = "Extra"
        return sauce_input
    elif sauce_input == "l" and "L":
        sauce_input = "Light"
        return sauce_input
    else:
        print("thats not an option")

def toppings_pizza():
    print("""(E)xtra cheese, (M)ushrooms, (G)oat cheese
(T)omatoes, (P)ineapple, (F)resh veggies
(K)alamata olives, (G)reen olives, (B)lack olives
B(A)con, Pepperon(I), (H)am, Bee(F)""")
    toppings_list = []
    while(True):
        toppings_input = input("Enter a topping or done:")
        toppings_input = toppings_input.lower()
        while toppings_input != "e" and toppings_input != "m" and toppings_input != "g" and toppings_input != "t" and toppings_input != "p" and toppings_input != "f" and toppings_input != "k" and toppings_input != "g" and toppings_input != "b" and toppings_input != "a" and toppings_input != "i" and toppings_input != "h" and toppings_input != "done":
            print("That is not a valid input. Try again.")
            toppings_input = input("Enter a topping or done:")
            toppings_input = toppings_input.lower()
        if toppings_input == "e" and "E":
            toppings_input = "Extra cheese"
            toppings_list.append(toppings_input)
        elif toppings_input == "m" and "M":
            toppings_input = "Mushrooms"
            toppings_list.append(toppings_input)
        elif toppings_input == "g" and "G":
            toppings_input = "Goat cheese"
            toppings_list.append(toppings_input)
        elif toppings_input == "t" and "T":
            toppings_input = "Tomatoes"
            toppings_list.append(toppings_input)
        elif toppings_input == "p" and "P":
            toppings_input = "Pieapple"
            toppings_list.append(toppings_input)
        elif toppings_input == "f" and "F":
            toppings_input = "Fresh veggies"
            toppings_list.append(toppings_input)
        elif toppings_input == "k" and "K":
            toppings_input = "Kalamata olives"
            toppings_list.append(toppings_input)
        elif toppings_input == "g" and "G":
            toppings_input = "Green olives"
            toppings_list.append(toppings_input)
        elif toppings_input == "b" and "B":
            toppings_input = "Black olives"
            toppings_list.append(toppings_input)
        elif toppings_input == "a" and "A":
            toppings_input = "Bacon"
            toppings_list.append(toppings_input)
        elif toppings_input == "i" and "I":
            toppings_input = "Pepperoni"
            toppings_list.append(toppings_input)
        elif toppings_input == "h" and "H":
            toppings_input = "Ham"
            toppings_list.append(toppings_input)
        elif toppings_input == "f" and "F":
            toppings_input = "Beef"
            toppings_list.append(toppings_input)
        else:
            break
    return toppings_list

def main():
    pizza_list = []
    number_check = 1
    while(True):

        get_welcome = welcome_input()

        if get_welcome == "o":
            while(True):

                get_size = size_pizza()
                size = Pizza(size = get_size)

                get_crust = crust_pizza()
                crust = Pizza(size = get_size, crust = get_crust)

                get_sauce = sauce_pizza()
                sauce = Pizza(size = get_size, crust = get_crust, sauce = get_sauce)

                get_toppings = toppings_pizza()
                if len(get_toppings) == len([1]):
                    str_toppings = ''.join(get_toppings[0])
                    str_toppings_2 = "no topping"
                    str_toppings_3 = "no topping"

                    toppings = Pizza(size=get_size, crust=get_crust, sauce=get_sauce, topping=str_toppings,
                                 topping_2=str_toppings_2, topping_3=str_toppings_3)
                    final_pizza = Pizza(size=get_size, crust=get_crust, sauce=get_sauce, topping=str_toppings,
                                    topping_2=str_toppings_2, topping_3=str_toppings_3, done="not done", number="{0}".format(number_check))
                    # print(final_pizza.display_pizza())
                elif len(get_toppings) == len(["1", "2"]):
                    str_toppings = ''.join(get_toppings[0])
                    str_toppings_2 = ''.join(get_toppings[1])
                    str_toppings_3 = "no topping"

                    toppings = Pizza(size=get_size, crust=get_crust, sauce=get_sauce, topping=str_toppings,
                                 topping_2=str_toppings_2, topping_3=str_toppings_3)
                    final_pizza = Pizza(size=get_size, crust=get_crust, sauce=get_sauce, topping=str_toppings,
                                    topping_2=str_toppings_2, topping_3=str_toppings_3, done="not done", number="{0}".format(number_check))
                    # print(final_pizza.display_pizza())
                elif len(get_toppings) == len(["1", "2", "3"]):
                    str_toppings = ''.join(get_toppings[0])
                    str_toppings_2 = ''.join(get_toppings[1])
                    str_toppings_3 = ''.join(get_toppings[2])

                    toppings = Pizza(size=get_size, crust=get_crust, sauce=get_sauce, topping=str_toppings,
                                 topping_2=str_toppings_2, topping_3=str_toppings_3)
                    final_pizza = Pizza(size=get_size, crust=get_crust, sauce=get_sauce, topping=str_toppings,
                                    topping_2=str_toppings_2, topping_3=str_toppings_3, done="Done", number="{0}".format(number_check))
                    # print(final_pizza.display_pizza())
                else:
                    final_pizza = Pizza(size=get_size, crust=get_crust, sauce=get_sauce, topping="no topping",
                                    topping_2="no topping", topping_3="no topping", done="not done", number="{0}".format(number_check))
                    # print(final_pizza.display_pizza())

                print("This order number is {0}".format(number_check))
                number_check = number_check + 1

                pizza_list.append(final_pizza)
                break

        elif get_welcome == "f":
            order_input = eval(input("Please enter the order number: "))
            while order_input > len(pizza_list):
                print("That is not a valid order number. Try again")
                order_input = eval(input("Please enter the order number: "))
            for x in pizza_list:
                if x.done == "Done":
                    break

        elif get_welcome == "d":
            if len(pizza_list) == 0:
                print("All orders complete")
            for x in pizza_list:
                if x.done == "not done":
                    print("{0} is not complete".format(x.number))
                elif x.done == "Done":
                    continue
                else:
                    print("All orders complete")
                    break

        elif get_welcome == "e":
            quit()

main()