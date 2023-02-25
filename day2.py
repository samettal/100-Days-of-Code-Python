print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill? '))
tip_percentage = input('What percentage tip would you like to give? ')
people = int(input('How many people to split the bill? '))
total_tip = total_bill * float('0.'+tip_percentage)
top_total = total_bill + total_tip
per_capita = top_total / people
print(f'Each person should pay: ${per_capita: .2f}')