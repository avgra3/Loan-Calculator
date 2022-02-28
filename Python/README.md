# Python Car Loan Calculator

## How to use

To use this program, in the same directory or entering the path to the [main.py](main.py) file, run the following in your command line:

```bat:
python [PATH\TO\FILE\]main.py 
```

You will be prompted to enter the payment amount, the estimated term of te loan, the APR, the amount which you expect to pay each month and your down payment.

Based on those inputs, you the program will calculate how long it will take for your to pay off your loan. If at the end of the term the amount remaining is greater than zero, you will see how much is remaining on your loan, how much you have paid on your loan and a message suggesting paying more towards the loan per month.

## Testing

There is a [Unit Test file](test_main.py) included. The test usses the [unittest](https://docs.python.org/3/library/unittest.html) module which is included in the base install of Python. To run the test script from your command line, run the following:

```bat:
python [PATH\TO\FILE\]test_main.py 
```

You should find that one test is run with no failures. The test script checks the following:

- If any of the entered values are string values, a Value Error is raised?
- If the combination of values is entered and we expect the remaining principal is zero, will the amount remaining be equal to zero?
- If the combination of values entered and we don't expect to pay off the loan in the entered term, will the current remaining value be greater than zero?

This is not an exhaustive list of cases which does not include edge cases which may causes unexpected errors in our code.
