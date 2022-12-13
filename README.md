# How this works

   Summit schools grade projects (worth 70% of the overall grade) in a weird way.
Each final product (checkpoints do not count for grades) is graded on several points, known as cognitive skills or rubric dimensions.
The highest score given for each cognitive skill/rubric dimension in a given class is the overall cognitive skill.
the average of all overall skills becomes the overall grade for the unit.

   This system makes some projects (ones that have a lot of skill you dont have a good grade in) much more important to overall grades.
This program find combination of products that provide the best grade with minimum effort.

# System requirements

You must have [python 3](https://www.python.org/downloads/) installed.

This cannot be done on a Chromebook without enabling developer mode. (This means you cant run this on a school laptop without getting IT to unlock it first).

You must also have the required dependency's installed. This can be done by running ``pip3 install -r requirements.txt`` at the root of the project.

# Running it.

## Obtaining your cookie

Your browsers cookies are small text files used by servers to keep track of devices for authentication purposes.
To allow this program to see your platform, you must obtain your cookie string (**DO NOT SHARE THIS WITH OTHERS (even me), IT WILL GIVE THEM ACCESS TO YOUR ACCOUNT**).

1. Go any page on the platform.
2. Open developer tools (Ctrl-Shift-I in most browsers)
3. Go to the "Network" tab
4. Reload the page
5. Click on the first request (the one at the top, you will have to scroll)
6. Find the window now showing "Response Headers", scroll the window down until you see "Request Headers" and later ``cookie: ``
7. Right click on the line starting with ``cookie`` and click "copy value"
8. At the root of the repo, create a plain text file called ``cookie`` and paste in the long string (on one line) and save it.

## Collecting data

The script collects data for a single school year, this is the number at the end of the url when you are looking at the timeline: ``https://www.summitlearning.org/my/year/[YEAR]``

Run ``python3 api.py [YEAR]``, replacing the YEAR with current academic year number (2023 as of this writing).

It will download data for each course you are a part of and save the resulting data in a file named "data.json". (This should take less than a second)

## Analyzing it

Now, run ``python3 solver.py`` and it will display a list of all projects in descending order of importance for every class.

The number to the left of the URL is the grade you will get in that class if you stop at that one. (This is the *project* grade, which maxes out a 70% of the actual grade on your transcript)

This is an snippet of what the output will look like:

```
# Intro to Visual Arts [DE] #
        53%     67%     https://www.summitlearning.org/my/projects/1792527/     Design Theory
        76%     83%     https://www.summitlearning.org/my/projects/1792525/     Illustation
        100%    100%    https://www.summitlearning.org/my/projects/1815604/     Human proportion
```
The columns are: **% skill average** if all projects before and including this one are compleated, The **overall grade** if you do so, The URL of the project, The **Name** of the project.

If you do just these 3 projects (out of 7!) you will get 100% on projects, for a *minimum* of 70% on your transcript. 
This will be the case even if you get a **0** (You must submit something, but the grade does not matter) on all other projects.
Just *two* projects are required to pass.

```
# Physics in the Universe [DE 22] #
        71%     80%     https://www.summitlearning.org/my/projects/1800199/     Going in Circles with Asteroids
        100%    100%    https://www.summitlearning.org/my/projects/1800198/     Sound and Light
```

One project is enough to get a B- overall (assuming 100%), and two (out of 4) can get you 100%!
