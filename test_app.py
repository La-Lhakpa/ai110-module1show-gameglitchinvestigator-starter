from app import get_range_for_difficulty, check_guess, update_score


# --- Fix 1: Correct range per difficulty ---

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50


# --- Fix 2: check_guess gives correct directional messages ---

def test_guess_too_high_says_lower():
    outcome, message = check_guess(40, 18)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low_says_higher():
    outcome, message = check_guess(5, 18)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_guess_correct():
    outcome, message = check_guess(18, 18)
    assert outcome == "Win"


# --- Fix 3: Score never goes negative ---

def test_score_does_not_go_negative_on_too_low():
    score = update_score(0, "Too Low", 1)
    assert score >= 0

def test_score_does_not_go_negative_on_too_high_odd_attempt():
    score = update_score(0, "Too High", 1)  # odd attempt subtracts
    assert score >= 0

def test_score_does_not_go_negative_after_many_wrong_guesses():
    score = 0
    for attempt in range(1, 10):
        score = update_score(score, "Too Low", attempt)
    assert score >= 0

def test_score_increases_on_win():
    score = update_score(0, "Win", 1)
    assert score > 0
