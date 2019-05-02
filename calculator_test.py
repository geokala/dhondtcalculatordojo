from calculator import election


def test_seats_should_give_votes():
    seats = 1
    candidates = {
        'sandy': 43,
        'pradeep': 924,
        'john': 23,
        'shaunick': 3
    }
    expected = {
        'sandy': 3,
        'pradeep': 3,
        'john': 3,
        'shaunick': 0
    }
    assert election(seats, candidates) == expected
