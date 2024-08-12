# Course project: Build a probability calculator

import copy
import random
from collections import Counter

class Hat:
    def __init__(self, **args):
        self.contents = []
        for color, n in args.items():
            for i in range(n):
                self.contents.append(color)

    def draw(self, number_of_draws):
        sample = []
        if number_of_draws >= len(self.contents):
            sample = copy.copy(self.contents)
            self.contents = []
            return sample
        for _ in range(number_of_draws):
            index = random.randrange(len(self.contents))
            sample.append(self.contents.pop(index))
        return sample

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    expected = Counter(expected_balls)
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        sample = Counter(hat_copy.draw(num_balls_drawn))
        successes += (expected <= sample)
    return successes / num_experiments
