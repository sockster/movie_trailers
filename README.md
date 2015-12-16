README
12-2015
my_movie_data.py Movie Trailer Page
	




-----> WHAT'S NEEDED
- Python must be installed in the working environment (your computer or server)
- A browser (no Internet connection needed, though)
- Files:
  > my_movie_data.py
  > media.py
  > fresh_tomatoes_1.py  NOTE: you MUST use the "_1" version of fresh_tomatoes
	




-----> INSTALL PYTHON
You may already have Python installed on your computer.

  To check, simply open a Command Line or Terminal window.
  Just type the word:
     python
     
  Python is already installed if you see something similar to:
     Python 2.7.10 (default, Jul 14 2015, 19:46:27) 
     [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
     Type "help", "copyright", "credits" or "license" for more information.
     >>> 

  If you don't see something like the above test, you'll need to install Python.
  The following guide will help you through this (pretty) painless process:
  https://wiki.python.org/moin/BeginnersGuide/Download
	




-----> RUNNING THE SCRIPT
Once you know you have Python installed, you're ready to go!
  - Put the 3 files (my_movie_data.py, media.py, and fresh_tomatoes_1.py) in a folder together
  - In your Command Line or Terminal window, navigate to the folder you just created containing the 3 files
  - Type the following (you may want to copy-and-paste it):
  
    python my_movie_data.py
	(that's: python [SPACE] my_movie_data.py)

  - The script will open a browser window (or new tab, if your browser was already open), and
  - Present the movie trailer page to you
  - Clicking on a thumbnail of a movie poster will show you the trailer for that film

  ENJOY!
	




-----> UNDER THE HOOD
my_movie_data.py:
  - Imports the functions contained in fresh_tomatoes_1.py and media.py
  - Contains the (text and URL) data for each film
  - Calls fresh_tomatoes_1.py's module to open a web page and display the data
  
media.py
  - Defines the objects within the class "Movies"
  - Defines the action of the module show_trailer
  
fresh_tomatoes_1.py
  - Imports 3 Python built-in functions to take advantage of modules contained therein
  - Calls the Bootstrap framework for the site
  - Sets up the CSS styles to use in this movie trailer site
  - Calls the module to create the output HTML file
  - Calls the dynamically created content to populate the HTML file
  
  
  
  

