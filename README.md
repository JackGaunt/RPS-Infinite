# RPS-Infinite
<!-- TABLE OF CONTENTS -->
Table of Contents
<ol>
	<li><a href="#about-the-project">About The Project</a></li>
<li><a href="#code-description">Code Description</a></li>
<li><a href="#grid-visualization">Grid Visualization</a></li>
<li><a href="#whats-the-point">What's the Point?</a></li>
</ol>

<!-- ABOUT THE PROJECT -->
## About The Project
Basic rock, paper, scissors program that uses an interesting way to determine who won.

RPS is defined by having three moves. Rock, paper, and scissors. But there can be more.

One of the more famous "improvements" is rock, paper, scissors, lizard, spock where there are five moves. This can be continued forever although it may get even more confusing.

At some point, I though about grids and how each element on a grid can be defined as a sum of its row and column number. 
Not too exciting but what if we changed those indices from incrementing numbers to odd numbers or squared numbers. 
I then combined this with the idea of an RPS game where more and more moves are added.

<!-- CODE DESCRIPTION -->
## Code Description
The code itself is pretty simple.
The user is asked for a size of the game. This must be an odd number and greater than 2, ex. 3.

The user can then choose their move and the computer chooses theirs using the random package.

The computer's calculated move is chosen randomly between 1 and the number of moves inclusive.
The computer's move is then multiplied by 2 to the power of (num_moves - 1) / 2 to get the computer's calculated move.

The computer's calculated move and the human's move are then added together.
* If that number modulo the number of moves is equal to 0, there is a draw.
* If modulo is less than the number of moves divided by 2, human wins.
* If modulo is greater than the number of moves divided by 2, computer wins.

<!-- GRID VISUALIZATION -->
## Grid Visualization
H = Human move
C = Computer move
* If box blue, human wins.
* If box orange, computer wins.
* If box grey, draw.
![RPS_Visualization](https://user-images.githubusercontent.com/90910858/150020392-547d233f-e92b-4536-8986-fcd06834bcfd.png)



<!-- What's the Point? -->
## What's the Point?
Using this code for an actual RPS program makes no sense. 
It is much easier and faster to just say, if the human move is greater than the computer move and not less than the total number of moves / 2, human wins.
This would make the code even smaller, faster, simpler, and able to use more moves than this code ever could.
(Right now, it caps at 2001 because the computer can't automatically square a number bigger than that)

This code is more of a question to myself? I had a thought and wondered if it made sense. 
It did, and I was able to make a pretty short script to prove my theory.
Maybe this idea will be useful in the future, but for now, it's best proof of concept is an unoptimized RPS program.

The best part is that I can put this on my personal GitHub account for some quick satisfaction.
I can also test out GitHub for personal use as I've only used it for work.
This is not the most complicated code I've written, but it is the most complicated code I've done in my free time, and I am happy with the outcome.
