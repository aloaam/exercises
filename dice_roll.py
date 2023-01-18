"""
Computes the probabilities for the sum of points when throwing two dices.
"""
import itertools

import pandas as pd


def compute_probability_for_sum(sum_of_dices: int) -> float:
    if sum_of_dices < 2 or sum_of_dices > 12:
        raise ValueError(f"The sum of two dices must be in the range [2, 12]. Value sent: {sum_of_dices}")

    probabilities: pd.DataFrame = _get_two_dice_sum_probabilities()

    return probabilities.loc[sum_of_dices, 'probability']


def _get_two_dice_sum_probabilities() -> pd.DataFrame:
    """
    Returns : pd.DataFrame
    -------
    A pd.DataFrame that contains the probabilities of the sum of rolling two dices:

    e.g.,
        sum  probability
    7     6     0.166667
    6     5     0.138889
    8     5     0.138889
    5     4     0.111111
    """

    dice_count: int = 36
    rolled_dice_sums: pd.DataFrame = _get_rolled_dice_sums()

    probabilities: pd.DataFrame = rolled_dice_sums['sum'].value_counts().to_frame()
    probabilities['probability'] = probabilities['sum'] / dice_count

    return probabilities


def _get_rolled_dice_sums() -> pd.DataFrame:
    """
    Returns : pd.DataFrame
    -------
    A pd.DataFrame which contains all the possible outputs for rolling two dices and its sum:

    e.g.,
        0  1  sum
    0   1  1    2
    1   1  2    3
    2   1  3    4
    3   1  4    5

    ...
    33  6  4   10
    34  6  5   11
    35  6  6   12
    """
    dice_output: tuple = (1, 2, 3, 4, 5, 6)
    rolled_dice_outputs: pd.DataFrame = pd.DataFrame(itertools.product(dice_output, dice_output))
    rolled_dice_outputs['sum'] = rolled_dice_outputs.sum(axis=1)

    return rolled_dice_outputs


if __name__ == "__main__":

    print('The probability for getting the following number as the result of rolling 2 dice are:')
    for i in range(2, 13):
        print(f'{i}: {compute_probability_for_sum(i):.2%}')
