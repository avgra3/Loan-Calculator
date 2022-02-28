# Car Loan Calculator

## Purpose

The purpose of this project is to create a simple and quick calculator to determine how long it will take a person to pay off their car loan given several inputs.

Although this app is basic, it could be applied to other types of loans which function in a similar manner.

Feel free to contribute to this project with other languages or refactoring of the current code.

## Math and Financial Terms Used

In this program there are several inputs that are needed.

**Principal:** The amount that you originally agree to pay back to the lender.

**APR:** Annual percentage rate. This is the anual percentage rate of a loan. This is similar to an interest rate. If you want to calculate the interest rate per month, you would divide the APR by 12 (for each month in a year).

**Down Payment:** The initial amount you pay before interest towards the principal amount. Essentially, a large down payment can greatly reduce the time it takes to pay off a loan.

### Maths

To calculate each month the total amount owed on a loan, we use the following formula.

$$ P_0 = principal - downPayment $$

$$ P_n = (P_{n-1}- montlyPayment) \times \left( \frac{APR}{12} + 1 \right)$$

The above assumes that APR is represented as a decimal, i.e., if $APR=8%$ then we would use $0.08$ as our APR.

## Python

The Python 3 method was created using only the default packages. The reason being that it will allow a person to use the python module on any machine which supports Python.

For this project Python 3.9 was used. If you need to install Python, head to the downloads [page](https://www.python.org/downloads/), or to the [Anaconda](https://www.anaconda.com/products/individual) webpage if you would rather use conda to manage your enviornments.

### How to Use (recommended)

From your command line run the following, ensuring the correct path to your [main.py](./Python/main.py) file.

```python:
python .\PATH_TO_FILE\main.py
```

For Mac and Linux users, you will more than likely have to use the following commands in your terminal.

```python:
python3 ./PATH_TO_FILE/main.py
```

## C# and .Net

This approach was taken since the .Net framework can allow for a more robust program. However, this current program shows that although it is possible to create a basic console app, there are more parameters involved due to the way C# is compiled.

For this project, .Net sdk version 6.0.102 was used. If you need to install this version of the SDK, please head to the [.Net](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) download page.

### How to use (recommended)

We will assume that you are building this C# program from scratch, so from your command line run the following from within the same directory as the main program files (they have extensions of \*.cs and \*.csproj.

```bat:
dotnet build -o [OUTPUT_DIRECTORY]
```

Once the build has completed, you will need to navigate to the [Debug folder](./Csharp/bin/Build/). If you are running on Windows, you will see the \*.exe file. If you run that program, you will be able to run your program.

If you would rather just build the _release_ version of this app, try the following when you are in the same directory as the _*.cs_ file. (notice how similar these commands are).

```bat:
dotnet publish
```

Which will send the executable and .dll to this location on Windows: [`.\bin\Debug\net6.0\`](./Csharp/bin/Debug/net6.0/)
