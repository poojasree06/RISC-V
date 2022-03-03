# RISC-V-Simulator

# Developers:
* Pooja Sree(CS20B002)
* Namitha Reddy(CS20B011)

# PHASE-1
* Main program to develop simulator is present in simulator.py file
* Language used to write program : Python
* Each instruction is of 32 bits
* Simulator supports following RISC-V instructions :

```Arithmetic instructions --> add , sub , addi
>  Arithmetic instructions --> add , sub , addi
>      Memory instructions --> lw , sw
>     Logical instructions --> and , and
>      Branch instructions --> bne , beq , bge , bgt , ble
>        Jump instructions --> j
>       Shift instructions --> slli
>         Set instructions --> slt
>       pseudo instruction --> li
>          lui instruction --> loads upper 20 bits into register
 ```

* Simulator supports atleast 4KB of memory
* It also supports single step execution
* The developed simulator reads in assembly file(.s file) , execute instructions and finally outputs the contents in registers and memory along with PC count
* It points out the errors if any..

