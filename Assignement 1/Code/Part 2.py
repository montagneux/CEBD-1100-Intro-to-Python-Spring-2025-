# Preliminary work
import csv
csvfile = "/Users/gabrielimbeau/PycharmProjects/CEBD-1100-Intro-to-Python-Spring-2025-/Assignement 1/Files/50000_Sales_Records.csv"

# Importing the file and read it.
csv_data = []
try:
    with open(csvfile, mode = "r", encoding = "utf-8") as input_file:
        reader = csv.reader(input_file, delimiter=",")
        csv_data = list(reader)
# Close programme in case of a fileread error.
except IOError:
    print("Sorry an error has occurred.")

# Formats sales channels
channel_data = {}

for row in csv_data: # Creating a fake csv for just the channels
    channel = row[3]
    try:
        units = int(row[8])
        revenue = float(row[11])
    except ValueError:
        continue

    if channel not in channel_data: # Formats new rows into the new csv.
        channel_data[channel] = {"total_units": 0, "total_revenue": 0.0}

    channel_data[channel]["total_units"] += units # Populates the new column, same for next line.
    channel_data[channel]["total_revenue"] += revenue

# Totals per channel
for channel, totals in channel_data.items():
    if channel == "Offline":
        offline_units = int(totals["total_units"])
        offline_revenue = float(totals["total_revenue"])
    else:
        online_units = int(totals["total_units"])
        online_revenue = float(totals["total_revenue"])

# Average revenue per unit per channel
offline_average_revenue = float(offline_revenue / offline_units)
online_average_revenue = float(online_revenue / online_units)

# Big totals
total_units = offline_units + online_units
total_revenue = offline_revenue + online_revenue
total_average_revenue = total_revenue / total_units

# Making outputs printable
str_off_rev = "$" + str(round(offline_revenue, 2))
str_off_av = "$" + str(round(offline_average_revenue, 2))

str_on_rev = "$" + str(round(online_revenue, 2))
str_on_av = "$" + str(round(online_average_revenue, 2))

str_tot_rev = "$" + str(round(total_revenue, 2))
str_tot_av = "$" + str(round(total_average_revenue, 2))

# Formatting the output txt
txtfile = "/Users/gabrielimbeau/PycharmProjects/CEBD-1100-Intro-to-Python-Spring-2025-/Assignement 1/Files/Sales_Report.txt"

sales_report_body = (
    f"Sales Report\n"
    f"------------\n\n"
    f"Produced on: 18-04-2025\n\n"
    f"Channels analysed: Offline, Online\n\n"
    f"Total, x channels\n\n"
    f"Offline\n\n"
    f"\tTotal units sold:\t\t\t\t{offline_units}\n"
    f"\tTotal revenue per unit:\t\t\t{str_off_av}\n"
    f"\tTotal revenue of sales:\t\t\t{str_off_rev}\n\n"
    f"Online\n\n"
    f"\tTotal units sold:\t\t\t\t{online_units}\n"
    f"\tTotal revenue per unit:\t\t\t{str_on_av}\n"
    f"\tTotal revenue of sales:\t\t\t{str_on_rev}\n\n"
    f"Grand totals\n\n"
    f"\tTotal units sold:\t\t\t\t{total_units}\n"
    f"\tTotal revenue per unit:\t\t\t{str_tot_av}\n"
    f"\tTotal revenue of sales:\t\t\t{str_tot_rev}\n\n"
    )

with open(txtfile, mode = "w", encoding = "utf-8") as output_file:
    output_file.write(sales_report_body)