import os
import msvcrt as m
import Main_menu
import LGU_MENU
import datetime

# Post notice
def Post_Notice():
    LGU_MENU.border2()
    print("\n")
    print('{:^170}'.format("Post Notice:"))
    print('{:^170}'.format("─" * 50))
    print("\n\n")
    
    print('{:^165}'.format("─" * 120))
    print("\n")
    announcement = input('{:>46}'.format("Enter the Notice: "))
    Time = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

    with open("Notice_File.txt", 'a') as file:
        file.write(f"{Time}|{announcement}\n")

    print("\n\n")
    print('{:^165}'.format("─" * 120))
    print("\n\n")
    print('{:>60}'.format("Notice posted successfully!"))
    print("\n")
    print('{:>67}'.format("Press enter key to return to the menu..."))
    m.getch()

#View Notice
def View_Notice():
    LGU_MENU.border2()
    print("\n\n")
    print('{:^170}'.format("[LGU] Notice Board"))
    print('{:^170}'.format("─" * 50))
    print("\n\n")

    print(f"{'┌':>15}{"─" * 147}┐") 
    print(f"{'':<15} {'No.':<5} {'TIME':<25} {'   NOTICE   ':<100}")
    print(f"{'├':>15}{"─" * 147}┤")

    if not os.path.exists("Notice_File.txt"):
        print("\n\n\n\n")
        print('{:^170}'.format("No Notice found."))
        print('{:^170}'.format("Press enter key to return to the menu..."))
        print("\n\n\n\n")
        print(f"{'├':>15}{"─" * 147}┤")
        m.getch()
        return

    with open("Notice_File.txt", 'r') as file:
        notices = file.readlines()

    if not notices:
        print("\n\n\n\n")
        print('{:^170}'.format("No Notice found."))
        print('{:^170}'.format("Press enter key to return to the menu..."))
        print("\n\n\n\n")
        print(f"{'├':>15}{"─" * 147}┤")
        m.getch()
        return

    for i, line in enumerate(notices):
        Time, Notice = line.strip().split("|")
        print("")
        print(f"{'':>15} {i + 1:<5} {Time:<25}  {Notice:<100}")
        print("")
        print(f"{'├':>15}{"─" * 147}┤")
        
    print("\n\n")
    print('{:^170}'.format("Press enter key to return to the menu..."))
    m.getch()

#delete Notice
def delete_Notice():
    LGU_MENU.border2()
    print("\n\n")
    print('{:^170}'.format("[LGU] Delete Notice"))
    print('{:^170}'.format("─" * 59))
    print("\n\n")
    View_Notice()
    print("\n")

    if os.path.exists("Notice_File.txt"):
        with open("Notice_File.txt", 'r') as file:
            notices = file.readlines()     

        try:
            print("\n")
            Notice_number = int(input('{:>60}'.format("\nEnter the Notice number to delete (0 to exit): "))) - 1
            if Notice_number == -1:
                print('{:^170}'.format("Exiting delete operation..."))
                return

            elif 0 <= Notice_number < len(notices):
                del notices[Notice_number]
                with open("Notice_File.txt", 'w') as file:
                    file.writelines(notices)
                print("\n")
                print('{:^170}'.format("Notice deleted successfully!"))
                m.getch()
            else:
                print("\n")
                print('{:^170}'.format("Invalid Notice number."))
                m.getch()
        except ValueError:
            print("\n")
            print('{:^170}'.format("Invalid input. Please enter a valid number."))
            m.getch()
        print('{:^170}'.format("Press enter key to return to the menu..."))
