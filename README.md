# Password checker
This is a simple project that checks your password to give it a **rate** (weak-strong).

The program also verify a huge library of **common-passwords** (109,843 precisely) to make sure you're not using a password that can be hacked. Why? There's a method of hacking called **dictionary attack** that try to break into systems by automatically testing a list of common words, phrases, and leaked passwords. This project aim to prevent it from happening, by flagging it when you type the password and warning you

#### Hash
Hash is function that we use to transfer data into an output, this output is called **hash values**, **hash codes**, **digests**. They output a fixed-length string of characters. There's two hash types, **cryptographic** and **non-cryptographic**. A **one way hash** cannot practically be reversed to recover the original input. That's why websites store hash instead of passwords, this way it's safer, even if the attacker get the hash, there's almost no use on it. What they can do is hash common passwords and check whether any of them match the stolen hash

<br>

## To Do
- hashlib function

<br>

#### Sources used to resolve the project
- https://www.geeksforgeeks.org/python/string-punctuation-in-python/
- https://www.w3schools.com/python/python_file_open.asp
- https://www.geeksforgeeks.org/python/reading-writing-text-files-python/
- https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
- https://docs.python.org/3/tutorial/inputoutput.html
- https://www.geeksforgeeks.org/python/string-punctuation-in-python/
- https://docs.python.org/3/library/string.html
