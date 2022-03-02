.data
	array: .word 100,5,6,7     #output:200 ,105,106,107
.text
main:
	lui t0,0x10010
	addi t2,t2,0   #i =0
	addi t3,t3,4   #n=4
	for: 
	bge t2,t3,exit        #i>=4 exit 
	lw t4,0(t0)          # t4=a[0]
	addi t4,t4,100       #t4=t4+100
	sw t4,0(t0)         # a[0]=t4
	addi t0,t0,4   
	addi t2,t2,1        #i=i++
	j for
	exit:
