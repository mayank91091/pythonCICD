import subprocess
import datetime

# Define the command to run your Python project
# Replace 'your_project.py' with your project's main script or command
project_command = ["python", "main.py"]

# Define the log file name with a timestamp
log_file_name = f"build_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

try:
    # Run the project command and capture the output
    with open(log_file_name, 'w') as log_file:
        process = subprocess.Popen(project_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        
        for line in process.stdout:
            print(line, end='')  # Print the output to the console
            log_file.write(line)  # Write the output to the log file
        
        for line in process.stderr:
            print(line, end='')  # Print the error messages to the console
            log_file.write(line)  # Write the error messages to the log file

    print("Project execution completed.")

except Exception as e:
    print("Error:", e)

# The log file will be automatically closed when the 'with' block exits
