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

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PHASE-2
* 
* Run file main.py present in phase_2 folder.
* The program executes all the instrutions and display the pipeline stages of each instruction ,number of stalls, IPC(Intructions per Cycle).
* After executing all of the instructions, it also displays the registers and memory states(developed in Phase-1).
* There are five pipleine stages in the developed Simulator.
```    Instruction Fetch(IF) --> Fetches Instruction from the memory
>      Instruction Fetch(IF) --> Fetches Instruction from the memory
>        Register Decode(RF) --> Decodes the Instructions   --? 
> Arithematic Logic unit(EX) --> Performs Arithematic and Logical Calculations
>                Memory(MEM) -->
>             Write Back(WB) --> Writes Back to the Memory
 ```
