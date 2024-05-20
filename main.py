import subprocess

# List of file names
file_names = ['pubsubAMP.py', 'pubsubAMS.py', 'pubsubTMP.py', 'pubsubTMS.py']

# List to store the subprocesses
processes = []

# Start a subprocess for each file
for file_name in file_names:
    process = subprocess.Popen(['python', file_name])
    processes.append(process)

# Wait for all subprocesses to finish
for process in processes:
    process.wait()
