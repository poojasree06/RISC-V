.data
	array: .word 100,5,6,7
.text
main:
	.data
	array: .word 100,5,6,7
.text
main:
	lui t0,0x10010
	lw t1,0(t0)          # t4=a[0]
    sub t4,t1,t3
    and s1,t1,s2
    or s3,t1,s4
