import os
import filecmp
import difflib

labName = input("Place it in the same folder with your lab code.\n"
                "Also, put all the test cases, including input and output in the same folder \"testcase\"\n"
                "Please specify the lab/PA (e.g. lab3/pa1).\n")

print("Compiling the code into executable!")

if os.system('g++ -std=c++11 ' + labName + '.cpp' + ' -o ' + labName) != 0:
    print("Compiler reports an error. Please check your code!")
    print("=================================================================")
    exit(0)

numTestcase = int(len(os.listdir('./testcase')) / 2)

inputFileName = input("Please specify the format of the input file, use \"*\" to replace case number.\n"
                      "For example, if one of your input file is input01.txt, enter input0*\n")

outputFileName = input("Please specify the format of the output file, use \"*\" to replace case number.\n"
                       "For example, if one of your output file is output01.txt, enter output0*\n")

print("The program will now go over " + str(numTestcase) + " test cases provided.")

keepFile = input("After testing, do you want to keep the output of your program? [Y/n] ")

sumCorrect = 0

for currentLabCase in range(numTestcase):

    currentInputFileName = inputFileName.replace('*', str(currentLabCase + 1)) + ".txt"

    currentOutputFileName = outputFileName.replace('*', str(currentLabCase + 1)) + ".txt"

    if os.system('./' + labName + '< testcase/' + currentInputFileName + ' > myOutput' + str(
            currentLabCase + 1) + ".txt") != 0:
        print("Error occurred! Please double check whether file names are correct!")
        exit(0)

    print("\n=================================================================\n")
    print("Testing case " + str(currentLabCase + 1) + "\n")

    with open("./testcase/" + currentOutputFileName) as correctOutput, open(
            "myOutput" + str(currentLabCase + 1) + ".txt") as myOutput:
        differ = difflib.Differ()

        for line in differ.compare(myOutput.readlines(), correctOutput.readlines()):
            print(line)

        correct = filecmp.cmp("./testcase/" + currentOutputFileName,
                              "myOutput" + str(currentLabCase + 1) + ".txt")

        if correct:
            print("Test case passed!")
            sumCorrect += 1
        else:
            print("Incorrect output!")

        if keepFile == "n" or keepFile == "N":
            os.remove("myOutput" + str(currentLabCase + 1) + ".txt")

print("\n=================================================================\n")

if sumCorrect == int(numTestcase):
    print(str(numTestcase) + " test cases tested!\n")
    print("All output are correct!")
else:
    print(str(numTestcase) + " test cases tested!\n")
    print(str(sumCorrect) + " of " + str(numTestcase) + " test cases are correct!\n")
