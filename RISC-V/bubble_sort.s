# bubble sort
# slli,li addi,add,lui,beq,lw,sw,j
.data
	array: .word 0,-6,-5,9,10
.text
	main:
		lui s1,0x10010 #address of array
		addi s2,s2,5  # size  change size according to array size in data part
		addi s3,s3,0  #i=0
		addi s5,s2,-1  #size-1
		for1:
		bge s3,s5,exit   # if(i>=size-1)
		addi s4,t1,0     # j=0    #t1=0 
		sub s6,s5,s3   #size-1-i 
		for2:
		bge s4,s6 ,end1  # if(j>=(size-i-1) go to for1  end
		slli t2,s4,2   #s4<<2
		add t3,s1,t2  # A+ j*4  base address
		lw t4,0(t3)   # A[0]
		lw t5,4(t3)    # A[4]
		bgt t4,t5,swap
		addi s4,s4,1   # j=j+1
		j for2
		end1: 
		addi s3,s3,1   # i=i+1		
		j for1       # jump to for1
		swap:
		sw t5,0(t3)   # a[0]=s[4]
		sw t4,4(t3)  # a[4]=a[0]
		addi s4,s4,1  # j=j+1
		j for2
		exit: