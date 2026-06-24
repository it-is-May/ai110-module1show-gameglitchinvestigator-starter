# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? 
  - It printed the welcome message from streamlit and asked for email (not for login purpose) then it loaded to the application. There is a setting panel on the left side of the screen with difficulty dropdown (easy, normal, hard) and "Normal" by default, an input range of 1 to 100 (not clickable), and number of allowed attempts of 8 (not clickable). In the middle of the screen, there is a dropdown of Developer Debug Info table under the line "Guess a number between 1 and 100. Attempts left: 7". Underneath is the space to type a guess, Submit Guess button, New Game button, checked Show hint box.
- List at least two concrete bugs you noticed at the start  
  - Attempts left: 7 (allowed = 8) & Attempts: 1 on the Developer Debug Info
  - Score showed negative number (-5) after the first attempt

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Start game on Normal mode | Attempts = 0 and Attempts left = 8 | Attempts = 1 and Attempts left = 7 | None |
| Guess 20 when secret is 27 | Feedback says “Too Low” or “Go HIGHER!” | Feedback says “Go LOWER!” | None |
| Make several guesses, then click New Game | History clears, score resets to 0, attempts reset to 0 | Previous history remains and score stays 25 | None |
| Type 25 and press Enter | Guess submits or app clearly requires button click | Guess is not submitted, but state/history becomes confusing | None |


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Claude Code: mainly for fix review and code understanding
  - ChatGPT: alternative when Claude Code had an internal API 500 error; for understanding the entire code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - Claude Code suggested decrementing the attempt state from 1 to 0 because it counts an attempt before the user even submits any guess.
    - I verified the fix by using live testing, and the attempt counter worked properly when I restarted a new game or reloaded the page. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - Claude Code suggested removing `msg` from the first `check_guess()` test, which would avoid verifying the success message `"🎉 Correct!"`. I treated this as misleading because the function returns both an outcome and a message, so the test should check both values. I verified this by reviewing `logic_utils.py` and confirming that the expected output for a correct guess includes both `"Win"` and `"🎉 Correct!"`.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - A bug is fixed when it runs properly on given controlled test environment and/or during live testing.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - For high/low feedback bug, I ran 5 tests using pytest, the first one checks whether the winning condition is correctly applied. The remaining 4 test cases check high/low bug, but in slightly different ways.
    - The first two check whether the swapped feedback is correctly aligned with the correct outcome (e.g.,outcome = too high --> go lower, and vice versa). 
    - The last two check the feedback on typecasted values as string order doesn't reflect numerical order.
    - After running all 5 tests, I did a live test by running app.py and verified that the feedback is aligned with the input.
  - For attempt counter initialization bug, I did live testing since attempt counter initialization was not a bug inside the main logic (4 functions).
- Did AI help you design or understand any tests? How?
  - I used Claude Code to help understand the given test cases in the original version of test_game_logic.py for high/low bug then design a new set of test cases that is suitable and holistically checks on my fix. I also used it to find the appropriate testing method for attempt counter initialization.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Streamlit reruns the entire script whenever the user interacts with the page or reloads the app. Session state acts as persistent memory between reruns. The attempt counter bug occurred because the session state variable was initialized to 1 instead of the correct starting value, causing the game to begin with one attempt already counted.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - I would reuse meta prompting, caveman, and interactive Q&A in future labs or projects. Meta prompting helped me use ChatGPT to create more effective prompts for Claude Code. Caveman helped reduce unnecessary output and keep responses focused, while interactive Q&A helped me break down large pieces of code and confirm my understanding before moving on.
- What is one thing you would do differently next time you work with AI on a coding task?
  - I would install Obsidian to use with Claude to save my chats.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project changed how I think about AI-generated code because I realized AI can speed up debugging, but I still need to verify the logic myself. I treated AI more like a teammate than an autopilot by testing its suggestions before accepting them.

