# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---The first look of game for me was not interesting as it was all descriptions and texts box. 
---The hints were backwards and it was giving the wrong message after each guess.
---Even though range was between 1-50 in hard mode, when I entered "100" it gave me message to Go Higher. And the button for new game doesnt work.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---I used Claude for this project. AI correcltly found out what was wrong in the code logic when I explained him the bugs I found which was on hints being backward. And it fixed it.
--- 2nd bug on incorrect range for secret number couldn't be fixed at first and it gave me the same answer even after changing few logics on code. But after 2nd prompt it gave me correct code to fix it. 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

--- In order to find the bug was really fixed was I tried playing the game manually 2-3 times. And then created a test for it with the help of Claude. 
--- I played Hard mode with range 1-50 and was able to get the correct answer. 

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.I
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---I think the secret number kept changing in the original app because On even attempts, the secret was converted to a string, and on odd attempts it stayed an integer. Because string and numeric comparisons behave differently (e.g., `"9" > "10"` is True but `9 > 10` is False), the Too High/Too Low hints flipped, making it seem like the secret number was changing when it was actually the data type switching.

--- I would explain to them that streamlit "reruns" is like a game where if you touch anything then it restarts. 

---This was fixed by removing the type-switch logic at app.py and always passing the secret number as an interger to check_guess. 


## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

---From this project, I learnt how simple format of coding could change the whole logic of a project. I would use it in the future to be extra careful with the wordings. I would also test my project as much as I can before deploying.

---Next time, I want to read the code first and figure out the bugs myself and try to fix it first before AI. 

---This project taught me:
    -> How games are built. 
    -> How logics behind certain function worked.
     

