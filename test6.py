import obd
import time
import os
import sys

# Save the original sys.stdout for later use
original_stdout = sys.stdout

# Redirect sys.stdout to a text file
log_file_path = "console_output.txt"
sys.stdout = open(log_file_path, "w")

os.system('cls')
Wait = time.sleep
for x in range(61):
    if x >= 30:
        print('Check the Cable. Plug it in and out maybe?')
        print()
    if x == 60:
        os.system('cls')
        print('connection timeout, Unable to make connection. Please try again.')
        print()
        print('Check the Cable. Plug it in and out maybe?')
        exit()

    try:
        connection = obd.OBD()  # auto-connects to USB or RF port
        cmd = obd.commands.SPEED  # select an OBD command (sensor)
        response = connection.query(cmd)  # send the command, and parse the response
        print(response.value)  # returns unit-bearing values thanks to Pint
        print(response.value.to("mph"))  # user-friendly unit conversions
        break
    except:
        Wait(0.5)
        os.system('cls')
        pass

print('Hey its actually working...')

# Restore the original sys.stdout
sys.stdout = original_stdout

# Close the log file
sys.stdout.close()
