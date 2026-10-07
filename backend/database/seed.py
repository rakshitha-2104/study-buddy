"""Starter question bank: 6 subjects x 4 units x 3 levels (easy, medium, hard).

Each tuple is (question, "opt A|opt B|opt C|opt D", index_of_correct_option).
Unit themes follow the usual structure of these courses. Please have a faculty
member map them to the exact Bengaluru City University syllabus and add more
questions per unit - the app picks up new rows automatically.
"""
import json

SUBJECTS = {
    "cn": "Computer Networks", "dbms": "DBMS", "python": "Python",
    "java": "Java", "c": "C Programming", "cyber": "Cyber Security",
}

# QB[subject] = [unit1, unit2, unit3, unit4]; each unit = [easy, medium, hard]
QB = {
 "cn": [
  [("Which device connects different networks and forwards packets between them?", "Router|Hub|Repeater|Switch", 0),
   ("How many layers are in the OSI model?", "5|7|4|6", 1),
   ("Which topology gives the most fault tolerance because every node links to every other?", "Bus|Star|Mesh|Ring", 2)],
  [("A MAC address is how many bits long?", "32|48|64|128", 1),
   ("Which method does classic Ethernet use to handle collisions?", "CSMA/CD|TDMA|Token passing|Polling", 0),
   ("Which error-detection method is based on polynomial division?", "Parity bit|Checksum|CRC|Hamming code", 2)],
  [("An IPv4 address has how many bits?", "16|32|64|128", 1),
   ("Which protocol maps an IP address to a MAC address?", "DNS|DHCP|ARP|ICMP", 2),
   ("How many usable host addresses are in a /26 IPv4 network?", "64|62|30|126", 1)],
  [("Which protocol is used to load web pages securely?", "FTP|HTTPS|SMTP|Telnet", 1),
   ("Which transport protocol is connection-oriented and reliable?", "UDP|IP|TCP|ICMP", 2),
   ("Which TCP mechanism stops a fast sender from overwhelming a slow receiver?", "Flow control|Routing|Subnetting|Switching", 0)],
 ],
 "dbms": [
  [("What does DBMS stand for?", "Database Management System|Digital Base Mapping System|Data Binary Management Software|Direct Backup Management System", 0),
   ("In an ER diagram, a rectangle represents a(n)?", "Attribute|Entity|Relationship|Key", 1),
   ("Changing storage structure without changing the logical schema is called?", "Logical independence|Physical independence|Schema binding|View independence", 1)],
  [("Which SQL command retrieves data?", "INSERT|SELECT|UPDATE|DROP", 1),
   ("Which key uniquely identifies each row in a table?", "Foreign key|Primary key|Composite view|Index key", 1),
   ("Which join returns all rows of the left table even without a match on the right?", "INNER JOIN|LEFT JOIN|CROSS JOIN|SELF JOIN", 1)],
  [("Normalization is used to?", "Reduce redundancy|Increase redundancy|Delete tables|Encrypt data", 0),
   ("A table is in 2NF when it is in 1NF and has no?", "Transitive dependency|Partial dependency|Multivalued attribute|Foreign key", 1),
   ("BCNF requires that for every dependency X -> Y, X is a?", "Non-key attribute|Superkey|Foreign key|Prime attribute only", 1)],
  [("Which letter of ACID means 'all or nothing'?", "A|C|I|D", 0),
   ("Which command permanently saves a transaction?", "ROLLBACK|COMMIT|SAVEPOINT|REVOKE", 1),
   ("Reading data written by another uncommitted transaction is called a?", "Lost update|Dirty read|Phantom row|Deadlock", 1)],
 ],
 "python": [
  [("Which function prints output in Python?", "echo()|print()|write()|show()", 1),
   ("What is the type of 3.14?", "int|str|float|bool", 2),
   ("What is the output of 7 // 2 ?", "3.5|3|4|2", 1)],
  [("Which keyword defines a function?", "func|define|def|function", 2),
   ("How many times does the loop 'for i in range(3)' run?", "2|3|4|1", 1),
   ("What does a function return if it has no return statement?", "0|None|False|Error", 1)],
  [("Which brackets create a list?", "()|{}|[]|<>", 2),
   ("Which of these is immutable?", "list|dict|set|tuple", 3),
   ("What is len({1, 2, 2, 3}) ?", "4|3|2|1", 1)],
  [("Which function opens a file?", "open()|file()|read()|load()", 0),
   ("Which keyword creates a class?", "object|class|def|type", 1),
   ("What is the constructor method in a Python class called?", "__init__|__start__|constructor|__make__", 0)],
 ],
 "java": [
  [("Java source files have which extension?", ".class|.java|.jar|.js", 1),
   ("Which is NOT a primitive type in Java?", "int|boolean|String|char", 2),
   ("Which component executes Java bytecode?", "JDK|JVM|javac|IDE", 1)],
  [("Which keyword is used to inherit a class?", "implements|extends|inherits|import", 1),
   ("Which keyword refers to the parent class?", "this|super|parent|base", 1),
   ("Can a Java class extend more than one class?", "Yes|No|Only abstract classes|Only final classes", 1)],
  [("Which block always runs after try-catch?", "finally|else|default|end", 0),
   ("Which keyword manually throws an exception?", "throws|throw|catch|raise", 1),
   ("Which of these is a checked exception?", "NullPointerException|IOException|ArithmeticException|ClassCastException", 1)],
  [("Which class can you extend to create a thread?", "Thread|Process|Task|Timer", 0),
   ("Which collection does not allow duplicates?", "ArrayList|Set|LinkedList|Vector", 1),
   ("Which keyword lets only one thread run a method at a time?", "volatile|synchronized|static|final", 1)],
 ],
 "c": [
  [("Which header file is needed for printf?", "stdlib.h|stdio.h|string.h|math.h", 1),
   ("Size of int on most modern systems (in bytes)?", "1|2|4|8", 2),
   ("What does printf(\"%d\", 5/2); print?", "2.5|2|3|0", 1)],
  [("Which loop runs at least once?", "for|while|do-while|if", 2),
   ("Array indexing in C starts from?", "1|0|-1|2", 1),
   ("For int a[5]; the valid indexes are?", "1 to 5|0 to 4|0 to 5|1 to 4", 1)],
  [("Which operator gives the address of a variable?", "*|&|#|@", 1),
   ("What does a pointer store?", "A value|A memory address|A function name|A file", 1),
   ("How do we pass an argument by reference in C?", "Using pointers|Using references|Using macros|Using arrays only", 0)],
  [("Which keyword defines a structure?", "struct|union|record|class", 0),
   ("Which function opens a file in C?", "open()|fopen()|fread()|fstart()", 1),
   ("Which function frees dynamically allocated memory?", "delete|free|remove|release", 1)],
 ],
 "cyber": [
  [("In the CIA triad, what does 'C' stand for?", "Control|Confidentiality|Capacity|Copy", 1),
   ("Which attack tricks users into giving credentials through fake emails?", "Phishing|DDoS|Buffer overflow|Brute force", 0),
   ("Flooding a server so users cannot reach it attacks which property?", "Confidentiality|Integrity|Availability|Authenticity", 2)],
  [("Encryption converts plain text into?", "Cipher text|Source code|A log file|A binary patch", 0),
   ("Which of these is a symmetric algorithm?", "RSA|AES|ECC|DSA", 1),
   ("A digital signature is created using the sender's?", "Public key|Private key|Session ID|IP address", 1)],
  [("What does a firewall do?", "Filters network traffic|Speeds up internet|Stores files|Compresses data", 0),
   ("What does VPN stand for?", "Virtual Private Network|Verified Public Node|Virtual Protected Net|Very Private Network", 0),
   ("Which system actively blocks attacks it detects?", "IDS|IPS|DNS|NAT", 1)],
  [("India's main law on cyber crime and e-commerce is the?", "IT Act, 2000|Cyber Act, 1990|Data Act, 2010|Net Act, 2005", 0),
   ("Pretending to be someone else online to cheat is called?", "Identity theft|Cloud sync|Port scanning|Caching", 0),
   ("Which Indian law (2023) deals with personal data protection?", "DPDP Act, 2023|Companies Act|Indian Telegraph Act|Copyright Act", 0)],
 ],
}

def seed(db):
    """Insert subjects and questions once (skips if already seeded)."""
    if db.execute("SELECT COUNT(*) FROM subjects").fetchone()[0]:
        return
    for sid, name in SUBJECTS.items():
        db.execute("INSERT INTO subjects VALUES (?, ?)", (sid, name))
        for unit_no, trio in enumerate(QB[sid], start=1):
            for level, (text, opts, ans) in zip(("easy", "medium", "hard"), trio):
                db.execute(
                    "INSERT INTO questions (subject_id, unit, level, text, options, answer) "
                    "VALUES (?,?,?,?,?,?)",
                    (sid, unit_no, level, text, json.dumps(opts.split("|")), ans))
    db.commit()