
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name: Nesamani Victor
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    # Handle negative amount
    if amount < 0:
        return 0.0

    # Handle same currency conversion
    if from_currency == to_currency:
        return round(float(amount), 2)
    
    # Get conversion rate and calculate converted amount
    rate = conversion_rate[from_currency][to_currency]
    result = amount * rate

    return round(result, 2)

# Submit only this file currency_converter.py with the completed function.

# Remove any additional code you may have added during development and testing.
# --- LOCAL TESTING ONLY (Delete/Comment this out before submitting to Gradescope) ---
#print(currency_converter(101, 'GBP', 'CNY'))  # Should print 933.24[cite: 1]
#print(currency_converter(50, 'GBP', 'GBP'))   # Should print 50.0
#print(currency_converter(-10, 'INR', 'PHP'))  # Should print 0.0[cite: 1]