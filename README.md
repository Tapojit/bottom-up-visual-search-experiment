# Effects of Various Parameters on Bottom Up Visual Search

The purpose of this study was to better understand exogenous attention. Its design consists of participants detecting an item in a computer display that is different than the surrounding items and pressing a button on a keyboard to indicate they have observed the item that is different.

In total, participant sessions were run on **four conditions**, each of which contain multiple trials. On some trials, there are multiple items and on other trials there are only single items. Eg:

<img width="500" height="500" src="https://github.com/Tapojit/bottom-up-visual-search-experiment/blob/master/condition%203/studies/study%202017-04-25%2022_51_51.690479/frames/frame%201.png">

<img width="500" height="500" src="https://github.com/Tapojit/bottom-up-visual-search-experiment/blob/master/condition%203/studies/study%202017-04-25%2022_51_51.690479/frames/frame%200.png">

The goal of our study was to examine how different numbers of items, and visual properties of the items affect reaction times and accuracy. There are a few different visual parameters/conditions we tested for possible effects on these results. The basic design of the studies was a color-based single item vs. distractor visual search task, with responses to which corner (left or right) is
cut off of a “target” item. The target is distinguished from the distractors by it being the sole item of a different color, between the options of red or green.

One condition we varied was the general axis of display; all stimuli were arranged in a rectangular pattern, and we rotated the positions so that the rows appear in the shape of both a “tall” or “wide” rectangle. Other conditions tested include visual angles, number of distractors, color, and shape or size of targets/distractors.

*Check out [**this**](https://drive.google.com/drive/u/1/my-drive) document for a comprehensive explanation of the study*

## Getting started

The experiment was set up using a python-based open source platform called **PsychoPy**, which allows you run a wide range of neuroscience, psychology and psychophysics experiments. You can download PsychoPy from [here](http://www.psychopy.org/).

For each of the conditions, you can start the session by running **Expt.py** in PsychoPy GUI.

Each of the conditions contain their own **Expt.py** scripts to be run in PsychoPy GUI.

##  Roles
* **Julian Oks**(@julianoks)- implemented distractor frame generation in **distractors.py**.
* **Kirsten Lydic**(kol16@hampshire.edu)- ran participant sessions, carried out documentation and managed the experiment by coming up with conditions for participant sessions.
* **Tapojit Debnath Tapu**- implemented distractor frame display pipeline using PsychoPy. The pipeline codebase is available in **Expt.py**.
* **Ethan Meyers**- Faculty advisor for this study.
