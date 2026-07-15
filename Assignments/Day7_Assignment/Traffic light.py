import time

A = [1, 0, 0, 1]  # Signal A state: 1: Red, 0: Yellow, 2: Green
B = ["Off", "Off", "Off", "Off", "Off", "Off"]  # Red, Yellow, Green for Poll A and Poll B

print("Poll A ==================== Poll B")

while True:
    # Signal A logic
    if A[0] == 1: # Red
        B[0], B[1], B[2] = "On", "Off", "Off"
    elif A[0] == 0: # Yellow
        B[0], B[1], B[2] = "Off", "On", "Off"
    else: # Green
        B[0], B[1], B[2] = "Off", "Off", "On"

    # Signal B logic
    if A[1] == 1: # Red
        B[3], B[4], B[5] = "On", "Off", "Off"
    elif A[1] == 0: # Yellow
        B[3], B[4], B[5] = "Off", "On", "Off"
    else: # Green
        B[3], B[4], B[5] = "Off", "Off", "On"

    print(f"Poll A - Red: {B[0]}, Yellow: {B[1]}, Green: {B[2]}")
    print(f"Poll B - Red: {B[3]}, Yellow: {B[4]}, Green: {B[5]}")
    
    time.sleep(5)

    # State transition logic (Red -> Green -> Yellow -> Red)
    # This is a simple sequence example
    if A[0] == 1: A[0] = 2   # Red to Green
    elif A[0] == 2: A[0] = 0 # Green to Yellow
    else: A[0] = 1           # Yellow to Red

    if A[1] == 1: A[1] = 2
    elif A[1] == 2: A[1] = 0
    else: A[1] = 1

    print("\n After 10 sec ====================")