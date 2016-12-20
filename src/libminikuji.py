#!/usr/bin/env python
# -*- coding: utf-8 -*-


ALL_VALUES = list(xrange(1, 10))

SCORES = {
     6: 10000,
     7:    36,
     8:   720,
     9:   360,
    10:    80,
    11:   252,
    12:   108,
    13:    72,
    14:    54,
    15:   180,
    16:    72,
    17:   180,
    18:   119,
    19:    36,
    20:   306,
    21:  1080,
    22:   144,
    23:  1800,
    24:  3600,
}

LINES = {
    # 縦
    2: (1, 4, 7),
    3: (2, 5, 8),
    4: (3, 6, 9),
    # 横
    6: (1, 2, 3),
    7: (4, 5, 6),
    8: (7, 8, 9),
    # 斜め
    1: (1, 5, 9),
    5: (3, 5, 7),
}


def new_board():
    return [0] * 9


def get_possible_values(values, level):
    if level == 1:
        return [(x, ) for x in values]

    ret = []
    tmp = list(values)
    for x in values:
        tmp.remove(x)
        for y in get_possible_values(tmp, level - 1):
            ret.append((x, ) + y)

    return ret


def get_free_indexes(board):
    return tuple(x for x in ALL_VALUES if board[x - 1] is 0)


def get_line_values(board, line_id):
    values = [board[x - 1] for x in LINES[line_id]]
    return tuple([x for x in values if x is not 0])


def is_reach(board, index):
    for line_id in LINES.keys():
        if index in line and len(get_line_values(board, line_id)) == 2:
            return True
    return False


def get_expected_values(board, fixed_values):
    level = 3 - len(fixed_values)
    if level == 0:
        return [fixed_values]

    # fix for pythonjs
    candidate_values = []
    for candidate_value in ALL_VALUES:
        if not candidate_value in board and not candidate_value in fixed_values:
            candidate_values.append(candidate_value)

    expected_values = get_possible_values(candidate_values, 3 - len(fixed_values))
    return [fixed_values + x for x in expected_values]


def get_expected_scores(board, line_id):
    fixed_values = get_line_values(board, line_id)
    expected_values = get_expected_values(board, fixed_values)
    return  [SCORES[sum(x)] for x in expected_values]


def calc_expected_points_with_line(board, line_id):
    expected_scores = get_expected_scores(board, line_id)
    return sum(expected_scores) * 1.0 / len(expected_scores)


def calc_higher_expected_index(board):
    free_indexes = get_free_indexes(board)

    scores = {}
    for index in free_indexes:
        expected_scores_per_line = [calc_expected_points_with_line(board, x) for x in LINES.keys() if index in LINES[x]]
        score = sum(expected_scores_per_line)
        if not score in scores:
            scores[score] = []
        scores[score].append(index)

    return scores


def calc_higher_expected_line(board):
    scores = {}
    for line_id in LINES.keys():
        score = calc_expected_points_with_line(board, line_id)
        if not score in scores:
            scores[score] = []
        scores[score].append(line_id)
    return scores
