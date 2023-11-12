def find_key_for(name):
    return f"381A52{name[2:8]}"

existing_keys = []
try:
    existing_file = open("passwords.txt","r")
    for line in existing_file.readlines():
        line = line.strip()
        if (line == ""):
            continue
        existing_keys.append(line.split(": ")[0])
    existing_file.close()
except FileNotFoundError:
    print("[WARN] passwords.txt does not exist (will create)")

append_file = open("passwords.txt","a")

list_file = open("list.txt","r")
for line in list_file.readlines():
    line = line.strip()
    if ((line == "") or (line in existing_keys)):
        continue

    new_line = f"{line}: {find_key_for(line)}\n"
    append_file.write(new_line)
    print(new_line[:-1])

list_file.close()
append_file.flush()
append_file.close()
print("Done!")