from calculator import election


def test_seats_should_give_votes():
    seats = 1
    candidates = {
        'sandy': 43,
        'pradeep': 924,
        'john': 23,
        'shaunick': 3,
    }
    expected = {
        'sandy': 0,
        'pradeep': 1,
        'john': 0,
        'shaunick': 0,
    }
    assert election(seats, candidates) == expected


def test_1_candidate():
    seats = 100
    candidates = {
        'sandy': 43,
    }
    expected = {
        'sandy': 100,
    }
    assert election(seats, candidates) == expected


def test_1_seat():
    seats = 1
    candidates = {
        'sandy': 43,
        'pradeep': 924,
        'john': 23,
        'shaunick': 3,
    }
    expected = {
        'sandy': 0,
        'pradeep': 1,
        'john': 0,
        'shaunick': 0,
    }
    assert election(seats, candidates) == expected


def test_wikipedia_example():
    seats = 8
    candidates = {
        'Party A': 100000,
        'Party B': 80000,
        'Party C': 30000,
        'Party D': 20000,
    }
    expected = {
        'Party A': 4,
        'Party B': 3,
        'Party C': 1,
        'Party D': 0,
    }
    assert election(seats, candidates) == expected


def test_wikipedia_example():
    seats = 8
    candidates = {
        'Party A': 100000,
        'Party B': 80000,
        'Party C': 30000,
        'Party D': 20000,
    }
    expected = {
        'Party A': 4,
        'Party B': 3,
        'Party C': 1,
        'Party D': 0,
    }
    assert election(seats, candidates) == expected
