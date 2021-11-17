[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6324575&assignment_repo_type=AssignmentRepo)
# Named-Entity Recognition THA
In this assignment you will assess named-entities of college football teams from ESPN. This assignment is a little more complicated than the ICE because of how ESPN presents the data on the website. The difficult part is pulling the data from ESPN; however, I do provide you some guidance as to how to accomplish this.

To submit, please perform the following:
1. Push your Python script file to GitHub.
1. Upload your Word file to GitHub.
1. Push your tab-delimited file exported from Python to GitHub.

### Pulling Data from ESPN (8 pts.)
In this assignment, you will pull data from ESPN for college football matches in order to determine the most impactful players. Navigate to [ESPN's college football scores](https://www.espn.com/college-football/scoreboard). You should see the scores from the top 25 ranked teams. Select 3 games you will pull data from. If OSU or BYU is in the top 25, then you will use them for this assignment; otherwise, you are free to select any team. For each game, using `Selenium`, retrieve the play-by-play data for all types of plays, not just scoring plays.

If the `Play-by-Play` link is not shown, then using `Selenium` you can navigate to the play-by-play information by clicking the `Box Score` link; then on the menu that appears on the new webpage, click `Play-by-Play`.

You will need to create a dataframe with 3 columns: `play`, `team`, and `opponent`. Insert each individual play as a record into the dataframe where `play` contains the text of the play, `team` contains the name of the team who is on offense, and `opponent` is the name of the team playing defense.

ESPN does not list who is on offense with text; the only indication is a logo, which is a png file. Luckily, each team has a unique filename for the png file. For example, BYU's is `252.png`; OSU's is `197.png`.

At first glance, it may appear you need to hard-code the values. Yet, one way of automating this part is creating a function that assigns the team name in text based on the png filename. How would you make this dynamic and flexible for each webpage you scrape? Look at the top of a play-by-play page. Each team will have team info listing the team name and logo, fairly close together. You can obtain the png filename and the team name using xpath. It would be a simple matter of storing all the team names and png filenames as a dictionary (with key-value pairs).
  
Here are the xpaths for that info for both teams:
  * Team Logo: `//div[@class="team-container"]/div[@class="team-info-logo"]/div[@class="logo"]/a/img`
  * Team Name: `//div[@class="team-container"]/div[@class="team-info"]/div[@class="team-info-wrapper"]/a/span[3]`

For this part, perform the following tasks:
* Create a function that assigns the team's name based on the png filename (see [here](https://www.w3schools.com/python/python_functions.asp) for a refresher on Python functions) (3 pts.)
* Scrape the play-by-play data (3 pts.)
* Store the play-by-play data in a data frame (1 pt.)
* Export the data frame as a `csv` file (1 pt.)

### Extracting Named-Entities (2 pts.)
Now that you have the plays of each game saved into a dataframe, you need to extract the names and perform a little analysis. Perform the following analyses:
* For each match, determine the top 2 frequently mentioned names (1 pt.)
*	Based on your findings, for each match, who do you feel is the top contributing player? (1 pt.)# homework1
