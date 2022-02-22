# Car Loan Calculator

## Purpose

The purpose of this project is to create a simple and quick calculator to determine how long it will take a person to pay off their car loan given several inputs.

### Python

The Python 3 method was created using only the default packages. The reason being that it will allow a person to use the python module on any machine which supports Python.

For this project Python 3.9 was used. If you need to install Python, head to the downloads [page](https://www.python.org/downloads/), or to the [Anaconda](https://www.anaconda.com/products/individual) webpage if you would rather use conda to manage your enviornments.

## C# and .Net

This approach was taken since the .Net framework can allow for a more robust program. However, this current program shows that although it is possible to create a basic console app, there are more parameters involved due to the way C# is compiled.

For this project, .Net sdk version 6.0.102 was used. If you need to install this version of the SDK, please head to the [.Net](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) download page.

## Math and Financial Terms Used

In this program there are several inputs that are needed.

**Principal:** The amount that you originally agree to pay back to the lender.

**APR:** Annual percentage rate. If you have an APR. This is the anual percentage rate of a loan. This is similar to an interest rate. If you want to calculate the interest rate per month, you would divide the APR by 12 (for eaach month in a year).

**Down Payment:** The initial amount you pay before interest towards the principal amount. Essentially, a large down payment can greatly reduce the time it takes to pay off a loan.

### Maths

To calculate each month the total amount owed on a loan, we use the following formula.

$P_0 = principal - downPayment$

$P_n = (P_{n-1}- montlyPayment) \times (APR/12 + 1)$

The above assumes that APR is represented as a decimal, i.e., if $APR=8%$ then we would use $0.08$ as our APR.
