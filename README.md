# Project Runtime Terror

# PLEASE MERGE YOUR BRANCH TO DEVELOPER FIRST AND THEN UPON REVIEW TO MASTER

![whiteboard](https://user-images.githubusercontent.com/36493057/65994159-afdcfe80-e460-11e9-9c93-bd582da3f732.jpg)

## Project Abstract
Creating schedules every semester is a stressful and time-consuming process, especially with the unintuitive way TU Portal displays class data. This application uses a public facing version of the Self-Service Banner class search function to obtain data on classes and present it in a more useful format. Users input their desired classes and the application will present a calendar-view of the different possible schedules with those classes. This goes a step further than tools such as Coursicle, which still force you to manually select classes and figure out which ones work together.

![schedulemaker](https://user-images.githubusercontent.com/36493057/65994158-afdcfe80-e460-11e9-9673-721ce5b85e96.png)
![schedulemaker-class](https://user-images.githubusercontent.com/36493057/65994160-afdcfe80-e460-11e9-9a8b-69f60add02c4.png)

This project already has some previous foundational code that can be viewed [here](https://github.com/paulhutchings/tu-schedule-maker). The existing code is written in JavaScript for NodeJS, but it does not have to stay that way.

## Project Relevance
This project is relevant to the goals of CIS 3296 as it incorporates many topics and concepts, including, but not limited to:
*	Testing (and Test-Driven Development) - since we are relying on outside actors, unit testing will play a big role in ensuring that the data the application receives is correct. It will also be necessary to test the schedule-generating algorithm to ensure that it does work as intended.
*	Database access - While optional, I believe that this project could benefit from integrating with a database, to hold the data in a more usable and easily accessible format to be used by the application.
*	UML - various types of UML diagrams can be created to illustrate and plan the architecture of the application before code is written, saving time and hassle.
*	Design patterns - There are several problems facing this application that may be solvable with existing design patterns.
*	Version control - I would like to see this project extend into the future beyond this class, which means adding new features, and maintenance. This requires keeping track of different version as new features and fixes are developed.
The project would be available for students to use once completed, and the principles learned in this class could be further applied to refine and improve the software by adding new features.

## Conceptual Design
There are several parts to this project. The core element that drives it is the algorithm that creates the schedules. There is a back end, which includes sending requests to the Temple server to keep the data up-to-date, parsing the HTML responses (the server won't return anything else, I've tried), and potentially putting the data into an intermediate database to have on-hand for the application. The front end would be one or more web pages to provide the application with a user interface to collect input and display the results.
I am able to work on any aspect of the project, though I feel I would be most equipped to implement the algorithm and parts of the back-end, as I do not have very much experience in front-end web design.

## Additional Insights
Luke: Web scraping can often be unreliable as web sites can randomly block a scraper through pattern / bot detection. Additionally, if a web sites design changes, the entire parsing process can change. ALthough we may be able to scrape periodically, it would be a good idea to cache scraped information in a database or get direct access to a database to avoid web scraping altogether.

Saad: Writing a robust web scraper is often difficult because many sites try to prevent web scraping activities.Scraping simple website that don't have js/ajax mechanism is not easy but simpler websites work just fine. Since Temple does not let us scrape their website, we should try to get access to Temple's database.
Problem arises when we scrape the data manually as the website does not allow a bot to interact with certain elements. As such we need to add in manual clicks to it to get arround it


## Required Resources
- Group members 
   * Knowledge of front-end web design and databases/cloud services
- Hardware and software resources required:
   * Server/hosting (consider AWS/cloud)

## Additional Insights
- Luke:
  Web scraping can often be unreliable as web sites can randomly block a scraper through pattern / bot detection. Additionally, if a web sites design changes, the entire parsing process can change. ALthough we may be able to scrape periodically, it would be a good idea to cache scraped information in a database or get direct access to a database to avoid web scraping altogether.
  
  - Dishant:
    Although we are trying to scrape coursicle, it might be better to scrape directly from the temple course offering that are available to the open public. This might create issues with Temple that might have to be dealt with later on.
## Environment
- Programming Language: Python3, Oracle SQL, HTML, CSS, JavaScript
- Development Environment: Android Studio, Emacs, Oracle SQL Developer
 
## Team Members
-Ahmad Saad
-Luke Jakielaszek
-Dishant Patel
