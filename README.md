# Stackoverflow-lite-APIs

# Stackoverflow-lite-application endpoints


## The following are API endpoints that allow a user to:
    - Create an account and log in.
    - A user can post questions.
    - A user can delete questions they had posted.
    - A user can post answers
    - A user can view the answers
    - A user can accept an answer out of all the answers to his/her queston as they preferred answer
    - A user can upvote or downvote an answer.
    - A user can comment on an answer.
    - A user can fetch all questions he/she has ever asked on the platform
    - A user can search for questions on the platform
    - A user can view questions with the most answers.

#  Here is a list of the expected endpoints
#### Users Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/auth/signup` | Add a user
GET | `/api/v1/auth/users` | Lists all users
GET | `/api/v1/auth/users/{user_id}` | Retrieve a user
POST | `/api/v1/auth/login` | Login a user

#### Questions Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions` | Add a question
GET | `/api/v1/questions` | Lists all questions
GET | `/api/v1/questions/?q={search_string}` | Search a questions
GET | `/api/v1/questions/{question_id}` | Retrieve a question
PUT | `/api/v1/questions/{question_id}` | Edit a question of a logged in user
DELETE | `/api/v1/questions/{question_id}` | Delete a request of a logged in user

#### Answers Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions/{question_id}/answers` | Add an answer
GET | `/api/v1/questions/answers` | Lists all answers
GET | `/api/v1/questions/answers/{answerID}` | Retrieve an answer
PUT | `/api/v1/questions/{question_id}/answer/{answerID}` | Edit an answer
DELETE | `/api/v1/questions/{question_id}/answer/{answerID}` | Delete an answer
POST | `/api/v1/questions/answers/vote/{answer_id}` | Upvote/DownVote an answer
POST | `/api/v1/questions/answers/comment/{answer_id}` | Comment on an answer


# Testing the endpoints
Install python then using pip install, install flask.
clone the repository
Ensure that postman is installed.
From the terminal,locate the repository and run python run.py
Open postman and test the endpoints



## Credits
This challenge was part of the Bootcamp 36 NBO Andela.

## Author
Michael Mbugua.

## Contribution
Fork this repository, contribute then create a pull request to the gh-pages branch.

