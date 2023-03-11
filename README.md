# COMP2011-Check-Code

This single python file is used to check the test cases provided by the lab and PA in macOS and Linux. It is used to replace zinc auto grader function as zinc no longer provide Standard I/O Test anymore.

To use the checker, put `codeChecker.py` with your lab source code in the same folder. Create a folder `testcase`. Put all the input and output inside `testcase`.

Run the following in your terminal:

```py
python3 codeChecker.py
```

and follow the instructions.

If you see symbols `+` or `-` in front of a line, that means your output is different from the output they provided. Double check your code.

`+` is the line that is in output they provided, while `-` is the line that is in your output.

No symbols will be shown if your output matches exactly with the output they provided.

P.S. I haven't checked it on macOS.
