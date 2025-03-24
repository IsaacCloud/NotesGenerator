#Notes Generator

# Device Types
# - Internet Connected Devices
device_tablet = "Tablet"
device_router = "Router"
device_phone = "Phone"
device_pers = "PERS"

# - Bluetooth Devices
device_pulseox = "Pulse Oximeter"
device_scale = "Weight Scale"
device_bp = "Blood Pressure Machine"
device_thermometer = "Thermometer"

device_types = ["1", "2", "3", "4"]

# Welcome
print("*** Ticket Notes Generator ***")

# Input logic
device_type = input("Enter the Device Type: \n 1) Tablet \n 2) Router \n 3) Phone \n 4) PERS \n CHOICE: " )
if device_type not in device_types:
       device_type = input("You must enter the Device Type from the following: \n 1) Tablet \n 2) Router \n 3) Phone \n 4) PERS \n CHOICE: " )
#add device confirmation at some point
asset_tag = input("Enter the Asset Tag: "):
serial_number = input("Enter the Serial Number: ")
kit_assigned = input("Was the device assigned to a HTK? Y/N ")
if kit_assigned == "Y" or "y" or "Yes" or "yes" or "YES":
       kit_name = input("Enter the Kit Name: ")
issue = input("Describe the issue: ")
resolution = input("Provide the solution: ")
follow_up = input("Is a follow up with the user required? Y/N ")
if follow_up == "Y":
       follow_up_date = input("Please enter a follow up date in DD/MM/YYYY format: ")

# Output Summary
print(f"There was a problem with the {device_type} with asset tag {asset_tag} and the serial number {serial_number}. The issue was that {issue}. The problem was solved by {resolution}.")