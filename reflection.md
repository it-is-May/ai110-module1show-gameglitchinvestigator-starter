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
