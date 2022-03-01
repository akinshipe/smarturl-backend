
<h2>Working Version</h2>




When both frontend and backend are correctly deployed, it should work exactly like the live demo<br>
<a href="https://test.learnershub.co.za/" target="_blank">Link to Live Demo</a>


<h2>Built with</h2> 

1.	Django
2.	Django Rest Framework






<h2>Plans for Production Version And Scalability</h2>

1.	Little or no input validation has been done while taking requests from the API Endpoint, In a production Version. This will definitely not be the case.
2.	The algorithm used for shortening is not scalable. The current shortening algorithm takes in a path to be shortened; finds the square root of the length of the path; generates a random string from the ASCII letters and digits with length correlating to the square root of the inputted path length. In production, pre-generating all possible short URL paths in the dB and assigning them on an as-needed basis may be a better approach. To speed up the system. The pre-generated short URLs may be stored in several tables; a mapping function can then be used to map URLs to the required table(sort of like the way the Hash tables data structure works). When all URLs in a particular table has been assigned, a linear probing mechanism can be employed to look for the next available table.
3.	The current version uses the SQLite DB that comes with Django. This was used to avoid you dealing with provisioning and configuring a MySQL or PostgreSQL database when you want to re-deploy it. For scalability reasons, Sqlite db should never be deployed in production.
4.	The debug settings in the settings.py file has been left on True to allow you to monitor things while trying to re-deploy. This should be turned off in production
5.	Security implementations like brute-forcing or SQL injection needs to be catered for in a production version


<h2>Deployment Instruction</h2>



Since there are 1001 possible hosting deployment choices, these deployment instructions will only be specific to configuring the app to work as intended and not about the actual process of deploying the app to a specific provider.

1. 	Like all other Django apps, the app's entry point is the wsgi.py file in the project directory(smarturl/wsgi.py). 
2. 	If you are going to access the Rest framework web API view of this application, please make sure to add  the URL where you deployed the app to the ALLOWED_HOST list  on line     28 in smarturl/settings.py
3.	 Make sure to update the BASE_URL constant in api/views.py  to the full URL path you are hosting the ReactJs frontend app. Make sure the path ends with a backslash. Do not       forget to ensure the proper protocol (http//: or https//:) is used to avoid unpredictable behaviour
4.	 Make sure to add the exact BASE_URL you changed in step 3 above to CORS_ORIGIN_WHITELIST settings in smarturl/settings.py.
5.	 A requirements.txt file has been included in the root directory. Run pip install -r requirements.txt while in your virtual environment to install all the packages required       by this application
6.	Follow other deployment steps advised by your hosting provider and environment
