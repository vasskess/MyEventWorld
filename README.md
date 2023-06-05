<a name="home"></a>
|Introduction|
|:---------------------------:|
**For educational purposes, I have developed a Django project following the completion of my web framework course at SoftUni. This project serves as a practical application of the concepts and techniques I learned. Through this project, I aim to further solidify my understanding of Django and enhance my skills in web development. While the project may not have a specific commercial or real-world application, it serves as a valuable learning experience and a testament to my progress in Django development.**
</br>

|Project Overview |
|:---------------------------:|
**The app is divided into two sections - Public and Private.</br> Unauthenticated users are granted access to the landing page, which displays a list of events [events-list](#events) and provides detailed information about [individual event](#events). They also have access to the [Event Creator page](#creators), where registered profiles are showcased. Furthermore, unauthenticated users can explore the complete details of a specific creator (single-creator picture). In addition, unauthenticated users have the ability to perform searches on both the creators page [creators-search](#searches) and the event page [events-search](#searches).**


**Authenticatedusers have access to a range of enhanced features within the app. They can create events, providing detailed information about themselves and adding their interests. Authenticated users have full control over their content, allowing them to create, view, update, and delete their events, interests, and profile information or even their profile if they dont want it anymore. Additionally, they can share their experiences by leaving one-time reviews for events created by other users. This enables them to provide valuable feedback and insights. Authenticated users also have the privilege of exchanging messages with other registered users, fostering seamless communication and facilitating interaction within the app.**
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
The project incorporates the customizable and customized admin panel through the use of 'django-admin-interface' library. 👉 [admin](#admin).

</br>

|Future TODO Implementations|
|:-----------------------:|
- [ ] Extend Project with REST capabilities
- [ ] Write Integration Tests

<a name="events"><p align="center">Events</p></a>
-----------------------
Events | Single Event
----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/cb0398d8-7aca-41a6-94d5-3305b574ac87) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/c498d471-dd81-495c-abda-1f0d83647418)
-----------------------

<a name="creators"><p align="center">Creators</p></a>
-----------------------
Creators | Single Creator
----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/1816cce9-30e9-4ad6-9efc-605e1e9f3a7b) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/1751e4bf-f4ce-4a64-86ea-70e4e76c7e05)
-----------------------

<a name="searches"><p align="center">Searches</p></a>
-----------------------
Creators | Events
-----------------------  | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/11f68dbd-ee9a-4a6f-8c30-932bb69672bc) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/168a6b5f-d717-40ae-9d68-a7cf96d00b2c)
-----------------------

<a name="examples"><p align="center">Flash Messages Examples</p></a>
-----------------------
Creation | Deletion | Updating | Sent
----------------------- | ----------------------- | ----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/70d64c6b-e3e0-4abf-97aa-03fb28724c60) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/611f3266-9125-4614-bc27-969dfa50431b) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/2479f09e-4b45-44e9-b34a-34fdab86c4dc) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/029a37aa-feb6-4380-abb3-119f4743ef5e)
-----------------------

<a name="mixin"><p align="center">Ownership Mixins</p></a>
-----------------------
Users | Events
----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/e4fe76a2-0607-4310-a810-e9b8c827c91b) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/dc48024a-8ba7-4f64-890d-d5fd972ec005)
-----------------------

<a name="middleware"><p align="center">Custom Middleware</p></a>
-----------------------
Middleware | Renders
----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/590c65fd-1e13-459d-b149-535ba7b33ca6) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/73815b9e-c85a-4c79-a9f2-65053127853c)
-----------------------

<a name="errors"><p align="center">Error Templates</p></a>
-----------------------
Error 400 | Error 403 | Error 404 | Error 500 & Above
----------------------- | ----------------------- | ----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/11967b17-4867-4923-ae10-ba723f636193) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/0b984a08-7f0a-4073-8864-3618c4c43a7e) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/b7a18dcc-5778-47c9-ba67-536fbc1f3b54) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/b24c8524-5e88-4001-a782-b0b6158d8499)
-----------------------
<a name="anchorjs"><p align="center">JavaScript</p></a>
-----------------------
Navbar | Footer
----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/56ef4dda-13a1-4e0f-9031-eef0398cd167) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/9f846817-6d98-4d8e-8acd-1bb8c89aaaae)
-----------------------

<a name="admin"><p align="center">AdminSite & AdminCode</p></a>
-----------------------
Layout Customization | AdminSite Customization
----------------------- | -----------------------
![](https://github.com/vasskess/MyEventWorld/assets/96621183/7d677b97-76ee-4ace-8636-de0e68263b0f) | ![](https://github.com/vasskess/MyEventWorld/assets/96621183/ffd1fda3-0d63-41bc-be66-68cea335403b)
-----------------------
<a align="center">[Back to Top](#home)</a>
