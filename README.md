<a name="home"></a>
|Introduction|
|:---------------------------:|
**For educational purposes, I have developed a Django project following the completion of my web framework course at SoftUni. This project serves as a practical application of the concepts and techniques I learned. Through this project, I aim to further solidify my understanding of Django and enhance my skills in web development. While the project may not have a specific commercial or real-world application, it serves as a valuable learning experience and a testament to my progress in Django development.**
</br>

|Project Overview |
|:---------------------------:|
**The app is divided into two sections - Public and Private.</br> Unauthenticated users are granted access to the landing page, which displays a list of events [events-list](#events) and provides detailed information about [individual event](#events). They also have access to the [Event Creator page](#creators), where registered profiles are showcased. Furthermore, unauthenticated users can explore the complete details of a specific creator (single-creator picture). In addition, unauthenticated users have the ability to perform searches on both the creators page [creators-search](#searches) and the event page [events-search](#searches).**


**Authenticated users have access to a range of enhanced features within the app. They can create events, providing detailed information about themselves and adding their interests. Authenticated users have full control over their content, allowing them to create, view, update, and delete their events, interests, and profile information or even their profile if they dont want it anymore. Additionally, they can share their experiences by leaving one-time reviews for events created by other users. This enables them to provide valuable feedback and insights. Authenticated users also have the privilege of exchanging messages with other registered users, fostering seamless communication and facilitating interaction within the app.**
|:---------------------------:|
</br>

|Implemented Features|
|:---------------------:|
My project is built upon an extended AbstractBaseUser model, ensuring a streamlined and efficient database by eliminating unnecessary data. To enhance security and uniqueness, custom UUID4 is implemented as primary keys. Error handling and validations are in place to ensure a smooth user experience.
For seamless user registration, welcome email is sent asynchronously, leveraging Celery and Redis. To utilize this functionality, you will need to configure Celery and Redis 👉 [ClickMe](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html) -- Since i had some issues with the Celery command for Windows </br> 🛑 **celery -A MyEventWorld worker --pool=solo --loglevel=info** 🛑 </br> --  ☝️ This is the one that should work  👆 -- </br> **Sometimes you'll need to start the command again if you restart the app in order to work !**
Additionally, email functionality is essential for the built-in "Forgot Password" recovery feature, which I have integrated using Gmail with 2-step verification
You can read more how to do it here 👉 [Clicky](https://www.abstractapi.com/guides/django-send-email)
Cloudinary is utilized as the storage solution for event and profile pictures, ensuring reliable and scalable media management. 👉 [HowTo](https://www.section.io/engineering-education/uploading-images-to-cloudinary-from-django-application/)
To provide user-friendly feedback, one-time flash messages are implemented for various actions, such as user creation, deletion, interest/event management, and message handling. 👉 [Examples](#examples)
Custom mixins to prevent other logged users access to owner content profile/events by hand-typing primary keys. 👉 [Mixins](#mixin)
A global custom error middleware is implemented to handle and display errors in a consistent and user-friendly manner. 👉 [Middleware](#middleware), 👉 [Error Templates](#errors)
The project's frontend is developed using HTML and CSS - which should be responsive, but may not be the best one, since i'm not that good with front-end
A couple of simple JavaScript functions are implemented to enhance the functionality of the navigation bar and footer. 👉 [jsFuncs](#anchorjs).
The project incorporates the customizable and customized admin panel through the use of 'django-admin-interface' library. 👉 [Admin](#admin).
-----------------------
To use the full potential of the app, you need to follow these steps:
-----------------------
1. Clone the repository
 
   git clone https://github.com/vasskess/MyEventWorld.git

2. Create a virtual environment (venv).

3. Install the required dependencies by running the following command in the terminal:

    `pip install -r requirements.txt`

4. Set up a PostgreSQL database. You can read more here -> https://www.postgresql.org/

5. Press `Ctrl+Alt+R` to enter the `manage.py` terminal and access autocomplete for commands.

6. You can directly execute the `migrate` command to apply the migrations to the database - since the 'migration folders' are included in the project.

7. To enable the functionality of Cloudinary and email, you have two options:
  - Create an `.env` file with the required credentials.
  - Provide the Cloudinary and email credentials after the setup process. Refer to the app's implementation information for useful links.

Note: If you don't wish to set up Cloudinary and email, you can comment out those functionalities in settings.py, but they will not work.

By following these steps, you will be able to fully utilize the features of the app.

</br>

<a name="events"><p align="center">Events</p></a>
-----------------------
Events | Single Event
----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/a697ad99-9f8d-45a8-a663-12035b6f6a81) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/598fa06b-9f89-41b7-b71c-1e5c9087888e)
-----------------------

<a name="creators"><p align="center">Creators</p></a>
-----------------------
Creators | Single Creator
----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/7e2e3fde-795e-4b66-906c-ff3bf9338524) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/99eb25a1-159e-4f66-8239-93d69049d194)
-----------------------

<a name="searches"><p align="center">Searches</p></a>
-----------------------
Creators | Events
-----------------------  | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/a18584cb-4c57-40ca-a2f7-c2630c5b10b0) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/e9824521-5037-4fc5-a677-b717eebef8e3)
-----------------------

<a name="examples"><p align="center">Flash Messages Examples</p></a>
-----------------------
Creation | Deletion | Updating | Sent
----------------------- | ----------------------- | ----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/1462912c-cd9e-4eb5-a6e3-987306d168b9) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/1c0f0e10-6df5-4a6f-aa30-9fb2138640eb) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/a88e9e12-3d97-44f4-8b7b-ec7897857ecf) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/416faee9-987b-4f3b-9845-77dae252c16b)
-----------------------

<a name="mixin"><p align="center">Ownership Mixins</p></a>
-----------------------
Users | Events
----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/7c088503-5c95-4639-ab8e-c2f38f937bcb) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/44c722ba-a256-4c0d-a33a-d91933098947)
-----------------------

<a name="middleware"><p align="center">Custom Middleware</p></a>
-----------------------
Middleware | Renders
----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/fad7f62f-f02d-4e51-b556-c250022002b3) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/3c34c27c-6522-4514-9c9a-a3d266eb5cfe)
-----------------------

<a name="errors"><p align="center">Error Templates</p></a>
-----------------------
Error 400 | Error 403 | Error 404 | Error 500 & Above
----------------------- | ----------------------- | ----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/94466fd7-44aa-488b-9897-f49e37cb245a) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/d16a9625-1338-4339-a4a5-2d7620e24463) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/cdc80ff8-2fe5-4ba2-a976-3c4dfcfbd2d0) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/2a8499da-8917-4baf-88c7-b4a3e516b4ed)
-----------------------
<a name="anchorjs"><p align="center">JavaScript</p></a>
-----------------------
Navbar | Footer
----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/64fd8b3e-ac12-48c3-9a73-883c6c630f5d) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/63ada6fd-d281-41dd-938a-b68c4a05da27)
-----------------------

<a name="admin"><p align="center">AdminSite & AdminCode</p></a>
-----------------------
Layout Customization | AdminSite Customization
----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/fc77f5a8-ddff-42c8-8c96-975af4d8f170) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/f504afee-5f9c-477f-a6a2-4d18e631138e)
-----------------------
<a align="center">[Back to Top](#home)</a>
