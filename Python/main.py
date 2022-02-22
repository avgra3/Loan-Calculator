"""
This class calculates if a person's loan amount will be paid off at or before the end of the term.
If the remaining amount > 0, then we will receive a message with the remaining amount.
If the remaining amount == 0, we will get a success message with how long it look to pay off the loan in months. 
"""

class InterestCalc:
    # initialize the terms that we will be implementing
    def __init__(self, initial, rate, term, monthly_pay, down_payment):
        self.initial = initial
        self.rate = rate
        self.term = term
        self.monthly_pay = monthly_pay
        self.down_payment = down_payment

    # Get the user's input
    @classmethod
    def get_user_input(self):
        initial = float(input("What is the initial payment amount? "))
        term = int(input("How long is the supposed term? "))
        rate = (float(input("What is your APR? (Enter a percent) ")) / 100.0) /12.0
        monthly_pay = float(input("How much are you expecting to paying each month? "))
        down_payment = float(input("What is your down payment? "))
        return self(initial, rate, term, monthly_pay, down_payment)
    
    # Calculate the payments over time
    def loan_amount(self):
        per_month = []
        current_remaining = self.initial - self.down_payment
        print(f"\nStarting amount after down payment: ${round(current_remaining,2)}")
        for i in range(int(self.term)):
            current_remaining = (current_remaining- self.monthly_pay) * (self.rate + 1)
            per_month.append(current_remaining)
            if current_remaining <= 0:
                per_month[i] = 0
                print(f"\nAt this rate it will take {i} months to complete payments!\n")
                break
        
        """
        If the minimum value in the list is greater than 0, calculate the remaining amount at the end of the term.
        Calculate the remaining amounts if the person has not finished paying their loan.
        """
        if min(per_month) > 0:
            remaining = round(per_month[-1],2)
            so_far_paid = round(remaining - self.initial, 2)
            print(f"\nAt the end of {self.term} months, you have ${round(current_remaining,2)} remaining on your loan.\nYou have so far paid ${so_far_paid} on your loan...")
            print("You should consider paying more per month...\n")


if __name__ == "__main__":
    results = InterestCalc.get_user_input()
    results.loan_amount()
