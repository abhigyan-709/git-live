"""
Here we will learn about how the chmod codes are decided

r - read - 4
w - write - 2
x - executable - 1


chmod 755 <file-name> / <folder>

r - 4, r is represented by value of 4
w - 2, w is represented by value of 2
x - 1, x is represented by value of 1

owner - 4 + 2 + 1 = 7 - rwx
group - 4 + 0 + 1 = 5 - r-x
other - 4 + 0 + 1 = 5 - r-x

chmod 755 hello.py

chmod 400

owner - 1st - 4
group - 2nd - 0
other - 3rd - 0

chmod 400 <file-name>/<folder>

"""