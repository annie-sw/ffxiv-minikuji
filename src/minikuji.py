#!/usr/bin/env python
# -*- coding: utf-8 -*-
from libminikuji import *


def print_expected_table(board):
   for line_id in LINES.keys():
       fixed_values = get_line_values(board, line_id)
       expected_values = get_expected_values(board, fixed_values)
       expected_scores = [SCORES[sum(x)] for x in expected_values]
       print '*', line_id, fixed_values, (sum(expected_scores) - 300 * len(expected_scores))* 1.0 / len(expected_scores), expected_scores


def sample():
    import pprint
    import random
    board = [0] * 9;

    numbers = list(ALL_VALUES)
    def choice_number():
        v = random.choice(numbers)
        numbers.remove(v)
        return v

    board[random.choice(xrange(9))] = choice_number()

    for i in xrange(3):
        print '*** fase:', i, board
        expected_points = calc_higher_expected_index(board)
        pprint.pprint(expected_points)
        points, indexes = sorted(expected_points.items(), reverse=True)[0]
        board[indexes[0] - 1] = choice_number()

    print '*** last fase:', board
    expected_points = calc_higher_expected_line(board)
    pprint.pprint(expected_points)

    print_expected_table(board)

    points, lines = sorted(expected_points.items(), reverse=True)[0]
    line_id = lines[0]
    candidate_indexes = list(set(LINES[line_id]) & set(get_free_indexes(board)))
    for index in candidate_indexes:
        board[index - 1] = choice_number()

    values = get_line_values(board, line_id)
    score = SCORES[sum(values)]
    print 'selected line:', line_id, score, values

    return score


if __name__ == '__main__':
    import pprint
    #  scores = [sample() for x in xrange(100)]
    #  print sum(scores) * 1.0 / len(scores)

    board = [0] * 9;
    board[3 - 1] = 1

    expected_points = calc_higher_expected_index(board)
    pprint.pprint(expected_points)

    #  numbers = list(ALL_VALUES)
    #  def choice_number():
        #  v = random.choice(numbers)
        #  numbers.remove(v)
        #  return v

    #  board[random.choice(xrange(9))] = choice_number()

    #  for i in xrange(3):
        #  print '*** fase:', i, board
        #  expected_points = calc_higher_expected_index(board)
        #  pprint.pprint(expected_points)
        #  points, indexes = sorted(expected_points.items(), reverse=True)[0]
        #  board[indexes[0] - 1] = choice_number()

    #  print '*** last fase:', board
    #  expected_points = calc_higher_expected_line(board)
    #  pprint.pprint(expected_points)

    #  print_expected_table(board)

    #  points, lines = sorted(expected_points.items(), reverse=True)[0]
    #  line_id = lines[0]
    #  candidate_indexes = list(set(LINES[line_id]) & set(get_free_indexes(board)))
    #  for index in candidate_indexes:
        #  board[index - 1] = choice_number()

    #  values = get_line_values(board, line_id)
    #  score = SCORES[sum(values)]
    #  print 'selected line:', line_id, score, values
