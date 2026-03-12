<!-- First impressions -->
At the beginning, I was very unclear about how I'm gonna go through with every step, so it basically seemed like every other project where we have to use brute force to figure things out. 

To specify, I didn't know where to start, which functions to use, how to manage my states; oh, and I knew absolutely nothing about testing!

My approach to complete the assignments was first through the slides which were very clear on the instructions and then ask many many questions from copilot to shape some kind of idea of the next steps. That's why I used a free model.


<!-- Key Learnings -->
1.The thing I enjoyed learning the most and made the assignment actually fun was the socratic mode. The questions were actually really helpful! It helped me structure my mind on how to shape the project not just code around.

2.Also, I learned a thing or two about clean code structure. For example keeping a function "pure", treating parameters as immutable, and keeping logic separated from the UI, keeping different parts of logic itself separated

3.The way the agent was really interesting. It made me wanna create my own agent to help me learn more effectively or in other areas where I encounter a problem on a daily basis

4.Tests! Unfortunately I did not get the time to write the tests myself but I learned a lot about how they work and I think now TDD makes more sense to me. I understand that TDD is not scalable but with the help of AI and a developer who knows what's at stakes in their application, TDD can actually save A LOT of time later in the project

<!--CoPilot Prompting Experience -->
The questions copilot asked actually taught me to prompt better. For example, instead of "fix this", try to ask CoPilot more speciifc questions by going through my logic first. Instead I'd ask "I know the .venv is activated and I'm running the test from the root but pytest is still failing" so it would give me a more helpful answer. 

The only prompts that I would consider "ineffective" were the ones where although CoPilot had access to my files, it couldn't tell why pytest was failing. I still haven't figured out why. I opted for an alternative for this one

<!-- Limitations and Reliability -->
I haven't really faced any hallucination per say but the issue I mentioned above where it just couldn't find out the reason behind the ModuleNotFound error still remains a question for me as though why that happened.

P.S. I just ran into this while trying to generate tests. The new tests are no different than the last tests and still ambiguous although I asked CoPilot to make the tests point to something rather than showing me unclear test results.

<!-- Overall Reflection -->
Overall, the usage of AI in the project felt like a patient senior developer/mentor guiding me through my code which made me feel less miserable in terms of shaping the architecture of the project.
Also, throughout the few frontend projects that I worked on before, I had noticed that when you don't have a grasp on the project structure and don't think about error handling from the very beginning, there will be a lot of time needed for debugging and testing which could have been avoided by thinking about them at the beginning, which was exactly what felt right during this project!