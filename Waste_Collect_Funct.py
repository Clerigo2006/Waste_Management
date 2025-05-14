import os
import msvcrt as m
import Main_menu
import datetime
import LGU_MENU

# Collect_Waste function
def Collect_Waste():
    Main_menu.border2()
    print('{:^60}'.format("Collecting waste:"))
    print("\n\n")
    print('{:^165}'.format("─" * 100))
    print("\n")

    Name = input('{:>105}'.format ("Enter Name of the Resident                                            : "))
    Area = input ('{:>105}'.format("Enter Area                                                            : "))

    Waste_Type = input('{:>105}'.format("Enter Type of Waste (e.g., [P] Plastic, [O] Organic, [M] Metal)       : ")).upper()
    if Waste_Type == "P":
        Waste_Type = "Plastic"
    elif Waste_Type == "O":
        Waste_Type = "Organic"
    elif Waste_Type == "M":
        Waste_Type = "Metal"
    else:
        print("\n\n")
        print('{:^165}'.format("─" * 100))
        print("\n\n")
        print('{:^130}'.format("Invalid waste type. Please enter [P], [O], or [M]."))
        m.getch()
        return  
    try:
        Waste_Weight = float(input('{:>105}'.format("Enter Weight of Waste (in kg)                                         : ")))
        print("\n\n")
        print('{:^165}'.format("─" * 100))
    except ValueError:
        print("\n\n")
        print('{:^130}'.format("Invalid weight. Please enter a numeric value."))
        return
    Time = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

    with open("Waste_Collection_File.txt", 'a') as file:
        file.write(f"{Time}|{Name}|{Area}|{Waste_Type}|{Waste_Weight}\n")

    print("\n\n\n\n")
    print('{:^130}'.format("Waste collection recorded successfully!"))
    print('{:^130}'.format("Press enter key to return to the menu..."))
    m.getch()

# View Waste that been collected
def View_Collection_List():
    LGU_MENU.border2()
    print("\n")
    print('{:^170}'.format("[LGU] Waste Collection List"))
    print('{:^170}'.format("─" * 50))
    print("\n\n")

    print(f"{'┌':>15}{"─" * 147}┐")     
    print(f"{'':<20}{'No.':<5} {'TIME':<25} {'NAME':<40} {'AREA':<40} {'TYPE':<15} {'WEIGHT (kg)':<10}")
    print(f"{'├':>15}{"─" * 147}┤") 

    # Check if the file exists and is not empty
    if not os.path.exists("Waste_Collection_File.txt"):
        print("\n\n\n\n\n")
        print('{:^170}'.format("No waste collection records found."))
        print("")
        print('{:^170}'.format("Press enter key to return to the menu..."))
        print("\n\n\n\n")
        print(f"{'├':>15}{"─" * 147}┤") 

        m.getch()
        return

    # if the file exist Read the file and display the contents
    with open("Waste_Collection_File.txt", 'r') as file:
        collections = file.readlines()

    # if file exist but empty
    if not collections:
        print("\n\n\n\n\n")
        print("\n\n")
        print('{:^170}'.format("No waste collection records found."))
        print("")
        print('{:^170}'.format("Press enter key to return to the menu..."))
        print("\n\n\n\n")
        print(f"{'├':>15}{"─" * 147}┤")
        m.getch()
        return

    # calucate the total weight and waste summary
    total_weight = 0
    waste_summary = {}


    for i, line in enumerate(collections):
        Time, Name, Area, Waste_Type, Waste_Weights = line.strip().split("|")
        Waste_Weight = float(Waste_Weights)
        total_weight += Waste_Weight

        if Waste_Type in waste_summary:
            waste_summary[Waste_Type] += Waste_Weight
        else:
            waste_summary[Waste_Type] = Waste_Weight

        print(f"{'':<20}{i + 1:<5} {Time:<25} {Name:<40} {Area:<40} {Waste_Type:<15} {Waste_Weight:<10.2f}")
        print(f"{'├':>15}{"─" * 147}┤")
    
    # Print the summary of the waste collection
    print("\n\n")
    print('{:^50}'.format("Summary:"))
    print('{:>62}'.format(f"Total Waste Collected: {total_weight:.2f} kg"))
    print("")
    print('{:^70}'.format("Waste Types Breakdown:"))
    for waste_type, weight in waste_summary.items():
        print(f" {"":<30} - {waste_type:<15}: {weight:.2f} kg")

    print("\n")
    print('{:^170}'.format("Press enter key to return to the menu..."))
    m.getch()

# Delete Waste Collection
def delete_collection():
    LGU_MENU.clear()
    LGU_MENU.border2()
    print("\n")
    print('{:^170}'.format("[LGU] Delete Waste Collection List"))
    print('{:^170}'.format("─" * 53))
    print("\n\n")

    # Call the function 
    View_Collection_List()
    print("\n")    
    if os.path.exists("Waste_Collection_File.txt"):
        with open("Waste_Collection_File.txt", 'r') as file:
            collections = file.readlines()

        try:
            collection_number = int(input('{:>60}'.format("Enter the collection number to delete (0 to exit): "))) - 1
            if collection_number == -1:
                print('{:^170}'.format("Exiting delete operation..."))
                return
            elif 0 <= collection_number < len(collections):
                del collections[collection_number]
                with open("Waste_Collection_File.txt", 'w') as file:
                    file.writelines(collections)
                print("\n")
                print('{:^170}'.format("Collection deleted successfully!"))
                m.getch()
            else:
                print("\n")
                print('{:^170}'.format("Invalid collection number."))
                m.getch()
        except ValueError:
            print("\n")
            print('{:^170}'.format("Invalid input. Please enter a valid number."))
            m.getch()
