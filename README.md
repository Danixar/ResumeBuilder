# ResumeBuilder - Python Project

Author: Evan Wiegers

April 2020

**Note:** This program's code is lackluster at best and needs to be updated to utilize more of an declarative programming paradigm. In hindsight, I really should have done this in Node.

This project is meant to create resume PDF's which are tailored for a specific job posting. To edit the 
information in the resume, edit the variables in Main.py - to alter the structure or format of the resume itself alter 
the function build in Builder.py in the Support package. This project makes use of Docker so be sure to have that downloaded.

# How to use: 

1) Download this project from GitHub and navigate towards the project folder

2) On the command line run something like this :
	```bash
	docker build -t resumebuilder .
	docker run --rm -it -v /Users/evanwiegers/Downloads:/home/resumes resumebuilder
	```

3) Once prompted, enter the name of the posting or None if there isn't any.  If not none, additional prompts may, 
depending on your responses, ask for the posting URL, company, and company address, and whether you want to produce a 
cover letter as well - answer all of the prompts properly and thoroughly

4) The new, tailored PDF should then appear in the folder volume mapped to the /home/resumes folder
