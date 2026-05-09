# Saving a .json file using Python
- My Mercenary Management System (OOP Practice)
Yo! This is one of my early Python projects where I built a system to manage a squad of mercenaries. I wanted to move beyond just basic scripts, so I challenged myself to build something with more "structure."

- What's inside?
Role Selection: You can add units as standard Mercenaries, Snipers, or Medics.

The Promotion Loop: My favorite part! You can promote units from Rank E all the way to S, and the system automatically calculates their salary raises and stat buffs.

Smart Storage: I used JSON so you don't lose your squad data when you close the program.

Bulk Commands: You can promote or remove everyone at once—perfect for when you're feeling like a real commander.

- What I learned from this:
Building this wasn't just about making a game tool; it was a deep dive into Object-Oriented Programming (OOP). I learned how to use Inheritance so that Snipers and Medics could "inherit" traits from a base Mercenary class while still having their own unique skills. I also got comfortable handling external files and using the match-case logic to keep the menu clean.

- What’s next?
This is just the foundation! I can see myself scaling this into a full Roblox RPG backend or a tactical mercenary simulator. The logic I built here for ranks and data saving is exactly what’s needed for more complex game development projects I'm planning.


# Minimalist CLI Diary (Python Persistence Practice)
Yo! Check this out. I built a super lightweight, no-nonsense Diary app that runs right in your terminal. I wanted a quick way to jot down thoughts without opening a heavy editor, so I made this!

- What's inside?
Instant Timestamping: Every time you add a note, the system automatically tags it with the exact date and time.

Persistent Memory: It uses JSON formatting to save your notes into a diary.txt file, so your secrets are safe even after you close the app.

Simple CLI Commands: Just type add, show, or clear to manage your entries. Fast and efficient.

Clean Layout: I added some visual dividers to make reading back your notes easy on the eyes.

- What I learned from this:
This project was a great way to practice Data Persistence. I learned how to handle Python's json library to read and write structured data. It also helped me get comfortable with Nested Functions and the Match-Case statement to keep the control flow clean and easy to read.

- What’s next?
This is a perfect base for something bigger! I’m thinking about adding Keyword Search to find old notes instantly or even Encryption to make the diary private. Since I love Liquid Glass and Glassmorphism designs, I might eventually turn this logic into a beautiful web app or a desktop GUI!
