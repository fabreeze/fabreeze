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
git commit -a -m "Saving my work, just in case"
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

# <markdowncell>

# ## [Codeacademy](http://www.codecademy.com/en/tracks/python)

# <markdowncell>

# ##### pig latin module

# <codecell>

original = raw_input("input word:")
word = original.lower()
first = word[0]
piglatin = word[1:len(word)]+first+"ay"
if len(original)>0 and original.isalpha():
    print piglatin
else:
    print "empty"

# <markdowncell>

# Try to adapt for protocol writing

# <codecell>


