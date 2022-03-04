# Procedure:    bubbleSort
# Objective:    sort an array of integer elements 
# Input:        an address of an array of integers
# Output:       sorted array
.data
array:	.word 9,10,-4,-2
.text
main:
bubbleSort:
lui     t0, 0x10010
li      t1, 0     # i = 0;
li      t2, 0      # j = 0;
li      s1, 3      # array length
loop:
    beq     t1, s1, exit       # exit if i == length of array -1
    lui     t0, 0x10010
    li      t2, 0      # j = 0;
    forLoop:
        beq     t2, s1, exitForLoop   # exit loop if j==length of array -1
        lw      a0, 0(t0)         # a0 = array[j]
        lw      a1, 4(t0)         # a1 = array[j+1]
        ble     a0, a1, update        # if array[j]<=array[j+1] skip
        sw      a1, 0(t0)         # a[j+1] = a[j]
        sw      a0, 4(t0)         # a[j] = a[j+1]
        update:
        addi   t2, t2, 1         # j++
        #sll     $t3, $t2, 2         # t3 = j*4
        addi    t0, t0, 4        #
        j       forLoop
    exitForLoop:
        addi   t1, t1, 1  # i++;
        j   loop
exit:
   
