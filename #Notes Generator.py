#Notes Generator

# Imports
import sys # Used for exiting app if no asset tag is entered.
import pyperclip # Used to copy notes generated to clipboard.

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

asset_tag = "NA"
serial_number = "NA"
kit_name = "NA"
speed_test_results = "NA"
follow_up_date = "Not required."

# Welcome Message
print("\n*** Ticket Notes Generator ***")

# Input logic
device_type = input("Enter the Device Type: \n 1) Tablet \n 2) Router \n 3) Phone \n 4) PERS \n 5) Pulse Oximeter \n 6) Weight Scale \n 7) Blood Pressure Machine \n 8) Thermometer \n\n CHOICE: " )
if device_type not in device_types:
       print("You must enter the Device Type from the following: \n 1) Tablet \n 2) Router \n 3) Phone \n 4) PERS \n CHOICE: " )
device_name = device_types[device_type]
print(f"\nYou selected {device_name}.\n")


asset_tag = input("Enter the Asset Tag, enter '0000' if there is no Asset Tag: ")
if not asset_tag.isdigit():
    print("Please start over and enter a numerical value for the Asset tag.")
    sys.exit()


serial_number = input("Enter the Serial Number: ")
kit_assigned = input("Was the device assigned to a HTK? Y/N ")

if kit_assigned in ["Y", "y", "Yes", "yes", "YES"]:
       kit_name = input("Enter the Kit Name: ")
       kit_link = input("Paste the link to the kit: ")

speed_test = input("Were you able to run a speed test? Y/N: ")

if speed_test in ["Y", "y", "Yes", "yes", "YES"]:
        download_speed = input("Download Speed in Mbps: ")
        upload_speed = input("Upload Speed in Mbps: ")
        ping = input("Ping in ms: ")
        jitter = input("Jitter in ms: ")

        speed_test_results = f"Download: {download_speed}Mbps\nUpload: {upload_speed}Mbps\nPing: {ping}ms\nJitter: {jitter}ms"

issue = input("Problem: ")
cause = input("Cause: ")
resolution = input("Solution: ")
follow_up = input("Is a follow up with the user required? Y/N: ")
if follow_up in ["Y", "y", "Yes", "yes", "YES"]:
       follow_up_date = input("Please enter a follow up date in DD/MM/YYYY format: ")

# Output Summary to be copied and pasted into Incident Notes. Does not do spelling or grammar checks. Make corrections in the Notes field before submitting.
rma_notes = f"""
[code]<b>Summary:</b>[/code]

[code]<b>Device Type:</b>[/code] {device_name}
[code]<b>Asset Tag:</b>[/code] {asset_tag}
[code]<b>Serial Number:</b>[/code] {serial_number}
[code]<b>Kit Name: </b><a href="{kit_link}">{kit_name}</a>[/code]

[code]<b>Speed Test Results:</b>[/code]
{speed_test_results}

[code]<b>Problem:</b>[/code]
{issue}

[code]<b>Cause:</b>[/code]
{cause}

[code]<b>Resolution:</b>[/code]
{resolution}

[code]<b>Follow up: {follow_up_date}</b>[/code]
"""

print(rma_notes)
pyperclip.copy(rma_notes)
print("✅ RMA notes copied to clipboard! 📋")