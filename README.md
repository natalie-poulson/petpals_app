# PetPals App

## Scope:
PetPals is a social media oriented, full-stack web application that connects pet owners by means of sharing images of their pets. Using Django, Python, Javascript, jQuery, HTML, and CSS, our goal is to create an application that allows users to sign-up, create a profile for their pet, post pictures of their pets, and interact with other users through likes and comments. Users will be able to add friends and explore random photos of pets that have opted-in to having their pictures shared on a site-wide basis. 

## Getting Started
To run an instance of Pet Pals on your local machine, clone the repository, then run:

`python3 manage.py makemigrations`

`python3 manage.py migrate`

`python3 manage.py runserver`

## Built With
**Django/Python** - Web framework used to provide structure to web apps, enabling creation of dynamic, safe websites with managed data storage

**Javascript/JQuery** - Generates likes, follows, and hover effects, powering the frontend

**HTML/CSS** - Frontend structure and styling

**PostgreSQL** - Database Management System, used for storing app state, such as posts, comments, follows, and likes

## Users:
 Our target users are proud pet parents looking to share pictures of their pets and connect with other pet parents. 

## Features
* Create accounts on petpals with forms that will ensure proper input, and backend validation of forms
* Edit and customize your profile
* Upload custom pictures of your pets
* Comment on and 'like' pet photos of other users who you follow
* See which other users have liked your photos
* Explore page allows users to see randomly selected photos


## User Story: 

* A user will visit our homepage where they have an option to sign-in or sign up for PetPals 
    * A first-time user will select the ‘sign up’ button and complete a form prompting for pet’s username, owners email address, and a password to protect the account.
        * Once preliminary sign-up data is submitted, the user will be redirected to a profile page where they can optionally complete a profile customized with a profile picture and bio.
    * If the user selects the  ‘sign-in’ button, they will be redirected to their furry-friend feed containing images that have been posted by their friends
        * If a user does not have friends, their feed will appear empty, and the user can visit the ‘Explore’ page that all
    * Users can select from a nav bar containing links to:  
        * Profile: 
            * User’s profile page that shows user information, posts, and allows the user to search through their friend list
        * Explore
            * Features pictures of posts from users who have opted-in to having their photos featured which may be updated in the profile page
        * Post
            * User can create a post with a caption to upload a new photo of their pet
        * Feed
            * User will see uploaded photos of pets friends that can be interacted with through by liking or commenting on a photo
            * When a user hovers over a photo, the caption will appear for non-mobile development. 
            * For the responsive site, the caption will appear underneath the image
            * If a user clicks on the name that has been ‘posted by’, the user will be brought to the account that has been clicked ons’ profile page.
            * Underneath each post, a like count and comments button will be present
                * If the user clicks on comments, all comments will be toggled into view
                * If the user clicks on likes, the app will redirect to the likes page where user will be able to see which other users have liked the post in the format of “This {user} liked this {post} on {date} with a thumbnail of the liked image. 
        * Likes
            * User will be able to view posts that have been liked by other furry friends 


### Authors
* [Andrea Piazza](https://github.com/aza024)
* [Luke Engle](https://github.com/Cyrusluke925)
* [Natalie Poulson](https://github.com/natalie-poulson)

### Acknowledgments
Special thanks to our instructors Justin Castilla and Dalton Hart for assisting us with this project. 
* Thanks to [Pexels.com](https://www.pexels.com) for all stock images!

