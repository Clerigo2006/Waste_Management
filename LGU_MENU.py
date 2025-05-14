import os
import msvcrt as m
import Main_menu
import Waste_Collect_Funct
import Notice
import Show_Sched
import Residents_Menu

Reports_File = "Reports_File.txt"

# Clear screen
def clear():
    os.system('cls')

# line (short)
def border():
    for _ in range(50):
        print('-',end='')

# line (long)
def border1():
    for _ in range(178):
        print('-',end='')

#l ogo
def border2():
        clear()
        border1()
        print("")
        print('{:^170}'.format(" │ │ │┌──│  ┌──┐┌──┐┌──┬──┐┌──  ──┬──┌──┐  │ │ │┌──┐┌── ──┬──┌──  ┌──┬──┐┌──┐┌──┬┌──┐┌── ┌── ┌──┬──┐┌── ┌──┬ ──┬──"))
        print('{:^170}'.format(" │ │ │├──│  │   │  ││  │  │├──    │  │  │  │ │ │├──┤└──┐  │  ├──  │  │  │├──┤│  │├──┤│ ─┐├── │  │  │├── │  │   │  "))
        print('{:^170}'.format(" └─┴─┘└──└─┘└──┘└──┘┴  ┴  ┴└──    ┴  └──┘  └─┴─┘┴  ┴ ──┘  ┴  └──  ┴  ┴  ┴┴  ┴┴  ┴┴  ┴└──┘└── ┴  ┴  ┴└── ┴  ┴   ┴  "))

        print('{:^170}'.format("┌── ┬   ┬ ┌── ──┬──┌── ┌──┬──┐"))
        print('{:^170}'.format("└──┐└─┬─┘ └──┐  │  ├── │  │  │"))
        print('{:^170}'.format(" ──┘  ┴    ──┘  ┴  └── ┴  ┴  ┴"))
        border1()

# Waste_Collection Menu
def Waste_Collection_Menu():
    while True:
        clear()
        Main_menu.border2()
        print('{:^170}'.format("[LGU] Waste Collection"))
        print('{:^170}'.format("─" * 50))
        print("\n")
        print('{:>88}'.format("[A] Collect Waste"))
        print('{:>95}'.format("[B] View Collection List"))
        print('{:>92}'.format("[C] Delete Collection"))
        print('{:>92}'.format("[D] Back to Main Menu"))
        print("\n\n")
        print('{:^170}'.format("─" * 50))
        print("\n\n")

        selection = input('{:>90}'.format("Enter your choice: ")).upper()
        if selection == 'A':
            clear()
            Waste_Collect_Funct.Collect_Waste()
            m.getch()
        elif selection == 'B':
            clear()
            Waste_Collect_Funct.View_Collection_List()
            m.getch()
        elif selection == 'C':
            clear()
            Waste_Collect_Funct.delete_collection()
            m.getch()
        elif selection == 'D':
            print("\nGoing back to main menu...")
            m.getch()
            break
        else:
            print("\nInvalid choice. Please try again.")
            m.getch()

# Notice_Menu
def Notice_Menu():
    while True:
        Main_menu.border2()
        print('{:^170}'.format("Notice Post:"))
        print('{:^170}'.format("─" * 50))
        print("\n")
        print('{:>86}'.format("[A] Post Notice"))
        print('{:>92}'.format("[B] View Notice Posts"))
        print('{:>93}'.format("[C] Delete Notice Post"))
        print('{:>92}'.format("[D] Back to Main Menu"))
        print("\n\n")
        print('{:^170}'.format("─" * 50))
        print("\n\n")

        selection = input('{:>80}'.format("Enter your choice: ")).upper()
        if selection == 'A':
            clear()
            Notice.Post_Notice()          
        elif selection == 'B':
            clear()
            Notice.View_Notice()
        elif selection == 'C':
            clear()
            Notice.delete_Notice()
            m.getch()
        elif selection == 'D':
            print("Going back to main menu...")
            m.getch()
            break
        else:
            print("\nInvalid choice. Please try again.")
            m.getch()

# Schedule_menu
def schedule():
    while True:
        clear()
        Main_menu.border2()
        print('{:^170}'.format("[LGU] Waste Collection Schedule"))
        print('{:^170}'.format("─" * 50))
        print("\n ")
        print('{:>90}'.format("[A] View Schedule"))
        print('{:>92}'.format("[B] Update Schedule"))
        print('{:>94}'.format("[C] Back to Main Menu"))
        print("\n\n")
        print('{:^170}'.format("─" * 50))
        print("\n")
        selection = input('{:>70}'.format("Enter your choice: ")).upper()

        if selection == 'A':
            clear()
            Show_Sched.View_Schedule()
            m.getch()
        elif selection == 'B':
            clear()
            Show_Sched.update_schedule()
            m.getch()
        elif selection == 'C':
            print("\n")
            print('{:^170}'.format("Going back to main menu..."))
            m.getch()
            break
        else:
            print("")
            print('{:^170}'.format("Invalid choice. Please try again."))
            m.getch()

# Waste report 
def Waste_report():
    Residents_Menu.View_Report()
    print("─" * 178)

    print("\n\n")
    print('{:>40}'.format("Select:"))
    print(f"{'┌':>56}{'─'*61}┐")
    print(f"{'│':>56} {'':<10}{'[A] Update Status':<24} {'[B] Exit':<25}│")
    print(f"{'└':>56}{'─'*61}┘")
    select = input('{:>47}'.format("Enter Choice: ")).upper()

    if select == 'A':
        clear()
        Update_Status_Report()
        Waste_report()
        m.getch()
    elif select == 'B':
        print("\n")
        print('{:^170}'.format("Exiting..."))
        return
        m.getch()
          
    else:
        print("\n")
        print("Invalid Choice../")
        m.getch()

# Change the Status report of the resident
def Update_Status_Report():
    Residents_Menu.View_Report()

    if os.path.exists(Reports_File): 
        with open(Reports_File, 'r') as file:
            reports = file.readlines()
    
        print("─" * 178)
        print("\n\n")
        print('{:^170}'.format("Update Report Status"))
        print('{:^170}'.format("─" * 50))
        print("\n\n")

        try:
            report_number = int(input('{:>60}'.format("Enter the report number to update (0 to exit): "))) - 1
            if report_number == -1:
                print('{:^170}'.format("Exiting update operation..."))
                return
                
            elif 0 <= report_number < len(reports):
                Time, Name_Reporter, Location, Issue, Status = reports[report_number].strip().split("|")
                new_status = input('{:>67}'.format("Enter new status (e.g.,[R] Resolved, [I] In Progress): ")).upper()
                if new_status == "R":
                    new_status = "Resolved"
                elif new_status == "I":
                    new_status = "In Progress"
                else:
                    print("\n\n")
                    print('{:x^170}'.format("Invalid status. Please enter [R] for Resolved or [I] for In Progress."))
                    m.getch()
                    return

                reports[report_number] = f"{Time}|{Name_Reporter}|{Location}|{Issue}|{new_status}\n"

                with open(Reports_File, 'w') as file:
                    file.writelines(reports)

                print("\n")
                print('{:^170}'.format("Report status updated successfully!"))
                m.getch()

            else:
                print("\n")
                print('{:^170}'.format("Invalid report number."))
                m.getch()

        except ValueError:
            print("\n")
            print('{:^170}'.format("Invalid input. Please enter a valid number."))
            m.getch()

# Main Menu LGU
def Menu():
    while True:
        os.system('cls')

        Main_menu.border2()
        print('{:^170}'.format("[LGU] Waste - Management System"))
        print('{:^170}'.format("─" * 50))
        print("\n")
        print('{:>92}'.format("[A] Waste Collection"))
        print('{:>82}'.format("[B] Notice"))
        print('{:>84}'.format("[C] Schedule"))
        print('{:>93}'.format("[D] View Waste Report"))
        print('{:>82}'.format("[E] Logout"))
        print("\n\n")
        print('{:^170}'.format("─" * 50))
        print("\n\n")

        choice = input('{:>80}'.format("Enter Choice: ")).upper()

        if choice == 'A':
            clear()
            Waste_Collection_Menu()
            m.getch()
        elif choice == 'B':
            clear()
            Notice_Menu()
            m.getch()
        elif choice == 'C':
            clear()
            schedule()
            m.getch()
        elif choice == 'D':  
            clear()
            Waste_report()
            m.getch()
        elif choice == 'E':
            print("Logging out...")
            m.getch()
            Main_menu.main()
        else:
            print("Invalid choice. Please try again.")
            m.getch()
