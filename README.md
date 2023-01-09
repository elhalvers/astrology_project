# Codecademy CS Path Python Project

The goal of the project is to build a basic terminal program from scratch.

Project Objectives:

Build a terminal program using Python
Add at least one interactive feature using input()
Use Git version control
Use the command line and file navigation
Write a technical blog post on the project

One of the example projects was 'Today's Horoscope' so I build a simple application to learn about using API's.

The application asks a user if they want their daily horoscope. If they reply, yes it asks for their sign.
The input is used to pass a parameter to an API request which returns horoscope informatino particular to the user's sign.

I installed and used the requests module to make a client-side API request and used the json module method json.loads() to convert the
returned json object to a Python dictionary which I use to return formatted information back to the user.
