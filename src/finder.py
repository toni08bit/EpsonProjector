import re
import subprocess
import time

name_regex = re.compile(r'EBE[0-9A-Z]{5}-[A-Z]{2}[0-9]{2}[A-Za-z0-9@]{11}')
ssid_position = 7

running_subprocesses = []
read_names = []
try:
    read_file = open("list.txt","r")
    for line in read_file.readlines():
        line = line.strip()
        if (line == ""):
            continue
        read_names.append(line)
    read_file.close()
except FileNotFoundError:
    print("[WARN] list.txt does not exist (will create).")
append_file = open("list.txt","a")

def check_regex(found_name):
    return name_regex.match(found_name)

def rescan():
    scan_process = subprocess.Popen([
        "nmcli",
        "dev",
        "wifi",
        "rescan"
    ])
    running_subprocesses.append(scan_process)
    scan_process.wait()
    running_subprocesses.remove(scan_process)

def get_list():
    list_process = subprocess.Popen(
        args = [
            "nmcli",
            "-t",
            "dev",
            "wifi"
        ],
        stdout = subprocess.PIPE
    )
    running_subprocesses.append(list_process)
    list_process.wait()
    running_subprocesses.remove(list_process)
    scanned_names = []
    for read_name in read_names:
        scanned_names.append(read_name)
    for line in list_process.stdout.readlines():
        scanned_name = line.decode("utf-8").strip().split(":")[ssid_position]
        if (scanned_name not in scanned_names):
            if (check_regex(scanned_name)):
                print(f"!!! Adding: {scanned_name}")
                scanned_names.append(scanned_name)
                append_file.write(f"{scanned_name}\n")
                read_names.append(scanned_name)
            else:
                scanned_names.append(scanned_name)
                print(f"Ignored: {scanned_name}")

try:
    while True:
        print("----- DELAY -----")
        time.sleep(2)
        print("----- RESCANNING -----")
        rescan()
        print("----- GETTING LIST -----")
        get_list()
except KeyboardInterrupt:
    print("Saving file...")
    append_file.flush()
    append_file.close()
    print("Terminating processes...")
    for process in running_subprocesses:
        process.terminate()
    print("Done!")
