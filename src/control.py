import sys
import time

import _remote
import _interpreter


if (not _remote._check_interface()):
    print("[ERROR] Not connected to a supported projector.")
    sys.exit(1)

print("Please refer to the README.md for information about the simple scripts.")
print("Enter script name: (e.g. turn_off)")
requested_script = input()
opened_script = None
try:
    opened_script = open(f"scripts/{requested_script}","r")
except FileNotFoundError:
    try:
        opened_script = open(requested_script,"r")
    except FileNotFoundError:
        print("[ERROR] File not found!")
        sys.exit()

line_id = 0
for script_line in opened_script.readlines():
    line_id = (line_id + 1)
    script_line = script_line.rstrip()
    if ((script_line == "") or (script_line.startswith("#"))):
        continue
    script_line = script_line.split(" ")
    if (script_line[0] in _interpreter.supported_function_names.keys()):
        line_start = time.time()
        _interpreter.supported_function_names[script_line[0]](script_line[1:])
        print(f"Line {str(line_id)}: {str(round((time.time() - line_start) * 1000))}ms")
    else:
        print(f"Unexpected/Unknown command: {script_line[0]}")
        raise NotImplementedError

print("Done!")