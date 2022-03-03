.data
Array: .word 4,3,2,1,6

.text
main:
lui a0,0x10010        # we set address of Array[0]
li t0,0      # i
li t1,0      # j
li t2,5      # n-i
li s1,5      # n
add t3,zero,a0        # storing address of Array[0]
add t4,zero,t4        # another register to store address of Array[0]
LOOP0:
li t1,0                       #every time we go to outerloop set j=0 to again start execution of innerloop
addi t2,t2,-1                 # t2 gets updated with (n-i)-1 i.e t2-1 for upperbound of innerloop
add  t3,a0,zero

LOOP1:
lw s2,0(t3)
addi t3,t3,4
lw s3,0(t3)
addi t1,t1,1
slt t5,s2,s3           # t5=1 if s2<s3
bne t4,zero,condi
swap:
sw s3,0(t3)
sw s2,-4(t3)
condi:
bne t1,t2,LOOP1      # if j!=n-i-1

addi t0,t0,1
bne t0,s1,LOOP0      # if j!=n
