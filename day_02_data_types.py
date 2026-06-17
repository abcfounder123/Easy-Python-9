
"""

Data Types (15)

စာ သုံးခု
1. Character              --->  chr()
2. Character String       --->  str()
3. Documentation String   --->  doc

နံပါတ် သုံးခု
1. Integer                --->  int()
2. Floating-point number  --->  float()
3. Complex number         --->  complex()

စာရင်း ရှစ်ခု
1. Normal list            --->  list(), tuple()
2. Unique list            --->  set(), frozenset()
3. Binary list            --->  bytearray(), bytes()
4. Number                 --->  range()
5. Item list              --->  dict()

အခြေအနေ တစ်ခု
1. boolean data type      --->  bool()

Data types 15 မျိုး
စာ သုံးခု
နံပါတ် သုံးခု
စာရင်း ရှစ်ခု
အခြေအနေ တစ်ခု

#################################################

Exercises

1 to 99    =>  range(1, 100, 1)
start = 1
stop = 100
step = 1

1 to 100    =>  range(1, 101, 1)
start = 1
stop = 101
step = 1

2, 4, 6, ... to 100    =>  range(2, 101, 2)
start = 2
stop = 101
step = 2

1, 3, 5, ... to 99    =>  range(1, 100, 2)
start = 1
stop = 100
step = 2

100, 98, 96, ... to 2    =>  range(100, 1, -2)
start = 100
stop = 1
step = -2

99, 97, 95, ... to 1    =>  range(99, 0, -2)
start = 99
stop = 0
step = -2

-100, -98, -96, ... to  -2    =>  range(-100, -1, 2)
start = -100
stop = -1
step = 2

-2, -4, -6, ... to  -100    =>  range(-2, -101, -2)
start = -2
stop = -101
step = -2


255, 260, ..., 500
range(255, 501, 5)

500, 495, ..., 255
range(500, 254, -5)

0 to 10    =>  range(0, 11, 1)
start = 0
stop = 11
step = 1

range(0, 11, 1)
range(0, 11)    <--- step = 1
range(11)       <--- start = 0, step = 1

#################################################

Data types of Python (15)

1. str()
2. int()
3. float()
4. complex()
5. list()
6. tuple()
7. set()
8. frozenset()
9. bytearray()
10. bytes()
11. range()
12. dict()
13. bool()

14. memoryview()
15. NoneTypes

Python မှ သတ်မှတ်ထားသော Data types 15 မျိုး
စာ
နံပါတ် သုံးခု
စာရင်း ရှစ်ခု
အခြေအနေ တစ်ခု
data မဟုတ်တဲ့ နှစ်ခု

#################################################

Creating data types by name (14)

1. str()
2. int()
3. float()
4. complex()
5. list()
6. tuple()
7. set()
8. frozenset()
9. bytearray()
10. bytes()
11. range()
12. dict()
13. bool()
14. memoryview()

#################################################

1 + 2                     <--- Creating data types by symbols
int(1).__add__(int(2))    <--- Creating data types by name

#################################################

Creating data types by symbols (11)

1. quotes
2. .           decimal point
3. j
4. [ ]         square bracket
5. ( )         round bracket
6. { }         curly bracket
7. b
8. { }

Value is symbol.
1. integer   =>   1
2. boolean   =>   True False
3. NoneType  =>   None

#################################################

Name only
8. frozenset()
9. bytearray()
11. range()
14. memoryview()

#################################################

Knowledge

1. integer
   - underscore

2. float
   - underscore
   - e => exponent
     - e3 => 10 ** 3 => 10 * 10 * 10  => 1000
     - 1e3 => 1000.0
   - round()

3. collection, element

4. empty, any
   - 0, 0.0, 0j       =>  empty value
   - [], (), {}, ""   =>  empty element

5. tuple
   - comma
   - (1, )
   - ("Mg Mg", )

6. range
   - start, stop, step
   - shortcut
     - range(0, 10, 1)
     - range(0, 10)
     - range(10)

 7. dict
    - items   => [('name', 'Mg Mg'), ('age', 20), ('height', 5.5), ('marks', [60, 70, 80])]
    - keys    => ['name', 'age', 'height', 'marks']
    - values  => ['Mg Mg', 20, 5.5, [60, 70, 80]]
{
    "name": "Mg Mg",
    "age": 20,
    "height": 5.5,
    "marks": [60, 70, 80]
}

8. empty dict or empty set
   - {}   =>  dict

9. empty set
   - {}   <--- can not create by symbols
   - set()

"""

# Checking data type

b''
b'apple'

bytearray(b'')
bytearray(b'apple')

memoryview(b"apple")
# <memory at 0x1005f2080>

''
' '
'1000'
"1000"
'''1000'''
"""1000"""

0j
3 + 2j
1j
complex(3, 2)

0
-1
+1
1_000
1_000_000
1_000_000_000
1000000000

0.0
-1.0
+1.0
1.0
1000.0
.01
100.
0.
.0
1_000_000.0
1e6  # e6 = 1000000

1e9

1000000000000.0
1_000_000_000_000.0
1e12


1e-1  # e-1 = 1/10 = 0.1
1e-2  # e-2 = 1/100 = 0.01
1e-6  # e-6 = 1/1000000 = 0.000001
0.000001
1e-9  # 0.000000001
1.234e-9  # 0.000000001234

# correct answer = 0.0, 159e-15 => 0.00000000000000159
0.00
0.000
0.000000

0.1 + 0.2
0.30000000000000004

# 0.0  => rocket
# 0.000000000000001 => round => 0.00

["apple", "banana", "orange"]
[]
list()


()
tuple()
"Mg Mg", 20, 5.5
("Mg Mg", 20, 5.5)
(1, )
("Mg Mg", )

("Mg Mg")  # "Mg Mg"
(1)        # 1

(1 + 2) * 4

range(0, 10, 1)
range(0, 10)
range(10)
range(2, 101, 2)

{"name": "Mg Mg", "age": 20, "height": 5.5}

{
    "name": "Mg Mg",
    "age": 20,
    "height": 5.5,
    "marks": [60, 70, 80]
}

{}

{"apple", "banana", "orange"}
set()
frozenset()
frozenset({'apple', 'orange', 'banana'})  # frozenset
frozenset(['apple', 'orange', 'banana'])
frozenset(('apple', 'orange', 'banana'))

1000
0
int()

True
False
bool()

None

{}
dict()
set()
{1, }

"1000"
str(1000)

1000
int("1000")

1000.0
float(1000)
float("1000")

