# First round: Quotient = Votes
#
# Each round
# 
# Highest quotient gets a seat; recalculate that party's quotient
# On draw, random
# Quotient = Votes / (number_of_seats_gained_by_this_part + 1)
# Have we run out of seats? Yes then stop
#                           No: Goto next round


def election(number_of_seats, candidates):
    """Figure out how to win European elections.
    This party will tell you what you need to do to win European
    elections. It'll be fine.
    :param: number_of_seats - integer number of seats in election.
    :param: candidates - dict of candidate name: votes won

    :return: dict of candidates: seats won
    """

