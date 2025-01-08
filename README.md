This pet project involved programatically solving assorted daily puzzles. At the time I was really enjoying the games like Wordle, Strands, Letter Boxed (All from NYT) and Squaredle. I started with Squaredle since it seemed like it would make the most interesting algorithm / program. 

**Squaredle Summary**
In Squaredle, you are given a grid of letters (they can be any letter, including repeats). Traditionally, it's a 4×4 grid, though there are cases where its a different size or even shape. You then make a path of letters to make words (4 chars min). On this path, each letter / tile can only be used once. Connections can be made in any direction (Cardinal + Diagonals) immediately surrounding the previous letter / tile (3×3 centered on it).
The goal is to find all of the words in the grid. They have a list of posible words (from the scabble dict; More on this in a bit) which they've currated for the more well known words (as determined by them and the community). Only those more common words are included in the completion of the puzzle, though the other words can still be input as bonus words (it even gives you a little pop-up for finding all of the bonus words).


**My Squaredle Program**
So, there are a couple parts to the program:
	1) Getting the board (what chars are in what position)
	2) Processing the board to find the possible words
	3) Outputting the found words to the website (For automatic finishing, if I wanted to)

For **step 1**, I didn't feel like learning character / image recognition, so (having a backgound in web dev.), I took a look into the website's source code where... I didn't find anything easily. (It's probably there somewhere. It's just burried deep enough that I didn't feel like taking the obscene amount of time to find the info I needed) So, I gave up and just decided to hard-code / manually input the board (I've been calling it 'the grid' as well). Thus the 'input.txt' file was born.
\**I didn't feel bad about skipping over this step since (at the time) I planned on coming back to it and actually doing it "right". That and it was just a fun pet project and not actually required for anything, so I get to make the rules.*

**Step 3** is more straightforward to explain, so I'll briefly touch on it before getting to the meat of the program. Basically, after poking around the settings and help info, I found out that you can use the keyboard to input the letters (It would just auto-make a path if it's a legitamate path, including jumping around if there were more than one possibility and the one currently highlighted no longer fit the path you were typing). Long story short, that made it really easy to input things into the website. (I had previously only played on my phone, i.e. no keyboard naturally available)

Back to **step 2**... Actually, now that I'm thinking through what needs to be explained, essentially I read in the grid (input), compute every possible combination, then check that against a list of words I hosted on a localhost database (that is now gone since I didn't think about any of my database files when I reset / switched computers... Oops). Weirdly, I had the most problem getting the wordlist. I knew exactly which word-list they used (some recent release of the official Scrabble dictionary). What I didn't know was that you had to pay (become a member of the scrabble something-or-other) to get access to the list. Since this was just a small pet project, and I was a poor college student, I didn't want to pay for a word list I would probably only use this one time (then maybe a few random times after just because I already had it. *Maybe*). You might be supprised how difficult it is to find a SQL input file of every word in the english language. Or, for that matter, a simple text list of "all" (a lot) of the words, which I moved on to after a while of searching. I ended up with a *semi*-complete list of *most* of the *common* words in the english language. Bassically, I had a massively incomplete list of english words which, as I found out not too long after, did not have all of the words in the common list used by Squaredle (I expected as much for the bonus words).

So, I had to write a whole other script to input this massively-incomplete list of words into a database. This program ended up being much more useful than I originally anticipated. Thus the 'database.txt' file (input) and the 'input_Database.py' files happened.

Once I had a list of words to check the possible combinations with, I incorporated that into the program, eventually moving to inside the function that made up the combinations (instead of storing every-single-possible-cobination), saving a bunch of processing power I didn't need anyways (But, it made me feel good). If you've noticed, there are actually 3 Squaredle programs. That's intentional. Each has a different purpose:

'squaredle.py' — The base script. It runs through the whole process and just dumps the output in the console (I use a terminal / CLI to run my programs; Yes, I'm weird to not use a IDE to run them).
'squaredle_input.py' — This does the same thing as the base script, but adds on the typing-to-input functionality.
'squaredle_search.py' — Instead of checking each combination with the database, this version just inputs (types) each possible combination in order to find all of the other words missing in the database.

**Letter-Boxed**
This is a small puzzle game in the NYT games package. Bassically, you have a square with 3 letters on each side (letters repeated, just never on the same side). You make words by combining letters in any order, the only limit being that the next letter had to be on a different side than the last. But, you could use each letter as many times as you wanted to (including in the same word). The goal is to use every letter in as few words as possible.

So this one actually dissapointed me a bit. First, I made the program, using hard-coded sides as the *"input"*. Part-way through coding the logic, I decided to fix the input (automatically grabbing the letters on each side, instead of hard-coding them) before implementing the word-check part. This is when I came across, right there, in plain text, already in JSON format, all of the game data. This data included not just the sides and which characters went where, but a list of every single word that would be accepted and... *THE ANSWER*... Completely needlessly, they included one of the combinations of words that used all the letters in the least number of words. Not that many people are going to be casually digging around the HTML/JavaScript, but even to run the game completely browser-side (never sending anything to a server to check words or something), you don't need the answer... I don't know... For whatever reason, after finding that, the whole game lost a lot of its appeal to me. Nonetheless, I did finish the program, using their list of words to check if something is an acceptable word or not (the rest of the calculation & combination-making is still done using an algorithm; Basically, I just replaced checking the database with checking their list).


All-in-all, they were fun projects to dink around with for a bit.
