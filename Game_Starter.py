import Project_game
import webbrowser
import time


def open_website(link):
    '''
    INPUT:
      Website link
    OUTPUT:
      None, it opens the website
    '''
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(link)


while 1:

    option = ('''
    S = Start Game
    A = Analysis of your performance in the game
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
            if len(ask_time) == 5 and ask_time[0:1].isdigit() and ask_time[3:4].isdigit() and ask_time[2] == ":":
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
    else:
        print("Invalid input, please try again!")
