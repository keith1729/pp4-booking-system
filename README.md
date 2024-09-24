# Golf Booking Site

## Table of Contents:

1. UX-Design
    - Planning
        - Design Thinking 
        - Agile
        - User Stories
        - Website Flow
    - WireFrames
        - Styles
        - Fonts
        - Colours

2. Database Model
    - ERD

3. Features
    - Existing Features
    - Future Features

4. Technologies Used
    - Languages
    - Frameworks and Libraries
    - Tools

5. Manual Testing
    - Responsiveness
    - Browser Compatibility
    - Lighthouse
    - Code Validation
    - User Stories
    - Features
    - Bugs

6. Deployment
    - Heroku

7. References
    - Credits

## UX-Design
### Planning
#### Design Thinking:

From the start when developing this website I imagined the site from the users perspective. This immediately posed questions such as: 
- Why would a user want to visit this website?
    - The website provides a booking service for tee times on a golf course.
- What would bring a user back to the website?
    - A user would return to the website if they experience a user-friendly interface with easy navigation and a streamlined booking service.

#### Agile Planning:

An agile approach was taken for the planning of this website. This allowed me to take an iterative strategy towards the projects goals and break down the user stories into smaller tasks, I thought about these in terms of accepted criteria(AC). Also this allowed me to be flexible throughout the websites development and refine, adjust and add features to the website as needed. A kanban board was used for project management where I could assign labels of 'Must Have', 'Could Have' and 'Should Have' to my user stories. As I worked on each I moved them from 'Todo' to 'In Progress' to 'Done' which gave me a clear plan of what stage the project was in and which features took priority.

#### User Stories:

The user stories were written from the users perspective. This gave me the opportunity to envisage what a user would want to see on the home page, login page etc. The following user stories were completed throughtout the development of the website:
- New User Registration
    - As a 'non-registered user' I can 'create an account' so that 'I can use the websites service'.
- Login/Logout
    - As a 'registered user' I can 'login and logout' so that 'I can access my account securely'.
- Make a Booking
    - As a 'registered user' I can 'access a booking page' so that 'I can book a tee time'.
- View a Booking
    - As a 'registered user' I can 'access a list of my bookings' so that 'I can view my bookings'.
- Update a Booking
    - As a 'registered user' I can 'access a list of my bookings' so that 'I can update a booking'.
- Delete a Booking
    - As a 'registered user' I can 'access a list of my bookings' so that 'I can delete a booking'.

#### Website Flow:

Writing the user stories allowed me to visualise how the website would take form and what features should be where and when they should be there.

### Wireframes

Balsamiq was leveraged for making wireframes which would guide the development process.

- Home page

  <img src="assets/images/wireframes-homepage.PNG" alt="Wireframes Home">

<br/>

- Registration page

  <img src="assets/images/wireframes-register.PNG" alt="Wireframes Registration">

<br/>

- Login page

  <img src="assets/images/wireframes-login.PNG" alt="Wireframes Login">

<br/>

- Booking page

  <img src="assets/images/wireframes-booking.PNG" alt="Wireframes Booking">

<br/>

- My bookings page

  <img src="assets/images/wireframes-mybookings.PNG" alt="Wireframes My Bookings">

#### Styles:

#### Fonts:

#### Colours:

## Database Model
### ERD:

- The ERD shows the Booking model and its associated fields. The user field has a many to one relationship with djangos built-in User model as a single user can have many bookings but each booking is related to only one user.

<img src="assets/images/erd-booking.PNG" alt="ERD Booking">

## Features
### Existing Features:

- Header
    - Logged out - shows the logo and gives options to register new account, login and see the about page for the website.
    <img src="assets/images/features-header1.png" alt="Features Header/logged_out">

    - Logged in - also shows logo and about page and gives options for booking a tee time, viewing my bookings and safely logging out of my account.
    <img src="assets/images/features-header2.png" alt="Features Header/logged_in">

- Footer

This includes the social media links for the golf course.

<img src="assets/images/features-footer.PNG" alt="Features Footer">

- Register New Account

This allows a user to register a new account.

<img src="" alt="Features Registration">

- Login

This provides log in functionality.

<img src="" alt="Features Login">

- Book a Tee Time

Enables a registered user with booking capabilities.

<img src="" alt="Features Booking">

- View Bookings

Presents a list of a logged in users bookings.

<img src="" alt="Features View Bookings">