# Input section

name = input("For server: Input your first name.\n") # I'm having fun

while True: # The number of diners, ensuring int and > 0
    try:
        diners = int(input("For server: How many ways does the table want to split the bill? \nEnter an integer greater than 0:\n"))
        if diners < 1:
            print("Error: That integer was not greater than 0.")
        else:
            break
    except ValueError:
        print("Error: That was not an integer.")

while True: # The initial cost of the meal, ensuring float, period use, greater than 0, and removing $
    cost = input("For server: What was the cost for all meals at the table? \nEnter in either French,00$ or $English.00 format:\n")
    cost = cost.replace(",", ".")
    fl_cost = cost.strip("$")
    try:
        fl_cost = round(float(fl_cost), 2)
        if fl_cost < 0:
            print("Error: That integer was not greater than 0.")
        else:
            break
    except ValueError:
        print("Error: There were unexpected characters present.")

price_bill = "$" + str(round(fl_cost, 2))

print("\n-----------------------------------------\nPlease hand the terminal to the customer.\n-----------------------------------------\n")

print(f"Thank you for dining with us!\nWe hope you enjoyed {name}'s service this evening!\nWould you like to leave them a tip?")

while True: # Tip percentage among options, ensuring only the integer labels are valid inputs
    tip_label = input("The options are:\n1) Exceptional: 20%\t2)Good: 15%\t3) Basic: 10%\tHorrible: 0%\n")
    try:
        tip_label = int(tip_label)
        if tip_label < 1 or tip_label > 4:
            print("Error: Please select an option from 1 to 4.")
        else:
            break
    except ValueError:
        print("Error: Please select an option from 1 to 4.")

if tip_label == 1:  # Converts tip options to float values
    tip_percent = 0.2
elif tip_label == 2:
    tip_percent = 0.15
elif tip_label == 3:
    tip_percent = 0.1
elif tip_label == 4:
    tip_percent = 0.0
tip_percent_bill = str(int(tip_percent*100)) + "%"

# Calculator section
qc_taxrate = 0.09975
qc_taxed_amount = round(fl_cost * qc_taxrate, 2)
str_qctx =  "$" + str(qc_taxed_amount)

ca_taxrate = 0.05
ca_taxed_amount = round(fl_cost * ca_taxrate, 2)
str_catx =  "$" + str(ca_taxed_amount)

total_taxed = round(fl_cost + qc_taxed_amount + ca_taxed_amount, 2)
str_total_taxed = "$" + str(total_taxed)

amount_tipped = round(fl_cost * tip_percent, 2)
str_amount_tipped = "$" + str(amount_tipped)

grand_total = round(total_taxed + amount_tipped, 2)
str_grand_total = "$" + str(grand_total)

per_person = round(grand_total / diners, 2)
str_per_person = "$" + str(per_person)

# Final outputs:
print("\n--------------------------------------------------------------\nHere is your simplified receipt, thank you for dining with us!\n--------------------------------------------------------------\n")
print(f"The number of diners:\t\t\t\t\t\t\t\t{diners}\nThe price of the meal before tax:\t\t\t\t\t{price_bill}\n"
      f"GST (5%):\t\t\t\t\t\t\t\t\t\t\t{str_catx}\nQST (9,975%):\t\t\t\t\t\t\t\t\t\t{str_qctx}\nThe total including tax:\t\t\t\t\t\t\t{str_total_taxed}\n"
      f"The tip amount (based on the price before tax):\t\t{str_amount_tipped} ({tip_percent_bill})\n"
      f"The grand total including tax:\t\t\t\t\t\t{str_grand_total}\nThe amount owed per person:\t\t\t\t\t\t\t{str_per_person}\n"
      f"\nPlease come again soon :)")