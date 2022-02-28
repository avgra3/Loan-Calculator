"""
This will test our python main script.

unittest is part of the standard library so we won't need to install anything
"""
import unittest
from main import InterestCalc

# test class that inherits from unittest
class TestInterestCalc(unittest.TestCase):

    # We want to check that the user inputs are the correct data type that we want
    def test_get_user_input(self):

        def test_loan_amount(self):
            # Invalid inputs (should not be a string or character) or blank
            with self.assertRaises(ValueError):
                InterestCalc("175000", 8.06, 12, 350, 3000)
                InterestCalc(175000, "8.06", 12, 350, 3000)
                InterestCalc(175000, 8.06, "12", 350, 3000)
                InterestCalc(175000, 8.06, 12, "350", 3000)
                InterestCalc(175000, 8.06, 12, 350, "3000")

                InterestCalc("", 8.06 , 12, 350, 3000)
                InterestCalc(175000,  "", 12, 350, 3000)
                InterestCalc(175000, 8.06 , "", 350, 3000)
                InterestCalc(175000, 8.06 , 12, "", 3000)
                InterestCalc(175000, 8.06 , 12, 350, "")

            # Make sure a loan pays off in correct amount of time
            paysOff = InterestCalc(25000, 3.11, 60, 450, 0)
            self.assertEqual(paysOff.current_remaining, 0)

            # If we don't pay off the loan in the correct amount of time
            # Should be able to pay off at 60 months
            notPaysOff = InterestCalc(25000, 3.11, 50, 450, 0)
            self.assertNotEqual(notPaysOff.current_remaining, 0)

# Structure of our class
# InterestCalc(initial, rate, term, monthly_pay, down_payment)

# So we can just run the file using the below in the command line:
# python test_main.py
if __name__ == "__main__":
    unittest.main()