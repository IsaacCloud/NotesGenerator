#Notes Generator

import sys 

# Device Types
device_types = {
       "1": "Tablet",
       "2": "Router",
       "3": "Phone",
       "4": "PERS",
       "5": "Pulse Oximeter",
       "6": "Weight Scale",
       "7": "Blood Pressure Machine",
       "8": "Thermometer"
}

speed_test_results = "NA"

# Welcome Message
print("*** Ticket Notes Generator ***")

# Input logic
device_type = input("Enter the Device Type: \n 1) Tablet \n 2) Router \n 3) Phone \n 4) PERS \n 5) Pulse Oximeter \n 6) Weight Scale \n 7) Blood Pressure Machine \n 8) Thermometer \n CHOICE: " )
if device_type not in device_types:
       print("You must enter the Device Type from the following: \n 1) Tablet \n 2) Router \n 3) Phone \n 4) PERS \n CHOICE: " )
device_name = device_types[device_type]
print(f"You selected {device_name}.")

asset_tag = "NA"
asset_tag = input("Enter the Asset Tag, enter '0000' if there is no Asset Tag: ")
if not asset_tag.isdigit():
    print("Please start over and enter a numerical value for the Asset tag.")
    sys.exit()

serial_number = "NA"
serial_number = input("Enter the Serial Number: ")
kit_assigned = input("Was the device assigned to a HTK? Y/N ")
kit_name = "NA"
if kit_assigned in ["Y", "y", "Yes", "yes", "YES"]:
       kit_name = input("Enter the Kit Name: ")


speed_test = input("Were you able to run a speed test? Y/N: ")

if speed_test in ["Y", "y", "Yes", "yes", "YES"]:
        download_speed = input("Download Speed in Mbps: ")
        upload_speed = input("Upload Speed in Mbps: ")
        ping = input("Ping in ms: ")
        jitter = input("Jitter in ms: ")

        speed_test_results = f"Download:{download_speed}\nMbps Upload:{upload_speed}Mbps\nPing:{ping}ms\nJitter{jitter}ms"

issue = input("Problem: ")
cause = input("Cause: ")
resolution = input("Solution: ")
follow_up = input("Is a follow up with the user required? Y/N: ")
if follow_up == "Y":
       follow_up_date = input("Please enter a follow up date in DD/MM/YYYY format: ")
else:
       follow_up_date = "NA"

# Output Summary
# print(speed_test_results)
print(f"Copy and paste this summary into your ticket notes: \n\nDevice Reported: {device_name}\nAsset Tag: {asset_tag}\nSerial Number: {serial_number}\nKit Name: {kit_name}\n\nSpeed Test Resuluts:\n{speed_test_results}\n\nProblem:\n{issue}\n\nCause:\n{cause}\n\nResolution:\n{resolution}\n")
print(f"If a follow up is required, please follow up with the user on: {follow_up_date}")

# Output to file > figure this out.