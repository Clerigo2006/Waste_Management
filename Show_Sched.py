import os
import LGU_MENU
import msvcrt as m

# defualt sched
schedules = {"Sunday": "6:00am - 9:00am",
            "Monday": "6:00am - 9:00am", 
            "Tuesday": "6:00am - 9:00am", 
            "Wednesday": "6:00am - 9:00am", 
            "Thursday": "6:00am - 9:00am",
            "Friday": "6:00am - 9:00am", 
            "Saturday": "6:00am - 9:00am"}

# Shoe Schedule
def View_Schedule():
    LGU_MENU.border2()
    print("\n\n\n")
    print('{:^170}'.format("Waste Collection Schedule"))
    print('{:^170}'.format("─" * 50))
    print("\n\n")

    print(f"{'┌':>62}{'─'*46}┐" )
    print(f"{'':>62} {'DAY':<27} {'TIME':>11}      ")
    print(f"{'├':>62}{'─'*46}┤")

    for day, time in schedules.items():
        print(f"{"":>62} {day:<24} : {time:>11}   ")
        print(f"{'├':>62}{'─'*46}┤")

    print('{:^170}'.format("─" * 50))
    print("\n\n")
    print('{:^170}'.format("Press enter key to return to the menu..."))
    m.getch()

# Update the schedule
def update_schedule():
    LGU_MENU.border2()
    print("\n\n\n")
    print('{:^170}'.format("Update Schedule:"))
    print('{:^170}'.format("─" * 50))
    print("\n\n")

    print('{:^68}'.format("Current Schedule:"))
    View_Schedule()

    print("\n")

    day = input('{:>62}'.format("Enter the day to update (e.g., Monday): ")).capitalize()

    if day in schedules:
        new_time = input('{:>62}'.format(f"Enter new time for {day} (e.g., 6:00am - 9:00am): "))
        schedules[day] = new_time
        print("\n")
        print('{:^170}'.format(f"Schedule for {day} updated successfully!"))

    else:
        print("\n\n")
        print('{:^170}'.format("Invalid day. Please try again."))

    print('{:^170}'.format("Press enter key to return to the menu..."))
    m.getch()  
