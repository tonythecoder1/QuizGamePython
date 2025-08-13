# Python Quiz Application with Tkinter

This project is a simple yet effective quiz application built in Python, utilizing the Tkinter library to create a graphical user interface (GUI). It presents the user with a series of true or false questions, tracks their score in real-time, and provides instant visual feedback for each answer.

---

## Features

- **User-friendly GUI:** Built with Tkinter, providing an intuitive and clean interface.
- **Question Types:** True or False questions fetched dynamically.
- **Instant Feedback:** The interface changes color to green for correct answers and red for incorrect ones.
- **Score Tracking:** The user's score updates after each question and is displayed prominently.
- **End of Quiz Summary:** Displays the total score once all questions have been answered.
- **Button State Management:** Disables answer buttons while feedback is shown to prevent multiple clicks.

---

## Data Source

This quiz uses the [Open Trivia Database (OpenTDB)](https://opentdb.com/) API to fetch questions dynamically. Specifically, it calls the following endpoint to retrieve 10 medium difficulty questions from the "Entertainment: Video Games" category:

