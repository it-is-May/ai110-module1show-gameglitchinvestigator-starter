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
| guess of 20 | "Too Low" hint or "Go Higher" feedback | "Go LOWER!" feedback | None |
| guess of 19, uncheck Show Hint before Submit Guess, check Show Hint after Submit Guess | Hint is shown after click on Show Hint post Submit Guess | No hint is shown | None |
| guess of 25, hit enter to submit guess | Guess is submitted; Attempts left = 4; Attempts = 3 | Guess is not submitted; Attempts left = 5; Attempts = 3 | None |
| guess of 25 after enter error, use Submit Guess | Attempts left = 4; History must include "2: 25" | Attempts left = 5; History doesn't include "2: 25" | None |
| guess of 27 (correct ans), use Submit Guess | "Correct" feedback; Attempts left = 3; Attempts: 4; History includes "3: 27" | "Correct" feedback, Attempts left = 4, Attempts: 4, History didn't include "3: 27" | None |
| hit New Game button | History is refreshed; Attempts left = 8; Attempts: 0; Score: 0 | History contains "0: 20, 1: 19, 2: 25, 3: 27"; Attempts: 0, Attempts left = 8; Score: 25 | None |
| guess of 60 (new game) | History is updated to include the entry of 60; Attempts left = 7; Attempts: 1, Score is updated | History isn't updated to include the entry of 60; Attempts left = 8; Attempts: 0, Score isn't updated | None |
| refresh the web after "60" | History is refreshed; Attempts left = 8; Attempts: 0; Score: 0 | History is refreshed (no entries); Attempts left = 7; Attempts: 1; Score: 0 | None |
| guess of 70 after refresh | History includes an entry of 70; Attempts left = 6; Attempts: 2; Score changes; "Go HIGHER!" feedback | History shows no entries; Attempts left = 7; Attempts: 1; Score: 0; "Go LOWER!" feedback | None |


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
