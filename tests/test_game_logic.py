from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, msg = check_guess(50, 50)
    assert outcome == "Win"
    assert msg == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High" -> go lower
    outcome, msg = check_guess(60, 50)
    assert outcome == "Too High"
    assert msg == "📉 Go LOWER!"   # Bug A: too high -> go lower

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low" -> go higher
    outcome, msg = check_guess(40, 50)
    assert outcome == "Too Low"
    assert msg == "📈 Go HIGHER!"  # Bug A: too low -> go higher

def test_str_secret_too_low():
    # Bug B: "9" > "100" as strings -> wrong "Too High"
    outcome, msg = check_guess(9, "100")
    assert outcome == "Too Low"
    assert msg == "📈 Go HIGHER!"

def test_str_secret_magnitude():
    # Bug B other direction: string compare would wrongly say "100" < "20"
    outcome, msg = check_guess(100, "20")
    assert outcome == "Too High"
    assert msg == "📉 Go LOWER!"
