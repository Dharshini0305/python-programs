
 Raghu is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
#program
from collections import Counter
num_shoes = int(input())
shoes = list(map(int, input().split()))
num_customers = int(input())
shoe_counts = Counter(shoes)
total_earned = 0
for _ in range(num_customers):
    size, price = map(int, input().split())
    if shoe_counts[size] > 0:
        total_earned += price
        shoe_counts[size] -= 1
print(total_earned)
