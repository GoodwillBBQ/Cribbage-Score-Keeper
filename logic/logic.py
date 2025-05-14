SKUNK_LINE = 90
DOUBLE_SKUNK_LINE = 60

DEFAULT_VICTORY_POINTS = 1
SKUNK_VICTORY_POINTS = 2
DOUBLE_SKUNK_VICTORY_POINTS = 3

def is_skunk(score_1: int, score_2: int) -> bool:
    if min(score_1, score_2) > SKUNK_LINE:
        return False
    else:
        return True

def is_double_skunk(score_1: int, score_2: int) -> bool:
    if min(score_1, score_2) > DOUBLE_SKUNK_LINE:
        return False
    else:
        return True
    


def determine_victory_points(score_1: int, score_2: int) -> int:
    if is_skunk(score_1, score_2):
        if is_double_skunk(score_2):
            return DOUBLE_SKUNK_VICTORY_POINTS
        return SKUNK_VICTORY_POINTS
    else:
        return DEFAULT_VICTORY_POINTS