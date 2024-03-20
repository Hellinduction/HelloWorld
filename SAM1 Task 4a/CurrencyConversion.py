import pandas as pd
import Main


# The menu() function generates the UI the accepts and validates user choice
def menu():
    flag = True

    while flag:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling(GBP)")
        print("3. Pound (GBP) to Austrailan Dollars (AUD)")
        print("4. Austrailan Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        print("")
        print("######################################################")

        menu_choice = input("Please enter the number of your choice (1-6): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 6:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                return menu_choice

            # Gets the short version of the conversion information based on user menu choice


def get_currency(menu_choice):
    currencies = {
        '1': 'GBP - EUR',
        '2': 'EUR - GBP',
        '3': 'GBP - AUD',
        '4': 'AUD - GBP',
        '5': 'GBP - JPY',
        '6': 'JPY - GBP'}

    currency = currencies.get(menu_choice)

    return currency


# The get_conversion_rate function uses pandas to get the latest conversion rate
# Imports a csv file in to a data frame
# Uses 'iloc' to get the last/most recent value in the selected column
def get_conversion_rate(currency):
    df = pd.read_csv(Main.FILE_PATH)

    conversion_rate = round(df[currency].iloc[-1], 2)

    return conversion_rate


# Accepts and validates user input for teh amount they want to convert
def get_amount_to_convert(currency):
    print("You are converting: ", currency)

    flag = True

    while flag:
        conversion_amount = input("please enter the ammount you wish to convert")

        try:
            float(conversion_amount)
        except:
            print("Sorry, you must enter a numerical value")
            flag = True
        else:
            return conversion_amount


# Performs the converison and outputs the final values
def perfom_conversion(conversion_amount, conversion_rate, currency):
    amount_recieved = round(conversion_amount * conversion_rate, 2)

    print("##################################")
    print('You are converting {} in {}'.format(conversion_amount, currency[0:3]))
    print('You will recieve {} in {}'.format(amount_recieved, currency[6:9]))


def main():
    menu_choice = menu()
    currency = get_currency(menu_choice)

    conversion_rate = get_conversion_rate(currency)
    conversion_amount = float(get_amount_to_convert(currency))
    perfom_conversion(conversion_amount, conversion_rate, currency)
