# import os.path
import os
from sys import platform
import filecmp
import difflib

if platform == "win32":  # True if system is Windows
    system = 1
else:
    system = 0

labName = input("Place it in the same folder with your lab code.\nAlso, put all the test cases, including input and output in the same folder \"testcase\"\nPlease specify the lab (e.g. lab3).\n")

print("Compiling the code into executable!")

try:
    if os.system('g++ -std=c++11 ' + labName + '.cpp' + ' -o ' + labName) != 0:
        raise Exception()
except Exception:
    print("Compiler reports an error. Please check your code!")

numTestcase = int(len(os.listdir('./testcase')) / 2)

print("The program will now go over " + str(numTestcase) + " test cases provided")

keepFile = "Y"

keepFile = input("After testing, do you want to keep the output of your program? [Y/n] ")

sumCorrect = 0

for currentLabCase in range(numTestcase):
    if system:
        if os.system('Get-Content testcase/input' + str(currentLabCase+1) + '.txt | ./' + labName + '> myOutput' + str(currentLabCase+1) + '.txt') != 0:
            raise Exception()
    else:
        if os.system('./' + labName + '< testcase/input' + str(currentLabCase+1) + '.txt > myOutput' + str(currentLabCase+1) + ".txt") != 0:
            raise Exception()

    print("--------------------")
    print("Testing case " + str(currentLabCase + 1))

    with open("./testcase/output" + str(currentLabCase + 1) + ".txt") as correctOutput, open("myOutput" + str(currentLabCase + 1) + ".txt") as myOutput:
        differ = difflib.Differ()

        for line in differ.compare(myOutput.readlines(), correctOutput.readlines()):
            print(line)

        correct = filecmp.cmp(("./testcase/output" + str(currentLabCase + 1) + ".txt"), ("myOutput" + str(currentLabCase + 1) + ".txt"), shallow=False)

        if correct:
            print("Test case passed!")
            sumCorrect += 1
        else:
            print("Incorrect output!")

        if keepFile == "n" or keepFile == "N":
            os.remove("myOutput" + str(currentLabCase+1) + ".txt")

print("--------------------\n")

if sumCorrect == int(numTestcase):
    print("All output are correct!")
else:
    print("Not all output are correct!")
