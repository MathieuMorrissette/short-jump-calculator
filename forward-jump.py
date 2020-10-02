
current_address = int(input("Current adress :"), 16)
dst_address = int(input("Destination address :"), 16)

offset = dst_address - current_address

if offset <= 0:
    print("Error negative or zero offset")
    exit(0)


code = offset - 2

if(code > 127):
    print("Error cannot jump further than 127 bytes")
    exit(0)

print("JUMP CODE : EB " + hex(code)[2:].zfill(2))

