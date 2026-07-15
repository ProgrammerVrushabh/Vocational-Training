import time

A = [1, 0,0,1]
B = ["Off", "Off", "Off", "Off"]

print("Poll A ==================== Poll B")

while True:
    # Signal 1: Led 1 = Red, Led 2 = Green (opposite of each other)
    if A[0] == 0:
        B[0] = "Off"    # Red off
        B[1] = "On"     # Green on
    else:
        B[0] = "On"     # Red on
        B[1] = "Off"    # Green off

    # Signal 2: Led 3 = Red, Led 4 = Green (opposite of each other)
    if A[1] == 0:
        B[2] = "Off"    # Red off
        B[3] = "On"     # Green on
    else:
        B[2] = "On"     # Red on
        B[3] = "Off"    # Green off

    print("Led 1 (Red): ", B[0], end="    ::       ")
    print("Led 3 (Red): ", B[2], end="")
    print()
    print("Led 2 (Green): ", B[1], end="  ::       ")
    
    print("Led 4 (Green): ", B[3])
    

    time.sleep(10)

    
    A[0] = 1 - A[0]
    A[1] = 1 - A[1]
    

    print("\n After 10 seconds ====================")