
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

"""

1. Sequence
   - top
   - left
   - parenthesis first

#################################################

2. Selection (if, elif, else)

#####################################

1. if

ချိတ်ဆက်ထားတဲ့ condition မှန်ရင် အလုပ်လုပ်သည်။

#####################################

mark = int(input("Marks = "))

if mark >= 40:
    print("Exam pass.")

#####################################

2. else

ချိတ်ဆက်ထားတဲ့ condition မှားရင် အလုပ်လုပ်သည်။

#####################################

mark = int(input("Marks = "))

if mark >= 40:
    print("Exam pass.")

else:
    print("Exam fail.")

#####################################

mark = int(input("Marks = "))

c1 = mark >= 40

if c1:
    print("Exam pass.")

else:
    print("Exam fail.")

#####################################

3. all from all , one from one

mark = 500

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

if c2: print("Programmer.")

if c3: print("Engineer.")

if c4: print("Distance.")

#####################################

4. one from all

mark = 400

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

if not c1 and c2: print("Programmer.")

if not c1 and not c2 and c3: print("Engineer.")

if not c1 and not c2 and not c3 and c4: print("Distance.")

#####################################

5. one from all by Python ( elif ) ( else + if )

mark = 500

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

elif c2: print("Programmer.")

elif c3: print("Engineer.")

elif c4: print("Distance.")

#####################################

Programmer  =>  not c1 and c2             
Engineer    =>  not c1 and not c2 and c3
Doctor      =>  c1
Distance    =>  not c1 and not c2 and not c3 and c4

Doctor      =>  c1
Programmer  =>  not c1 and c2
Engineer    =>  not c1 and not c2 and c3
Distance    =>  not c1 and not c2 and not c3 and c4

Grade 12    =>  not c1 and not c2 and not c3 and not c4

#####################################

6. if + elif + else

if not c1 and not c2 and not c3 and not c4: print("Grade 12.")

#####################################

mark = int(input("Marks = "))

c1 = mark >= 500
c2 = mark >= 400
c3 = mark >= 300
c4 = mark >= 240

if c1: print("Doctor.")

elif c2: print("Programmer.")

elif c3: print("Engineer.")

elif c4: print("Distance.")

else: print("Grade 12.")

##########################################################################

Code quality

A+             90
A              80
B              70
C              50
F

A+  =>  c1
A   =>  not c1 and c2
B   =>  not c1 and c2 and c3
C   =>  not c1 and c2 and not c3 and c4
F   =>  not c1 and c2 and not c3 and not c4

c1 = mark >= 90
c2 = mark >= 80
c3 = mark >= 70
c4 = mark >= 50

#####################################

mark = 100

c1 = mark >= 90
c2 = mark >= 80
c3 = mark >= 70
c4 = mark >= 50

if c1:
    print("A+")

elif c2:
    print("A")

elif c3:
    print("B")

elif c4:
    print("C")

else:
    print("Fail")

time = + 8 micro sec,  1 to 4
memory = c1 to c4 (120 byte)

#####################################

mark = 75

if mark >= 90:
    print("A+")

elif mark >= 80:
    print("A")

elif mark >= 70:
    print("B")

elif mark >= 50:
    print("C")

else:
    print("Fail")

time = 1 to 4
memory = 0 to 30 byte

#####################################

mark = 30

if 100 >= mark >= 90:
    print("A+")

if 90 > mark >= 80:
    print("A")

if 80 > mark >= 70:
    print("B")

if 70 > mark >= 50:
    print("C")

if mark < 50:
    print("Fail")

c  => 9
if => 5

time = 14 micro sec
memory = 0 to 30 bytes

####################################################################################

"""

