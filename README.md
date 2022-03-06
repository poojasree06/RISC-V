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
   - Execution Mode - The program will execute all the instructions, and display the state of the registers and memory after executing all instructions.
   - Step by Step Mode - The program will run one instruction at a time.The next instruction will be executed only when the user presses a key.

# How to use it
* Download the zip file
* Paste your assembly code into instructions.s
* Run simulator.py 
