# backend-login

# Purpose
To create a fully functioning backend system with security using Flask and PostgreSQL  

# Used...
Python, Flask, PostgreSQL, Migration, SQLAlchemy, Bcrypt, JWT.  
Used migration to make it easier to update the tables in postgresql.  
  
# How does it work?
running the app.py will initiate the server. On the frontend, there are two textbox with placeholders of 'id' and 'pw'.  
Also, there are four buttons on the page.  
  
The submit button will allow the user to try logging in. The server will try to find the user input from the db. If the user information is not found on db, it will return 'wrong id/pw' page to the user. If found, allows the user to log in, providing the cookie with an access token created using jwt.  
  
The create button allows the user to create their account. If the input id is found in the db, it will alert the user that id is already being used. If not, it will save the id, and hash the pw using bcrypt before storing it into the db.  

The add button simply returns the value of id+pw.  
  
The security button will allow the user to have access only if the user has the access token. If the user is logged in(has the token in their cookie), it will allow user's access. If not, access will be denied.  
  
# Further more plans...
I am currently studying AWS to create my own website. Once made it, I will integrate the other agentic AI projects into the website, studying deeper into the backend systems.