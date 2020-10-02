

current_address = int(input("Current adress :"), 16)
dst_address = int(input("Destination address :"), 16)

offset = current_address - dst_address

if offset <= 0:
    print("Error negative or zero offset")
    exit(0)

code = int("0xFF", 16) - ((offset + 1))

if code > 128:
    print("Error cannot jump further than 127 bytes")


print("JUMP CODE : EB " + (hex(code)[2:].zfill(2)).upper())
