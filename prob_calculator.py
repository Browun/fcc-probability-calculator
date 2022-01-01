import copy
import random
from typing import List
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = self.produce_list(kwargs)

    def __str__(self) -> str:
        '''Returns the list of balls in the hat.'''
        return self.contents

    def produce_list(self, colours) -> List[str]:
        '''Produces a list of strings from the inputted colours.'''

        return [colour for colour in colours for n in range(colours[colour])]

    def draw(self, number_to_draw: int) -> List[str]:
        '''
        Removes balls from the hat (contents) and returns a list of the balls removed. Returns all the balls if the number requested to draw is greater than the number in the hat.
        '''

        if number_to_draw > len(self.contents):
            return self.contents

        removed_balls = [
            self.contents.pop(random.randint(0,
                                             len(self.contents) - 1))
            for i in range(number_to_draw)
        ]

        return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments) -> float:
    '''
    Returns the probability of having the expected balls drawn, given certain balls in the hat, a number of balls to draw, and number of experiments to average the result over.
    '''
    number_of_trues: List[bool] = []

    for exp in range(num_experiments):
        h = copy.deepcopy(hat)
        removed_balls: List[str] = h.draw(num_balls_drawn)

        number_of_trues.append(True if all([
            removed_balls.count(colour) >= expected_balls[colour]
            for colour in expected_balls
        ]) else False)

    return sum(number_of_trues) / num_experiments
