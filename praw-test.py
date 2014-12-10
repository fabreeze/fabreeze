# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Journal 
# 
# by /u/fabreeze <br>
# created on Dec 8, 2014

# <markdowncell>

# ##### Info about version control 
# 
# [git syntax tutorial](http://nbviewer.ipython.org/github/demotu/BMC/blob/master/notebooks/VersionControlGitGitHub.ipynb)

# <markdowncell>

# To clone this repo: <br>
# > git clone http://www.github.com/fabreeze/fabreeze.git

# <codecell>

%%bash
git add praw-test.ipynb praw-test.py

# <markdowncell>

# ### Save and commit changes to remove repository (github) 
# check terminal to input UN/PW

# <codecell>

%%bash 
git commit -a -m "saving notebook"
git push origin master

# <markdowncell>

# ### Save and hard reset local to mirror remote 
# [how-to source](http://stackoverflow.com/questions/1628088/how-to-reset-my-local-repository-to-be-just-like-the-remote-repository-head)

# <codecell>

%%bash
git commit -a -m "Saving work, just in case"
git branch savedwork
git fetch origin
git reset --hard origin/master

# <markdowncell>

# #### To install ipython notebook
# > sudo apt-get install python-pip <br>
# > pip install "ipython[all]"

# <markdowncell>

# To start an ipython session: 
# > ipython notebook --script

# <markdowncell>

# #### Useful extensions

# <markdowncell>

# Version Information Extension
# > %install_ext http://raw.github.com/jrjohansson/version_information/master/version_information.py

# <codecell>

%load_ext version_information

# <codecell>

%version_information

# <codecell>

!date

# <codecell>

from IPython.display import HTML
HTML('<iframe src=https://praw.readthedocs.org/en/v2.1.19/pages/getting_started.html width=700 height=350></iframe>')

# <markdowncell>

# ** Install PRAW**
# > pip install praw

# <markdowncell>

# ### Example 1: redditor karma by subreddit

# <codecell>

import praw
import pprint
user_agent = ("PRAW karma breakdown bot 0.1 by /u/fabreeze"
              "github.com/fabreeze/fabreeze")
r = praw.Reddit(user_agent=user_agent)
# Breaking down redditor karma by subreddit excercise
user_name = "fabreeze"
user = r.get_redditor(user_name)
thing_limit = 10
gen = user.get_submitted(limit=thing_limit)
karma_by_subreddit = {}
for thing in gen:
    subreddit = thing.subreddit.display_name
    karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0)
                                     + thing.score)
pprint.pprint(karma_by_subreddit)

# <markdowncell>

# FIN.

# <codecell>

from IPython.display import HTML
HTML('<iframe src=https://praw.readthedocs.org/en/v2.1.19/pages/writing_a_bot.html width=700 height=350></iframe>')

# <markdowncell>

# ### Example 2: persistent bot

# <codecell>

import time
import praw
import pprint
username = 'fabreeze'
r = praw.Reddit("PRAW tutorial example2 monitor bot 0.1 by /u/fabreeze"
              "github.com/fabreeze/fabreeze")
r.login(username) # syntax: r.login('username','password') | in this case, pw is prompted in terminal
already_done = []

#while TRUE:
    #subreddit = r.get_subreddit('learnpython')
    #for submission in subreddit.get_hot(limit=10):
submission = r.get_submission(submission_id = "105aru")
pprint.pprint(vars(submission))

# <codecell>

qtconsole

# <codecell>


