import sys

import _remote


if (not _remote._check_interface()):
    print("[ERROR] Not connected to a supported projector.")
    sys.exit(1)

print("Please refer to the README.md for information about the simple scripts.")
print("Enter script name: (e.g. turn_off)")
requested_script = input()