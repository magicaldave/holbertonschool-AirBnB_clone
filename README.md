This repository contains project files for the Holberton AirBnB clone project!
At a high level, the point of this project is to generate a mostly-functional AirBnB clone.

This project took place across four months, with four parts each.

## Part 1 - Command Interpreter
The first week involves building a Python console to interface with the higher-level aspects of the program. It uses a JSON file structure which will be replaced later by an actual SQL database.
### Here are some example usages:
Interactive Mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-interactive Mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
