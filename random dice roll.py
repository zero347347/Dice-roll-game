import random
print("For testing, you rolled, ", random.randint(1, 6))

dices_sum = 0
rolls_count = 0
answer_1 = "No"
key_1 = ""

while dices_sum != 7 and rolls_count < 5 and key_1 != "No":
    dices_sum = 0
    roll_dice_1 = random.randint(1, 6)
    print("For dice 1 you rolled, ", roll_dice_1)
    roll_dice_2 = random.randint(1, 6)
    print("For dice 2 you rolled, ", roll_dice_2)
    dices_sum = int(roll_dice_1) + int(roll_dice_2)
    print(f"The total sum of dice 1 & dice 2 is {dices_sum}")
    rolls_count += 1
    if dices_sum == 7:
        print("congratulations, you get 7")
    elif dices_sum < 7 or dices_sum > 7:
        print("Do you want to roll again ? Yes or No? ")
        key_1 = input("Yes or No? : ")
if rolls_count > 4:
    print("Out of rolls chance")


