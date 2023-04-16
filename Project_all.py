import Project_game
import matplotlib.pyplot as plt
import webbrowser
import time
import sql_tools
import sqlite3 as sql


def add_data(file_name, empty_list):
    '''
    INPUT:
      A file and an empty list
    OUTPUT:
      A list with all the data from the file inputted
    '''

    my_file = open(file_name, "r")
    with open(file_name, "r") as f:
        for line in f:
            x = line[:-1]
            empty_list.append(x)
    my_file.close()

    return empty_list


def open_website(link):
    '''
    INPUT:
      Website link
    OUTPUT:
      None, it opens the website
    '''
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(link)


def plot_comparison(title_name, x_name, y_name, arg_1, arg_2, arg_3, label_1, label_2):
    '''
    INPUT:
      Desired title name, x-axis name, y-axis,name, four arguments that want to
      be plotted, and the desired label (first arg will be plotted on x-axis,
      second arg will be plotted on y-axis). The legend will be on top right corner
    OUTPUT:
      A plotted graph compares two components with labels based on all the components entered
    '''
    plt.plot(arg_1, arg_2, label=label_1)
    plt.plot(arg_1, arg_3, label=label_2)
    plt.title(title_name)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.legend()
    plt.show()


def plot_data_linear(title_name, x_name, y_name, arg_1, arg_2, colors):
    '''
    INPUT:
      Desired title name, x-axis name, y-axis,name, two arguments that want to
      be plotted, and the desired color (first arg will be plotted on x-axis,
      second arg will be plotted on y-axis)
    OUTPUT:
      A graph plotted based on all the components entered
    '''
    plt.plot(arg_1, arg_2, color=colors)
    plt.title(title_name)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()


# add data into a list
all_data = []
bipolar_data = []
add_data("data.csv", all_data)           # Anxiety Data
add_data("bipolar.csv", bipolar_data)    # Bipolar Data

# Get 2019's data for all countries
year_2019_data = []
bi_2019_data = []
for i in all_data:
    if '2019' in i:
        year_2019_data.append(i)         # Anxiety Data

for i in bipolar_data:
    if '2019' in i:
        bi_2019_data.append(i)           # Bipolar Data

# Get countries, acronmies, and percentage
country = []
acronmy = []
percent = []
percent_bi = []

for x in year_2019_data:
    country.append(x.split(",")[0])
    acronmy.append(x.split(',')[1])
    percent.append(float(x.split(',')[-1]))    # anxiety data for 2019

for i in bi_2019_data:
    percent_bi.append(float(i.split(',')[-1]))  # bipolar data for 2019

# Get all the years with the last two numbers
all_years = []

for y in all_data:
    all_years.append(y.split(',')[-2])
all_years.pop(0)
all_years_2 = list(set(all_years))
all_years_2.sort()

all_years_final = []
for i in all_years_2:
    all_years_final.append(i[2:4])

while 1:

    option = ('''
    S = Start Game
    A = Analysis of your performance in the game
    B = Learn more about Bipolar Disorder Prevalence in each country
    M = Learn more about Anxiety prevalence in each country
    C = Conclusion
    L = Leave a comment
    P = Print out all data used for your reference
    E = End the program
    Choose an option: ''')

    menu_option = input(option)

    if menu_option == 'S':
        if __name__ == "__main__":
            Project_game.main()
            print("Hope you enjoyed the game.")
        change = True
        while change:
            ask_time = input(
                "Please type in the time you spent in the format of (min min : second second): ")
            if len(ask_time) == 5:
                if ask_time[0:1].isdigit() and ask_time[3:4].isdigit():
                    if ask_time[2] == ":":
                        if ask_time[0] != '0':
                            print(
                                "The time is too long, no way you spent this long in the game.")
                        elif ask_time[0] == '0':
                            if int(ask_time[1]) <= 9 and int(ask_time[3]) <= 5 and int(ask_time[-1]) <= 9:
                                confirm_input = input("Thank you for the information! The time you spent is: " + ask_time +
                                                      ". Type 'Yes' to confirm or 'No' to change: ")
                                if confirm_input == 'Yes':
                                    time_spent = int(
                                        ask_time[1]) * 60 + int(ask_time[3]) * 10 + int(ask_time[4])
                                    print("Thank you for the information! Your time spent in seconds is: "
                                          + str(time_spent) + " seconds")
                                    change = False
                                    break

                                elif confirm_input != 'No':
                                    print("Invalid input, please try again.")
                            else:
                                print("Please make sure it matches the format.")
                        else:
                            print("Please make sure it matches the format.")
                    else:
                        print("Please make sure it matches the format.")
                else:
                    print("Please make sure it matches the format.")
            else:
                print("Please make sure it matches the format.")

    elif menu_option == 'A':
        try:
            time_spent
        except NameError:
            print(
                "Please try the game first by selecting 'S', then come back to this section.")
        else:
            i = 3
            while i >= 1:
                time.sleep(1)
                print("You will be redirected to a webpage in " +
                      str(i) + " seconds")
                i -= 1
            open_website("website.html")
            if time_spent <= 40:
                category = 1
                description = "Got nothing to say, Genius"
            elif time_spent <= 80:
                category = 2
                description = "You are really close to a Genius"
            elif time_spent <= 120:
                category = 3
                description = "You are amazing at memorizing stuff"
            elif time_spent <= 160:
                category = 4
                description = "You are pretty good at this game"
            elif time_spent <= 200:
                category = 5
                description = "You got this, nailed this game"
            else:
                category = 6
                description = "You did well, there are actually more categories after this."
            print("\nNow I am sure you are more familiar with the term 'short - term memory, and you are in category: " +
                  str(category) + ", the matching description is: " + description + ".")

            print("\nHope you enjoyed this little game, the time you spent on the game can be directly linked "
                  + "to short term memory, which reflects anxiety and bipolar disorder level in human beings."
                  + " Surprising right? You can select 'B' and 'M' to learn more about these.")

    elif menu_option == 'B':
        try:
            category
        except NameError:
            print("Please check out the 'A' section before this.")
        else:
            checkpoint = True
            print(
                "The problem of increasing bipolar disorder has troubled the researchers for decades")
            while checkpoint:
                data_bi = []
                question = input(
                    "You can type in the Country Name to check that country's Bipolar Disorder Prevalence from 1990 - 2019 or 'Next' to proceed: ")
                if question in country:
                    for i in bipolar_data:
                        if question in i:
                            data_bi.append(float(i.split(',')[-1]))
                    plot_data_linear(question + " 's Bipolar Disorder Prevalence from 1990 - 2019",
                                     "Years", "Percent", all_years_final, data_bi, 'green')

                elif question == 'Next':
                    print("\n\n\n\n\n\n\n\n\n\nNow let's compare different countries' Bipolar Disorder Prevalence Percantage, type in two countries "
                          + "or 'No' to end this section")
                    while 1:
                        data_bi_2 = []
                        question_2 = input("Country Name 1 or 'No': ")
                        if question_2 in country:
                            for i in bipolar_data:
                                if question_2 in i:
                                    data_bi_2.append(float(i.split(',')[-1]))
                            question_3 = input("Country Name 2 or 'No': ")
                            data_bi_3 = []
                            if question_3 in country:
                                for i in bipolar_data:
                                    if question_3 in i:
                                        data_bi_3.append(
                                            float(i.split(',')[-1]))
                                print("A graph has been plotted")

                                plot_comparison("Comparison between two countries' Bipolar Disorder Prevalence",
                                                "Years", "Bipolar Disorder Prevalence Percentage", all_years_final, data_bi_2, data_bi_3, question_2, question_3)
                            elif question_3 == 'No':
                                print("Program Ended")
                                checkpoint = False
                                break

                            else:
                                print(
                                    "Probably the country doesn't exist or there is a typo, please try again!")

                        elif question_2 == 'No':
                            print("Program Ended")
                            checkpoint = False
                            break

                        else:
                            print(
                                "Probably the country doesn't exist or there is a typo, please try again!")
                else:
                    print(
                        "Probably the country doesn't exist or there is a typo, please try again!")

    elif menu_option == 'M':
        try:
            category
        except NameError:
            print("Please check out the 'A' section before this.")
        else:
            turning_point = True
            print(
                "Nowadays, the eleviation of anxiety level is also becoming a big issue in the society.")
            while turning_point:
                data = []
                ask = input(
                    "You can type in the Country Name to check that country's Anxiety Prevalence from 1990 - 2019 or 'Next' to proceed: ")
                if ask in country:
                    for i in all_data:
                        if ask in i:
                            data.append(float(i.split(',')[-1]))
                    plot_data_linear(ask + "'s Anxiety Prevalance from 1990 - 2019",
                                     "Years", "Percent", all_years_final, data, 'red')

                elif ask == 'Next':
                    print("\n\n\n\n\n\n\n\n\n\nNow let's compare different countries' Anxiety Prevalence Percantage, type in two countries "
                          + "or 'No' to end this section")
                    while 1:
                        data_1 = []
                        ask_2 = input("Country Name 1 or 'No': ")
                        if ask_2 in country:
                            for i in all_data:
                                if ask_2 in i:
                                    data_1.append(float(i.split(',')[-1]))
                            ask_3 = input("Country Name 2 or 'No': ")
                            data_2 = []
                            if ask_3 in country:
                                for i in all_data:
                                    if ask_3 in i:
                                        data_2.append(float(i.split(',')[-1]))
                                print("A graph has been plotted")

                                plot_comparison("Comparison between two countries' Anxiety Prevalence",
                                                "Years", "Anxiety Prevalence Percentage", all_years_final, data_1, data_2, ask_2, ask_3)
                            elif ask_3 == 'No':
                                print("Program Ended")
                                turning_point = False
                                break

                            else:
                                print(
                                    "Probably the country doesn't exist or there is a typo, please try again!")

                        elif ask_2 == 'No':
                            print("Program Ended")
                            turning_point = False
                            break

                        else:
                            print(
                                "Probably the country doesn't exist or there is a typo, please try again!")
                else:
                    print(
                        "Probably the country doesn't exist or there is a typo, please try again!")

    elif menu_option == 'C':
        try:
            time_spent
        except NameError:
            print("Please visit the previous sections first")
        else:
            try:
                turning_point
            except NameError:
                print("Please check out the 'B' and 'M' sections first")
            else:
                try:
                    checkpoint
                except NameError:
                    print("Please check out the 'B' and 'M' sections first")
                else:
                    result_anxiety = 0.03243 * time_spent - 2.2394
                    result_bipolar = 0.01128 * time_spent - 0.7893
                    final_anxiety = max(0, result_anxiety)
                    final_bipolar = max(0, result_bipolar)
                    if final_anxiety == 0:
                        if final_bipolar == 0:
                            print("Based on the time you spent in the game, the liklihood of you getting affected by either Anxiety or Bipolar"
                                  + " Disorder is almost 0.00%.")
                        elif final_bipolar == result_bipolar:
                            print("Based on the time you spent in the game, the liklihood of you getting affected by Anxiety is almost 0.00%. "
                                  + "And the likelihood of you getting affected by Bipolar Disorder is: "
                                  + str(max(0, result_bipolar)) + "%.")
                    elif final_anxiety == result_anxiety:
                        if final_bipolar == 0:
                            print("Based on the time you spent in the game, the liklihood of you getting affected by Anxiety is: "
                                  + str(max(0, result_anxiety)) + "%."
                                  + " And the likelihood of you getting affected by Bipolar Disease is almost 0.00%.")
                        elif final_bipolar == result_bipolar:
                            print("Based on the time you spent in the game, the liklihood of you getting affected by Anxiety is: "
                                  + str(max(0, result_anxiety)) +
                                  "%. And the likelihood of you getting affected by Bipolar Disorder is: "
                                  + str(max(0, result_bipolar)) + "%.")

    elif menu_option == 'L':
        try:
            turning_point
        except NameError:
            print("Please chech the 'B' and 'M' sectios first")
        else:
            try:
                checkpoint
            except NameError:
                print("Please chech the 'B' and 'M' sectios first")
            else:
                check = True
                while check:
                    comment = input("Thank you for using, hope you enjoyyed it! Would you mind leaving a comment of your experience?"
                                    + "('Yes' or 'No'): ")
                    if comment == 'Yes':
                        i = 3
                        while i >= 1:
                            time.sleep(1)
                            print("You will be redirected to the form in " +
                                  str(i) + " seconds")
                            i -= 1
                        open_website(
                            "https://docs.google.com/forms/d/e/1FAIpQLSdqsgsyxPxFl09LDL1O2uEDm6Ov2XzrO-YlkwBEX0XUa5Zgiw/viewform?usp=sf_link")
                        check = False
                        break

                    elif comment == 'No':
                        confirm = input(
                            "Are you sure you don't want to leave a comment? ('Yes' or 'No'): ")
                        if confirm == 'Yes':
                            print("Thank you for your feedback!")
                            i = 3
                            while i >= 1:
                                time.sleep(1)
                                print("You will be redirected to the form in " +
                                      str(i) + " seconds")
                                i -= 1
                            open_website(
                                "https://docs.google.com/forms/d/e/1FAIpQLSdqsgsyxPxFl09LDL1O2uEDm6Ov2XzrO-YlkwBEX0XUa5Zgiw/viewform?usp=sf_link")
                            check = False
                            break

                        elif confirm == 'No':
                            print("Thank you!")
                            check = False
                            break

                        else:
                            print("Invalid input, please try again!")
                    else:
                        print("Invalid input, please try again!")

    elif menu_option == 'P':
        print("Here are all the data used in the program merged into a single table with the first row of percent representing Bipolar Disorder"
              + " and second row representing Anxiety Prevalence")
        db_handle = sql.connect("test.db")

        in_file = open("bipolar.csv", "r")
        sql_tools.csv_to_table(db_handle, in_file, "Bipolar_Disorder", [
                               'TEXT', 'TEXT', 'INTEGER', 'REAL'])
        in_file.close()

        in_file = open("data.csv", "r")
        sql_tools.csv_to_table(db_handle, in_file, "Anxiety", [
                               'TEXT', 'TEXT', 'INTEGER', 'REAL'])
        in_file.close()

        my_list = """
        SELECT Bipolar_Disorder.Entity, Bipolar_Disorder.Code, Bipolar_Disorder.Year, Bipolar_Disorder.Percent, Anxiety.Percent
        FROM Bipolar_Disorder, Anxiety
        WHERE Bipolar_Disorder.Entity = Anxiety.Entity
        AND Bipolar_Disorder.Code = Anxiety.Code
        AND Bipolar_Disorder.Year = Anxiety.Year
        """

        sql_tools.print_select(db_handle, my_list)

        db_handle.close()

    elif menu_option == 'E':
        print("Program Ended.")
        break

    else:
        print("Invalid input, please try again!")
