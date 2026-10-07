"""Built-in tutor knowledge base (English). No API key needed.

Each entry: (subject, unit, [keywords], explanation, code_example)
- keywords: words/phrases the student's question may contain
- explanation: translated into the student's language when shown
- code_example: shown exactly as written (code is never translated)
To teach the bot something new, just add another tuple.
"""
KB = [
 # ---------------- Computer Networks ----------------
 ("cn", 1, ["osi", "layers", "layer model"],
  "The OSI model has 7 layers: Physical, Data Link, Network, Transport, Session, Presentation and Application. Each layer does one job and talks to the layer above and below it.", ""),
 ("cn", 1, ["topology", "star", "mesh", "bus", "ring"],
  "Topology is the shape of a network. Star: all devices connect to one central switch. Bus: one shared cable. Ring: devices form a circle. Mesh: every device links to many others, so it is very reliable but costly.", ""),
 ("cn", 2, ["mac", "ethernet", "csma", "collision"],
  "A MAC address is the 48-bit hardware address of a network card. Classic Ethernet used CSMA/CD: listen before sending, and if two devices send together (a collision), wait a random time and try again.", ""),
 ("cn", 3, ["ip address", "ipv4", "subnet", "subnetting"],
  "An IPv4 address has 32 bits. Subnetting splits a big network into smaller ones. A /24 network has 256 addresses, of which 254 can be given to devices.", "192.168.1.10   (an IPv4 address)\n255.255.255.0   (subnet mask for /24)"),
 ("cn", 3, ["arp", "router", "routing"],
  "ARP finds the MAC address that belongs to a known IP address. A router forwards packets between different networks by looking at its routing table.", ""),
 ("cn", 4, ["tcp", "udp", "transport"],
  "TCP is reliable: it sets up a connection and resends lost data (used for web and email). UDP is fast but does not guarantee delivery (used for video calls and games).", ""),
 ("cn", 4, ["http", "https", "dns"],
  "HTTP is the protocol for web pages and HTTPS adds encryption. DNS turns a name like google.com into an IP address.", ""),

 # ---------------- DBMS ----------------
 ("dbms", 1, ["dbms", "database"],
  "A DBMS is software that stores, organises and protects data, for example MySQL or Oracle. It reduces repeated data and lets many users share data safely.", ""),
 ("dbms", 1, ["er diagram", "entity", "attribute", "relationship"],
  "An ER diagram shows data as a picture. Entity = a thing (Student). Attribute = its property (Name). Relationship = a link between entities (Student enrolls in Course).", ""),
 ("dbms", 2, ["sql", "select", "query", "join"],
  "SQL is the language used to talk to a database. SELECT reads data. A JOIN combines rows of two tables using a common column.", "SELECT name FROM student WHERE marks > 60;"),
 ("dbms", 2, ["primary key", "foreign key", "key"],
  "A primary key uniquely identifies each row (like a student ID). A foreign key is a column that points to the primary key of another table.", "CREATE TABLE marks (\n  id INT PRIMARY KEY,\n  student_id INT REFERENCES student(id)\n);"),
 ("dbms", 3, ["normalization", "normalisation", "1nf", "2nf", "3nf", "bcnf"],
  "Normalization organises tables to remove repeated data. 1NF: one value in each cell. 2NF: no partial dependency. 3NF: no transitive dependency. BCNF: every determinant is a superkey.", ""),
 ("dbms", 4, ["transaction", "acid", "commit", "rollback"],
  "A transaction is a group of steps treated as one. ACID means Atomicity (all or nothing), Consistency, Isolation and Durability. COMMIT saves the work and ROLLBACK undoes it.", "BEGIN;\nUPDATE account SET bal = bal - 500 WHERE id = 1;\nCOMMIT;"),

 # ---------------- Python ----------------
 ("python", 1, ["variable", "datatype", "data type", "int", "float", "string"],
  "A variable stores a value. Common types: int (whole numbers), float (decimals), str (text) and bool (True or False).", "age = 18\nprice = 99.5\nname = 'Asha'\npassed = True"),
 ("python", 1, ["print", "input", "operator"],
  "print() shows output and input() reads what the user types. Use // for whole-number division and % for the remainder.", "print('Hello')\nx = input()\nprint(7 // 2)   # 3\nprint(7 % 2)    # 1"),
 ("python", 2, ["if", "loop", "for", "while"],
  "if/else lets the program decide. A for loop repeats a fixed number of times and a while loop repeats while a condition is true.", "for i in range(3):\n    print(i)   # 0 1 2"),
 ("python", 2, ["function", "def", "return"],
  "A function is a reusable block of code. You call it by its name and give it values.", "def add(a, b):\n    return a + b\n\nprint(add(2, 3))   # 5"),
 ("python", 3, ["list", "tuple", "dictionary", "dict", "set"],
  "A list can be changed, a tuple cannot, a set keeps no duplicates, and a dictionary stores key-value pairs.", "[1, 2, 3]            # list\n(1, 2, 3)            # tuple\n{1, 2, 3}            # set\n{'name': 'Asha'}     # dictionary"),
 ("python", 4, ["file", "open", "read", "write"],
  "Use open() to work with a file. The 'with' form closes the file for you automatically.", "with open('a.txt') as f:\n    data = f.read()"),
 ("python", 4, ["class", "object", "oop", "constructor", "__init__"],
  "A class is a blueprint and an object is made from it. __init__ is the constructor that runs when an object is created.", "class Student:\n    def __init__(self, name):\n        self.name = name\n\ns = Student('Asha')"),

 # ---------------- Java ----------------
 ("java", 1, ["jvm", "jdk", "jre", "bytecode"],
  "Java code is compiled into bytecode, and the JVM runs that bytecode on any computer. JDK has the tools to write and compile Java, and JRE has what is needed to run it.", ""),
 ("java", 1, ["datatype", "data type", "primitive", "variable"],
  "Java has 8 primitive types such as int, double, char and boolean. String is not primitive; it is a class.", 'int age = 18;\ndouble price = 99.5;\nString name = "Asha";'),
 ("java", 2, ["inheritance", "extends", "super"],
  "Inheritance lets a child class reuse a parent class. Use extends to inherit, and super to refer to the parent class.", "class Dog extends Animal {\n  void bark() { }\n}"),
 ("java", 2, ["interface", "abstract", "polymorphism"],
  "An interface lists methods that a class must write. Polymorphism means one method name can behave differently for different objects.", "interface Shape {\n  double area();\n}"),
 ("java", 3, ["exception", "try", "catch", "finally", "throw"],
  "Exceptions handle errors. Put risky code in try, handle the error in catch, and finally always runs. throw creates an exception and throws declares it.", 'try {\n  int x = 10 / 0;\n} catch (ArithmeticException e) {\n  System.out.println("Error");\n} finally {\n  System.out.println("Done");\n}'),
 ("java", 3, ["package", "import"],
  "A package groups related classes. Use import to use classes from another package.", "import java.util.*;"),
 ("java", 4, ["thread", "multithreading", "synchronized"],
  "A thread runs a task at the same time as other tasks. Create one by extending Thread or implementing Runnable. synchronized lets only one thread use a method at a time.", 'class T extends Thread {\n  public void run() {\n    System.out.println("Hi");\n  }\n}'),
 ("java", 4, ["collection", "arraylist", "hashmap"],
  "Collections store groups of objects. ArrayList is a resizable list, HashSet keeps no duplicates and HashMap stores key-value pairs.", 'ArrayList<String> list = new ArrayList<>();\nlist.add("Java");'),

 # ---------------- C Programming ----------------
 ("c", 1, ["printf", "scanf", "stdio", "header"],
  "printf() prints output and scanf() reads input. Both need the stdio.h header file.", '#include <stdio.h>\nint main() {\n  printf("Hello");\n  return 0;\n}'),
 ("c", 1, ["datatype", "data type", "int", "float", "char"],
  "Basic types: int for whole numbers, float or double for decimals, and char for one character. An int is usually 4 bytes.", "int a = 5;\nfloat b = 2.5;\nchar c = 'A';"),
 ("c", 2, ["loop", "for", "while", "do while"],
  "for repeats a known number of times, while repeats while a condition is true, and do-while always runs at least once.", 'for (int i = 0; i < 3; i++) {\n  printf("%d", i);\n}'),
 ("c", 2, ["array"],
  "An array stores many values of the same type. Indexes start at 0, so for 5 elements the valid indexes are 0 to 4.", "int a[5] = {1, 2, 3, 4, 5};"),
 ("c", 3, ["pointer"],
  "A pointer stores the memory address of another variable. & gives the address and * gives the value at an address.", 'int x = 10;\nint *p = &x;\nprintf("%d", *p);   // 10'),
 ("c", 3, ["function", "recursion", "call by value"],
  "A function is a reusable block of code. C passes arguments by value; to change the original variable, pass a pointer. Recursion means a function calls itself.", "int add(int a, int b) {\n  return a + b;\n}"),
 ("c", 4, ["structure", "struct", "union"],
  "A struct groups different types of data under one name.", "struct Student {\n  int id;\n  char name[20];\n};"),
 ("c", 4, ["file", "fopen", "fclose", "malloc", "free"],
  "fopen() opens a file and fclose() closes it. malloc() gets memory while the program runs, and free() gives it back.", 'FILE *f = fopen("a.txt", "r");\nint *p = malloc(5 * sizeof(int));\nfree(p);\nfclose(f);'),

 # ---------------- Cyber Security ----------------
 ("cyber", 1, ["cia", "confidentiality", "integrity", "availability"],
  "CIA triad: Confidentiality means only the right people see the data. Integrity means data is not changed secretly. Availability means data is there when needed.", ""),
 ("cyber", 1, ["phishing", "malware", "virus", "ransomware", "attack"],
  "Phishing uses fake emails or websites to steal passwords. Malware is harmful software such as viruses and ransomware. Never click unknown links.", ""),
 ("cyber", 2, ["encryption", "cryptography", "aes", "rsa", "symmetric"],
  "Encryption turns readable text into cipher text. Symmetric encryption (AES) uses one shared key. Asymmetric encryption (RSA) uses a public key and a private key.", ""),
 ("cyber", 2, ["hash", "digital signature", "signature"],
  "A hash is a fixed-size fingerprint of data, for example SHA-256. A digital signature proves who sent a message: it is made with the sender's private key and checked with the public key.", ""),
 ("cyber", 3, ["firewall", "vpn", "ids", "ips"],
  "A firewall filters network traffic. A VPN makes a private, encrypted tunnel over the internet. An IDS detects attacks and an IPS also blocks them.", ""),
 ("cyber", 4, ["it act", "cyber law", "dpdp", "law"],
  "India's IT Act, 2000 covers cyber crime and electronic records. The Digital Personal Data Protection (DPDP) Act, 2023 is about protecting personal data.", ""),
]