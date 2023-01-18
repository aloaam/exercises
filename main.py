import dice_roll

if __name__ == "__main__":

    print('The probability for getting the following number as the result of rolling 2 dice are:')
    for i in range(2, 13):
        print(f'{i}: {dice_roll.compute_probability_for_sum(i):.2%}')