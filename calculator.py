""" First round: Quotient = Votes

Each round

Highest quotient gets a seat; recalculate that party's quotient
On draw, random
Quotient = Votes / (number_of_seats_gained_by_this_part + 1)
Have we run out of seats? Yes then stop
                          No: Goto next round"""
import copy


def election(number_of_seats, candidates):
    """Figure out how to win European elections.
    This party will tell you what you need to do to win European
    elections. It'll be fine.
    :param: number_of_seats - integer number of seats in election.
    :param: candidates - dict of candidate name: votes won

    :return: dict of candidates: seats won
    """
    if number_of_seats <= 0:
        raise ValueError(
            'John does not like you doing this. Use more seats!'
        )
    if any(votes for votes in candidates.values() < 0):
        raise ValueError(
            'John also does not like negative amounts of votes.'
        )
    seats_won = {
        candidate_name: 0 for candidate_name in candidates
    }

    quotients = copy.copy(candidates)

    while number_of_seats > 0:
        highest = max(quotients, key=lambda x: quotients[x])
        seats_won[highest] += 1
        number_of_seats -= 1
        quotients[highest] = candidates[highest] / (seats_won[highest] + 1)

    return seats_won
