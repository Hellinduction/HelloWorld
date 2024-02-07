import pandas as pd
import pandas.core.frame
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#Displays the main menu and collects choice of menu item

FILE = "Task4a_data.csv"

def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. Show item with highest total and average sales for a time period")
        print("3. Show a graph displaying the change in sales of a specific item")

        main_menu_choice = input("Please enter the number of your choice (1-3): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 3:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)    

#Menu item selection form user and validates it
def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name

#Gets user input of start of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(start_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return start_date

#Gets user input of end of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(end_date)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return end_date


#imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(item, startdate, enddate):
    df1 = pd.read_csv(FILE)
    df2 = df1.loc[df1['Menu Item'] == item]
    df3 = df2.loc[:,startdate:enddate]

    return df3


def display_best_selling_items(start_date, end_date):
    original_data = pd.read_csv(FILE)
    data: pandas.core.frame.DataFrame = original_data.loc[:, start_date:end_date]

    data = data.iloc[:len(data) - 1, :]

    totals: list = data.sum(axis=1).tolist()
    averages: list = data.mean(axis=1).tolist()

    max_total = max(totals)
    max_total_item = original_data.iloc[totals.index(max_total)]["Menu Item"]

    max_average = max(averages)
    max_average_item = original_data.iloc[averages.index(max_average)]["Menu Item"]

    print(f"{max_total_item} is the best total selling item with {max_total} sales.")
    print(f"{max_average_item} is the best average selling item with {round(max_average, 2)} sales.")


def to_bool(b):
    b = b.lower()

    if b == "y" or b == "yes":
        return True

    if b == "n" or b == "no":
        return False

    return False


def display_graph(i):
    data: pandas.core.frame.DataFrame = pd.read_csv(FILE)
    # data = data.iloc[:len(data) - 1, :]

    entries = data.where(data["Menu Item"] == i).iloc[:, 2:].dropna()
    map = {}

    for key in entries:
        sub_entries = entries[key]

        for value in sub_entries:
            map[key] = value

    plt.plot(map.keys(), map.values())

    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
    plt.gcf().autofmt_xdate()

    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.title("Change In Sales")

    plt.show()


main_menu = menu()
if main_menu == 1:

    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date()
 
    extracted_data = get_selected_item(item, start_date, end_date)
    
    print("Here is the sales data for {} between dates {} and {}:".format(item, start_date, end_date))
    extract_no_index = extracted_data.to_string(index=False)

    print(extract_no_index)
elif main_menu == 2:
    start_date = get_start_date()
    end_date = get_end_date()

    display_best_selling_items(start_date, end_date)
elif main_menu == 3:
    item = get_product_choice()
    display_graph(item)


else:
    print('This part of the program is still under development')
