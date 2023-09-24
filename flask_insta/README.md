README.md 

Natalia Chernysheva
SQL Portfolio Project: Instagram Clone 

This project has two classes User and Post which allow to create new users, to update user information, to befriend other users, to post and like posts, to read friends' posts, and to delete users and posts. 

API Reference 

| POST | /users | To create new users |
| POST | /users/<int:id>/friends/<int:fr_pk>/add | To add a new friend |
| POST | /posts | To create a new post |
| GET | /users | To show information about all users |
| GET | /users/:id | To show information about a specific user |
| GET | /users/:id/liking_posts | To show all posts liked by the user |
| GET | /users/:id/friends | To show a list of all friends of a single user |
| GET | /users/:id/posts | To show a list of all posts of a single user |
| GET | /users/<int:id>/friends/<int:fr_pk>/posts | To show a list of all posts of a single from from the user's list |
| GET | /posts | To list all posts |
| GET | /posts/:id | To show a specific post |
| GET | /posts/:id/liking_users | To show all users who liked the post |
| PUT | /users/:id | To update information about a specific user |
| PUT | /posts/:id | To update a specific post |
| DELETE | /users/:id | To delete a specific user |
| DELETE | /users/<int:id>/friends/<int:fr_pk>/delete | To delete a friend  |
| DELETE | /posts/:id | To delete a specific post |


Questions: 
(1) How did the project's design evolve over time?
I started from copying the twitter project we practiced in class. Then, I expanded the user properties (I added the first and last names, bio, and friends). Further, I added the self-referential many-to-many relationship to add friends to users. Finally, I added the option to read friends' posts. 
(2) Did you choose to use an ORM or raw SQL? Why?
I chose ORM because ORM is entirely new to me and I wanted to have more practice with it since it seems to be used more frequently than raw SQL in coding in Python, including with Flask and Django. 
(3) What future improvements are in store, if any?
I would add the registration, login, logout options so that each user can only access the profiles and posts from their friends. I would also add the option to upload images as the original Instagram is a largely visual platform. 
