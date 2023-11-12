import sys

import _remote


if (not _remote._check_interface()):
    print("[ERROR] Not connected to a supported projector.")
    sys.exit()

# TODO