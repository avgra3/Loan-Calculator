using System;

// Input parameters
Console.WriteLine("What is the inital principal amount?");
decimal principal;
bool result_principal = decimal.TryParse(Console.ReadLine(), out principal);

Console.WriteLine("What is your expected term length? (Enter in months):");
uint expectedTermLength;
bool result_etl = uint.TryParse(Console.ReadLine(), out expectedTermLength); 

Console.WriteLine("What is your APR?:");
decimal apr;
bool result_apr = decimal.TryParse(Console.ReadLine(), out apr);
// apr is total percentage for the year, so if we want per month, then we divide by 12
// Then we divide by 100 since we are converting a percent to a decimal value.
apr = ((apr/12m)/100m);

Console.WriteLine("What are you willing to pay per month?");
decimal monthly_pay;
bool result_mp = decimal.TryParse(Console.ReadLine(), out monthly_pay); 

Console.WriteLine("What is your down payment amount?");
decimal dpayment;
bool result_dpayment = decimal.TryParse(Console.ReadLine(), out dpayment); 

// Calculating the actual loan amount
// Our initial array, which will be empty
// decimal[] months = new decimal[] {};
var months = new List<decimal> {};

// sets principal as initial value principal minus the downpayment
principal = principal - dpayment;
months.Add(principal);
Console.WriteLine($"Starting amount after down payment: ${months[0]}");

// Now we want a while loop to calculate our amount owed
for (int i = 0; i < expectedTermLength; i++)
{
    principal = (principal - monthly_pay) * (apr + 1m);
    months.Add(principal);
    if (principal <= 0)
    {
        principal = 0;
        Console.WriteLine($"Wow, it will take you {i} months to pay off your loan!");
        break;
    }
}

if (principal > 0)
{
    Console.WriteLine($"You have ${Decimal.Round(principal, 2)} remaining on your loan.");
}
// Just so the console window stays open.
Console.WriteLine("\nThank you for using this app! Press Enter to close program.");
Console.ReadLine();