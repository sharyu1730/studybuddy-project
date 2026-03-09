from flask import Flask, render_template, request

app = Flask(__name__)

# ================== FULL COURSE STRUCTURE ==================

course_structure = {

    "CO1":
    {

    # ================= BASIC MATHEMATICS =================
    "Basic Mathematics": {

        "Unit 1": {
            "Algebra": {
                "definition": "Algebra deals with variables and mathematical expressions.",
                "topics": [
                    "Polynomials: 2x³ + 3x² − x + 5",
                    "Degree = Highest power",
                    "Types: Linear, Quadratic, Cubic",
                    "Factorization methods (Common, Grouping, Identities)",
                    "Quadratic Formula: x = (-b ± √(b² − 4ac)) / 2a",
                    "Discriminant concept"
                ]
            }
        },

        "Unit 2": {
            "Trigonometry": {
                "definition": "Study of angles and triangle ratios.",
                "topics": [
                    "sinθ = opposite/hypotenuse",
                    "cosθ = adjacent/hypotenuse",
                    "tanθ = opposite/adjacent",
                    "sin²θ + cos²θ = 1",
                    "1 + tan²θ = sec²θ",
                    "Applications in height & distance"
                ]
            }
        },

        "Unit 3": {
            "Calculus": {
                "definition": "Study of limits, differentiation and integration.",
                "topics": [
                    "Limits: lim x→a f(x)",
                    "Differentiation: dy/dx",
                    "Derivative of x² = 2x",
                    "Integration: ∫x dx = x²/2",
                    "Applications in optimization"
                ]
            }
        },

        "Unit 4": {
            "Statistics & Probability": {
                "definition": "Collection and analysis of data.",
                "topics": [
                    "Mean, Median, Mode",
                    "Standard deviation",
                    "Probability formula P(A)"
                ]
            }
        },

        "Unit 5": {
            "Revision & Viva": {
                "definition": "Important revision and viva questions.",
                "topics": [
                    "Types of polynomials",
                    "Quadratic roots types",
                    "Trigonometric identities",
                    "Basic calculus formulas"
                ]
            }
        }
    },

    # ================= FUNDAMENTALS OF ICT =================
    "Fundamentals of ICT": {

        "Unit 1": {
            "Computer System": {
                "definition": "Basic components of computer system.",
                "topics": [
                    "Input devices: Keyboard, Mouse, Scanner",
                    "Output devices: Monitor, Printer",
                    "CPU: ALU, CU, Registers"
                ]
            }
        },

        "Unit 2": {
            "Memory Types": {
                "definition": "Types of computer memory.",
                "topics": [
                    "RAM (Volatile)",
                    "ROM (Permanent)",
                    "Cache memory",
                    "Secondary storage: HDD, SSD"
                ]
            }
        },

        "Unit 3": {
            "Software Types": {
                "definition": "Different types of software.",
                "topics": [
                    "System Software (Windows, Linux)",
                    "Application Software (MS Word)",
                    "Utility Software (Antivirus)"
                ]
            }
        },

        "Unit 4": {
            "Internet Concepts": {
                "definition": "Basics of Internet communication.",
                "topics": [
                    "IP Address (IPv4 32-bit)",
                    "DNS",
                    "HTTP & HTTPS",
                    "Email protocols (SMTP, POP3)"
                ]
            }
        },

        "Unit 5": {
            "Revision & Viva": {
                "definition": "Important ICT viva questions.",
                "topics": [
                    "Difference between RAM & ROM",
                    "Functions of CPU",
                    "What is DNS?",
                    "Types of software"
                ]
            }
        }
    },

    # ================= PHYSICS =================
    "Physics": {

        "Unit 1": {
            "Mechanics": {
                "definition": "Study of motion and forces.",
                "topics": [
                    "Force = mass × acceleration (F = ma)",
                    "Work = Force × Distance",
                    "Power = Work / Time"
                ]
            }
        },

        "Unit 2": {
            "Electricity": {
                "definition": "Study of electric current and circuits.",
                "topics": [
                    "Ohm’s Law: V = IR",
                    "Series circuit (Current same)",
                    "Parallel circuit (Voltage same)"
                ]
            }
        },

        "Unit 3": {
            "Magnetism": {
                "definition": "Study of magnetic fields.",
                "topics": [
                    "Magnetic field",
                    "Electromagnetism",
                    "Applications in motors"
                ]
            }
        },

        "Unit 4": {
            "Waves & Optics": {
                "definition": "Study of wave motion and light.",
                "topics": [
                    "Wave speed = fλ",
                    "Reflection & Refraction",
                    "Laws of optics"
                ]
            }
        },

        "Unit 5": {
            "Revision & Viva": {
                "definition": "Important physics viva questions.",
                "topics": [
                    "State Ohm's Law",
                    "Define work and power",
                    "Difference between series & parallel"
                ]
            }
        }
    },

    # ================= CHEMISTRY =================
    "Chemistry": {

        "Unit 1": {
            "Atomic Structure": {
                "definition": "Structure of atom.",
                "topics": [
                    "Atom = Nucleus + Electrons",
                    "Protons, Neutrons",
                    "Bohr model"
                ]
            }
        },

        "Unit 2": {
            "Chemical Bonding": {
                "definition": "How atoms combine.",
                "topics": [
                    "Ionic bond",
                    "Covalent bond",
                    "Valency"
                ]
            }
        },

        "Unit 3": {
            "Corrosion": {
                "definition": "Gradual destruction of metals.",
                "topics": [
                    "Rusting of iron",
                    "Prevention methods",
                    "Galvanization"
                ]
            }
        },

        "Unit 4": {
            "Acids & Bases": {
                "definition": "Chemical properties of acids and bases.",
                "topics": [
                    "pH scale",
                    "Neutralization reaction",
                    "Strong vs Weak acids"
                ]
            }
        },

        "Unit 5": {
            "Revision & Viva": {
                "definition": "Important chemistry viva questions.",
                "topics": [
                    "Define ionic bond",
                    "What is corrosion?",
                    "pH value meaning"
                ]
            }
        }
    },

    # ================= ENGINEERING GRAPHICS =================
    "Engineering Graphics": {

        "Unit 1": {
            "Orthographic Projection": {
                "definition": "2D representation of 3D object.",
                "topics": [
                    "Front view",
                    "Top view",
                    "Side view"
                ]
            }
        },

        "Unit 2": {
            "Isometric View": {
                "definition": "3D representation method.",
                "topics": [
                    "Isometric axes",
                    "Drawing rules",
                    "Dimensioning"
                ]
            }
        },

        "Unit 3": {
            "Sectional Views": {
                "definition": "Cut view of objects.",
                "topics": [
                    "Full section",
                    "Half section",
                    "Hatching lines"
                ]
            }
        },

        "Unit 4": {
            "Dimensioning": {
                "definition": "Rules for showing measurements.",
                "topics": [
                    "Aligned method",
                    "Unidirectional method",
                    "Dimension standards"
                ]
            }
        },

        "Unit 5": {
            "Revision & Viva": {
                "definition": "Important engineering graphics viva questions.",
                "topics": [
                    "Define orthographic projection",
                    "What is isometric view?",
                    "Dimensioning rules"
                ]
            }
        }
    }

},

    "CO2": {

# ================= APPLIED MATHEMATICS =================
"Applied Mathematics": {

    "Unit 1": {
        "Probability": {
            "definition": "Probability measures how likely an event is to occur in an experiment.",
            "topics": [
                "Formula: P(A) = Favorable outcomes / Total outcomes",
                "0 ≤ P(A) ≤ 1",
                "Conditional Probability: P(A|B)",
                "Independent & Dependent events"
            ],
            "example": "If a dice is rolled, probability of getting even number = 3/6 = 1/2",
            "applications": "Used in AI, Machine Learning, Risk Analysis, Weather Forecasting"
        }
    },

    "Unit 2": {
        "Statistics": {
            "definition": "Statistics deals with collection, analysis and interpretation of data.",
            "topics": [
                "Mean = Sum / Total values",
                "Median (middle value)",
                "Mode (most frequent value)",
                "Standard Deviation (data spread)"
            ],
            "example": "For 2,4,6 → Mean = 4",
            "applications": "Used in Data Science, Quality Control, Research"
        }
    },

    "Unit 3": {
        "Differential Equations": {
            "definition": "Equation involving derivative of a function.",
            "topics": [
                "dy/dx + y = 0",
                "Order and Degree",
                "First order differential equations"
            ],
            "example": "Used in population growth model",
            "applications": "Used in circuits, motion problems, mechanical systems"
        }
    },

    "Unit 4": {
        "Laplace Transform": {
            "definition": "Technique to convert differential equations into algebraic equations.",
            "topics": [
                "L{f(t)}",
                "Inverse Laplace Transform",
                "Laplace of sin(at)"
            ],
            "example": "L{sin(at)} = a/(s² + a²)",
            "applications": "Used in signal processing and control systems"
        }
    },

    "Unit 5": {
        "Revision & Viva": {
            "definition": "Important exam and viva preparation questions.",
            "topics": [
                "Define Probability",
                "Formula of Standard Deviation",
                "Define Differential Equation",
                "Application of Laplace Transform"
            ]
        }
    }
},

# ================= BASIC ELECTRICAL ENGINEERING =================
"Basic Electrical Engineering": {

    "Unit 1": {
        "Basic Laws": {
            "definition": "Fundamental laws governing electrical circuits.",
            "topics": [
                "Ohm’s Law: V = IR",
                "Kirchhoff’s Current Law (KCL)",
                "Kirchhoff’s Voltage Law (KVL)"
            ],
            "example": "If R=5Ω and I=2A → V=10V",
            "applications": "Used in circuit design and analysis"
        }
    },

    "Unit 2": {
        "AC & DC Circuits": {
            "definition": "Types of electric current and their properties.",
            "topics": [
                "DC → Constant current (Battery)",
                "AC → Alternating current (House supply 230V, 50Hz)",
                "RMS Value"
            ],
            "importance": "AC is used for long distance transmission"
        }
    },

    "Unit 3": {
        "Electrical Machines": {
            "definition": "Machines converting electrical energy into mechanical energy.",
            "topics": [
                "Transformer (Step-up & Step-down)",
                "DC Motor",
                "Induction Motor"
            ],
            "applications": "Used in industries and household appliances"
        }
    },

    "Unit 4": {
        "Measuring Instruments": {
            "definition": "Devices used to measure electrical quantities.",
            "topics": [
                "Voltmeter (Voltage)",
                "Ammeter (Current)",
                "Wattmeter (Power)"
            ],
            "example": "Voltmeter connected in parallel"
        }
    },

    "Unit 5": {
        "Revision & Viva": {
            "definition": "Important electrical viva questions.",
            "topics": [
                "State Ohm’s Law",
                "Difference between AC & DC",
                "Working of Transformer",
                "Define KCL & KVL"
            ]
        }
    }
},

# ================= COMPUTER PROGRAMMING =================
"Computer Programming": {

    "Unit 1": {
        "Structure of C Program": {
            "definition": "Basic format of C language program.",
            "topics": [
                "#include<stdio.h>",
                "main() function",
                "printf() & scanf()"
            ],
            "example": "Program to print Hello World",
            "importance": "Foundation of programming logic"
        }
    },

    "Unit 2": {
        "Control Statements": {
            "definition": "Statements that control program flow.",
            "topics": [
                "if-else",
                "switch",
                "for loop",
                "while loop"
            ],
            "example": "Check whether number is even or odd"
        }
    },

    "Unit 3": {
        "Arrays & Strings": {
            "definition": "Collection of similar data elements.",
            "topics": [
                "1D & 2D Arrays",
                "String functions (strlen, strcpy)",
                "Passing array to function"
            ]
        }
    },

    "Unit 4": {
        "Pointers & Functions": {
            "definition": "Pointers store memory addresses.",
            "topics": [
                "Pointer declaration",
                "Call by value",
                "Call by reference",
                "Recursion"
            ],
            "importance": "Used in dynamic memory and data structures"
        }
    },

    "Unit 5": {
        "Revision & Viva": {
            "definition": "Important programming viva questions.",
            "topics": [
                "What is pointer?",
                "Difference between array & pointer",
                "Structure of C program",
                "What is recursion?"
            ]
        }
    }
},

# ================= ENVIRONMENTAL STUDIES =================
"Environmental Studies": {

    "Unit 1": {
        "Ecosystem": {
            "definition": "Interaction between living and non-living components.",
            "topics": [
                "Food Chain",
                "Food Web",
                "Energy Flow"
            ],
            "example": "Grass → Deer → Lion"
        }
    },

    "Unit 2": {
        "Greenhouse Effect": {
            "definition": "Trapping of heat by greenhouse gases.",
            "topics": [
                "CO2 impact",
                "Global warming",
                "Climate change"
            ]
        }
    },

    "Unit 3": {
        "Renewable Energy": {
            "definition": "Energy obtained from natural resources.",
            "topics": [
                "Solar Energy",
                "Wind Energy",
                "Hydropower"
            ],
            "importance": "Eco-friendly and sustainable"
        }
    },

    "Unit 4": {
        "Sustainable Development": {
            "definition": "Development without harming future generations.",
            "topics": [
                "3R Principle (Reduce, Reuse, Recycle)",
                "Conservation of resources"
            ]
        }
    },

    "Unit 5": {
        "Revision & Viva": {
            "definition": "Important environmental viva questions.",
            "topics": [
                "Define ecosystem",
                "Causes of global warming",
                "What is sustainable development?",
                "Types of renewable energy"
            ]
        }
    }
}

},

    "CO3": {

    # ================= OBJECT ORIENTED PROGRAMMING (OOP) =================
    "Object Oriented (OOP)": {

        "Unit 1": {
            "Introduction to OOP": {
                "definition": "Object Oriented Programming is a programming paradigm based on objects and classes used to design real-world applications.",
                "topics": [
                    "Procedure Oriented vs Object Oriented Programming",
                    "Features of OOP (Encapsulation, Abstraction, Inheritance, Polymorphism)",
                    "Class and Object concept",
                    "Real-world examples of objects",
                    "Advantages of OOP over procedural programming",
                    "Applications of OOP in software development"
                ]
            }
        },

        "Unit 2": {
            "Encapsulation & Abstraction": {
                "definition": "Encapsulation binds data and functions together. Abstraction hides internal implementation details.",
                "topics": [
                    "Access Specifiers (private, public, protected)",
                    "Data hiding concept",
                    "Getter and Setter methods",
                    "Abstraction using classes",
                    "Example programs in C++",
                    "Security advantages of encapsulation"
                ]
            }
        },

        "Unit 3": {
            "Inheritance & Polymorphism": {
                "definition": "Inheritance allows one class to acquire properties of another. Polymorphism allows one function to behave differently.",
                "topics": [
                    "Types of inheritance (Single, Multiple, Multilevel, Hierarchical)",
                    "Function Overloading",
                    "Operator Overloading",
                    "Method Overriding",
                    "Virtual Functions",
                    "Runtime vs Compile-time Polymorphism"
                ]
            }
        },

        "Unit 4": {
            "Constructors & Destructors": {
                "definition": "Special member functions used to initialize and destroy objects.",
                "topics": [
                    "Default Constructor",
                    "Parameterized Constructor",
                    "Copy Constructor",
                    "Destructor",
                    "Constructor Overloading",
                    "Role in memory management"
                ]
            }
        },

        "Unit 5": {
            "Exception Handling & File Handling": {
                "definition": "Handling runtime errors and managing files in OOP.",
                "topics": [
                    "try, catch, throw keywords",
                    "Types of exceptions",
                    "File streams (ifstream, ofstream)",
                    "Reading and writing files",
                    "Error handling techniques",
                    "Practical programs"
                ]
            }
        }
    },


    # ================= DATABASE MANAGEMENT SYSTEM =================
    "Database Management System": {

        "Unit 1": {
            "Introduction to DBMS": {
                "definition": "DBMS is software used to store, manage, and retrieve data efficiently.",
                "topics": [
                    "Data vs Information",
                    "Database system components",
                    "Advantages of DBMS",
                    "Types of databases",
                    "Three level architecture",
                    "Data models (Hierarchical, Network, Relational)"
                ]
            }
        },

        "Unit 2": {
            "ER Model & Relational Model": {
                "definition": "ER model represents data visually. Relational model stores data in tables.",
                "topics": [
                    "Entities, Attributes, Relationships",
                    "Primary Key and Foreign Key",
                    "Cardinality",
                    "Mapping ER to relational schema",
                    "Normalization basics",
                    "1NF, 2NF, 3NF"
                ]
            }
        },

        "Unit 3": {
            "SQL Language": {
                "definition": "Structured Query Language used to interact with databases.",
                "topics": [
                    "DDL commands (CREATE, ALTER, DROP)",
                    "DML commands (INSERT, UPDATE, DELETE)",
                    "SELECT queries",
                    "WHERE, GROUP BY, ORDER BY",
                    "Joins (Inner, Left, Right)",
                    "Subqueries"
                ]
            }
        },

        "Unit 4": {
            "Transactions & Concurrency": {
                "definition": "Managing multiple users accessing database simultaneously.",
                "topics": [
                    "ACID properties",
                    "Transaction states",
                    "Concurrency control",
                    "Deadlock",
                    "Locking mechanisms",
                    "Recovery techniques"
                ]
            }
        },

        "Unit 5": {
            "Indexing & Security": {
                "definition": "Improving performance and protecting data.",
                "topics": [
                    "Indexing methods",
                    "B+ Trees",
                    "Authorization and authentication",
                    "Data encryption",
                    "Backup and recovery",
                    "Database security threats"
                ]
            }
        }
    },


    # ================= DIGITAL TECHNIQUES =================
    "Digital Techniques": {

        "Unit 1": {
            "Number Systems": {
                "definition": "Different ways to represent numbers in digital systems.",
                "topics": [
                    "Binary, Octal, Decimal, Hexadecimal",
                    "Conversion methods",
                    "1's and 2's complement",
                    "Binary arithmetic",
                    "Signed and unsigned numbers"
                ]
            }
        },

        "Unit 2": {
            "Logic Gates": {
                "definition": "Basic building blocks of digital circuits.",
                "topics": [
                    "AND, OR, NOT gates",
                    "NAND, NOR gates",
                    "XOR, XNOR gates",
                    "Truth tables",
                    "Boolean expressions"
                ]
            }
        },

        "Unit 3": {
            "Boolean Algebra & K-Map": {
                "definition": "Mathematical analysis of logic circuits.",
                "topics": [
                    "Boolean laws",
                    "De Morgan’s theorem",
                    "Simplification of expressions",
                    "Karnaugh Map (2,3,4 variables)",
                    "Logic circuit design"
                ]
            }
        },

        "Unit 4": {
            "Combinational Circuits": {
                "definition": "Circuits whose output depends only on present inputs.",
                "topics": [
                    "Half Adder & Full Adder",
                    "Subtractor",
                    "Multiplexer & Demultiplexer",
                    "Encoder & Decoder",
                    "Comparators"
                ]
            }
        },

        "Unit 5": {
            "Sequential Circuits": {
                "definition": "Circuits whose output depends on past inputs.",
                "topics": [
                    "Flip Flops (SR, JK, D, T)",
                    "Registers",
                    "Counters",
                    "Clock signals",
                    "Memory elements"
                ]
            }
        }
    },


    # ================= DATA STRUCTURE USING C =================
    "(DSU) Data Structure Using C": {

        "Unit 1": {
            "Introduction to Data Structures": {
                "definition": "Data structure is a way of organizing data efficiently.",
                "topics": [
                    "Primitive & Non-Primitive types",
                    "Linear & Non-linear structures",
                    "Time and Space complexity",
                    "Algorithm analysis (Big-O notation)"
                ]
            }
        },

        "Unit 2": {
            "Arrays & Strings": {
                "definition": "Linear data structures storing elements sequentially.",
                "topics": [
                    "1D and 2D arrays",
                    "Operations (Insertion, Deletion)",
                    "Searching (Linear, Binary)",
                    "Sorting techniques (Bubble, Selection)",
                    "String handling functions"
                ]
            }
        },

        "Unit 3": {
            "Stack & Queue": {
                "definition": "Abstract data types used for structured data handling.",
                "topics": [
                    "Stack operations (Push, Pop)",
                    "Applications (Expression evaluation)",
                    "Queue operations (Enqueue, Dequeue)",
                    "Circular queue",
                    "Implementation using arrays"
                ]
            }
        },

        "Unit 4": {
            "Linked List": {
                "definition": "Dynamic data structure using pointers.",
                "topics": [
                    "Singly linked list",
                    "Doubly linked list",
                    "Circular linked list",
                    "Insertion and deletion operations",
                    "Advantages over arrays"
                ]
            }
        },

        "Unit 5": {
            "Trees & Graphs": {
                "definition": "Non-linear data structures.",
                "topics": [
                    "Binary tree",
                    "Tree traversals (Inorder, Preorder, Postorder)",
                    "Binary Search Tree",
                    "Graph representation",
                    "DFS and BFS algorithms"
                ]
            }
        }
    }

},

    "CO4": {

# ================= JAVA PROGRAMMING =================
"Java Programming": {

    "Unit 1": {
        "OOP Concepts": {
            "definition": "Object Oriented Programming is a programming paradigm based on objects.",
            "topics": [
                "Encapsulation → Wrapping data and methods together",
                "Abstraction → Hiding internal implementation",
                "Inheritance → Child class inherits parent properties",
                "Polymorphism → Same method, different behavior"
            ],
            "code_example": """
class Student {
    String name;
    void display() {
        System.out.println("Name: " + name);
    }
}
"""
        }
    },

    "Unit 2": {
        "Control Statements & Loops": {
            "definition": "Used for decision making and repetition.",
            "topics": [
                "if-else",
                "switch",
                "for loop",
                "while loop"
            ],
            "code_example": """
for(int i=1; i<=5; i++){
    System.out.println(i);
}
"""
        }
    },

    "Unit 3": {
        "Exception Handling": {
            "definition": "Handling runtime errors using try-catch.",
            "topics": [
                "try block",
                "catch block",
                "finally block",
                "throw keyword"
            ],
            "code_example": """
try{
    int a = 10/0;
}
catch(Exception e){
    System.out.println("Error occurred");
}
"""
        }
    },

    "Unit 4": {
        "Multithreading": {
            "definition": "Executing multiple tasks simultaneously.",
            "topics": [
                "Thread class",
                "Runnable interface",
                "Synchronization"
            ],
            "code_example": """
class MyThread extends Thread {
    public void run(){
        System.out.println("Thread Running");
    }
}
"""
        }
    },

    "Unit 5": {
        "File Handling": {
            "definition": "Reading and writing files in Java.",
            "topics": [
                "File class",
                "FileReader",
                "FileWriter"
            ],
            "code_example": """
FileWriter fw = new FileWriter("test.txt");
fw.write("Hello");
fw.close();
"""
        }
    }
},

# ================= PYTHON PROGRAMMING =================
"Python Programming": {

    "Unit 1": {
        "Basics": {
            "definition": "Introduction to Python language.",
            "topics": [
                "Variables",
                "Data Types",
                "Input & Output"
            ],
            "code_example": """
name = input("Enter name: ")
print("Hello", name)
"""
        }
    },

    "Unit 2": {
        "Functions": {
            "definition": "Reusable block of code.",
            "topics": [
                "def keyword",
                "Arguments",
                "Return statement"
            ],
            "code_example": """
def add(a,b):
    return a+b
print(add(5,3))
"""
        }
    },

    "Unit 3": {
        "OOP in Python": {
            "definition": "Object Oriented Programming in Python.",
            "topics": [
                "Class",
                "Object",
                "Constructor (__init__)",
                "Inheritance"
            ],
            "code_example": """
class Student:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(self.name)
"""
        }
    },

    "Unit 4": {
        "File Handling": {
            "definition": "Reading and writing files.",
            "topics": [
                "open()",
                "read()",
                "write()"
            ],
            "code_example": """
file = open("data.txt","w")
file.write("Hello")
file.close()
"""
        }
    },

    "Unit 5": {
        "Libraries": {
            "definition": "Pre-written modules.",
            "topics": [
                "math",
                "random",
                "flask basics"
            ],
            "code_example": """
import math
print(math.sqrt(16))
"""
        }
    }
},

# ================= DATA COMMUNICATION & COMPUTER NETWORKS =================
"Data Communication and Computer Networks": {

    "Unit 1": {
        "OSI Model": {
            "definition": "7-layer networking model.",
            "topics": [
                "Physical",
                "Data Link",
                "Network",
                "Transport",
                "Session",
                "Presentation",
                "Application"
            ]
        }
    },

    "Unit 2": {
        "TCP/IP": {
            "definition": "Internet communication protocol.",
            "topics": [
                "TCP → Reliable",
                "UDP → Fast",
                "IP Address",
                "Port Numbers"
            ]
        }
    },

    "Unit 3": {
        "Routing & Switching": {
            "definition": "Data forwarding techniques.",
            "topics": [
                "Routing algorithms",
                "Switching methods",
                "Subnetting"
            ]
        }
    },

    "Unit 4": {
        "DNS & HTTP": {
            "definition": "Web communication basics.",
            "topics": [
                "DNS resolves domain names",
                "HTTP vs HTTPS",
                "Firewall"
            ]
        }
    },

    "Unit 5": {
        "Network Security": {
            "definition": "Protecting network systems.",
            "topics": [
                "Cryptography",
                "Malware",
                "Firewalls"
            ]
        }
    }
},

# ================= MICROPROCESSORS =================
"Microprocessors": {

    "Unit 1": {
        "8086 Architecture": {
            "definition": "Architecture of 8086 processor.",
            "topics": [
                "EU (Execution Unit)",
                "BIU (Bus Interface Unit)",
                "Registers"
            ]
        }
    },

    "Unit 2": {
        "Registers": {
            "definition": "Temporary storage locations.",
            "topics": [
                "AX, BX, CX, DX",
                "SP, BP",
                "Segment Registers"
            ]
        }
    },

    "Unit 3": {
        "Instruction Cycle": {
            "definition": "Fetch → Decode → Execute cycle.",
            "topics": [
                "Machine cycle",
                "T-states",
                "Clock cycles"
            ]
        }
    },

    "Unit 4": {
        "Assembly Language": {
            "definition": "Low-level programming.",
            "topics": [
                "MOV instruction",
                "ADD instruction",
                "INT 21H"
            ],
            "code_example": """
MOV AX, 0005H
MOV BX, 0003H
ADD AX, BX
"""
        }
    },

    "Unit 5": {
        "Interrupts": {
            "definition": "Signals to CPU.",
            "topics": [
                "Hardware interrupts",
                "Software interrupts",
                "INT 21H services"
            ]
        }
    }

}

    },

    "CO5":{

# ================= WEB TECHNOLOGIES =================
"Web Technologies": {

    "Unit 1": {
        "HTML Fundamentals": {
            "definition": "HTML (HyperText Markup Language) is used to create web page structure.",
            "topics": [
                "HTML document structure",
                "Headings, Paragraphs",
                "Lists (ul, ol)",
                "Links and Images"
            ],
            "code_example": """
<!DOCTYPE html>
<html>
<head>
<title>My Page</title>
</head>
<body>
<h1>Hello World</h1>
<p>This is a paragraph.</p>
</body>
</html>
"""
        }
    },

    "Unit 2": {
        "CSS Styling": {
            "definition": "CSS (Cascading Style Sheets) is used to style web pages.",
            "topics": [
                "Inline, Internal, External CSS",
                "Colors and Background",
                "Box Model",
                "Flexbox basics"
            ],
            "code_example": """
body {
    background-color: lightblue;
}
h1 {
    color: darkblue;
}
"""
        }
    },

    "Unit 3": {
        "JavaScript Basics": {
            "definition": "JavaScript is used to add interactivity to web pages.",
            "topics": [
                "Variables",
                "Functions",
                "Events",
                "DOM Manipulation"
            ],
            "code_example": """
function greet() {
    alert("Welcome!");
}
"""
        }
    },

    "Unit 4": {
        "Backend Basics": {
            "definition": "Server-side programming to handle data and logic.",
            "topics": [
                "Client-Server Architecture",
                "HTTP Methods (GET, POST)",
                "Database connection",
                "Introduction to Flask"
            ],
            "code_example": """
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from server"

app.run()
"""
        }
    },

    "Unit 5": {
        "Forms & Validation": {
            "definition": "Collecting user data from web pages.",
            "topics": [
                "HTML Forms",
                "Input types",
                "Form validation",
                "Basic authentication"
            ],
            "code_example": """
<form>
  <input type="text" placeholder="Enter name">
  <button type="submit">Submit</button>
</form>
"""
        }
    }
},

# ================= SOFTWARE ENGINEERING =================
"Software Engineering": {

    "Unit 1": {
        "SDLC Models": {
            "definition": "Software Development Life Cycle models.",
            "topics": [
                "Waterfall Model",
                "Agile Model",
                "Spiral Model",
                "Incremental Model"
            ]
        }
    },

    "Unit 2": {
        "Requirement Analysis": {
            "definition": "Understanding system requirements.",
            "topics": [
                "Functional Requirements",
                "Non-Functional Requirements",
                "SRS Document",
                "Feasibility Study"
            ]
        }
    },

    "Unit 3": {
        "Design & UML": {
            "definition": "System design using diagrams.",
            "topics": [
                "Use Case Diagram",
                "Class Diagram",
                "Sequence Diagram",
                "ER Diagram"
            ]
        }
    },

    "Unit 4": {
        "Testing": {
            "definition": "Verifying and validating software.",
            "topics": [
                "Unit Testing",
                "Integration Testing",
                "System Testing",
                "Black Box & White Box Testing"
            ]
        }
    },

    "Unit 5": {
        "Project Management": {
            "definition": "Managing software projects effectively.",
            "topics": [
                "Gantt Chart",
                "Risk Analysis",
                "Cost Estimation",
                "Version Control (Git basics)"
            ]
        }
    }
},

# ================= COMPUTER SECURITY =================
"Computer Security": {

    "Unit 1": {
        "Cryptography": {
            "definition": "Securing data using encryption.",
            "topics": [
                "Symmetric Encryption",
                "Asymmetric Encryption",
                "AES & RSA",
                "Hash Functions"
            ]
        }
    },

    "Unit 2": {
        "Malware & Threats": {
            "definition": "Types of cyber attacks.",
            "topics": [
                "Virus",
                "Worm",
                "Trojan",
                "Phishing",
                "Ransomware"
            ]
        }
    },

    "Unit 3": {
        "Network Security": {
            "definition": "Securing networks from attacks.",
            "topics": [
                "Firewall",
                "IDS/IPS",
                "VPN",
                "SSL/TLS"
            ]
        }
    },

    "Unit 4": {
        "Authentication & Authorization": {
            "definition": "Controlling user access.",
            "topics": [
                "Passwords & OTP",
                "Two-Factor Authentication",
                "Role-based access control"
            ]
        }
    },

    "Unit 5": {
        "Cyber Laws & Ethics": {
            "definition": "Legal aspects of cybersecurity.",
            "topics": [
                "IT Act",
                "Data Privacy",
                "Ethical Hacking basics"
            ]
        }
    }
},

# ================= MOBILE APPLICATION DEVELOPMENT =================
"Mobile Application Development": {

    "Unit 1": {
        "Android Basics": {
            "definition": "Introduction to Android app development.",
            "topics": [
                "Android Studio",
                "Activity Lifecycle",
                "Project Structure"
            ]
        }
    },

    "Unit 2": {
        "Layouts & UI": {
            "definition": "Designing mobile user interfaces.",
            "topics": [
                "Linear Layout",
                "Constraint Layout",
                "Buttons & TextViews"
            ]
        }
    },

    "Unit 3": {
        "Intents & Navigation": {
            "definition": "Switching between activities.",
            "topics": [
                "Explicit Intent",
                "Implicit Intent",
                "Passing data between activities"
            ],
            "code_example": """
Intent intent = new Intent(this, SecondActivity.class);
startActivity(intent);
"""
        }
    },

    "Unit 4": {
        "Database & Storage": {
            "definition": "Storing data in mobile apps.",
            "topics": [
                "SQLite",
                "Shared Preferences",
                "Firebase basics"
            ]
        }
    },

    "Unit 5": {
        "App Deployment": {
            "definition": "Publishing mobile applications.",
            "topics": [
                "APK generation",
                "Play Store submission",
                "App permissions",
                "App security"
            ]
        }
    }

}
},

    "CO6": {

# ================= ARTIFICIAL INTELLIGENCE =================
"Artificial Intelligence": {

    "Unit 1": {
        "Introduction to AI": {
            "definition": "Artificial Intelligence is the simulation of human intelligence in machines.",
            "topics": [
                "History of AI",
                "Narrow AI vs General AI",
                "Applications (Chatbots, Self-driving cars, Healthcare AI)",
                "AI vs ML vs Deep Learning"
            ]
        }
    },

    "Unit 2": {
        "Machine Learning": {
            "definition": "Machine Learning allows systems to learn from data without explicit programming.",
            "topics": [
                "Supervised Learning",
                "Unsupervised Learning",
                "Regression",
                "Classification",
                "Training and Testing Data"
            ],
            "code_example": """
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
"""
        }
    },

    "Unit 3": {
        "Neural Networks": {
            "definition": "Neural Networks are computing systems inspired by human brain neurons.",
            "topics": [
                "Perceptron",
                "Activation Functions (ReLU, Sigmoid)",
                "Backpropagation",
                "Deep Learning basics"
            ],
            "code_example": """
import tensorflow as tf
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
])
"""
        }
    },

    "Unit 4": {
        "Natural Language Processing (NLP)": {
            "definition": "NLP enables machines to understand human language.",
            "topics": [
                "Tokenization",
                "Stop words removal",
                "Sentiment Analysis",
                "Chatbot design"
            ]
        }
    },

    "Unit 5": {
        "AI Ethics & Applications": {
            "definition": "Ethical use of Artificial Intelligence systems.",
            "topics": [
                "Bias in AI",
                "Data Privacy",
                "Responsible AI",
                "Real-world AI systems"
            ]
        }
    }
},

# ================= CLOUD COMPUTING =================
"Cloud Computing": {

    "Unit 1": {
        "Cloud Basics": {
            "definition": "Cloud computing delivers computing services over the internet.",
            "topics": [
                "On-premise vs Cloud",
                "Public, Private, Hybrid Cloud",
                "Advantages of Cloud"
            ]
        }
    },

    "Unit 2": {
        "Service Models": {
            "definition": "Cloud service delivery models.",
            "topics": [
                "IaaS (Infrastructure as a Service)",
                "PaaS (Platform as a Service)",
                "SaaS (Software as a Service)"
            ]
        }
    },

    "Unit 3": {
        "Virtualization": {
            "definition": "Technology to create virtual machines.",
            "topics": [
                "Hypervisor",
                "Virtual Machine (VM)",
                "Containers (Docker)",
                "Resource Allocation"
            ]
        }
    },

    "Unit 4": {
        "Cloud Security": {
            "definition": "Security practices in cloud environment.",
            "topics": [
                "Data Encryption",
                "Access Control",
                "Multi-factor Authentication",
                "Cloud Firewalls"
            ]
        }
    },

    "Unit 5": {
        "Cloud Platforms": {
            "definition": "Major cloud service providers.",
            "topics": [
                "AWS basics",
                "Microsoft Azure",
                "Google Cloud Platform",
                "Deployment models"
            ]
        }
    }
},

# ================= INTERNET OF THINGS =================
"Internet of Things": {

    "Unit 1": {
        "IoT Introduction": {
            "definition": "IoT connects physical devices to the internet for data exchange.",
            "topics": [
                "IoT Architecture",
                "Sensors and Actuators",
                "Embedded Systems",
                "Smart Devices"
            ]
        }
    },

    "Unit 2": {
        "Microcontrollers": {
            "definition": "Microcontrollers control IoT devices.",
            "topics": [
                "Arduino",
                "Raspberry Pi",
                "GPIO Pins",
                "Basic interfacing"
            ],
            "code_example": """
void setup() {
  pinMode(13, OUTPUT);
}
void loop() {
  digitalWrite(13, HIGH);
}
"""
        }
    },

    "Unit 3": {
        "IoT Communication": {
            "definition": "Communication protocols used in IoT.",
            "topics": [
                "MQTT",
                "HTTP",
                "WiFi",
                "Bluetooth"
            ]
        }
    },

    "Unit 4": {
        "IoT Applications": {
            "definition": "Real-world IoT implementations.",
            "topics": [
                "Smart Home",
                "Smart Agriculture",
                "Health Monitoring Systems",
                "Industrial IoT"
            ]
        }
    },

    "Unit 5": {
        "IoT Security": {
            "definition": "Security in IoT systems.",
            "topics": [
                "Device authentication",
                "Data encryption",
                "Secure firmware updates"
            ]
        }
    }
},

# ================= PROJECT MANAGEMENT =================
"Project Management": {

    "Unit 1": {
        "Project Planning": {
            "definition": "Planning and organizing project tasks.",
            "topics": [
                "Project lifecycle",
                "Scope definition",
                "Work Breakdown Structure (WBS)"
            ]
        }
    },

    "Unit 2": {
        "Scheduling": {
            "definition": "Managing project timeline.",
            "topics": [
                "Gantt Chart",
                "PERT Chart",
                "Critical Path Method"
            ]
        }
    },

    "Unit 3": {
        "Risk Management": {
            "definition": "Identifying and handling project risks.",
            "topics": [
                "Risk identification",
                "Risk mitigation",
                "Contingency planning"
            ]
        }
    },

    "Unit 4": {
        "Agile & Scrum": {
            "definition": "Modern project management methodologies.",
            "topics": [
                "Scrum roles (Product Owner, Scrum Master)",
                "Sprints",
                "Daily Standup",
                "Kanban"
            ]
        }
    },

    "Unit 5": {
        "Project Evaluation": {
            "definition": "Monitoring and closing project.",
            "topics": [
                "Performance metrics",
                "Quality control",
                "Project documentation",
                "Post-project review"
            ]
        }
    }

}

        },
}

@app.route("/", methods=["GET", "POST"])
def home():
    selected_co = None
    selected_subject = None
    selected_unit = None
    unit_data = None

    if request.method == "POST":
        selected_co = request.form.get("co")
        selected_subject = request.form.get("subject")
        selected_unit = request.form.get("unit")

        if selected_co and selected_subject and selected_unit:
            unit_data = None

            if selected_co in course_structure:
                if selected_subject in course_structure[selected_co]:
                    if selected_unit in course_structure[selected_co][selected_subject]:
                        unit_data = course_structure[selected_co][selected_subject][selected_unit]
    return render_template(
        "index.html",
        data=course_structure,
        selected_co=selected_co,
        selected_subject=selected_subject,
        selected_unit=selected_unit,
        unit_data=unit_data
    )
if __name__ == "__main__":
    app.run(debug=True)
