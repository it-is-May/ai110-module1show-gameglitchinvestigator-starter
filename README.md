# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document The Experience

### Project Purpose
- This project involved debugging and repairing a Streamlit-based number guessing game. The goal was to identify reproducible bugs, refactor game logic into reusable functions, and verify fixes through automated and manual testing.
### Bugs Found
- Attempt counter started at 1 instead of 0, reducing available attempts at game start.
- High/low feedback messages were reversed.
- New Game did not fully reset game history and score.
- Pressing Enter did not submit guesses consistently.
### Fixes Applied
- Refactored guess evaluation logic into logic_utils.py.
- Corrected the high/low feedback behavior in check_guess().
- Fixed attempt counter initialization using Streamlit session state.
- Added and updated pytest tests to verify game logic.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Start the game in Normal mode.
2. Enter a guess lower than the secret number.
3. Game returns "Too Low" and "Go HIGHER!" feedback.
4. Enter the correct number.
5. Game displays the win message and updates the score.
6. Start a new game and verify the attempt counter reset correctly.


## 🧪 Test Results

```
tests/test_game_logic.py::test_winning_guess PASSED                                                                                  [ 20%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                                                 [ 40%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                                  [ 60%]
tests/test_game_logic.py::test_str_secret_too_low PASSED                                                                             [ 80%]
tests/test_game_logic.py::test_str_secret_magnitude PASSED                                                                           [100%]

============================================================ 5 passed in 0.11s ============================================================
```

## 🚀 Stretch Features

- No stretch features were implemented at the moment.
