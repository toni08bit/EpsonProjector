import time
import _remote


# ----------------------
## key([])
def key(args):
    for _ in range(int(args[1])):
        _remote._press_key(args[0])

## sleep([number: milliseconds])
def sleep(args):
    time.sleep(int(args[0]) / 1000)

# ----------------------
supported_functions = [key,sleep]
# ----------------------
    
supported_function_names = {}
for supported_function in supported_functions:
    supported_function_names[supported_function.__name__] = supported_function
