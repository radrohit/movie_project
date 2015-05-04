# Movie List # 


The Movie-List webpage allows webuser to do the following: Add a new movie, view the movies added, edit the movies and do a simple search for a movie.

## Movie fields ##
- Movie Title (required)
- Movie Release date (required )
- Movie Description (required)
- Movie Poster 
- Movie MPAA ratings (required)
- Movie IMDB ratings (required)
- Movie Genre (required)

## Project background ##
The website is built using django framework and uses aspect from Django tutorial documentation. The movie information are stored in sqlite3 which is part of python installation. To change the database go to settings.py.
HTML is stored in movie_list>templates>movie_list and css is stored in static>css. The webpage use bootstrap for CSS.

## Installation instruction: ##
Use pip to install
1. Python v 3.4
2. PIP 
3. django v 1.8
4. pillow

uses database sqlite3

## Running instruction: ##
This is tested on local server using windows
and on codeenvy web server

### Instruction on local server: ###
Run in command line start.bat on movie_project directory to start the server

### Instruction on Codeenvy webserver ###

After opening an account
- Select import project
- Click From a git hub repository and paste the git clone url.
- Click configure and select the python Project and next
- Click python > web > python27_django and save
- Click run at the top
- After webserver runs for few minute webpage link appears at the bottom


## Future possible additions ##
 - Add cast field and details about the cast
 - Add trailer field for movie and play it in the site
 - Delete function




