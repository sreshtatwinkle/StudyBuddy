# StudyBuddy

The Django project named StudyBuddy has different apps(which can be visible as different folders).
the following are the apps and provided on what they address in the project.

StudyBuddy(folder) -

StudyBuddy is the  project app where all the sub apps are connected through settings.py and urls.py.
DATABASE - As main functinality of this project is thorugh database , The connection of database i.e. postgersql is in Studybuddy/settings.py

StudyBuddy_main_app(folder) - 
This is the main app where it contains the base url page 


userprofile(folder) -
This app contains all the python code that is used for Authentication purpose. both login and registration code are written in userprofile/views.py . 
it is connected to main StudyBuddy project app thorugh userprofile/urls.py

chat_app(folder) -
This app contains all the python code that is used for chatting and connecting users. 
The whole python code of chatting has been included in chat_app/views.py.
it is connected to main StudyBuddy project app thorugh userprofile/urls.py.

static folder -
static folder contains all the image files,css files in it.

Templates folder -
This is the folder where i have provided all the html files in.
