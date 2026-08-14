Quizzler -- Interactive Trivia Quiz App

Quizzler is a Python-based True/False trivia quiz application that
started as a terminal-based quiz and was later upgraded into an
interactive Tkinter GUI application.

The project fetches quiz questions from the Open Trivia Database API,
processes the JSON response, and presents the questions through a
graphical interface. Users can answer questions using True/False
buttons, receive instant visual feedback, and track their score.

Features

Fetches quiz questions from the Open Trivia Database API

Supports True/False questions

Displays questions in a Tkinter graphical interface

True and False image buttons for answering

Instant visual feedback for correct and incorrect answers

Score tracking throughout the quiz

HTML entity decoding for API-provided question text

Object-Oriented Programming structure

Separates quiz logic from the user interface

Project Evolution

This project was originally developed as a terminal-based interactive
quiz while learning Python.

The original version displayed questions in the terminal, accepted
True/False input, checked answers using a QuizBrain class, and tracked
the score.

The project was later improved by adding a Tkinter GUI.

Terminal Version → GUI Version

Terminal Version
      ↓
Questions displayed in terminal
      ↓
User types True / False
      ↓
QuizBrain checks the answer
      ↓
Score displayed in terminal

             ↓ Upgrade

Tkinter GUI Version
      ↓
Questions displayed on a GUI
      ↓
User clicks True / False buttons
      ↓
QuizBrain checks the answer
      ↓
GUI provides visual feedback
      ↓
Score displayed on the interface

This evolution demonstrates how the same core Python logic can be reused
and improved by adding a graphical user interface.

Technologies Used

Python

Tkinter -- Graphical User Interface

Requests -- API requests

Open Trivia Database API -- Quiz question source

JSON -- API response/data handling

HTML -- Decoding HTML entities in API questions

Object-Oriented Programming (OOP)

Project Structure

quizzler-app/
│
├── images/
│   ├── true.png
│   └── false.png
│
├── data.py
├── main.py
├── question_model.py
├── quiz_brain.py
├── ui.py
└── README.md

File Overview

File                  Purpose