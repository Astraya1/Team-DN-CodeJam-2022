# TruckoMap: For 123LoadBoard Code.Jam() 2022
**Please review the [123LoadBoard Challenge for the challenge guidelines](https://codejam.123loadboard.com/).**

## Brief Description
This program allows truckers to find the most profitable trip to take when shipping loads sourced from a marketplace.

This program reads through a CSV file to then determine the most profitable trip a trucker can undertake. 

Truckers will start from a determined starting point and then drive to their destination nodes. Routes that connect each node are all linked to costs due to the driving costs. Some routes have profits linked to it if the route links you to the shipping destination.

## Team Members
- Justin Ma
  - GitHub: Astraya1
- Robert Liu
  - GitHub: Robert-liu3
- Jungsoo Lee
  - GitHub: jungsoolee1
- Howard Yu
  - GitHub: blissfulcat

# Post-Result Evaluation

## Inspiration
To figure out the most optimal path.
## What it does
The program was intended to find the most profitable path for truckers when fulfilling loads.
## How we built it
At first, we thought about implementing a customized bellman-ford algorithm to find the most profitable path. In the end, we realized the immense difficulty in basing our program through bellman-ford algorithm. We decided to pivot out program to a greedy algorithm. However, we ran out of time.
## Challenges we ran into
The possibility of multiple loads being in the same location proved a challenge to integrate in the bellman-ford algorithm. Furthermore, the time constraint associated to each trucker made it more challenging to figure out an algorithm.
## Accomplishments that we're proud of
We are proud that we have mastered the bellman-ford algorithm and tried to modify it to better suit our requirements. Even though we failed to realize the complexity of changing the bellman-ford algorithm, we have improved our skills in problem-solving and creativity.
## What we learned
We learned that charting out and breaking down every single requirements and instructions into issues and features is crucial to gain a full understand of the problem statement
## What's next for Team DN
We will try to solve this challenge after the hackathon.
