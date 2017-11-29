# PROJECT - ITEM CATALOG

# WHAT THIS PROJECT INCLUDES 
 
 1) static folder - which includes a file styles.css
 2) templates folder - which includes the following html files
    - category.html
    - deleteItem.html
    - editItem.html
    - item.html
    - login.html
    - main.html
    - menu.html
    - newCategory.html
 3) database_setupy.py - conatins the setup for the three tables(user, categories and items) we use in this project
 4) items.py - contains all the sqlalchemy commands to populate the dara in the database
 5) application.py  - runs the flask application on localhost:8000
 6) client_secret.json - you need to create one.
 
 (NOTE: In case you get an error while loggin in, you might want to create your own client_secret.json file)
 
 # STEPS TO CREATE NEW client_secret.json
 
1) Go to your app's page in the [Google APIs Console](https://console.developers.google.com/apis)
2) Choose Credentials from the menu on the left.
3) Create an OAuth Client ID.
4) This will require you to configure the consent screen, with the same choices as in the video.
5) When you're presented with a list of application types, choose Web application.
6) You can then set the authorized JavaScript origins, with the same settings as in the video mentioned in the link below.
    (Usually set it as 1) http://localhost:8000 and 2) http://127.0.0.1:8000 )    
7) You will then be able to get the client ID and client secret.
8) Download the file and save it as client_secret.json in the same directory as your application.py file

you can get more information [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/348776022975461/lessons/3967218625/concepts/39636486130923)
 
 (NOTE: ALways save the file name as client_secret.json only)

# STEPS TO RUN THIS PROJECT

 1) Download [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
    
 2) After Vagrant and VirtualBox is successfully installed you will need to run the following commands
    
    - From your terminal, inside the vagrant subdirectory, run the command 'vagrant up'. (This may take some time if you're doing it for the first time )
    - When vagrant up is finished running, you will get your shell prompt back. At this point, you can run 'vagrant ssh' to log in to your newly installed Linux VM!
    - change directory to /vagrant
    
 3) Next you will need to download the data for this project. You will need to unzip the catalog file after downloading it. Put this file into the vagrant directory, which is shared with your virtual machine.
 
 4) Change your directory to the one inside the catalog file. Run the commands in the following order
    - 'python database_setup.py'.
    - 'python items.py' (NOTE: you will get a message on the console if items are succesfully added)
    - 'python application.py'. (Your flask application begins running on http://localhost:8000)
    

# PROJECT DESIGN 

1) The main page (/menu) contain s the list of categories with the list of recently added items just below it. There is also a login and logout button at the top right corner of the page
2) Clicking on any of the category redirects to the url (/catalog/<category_name>)
3) Clicking on any of the items will further redirect it ro the url 
    (/catalog/<category_name>/<item_name>). You will see a description of the item an two buttons Edit and Delete if you've logged in.




    
    
