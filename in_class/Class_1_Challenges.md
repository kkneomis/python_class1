## Class Challenges

### Challenge 1

Modeling a person is a classic exercise for people who are trying to learn how to write classes. We are all familiar with characteristics and behaviors of people, so it is a good exercise to try.
Define a Person() class.

* In the __init()__ function, define several attributes of a person. Good attributes to consider are name, age, place of birth, and anything else you like to know about the people in your life.
Write one method. This could be as simple as introduce_yourself(). This method would print out a statement such as, "Hello, my name is Eric."
* You could also make a method such as age_person(). A simple version of this method would just add 1 to the person's age.
A more complicated version of this method would involve storing the person's birthdate rather than their age, and then calculating the age whenever the age is requested. But dealing with dates and times is not particularly easy if you've never done it in any other programming language before.
* Create a person, set the attribute values appropriately, and print out information about the person.
* Call your method on the person you created. Make sure your method executed properly; if the method does not print anything out directly, print something before and after calling the method to make sure it did what it was supposed to.


### Challenge 2

Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle. 



### Challenge 3

Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters



### Challenge 4

__Student Class__  
Start with your program from Person Class.

* Make a new class called Student that inherits from Person.
Define some attributes that a student has, which other people don't have.
* A student has a school they are associated with, a graduation year, a gpa, and other particular attributes.
Create a Student object, and prove that you have used inheritance correctly.
* Set some attribute values for the student, that are only coded in the Person class.
* Set some attribute values for the student, that are only coded in the Student class.
* Print the values for all of these attributes.

### Challenge 5

Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.


### Challenge 6

Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.


### Challenge 7

Define a class GameMachine that has must be initialized with one object variable: and coins (int)

The GameMachine has and __init__ and __repr__ function

It has the following methods:

1. play_game: Allows the user to play of the games below (call one of the other functions). Decrements coins by one each time a game is played. Once there are no more coins, the user can no longer play.

1. guessing_game: This generables a random number from 1-20. It keeps asking the user to guess the number until the users guesses correctly.

2. rps: (Rock paper scissors): Print "Rock, Paper, Scissors, Shoot", and asks the user to print one of the three. It then compares the user's choice to its own choice and declares a winner.

3. Another mini-game of your creation



### Challenge 8

Write a Python program to convert an integer to a roman numeral.

