start:
.data # Data section of bubble-sort program
Array: .byte 6,7,3,2,9,8
# Array of unsorted data
Arraysize: .byte 6
# Defining size of array
.text
 # Commands section of the program
andi t0, t0, 0 # Clear contents of register t0; Holds array location

andi t1, t1, 0 # Clear contents of register t1; Holds index of inner FOR loop
andi t3, t3, 0 # Clear contents of register t3; Holds content of current array location
andi t4, t4, 0 # Clear contents of register t4
andi t5, t5, 0 # Clear contents of register t5; Holds content of adjacent array location
andi t6, t6, 0 # Clear contents of register t6; Acts as temporary variable during swaps
la t0, Array # Load address where unsorted Array is stored
la t1, Arraysize # Load address where size of array is stored
lb t1, 0(t1) # Load a number from the array
addi t1, t1, -1 # Number of swaps to be made
andi x1, x1, 0 # Clear contents of x1
outerloop: # Outer FOR loop
bge x0, t1, outerend # Jump to end if t1=0 andi t2, 0 # Clear contents of register t2
innerloop: # Inner FOR loop
bge t2, t1, innerend # Jump to end of inner FOR loop if t2=t1
lb t3, 0(t0) # Load the first number from unsorted array to t3
lb t5, 1(t0) # Load the second number from unsorted array to t5
bgt t3, t5, swap # Swap if t3>t5
addi t0, t0, 1 # Increment index to move through the array
addi t2, t2, 1 # Increment index of inner FOR loop
j innerloop # Loop through inner FOR loop
swap: # Swap function
mv t6, t3 # Move t3 to t6 register
mv t3, t5 # Move t5 to t3 register
mv t5, t6 # Move t6 to t5 register
sb t3, 0(t0) # Store t3 to current array location
sb t5, 1(t0) # Store t5 to adjacent array location
addi t0, t0, 1 # Increment index to point to next array location
addi t2, t2, 1 # Increment index of inner FOR loop
j innerloop # Loop through inner FOR loop
innerend: # End of inner FOR loop
la t0, Array # Load address of array
addi t1, t1, -1 # Decrement outer index of outer FOR loop

j outerloop # Loop through outer FOR loop

outerend: j outerend