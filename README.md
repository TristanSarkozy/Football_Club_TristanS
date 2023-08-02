# FOOTBALL CLUB TRISTANS

## Purpose of the project
The Football Club Automation System is a web application that allows users to manage and track player information for a football club. The application is designed to provide a user-friendly interface for adding, editing, and listing players, as well as integrating with Google Sheets for data storage and management.
The deployed version can be accessed here:
https://football-club-tristans-08ff5ecdb235.herokuapp.com/

![UI dev 2023-08-02 18-03-12](https://github.com/TristanSarkozy/Football_Club_TristanS/assets/114732027/7fd6bdb4-1fe3-4695-8bfc-dc7e91c1507a)

## User Stories
The project is driven by user stories that reflect the needs and expectations of various users, including club administrators, coaches, and members. These stories guide the development of features to ensure that the application addresses real-world requirements.
- As a club administrator, I want to add and manage player information easily.
- As a coach, I want to update player details and search for specific players.
- As a club member, I want to view the player list and know the total number of players.

## Features
### Home Page
- When users access the application, they are greeted with a home page that displays the title and the choices;
![home page 2023-08-02 18-32-32](https://github.com/TristanSarkozy/Football_Club_TristanS/assets/114732027/263d695d-e6a2-4211-9324-caf1e9a394fd)
### Add Player
- In this section, users can input player details, including the player's name, age, number of goals scored, and number of games played.
- The application validates the input data to ensure that it meets certain criteria (valid name, valid age range, numeric goals scored and games played).
- If the input data is valid, the application adds the player to the football club's roster and updates the corresponding Google Sheets document with the new player's information.
![Add player 2023-08-02 18-42-55](https://github.com/TristanSarkozy/Football_Club_TristanS/assets/114732027/1c71c855-9b93-4f0e-aa64-efbf93bdaa10)
- If the input data is invalid, the application displays an error message indicating the issue (names should contain only letters, age out of range, non-numeric values), and users are prompted to correct their input.
![Invalid choices 2023-08-02 18-46-57](https://github.com/TristanSarkozy/Football_Club_TristanS/assets/114732027/f1c41451-b323-4886-83ee-e85d48f079e0)
- a message if the player's name already exists.
![player exists 2023-08-02 18-49-51](https://github.com/TristanSarkozy/Football_Club_TristanS/assets/114732027/6b22813e-8744-446e-91a0-9e6fce0992af)
### List All Players
- In this section, the application displays a list of all players currently in the football club, along with their names, ages, goals scored, and games played.
![list all players 2023-08-02 18-54-36](https://github.com/TristanSarkozy/Football_Club_TristanS/assets/114732027/6e64ebd6-e413-48c4-9921-ac8316b7bb0b)
### Edit Player
- In this section, users can select a player from the list and edit their details, including age, goals scored, and games played.
- The application validates the edited data similar to the "Add Player" section and updates the player's information.
- a message is displayed if the name was not found.
![Edit player 2023-08-02 19-03-28](https://github.com/TristanSarkozy/Football_Club_TristanS/assets/114732027/a80f4bd4-1243-4bd9-8201-fdb3fe6f189f)
### Exit 
the application displays a message when exiting the program.
![exit 2023-08-02 19-09-18](https://github.com/TristanSarkozy/Football_Club_TristanS/assets/114732027/45193176-de82-4b04-b625-a1c4eac625e8)
### Error Handling
- Throughout the application, proper error handling is implemented to catch various types of errors, such as invalid inputs, missing player names, or issues with updating Google Sheets.
- When errors occur, the application displays clear error messages to guide users and provide feedback on what went wrong.
### User Interface
- The application uses HTML templates to provide a user-friendly interface for inputting data, viewing player lists, and displaying error messages.
### Google Sheets Integration
- The application integrates with Google Sheets to store player information in a structured format.
- It uses the gspread library and Google service account credentials to authenticate and interact with Google Sheets.
![gspread 2023-08-02 19-15-11](https://github.com/TristanSarkozy/Football_Club_TristanS/assets/114732027/5204d14e-db53-4f76-be68-e5f05669e55f)
## Future Features
 
 A 'delete player' option to delete a player from the club and Google Sheets.

 ## Flowchart
 This flowchart provides a visual representation of the logical flow and decision points within the Football Club Automation System.
 ![Flowchart 2023-08-02 21-15-55](https://github.com/TristanSarkozy/Football_Club_TristanS/assets/114732027/eb44ba05-0d93-447c-93a1-a23fb6ec1e51)

## Technology
- Python for the backend logic.
- HTML for the frontend user interface.
- Google Sheets API (gspread) for integrating with Google Sheets.
- Github.
- Gitpod
- Heroku for deployment.

## Testing
The code was manually tested by doing the following:
- Passed the code through a PEP8 linter and confirmed there are no problems.
- The functionality was checked step by step with invalid inputs.

## Fixed Bugs
- Only minor bugs were found.

## Deployment
- Application developed and tested using Gitpod, a cloud-based development environment.
- The application is designed to be deployed on the Heroku platform, making it accessible to users via a web browser.
### Steps for deployment:
- Create a new Heroku application.
- Create a new Config_Var.
- Set the buildbacks to Python and NodeJS.
- Link the Heroku app to the repository.
- Click on Deploy button.

## Credits
- Love-Sandwiches project.
- Code Institute support(Slack groups, mentor, LMS).
- Stack Overflow, Youtube, W3Schools.