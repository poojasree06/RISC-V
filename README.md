# RISC-V-Simulator

# Developers:
* Pooja Sree(CS20B002)
* Namitha Reddy(CS20B011)

# PHASE-1
* Language used to write program : Python
* Main program to develop simulator is present in simulator.py file
* Each instruction is of 32 bits
* Simulator supports following RISC-V instructions :

```Arithmetic instructions --> add , sub , addi
>  Arithmetic instructions --> add , sub , addi
>      Memory instructions --> lw , sw
>     Logical instructions --> and , andi
>      Branch instructions --> bne , beq , bge , bgt , ble
>        Jump instructions --> j
>       Shift instructions --> slli, sll
>         Set instructions --> slt
>       pseudo instruction --> li
>          lui instruction --> loads upper 20 bits into register
 ```

* Simulator supports atleast 4KB of memory
* The developed simulator reads in assembly file(.s file).
* There are two execution modes supported:
* Execution Mode - The program will execute all the instructions, and display the state of the registers and memory after executing all instructions.
* Step by Step Mode - The program will run one instruction at a time.The next instruction will be executed only when the user presses a key.

# Guidelines
* The assembly program can contain .data and .text sections. There should be no text, apart from comments or blank lines, between the two sections
* The .data section can contain labels pertaining to word. Only integer data is supported
* When referring to a register, they must be referred to by their ABI names.Only ABI names are supported.
* A line containing a label may not contain any other instruction.
* Any memory element created in the data section is assigned an address starting from 0x10010000
* Except in displaying the address, all values used use the decimal number system.
* ---?
* Comments are supported

# How to use it
* Run simulator.py 
