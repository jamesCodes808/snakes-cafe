from textwrap import dedent

order = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0,
}

greeting = dedent(
    """
    ******************************************
    **    Welcome to the Snakes Cafe!       **
    **      Please see our menu below.      **
    **                                      **
    **   To quit at any time, type "quit"   ** 
    ****************************************** 
    """
)

menu = dedent(
    """
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    """
)

prompt_order = dedent(
    """
    ***********************************
    ** What would you like to order? **
    ***********************************
    """
)

goodbye = dedent(
    """
    *************************
    **  See you next time! **
    *************************
    """
)

def main():
    print(greeting)
    print(menu)
    print(prompt_order)

    while True:
        order_item = input("> ")
        if order_item == "quit" or order_item == "q":
            break

        if order_item not in order.keys():
            print("Sorry we don't serve that here")
        else:
            order[order_item] += 1
            if order[order_item] == 1:
                print(f"** {order[order_item]} order of {order_item} has been added to your order **")
            else:
                print(f"** {order[order_item]} orders of {order_item} have been added to your meal **")

    print(goodbye)

if __name__ == "__main__":
    main()