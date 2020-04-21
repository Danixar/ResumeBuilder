ResumeBuilder - Python Project

Author: Evan Wiegers

April 2020

This little project is meant to create resume PDF's which are tailored for a specific job posting. To edit the 
information in the resume, edit the variables in Main.py - to alter the structure or format of the resume itself alter 
the function build in Builder.py in the Support package.  This project makes use of custom-made classes and packages, 
website scraping with BeautifulSoup, small amounts of html, and reportlab's PDF creation; as such, install the 
aforementioned packages if you have not done so already.

To use this script do the following:

1) Download this project from GitHub

2) Run Main.py either on the command line or through an IDE such as Pycharm

3) Once prompted, enter the name of the posting or None if there isn't any.  If not none, additional prompts may, 
depending on your responses, ask for the posting URL, company, and company address, and whether you want to produce a 
cover letter as well - answer all of the prompts properly and thoroughly

4) The new, tailored PDF should then appear in the Resumes folder
