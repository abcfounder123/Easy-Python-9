
"""

Selection

1. Normal Statement ( ; end of line)
   - motor on
   - motor off
   - pass
   - fail

2. Conditional Statement
   - If water level is low, motor on.  
   - If water level is high, motor off. 
   - if exam pass, show "pass".
   - if exam fail, show "fail".

3. Conditional if Statement
   - boolean data type
   - True

3. Conditional else Statement
   - boolean data type
   - False

################################################

1. Conditional if, if
2. Code block
3. Conditional code block
4. Conditional if code block, if code block, if block 
5. Conditional else code block, else code block, else block  
6. Condition
7. Boolean value
   - empty => False
   - any   => True
8. program flow
9. control flow
10. : (code block)
11. pass (keyword name for pass)

################################################

8. program flow

1. input
2. assign
3. input
4. assign
5. if
6. l eq
7. r eq
8. and
9. print

username = input("username = ")
password = input("password = ")
if username == "Mg Mg" and password == "12345": print("login successful.")

################################################

Nested if (step.4)

Step.1 (condition => output?) (flow)

- 1010 => adgj
- 1011 => adgi
- 1000 => adh
- 1100 => ac
- 0100 => bf
- 0110 => be

################################################

c1 = 1
c2 = 0
c3 = 1
c4 = 0

if c1:
    print("a")
    if c2:
        print("c")
    else:
        print("d")
        if c3:
            print("g")
            if c4:
                print("i")
            else:
                print("j")
        else:
            print("h")

else:
    print("b")
    if c3:
        print("e")
    else:
        print("f")

################################################

Step.2 (output => condition?) (control)

print("Apple.1")  => 1011
print("Apple.2")  => 1010
print("Apple.3")  => 100-
print("Apple.4")  => 10--
print("Apple.5")  => 0-1-
print("Apple.6")  => 0-0-

################################################

c1 = 0
c2 = 0
c3 = 0
c4 = 1

if c1:
    print("a")
    if c2:
        print("c")
    else:
        print("d")
        print("Apple.4")
        if c3:
            print("g")
            if c4:
                print("i")
                print("Apple.1")          
            else:
                print("j")
                print("Apple.2")            
        else:
            print("h")
            print("Apple.3")              
else:
    print("b")
    if c3:
        print("e")
        print("Apple.5")
    else:
        print("f")
        print("Apple.6")

################################################

Step.3 (condition => new code)

101   =>   print("new.1")
100   =>   print("new.2")
0-1   =>   print("new.3")
0-0   =>   print("new.4")

111   =>   print("new.5")
110   =>   print("new.6")

011   =>   print("new.7")
00-   =>   print("new.8")
010   =>   print("new.9")

1011  =>   print("new.10")
1010  =>   print("new.11")

################################################

if c3:
    print("new.5")

else:
    print("new.6")


if c2:
    if c3:
        print("new.7")
        
################################################

c1 = 1
c2 = 0
c3 = 1
c4 = 0

if c1:
    print("a")
    if c2:
        print("c")
        if c3:
            print("new.5")
        else:
            print("new.6")
    else:
        print("d")
        if c3:
            print("g")
            print("new.1")
            if c4:
                print("i")
                print("new.10")
            else:
                print("j")
                print("new.11")
        else:
            print("h")
            print("new.2")

else:
    if c2:
        if c3:
            print("new.7")
        else:
            print("new.9")
    else:
        print("new.8")

    print("b")
    if c3:
        print("e")
        print("new.3")
    else:
        print("f")
        print("new.4")

################################################ 

Step.4 ( idea => code )

print("motor on.")

------------------------------------------------- 

1. low level

if low_level:
    print("motor on.")
    
################################################ 

2. electric, not electric  

if low_level:
    if electric:
        print("motor on.")
    else:
        print("generator on.")
        print("motor on.")
        
################################################  

3. short circuit, not short circuit

if short_circuit:
    print("call mechanic.1")
else:
    print("motor on.")
    
------------------------------------------------- 
    
111
low_level + electric + short_circuit   =>   print("call mechanic.1")
    
101
low_level + not electric + short_circuit   =>   print("call mechanic.2")   
    
110
low_level + electric + not short_circuit   =>   print("motor on.")
    
100
low_level + not electric + not short_circuit   =>   print("motor on.")
   
10   =>   print("generator on.")   
101  =>   print("generator off.")

------------------------------------------------- 

low_level = 1
electric = 1
short_circuit = 0

if low_level:
    if electric:
        if short_circuit:
            print("call mechanic.1")
        else:
            print("motor on.")

    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic.2")
            print("generator off.")
        else:
            print("motor on.")

################################################

4. motor.2

print("motor.2 on.") 

-------------------------------------------------

111
low_level + electric + short_circuit   =>   print("motor.2 on.")   

101
low_level + not electric + short_circuit   =>   print("motor.2 on.")

-------------------------------------------------

low_level = 1
electric = 0
short_circuit = 1
short_circuit_2 = 1


if low_level:
    if electric:
        if short_circuit:
            print("call mechanic for m1")
            print("motor.2 on.")
        else:
            print("motor on.")

    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic for m1")
            print("motor.2 on.")
        else:
            print("motor on.")

 
################################################

5. short_circuit_2, not short_circuit_2   
    
1111          =>    print("call mechanic for m1")
                    print("call mechanic for m2")
                    
1011          =>    print("generator on.")
                    print("call mechanic for m1")
                    print("call mechanic for m2")
                    print("generator off.")
                                        
1110          =>    print("call mechanic for m1")
                    print("motor.2 on.")
                    
1010          =>    print("generator on.")
                    print("call mechanic for m1")
                    print("motor.2 on.")
                    
-------------------------------------------------

low_level = 1
electric = 1
short_circuit = 1
short_circuit_2 = 0


if low_level:
    if electric:
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit_2:
                print("call mechanic for m2")
            else:
                print("motor.2 on.")
        else:
            print("motor on.")

    else:
        print("generator on.")
        if short_circuit:
            print("call mechanic for m1")
            if short_circuit_2:
                print("call mechanic for m2")
                print("generator off.")
            else:
                print("motor.2 on.")
        else:
            print("motor on.")

################################################

6. m3

print("motor.3 on.")

################################################

7. short_circuit_3, not short_circuit_3 

11111  
10111 

11110 
10110 

################################################

8. m4

9. short_circuit_4, not short_circuit_4 

################################################################################################

"""
