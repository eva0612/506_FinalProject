506 Final Project Readme_Kehan Liao



1. To be specific I used the number of football ticket sales to compare the relationship between the popularity of football game and the degree of competitiveness. So, I extracted the number of times that the resell and request of specific games from Facebook group “Maize Market”, to compare with the game statistics(home team, away team, home points, away points) extracted from Sportradar.com. 

The output analysis, as you can see from the excel sheet (see ResultSheet.xlsx) that R Square = 0.142368624 which means that there's no significant correlation between the popularity of the team and the inquiries of the tickets. But it is also biased due to the limited amount of the data.

2. You will need to download and import the packages (see package list in 4.)before you can run the python file (name: 506_Final_KL.py). After it done running, you can open excel file name:"games.xlsx" and see the game results generated from the program. You don't need to type in anything. 

In games.xlsx, Message Count is the data from Facebook that the number of times each team appeared in the group posting. Away team, Home Team, Away Point, Home Point are data from sport radar.

You should also look at the file ResultSheet.xlsx to see the anaylsis, sheet 1 in ResultSheet.xlsx is the same data as the "games.xlsx" (in case the games.xlsx doesn't work). 


3. Files that are submitted:
	python file: 506_Final_KL.py
	facebook cached data file: cached_fb.txt
	sportradar cached data file: srcached_results.txt
	excel analysis: ResultSheet.xlsx
	README.txt
	506 Final Project Plan_KL


4. Python packages that used:
   pandas
   requests
   json
   pickle
   csv
   unittest

5. Two APIs that I used:
	API for Facebook: https://developers.facebook.com/tools/explorer
	API for Sportradar: http://developer.sportradar.com
	
	* Ideally there's no need to do anything else besides install the packages to run the code, since all the data is in cached file and saved locally. In case the cached file don't work:
	1). Since the Facebook require the access token, so the person whoever needs to run my program has to be in the Facebook group (Maize Market), and paste their access token to my python code. Or, I could also provide the cached data for him/her to see my source.
	2). To access Facebook API needs the user to login to Facebook to get the access token, in which to get access to MarketNoire group ID. To access Sportradar API need to register for account first and get API keys to access the data. 

6. Approximate line numbers in Python file to find the following mechanics requirements:
- Sorting with a key function: 17
- Use of list comprehension OR map OR filter: 93
- Class definition beginning 1: 84
- Class definition beginning 2: 163
- Creating instance of one class: 100
- Creating instance of a second class: 190
- Calling any method on any class instance (list all approx line numbers where this happens, or line numbers where there is a chunk of code in which a bunch of methods are invoked): 84-98; 163-187
- (If applicable) Beginnings of function definitions outside classes: 148
- Beginning of code that handles data caching/using cached data: 28; 128
- Test cases: 208


8. Rationale for project: why did you do this project? Why did you find it interesting? Did it work out the way you expected?

I was always wondering if there's a correlation between the game popularity and the game competiveness. It's less correlation than what I have expected.





