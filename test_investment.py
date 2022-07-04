#!/usr/bin/python3

#Have the user enter their investment amount and expected interest
#each year their investment will increase by their investment + their investment * interest rate is
#print out the earnings a 10 year period

your_investment = input("How much to invest : ")
interest_rate = input("Interest rate : ")
your_investment = float(your_investment)

interest_rate = float(interest_rate) * .01

for i in range(10):
    your_investment = your_investment + (your_investment * interest_rate)

print("Investment after 10 years : {:.2f}".format(your_investment))
