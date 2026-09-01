# =========================================================
# ROLE-SPECIFIC JOB READINESS QUESTIONS
# =========================================================

JOB_READINESS_QUESTIONS = {

    "Python Developer": [

        {
            "question": "Which Python data structure is best suited for storing key-value pairs?",
            "choices": [
                ("a", "List"),
                ("b", "Tuple"),
                ("c", "Dictionary"),
                ("d", "Set"),
            ],
            "answer": "c"
        },

        {
            "question": "What is the main purpose of a Python virtual environment?",
            "choices": [
                ("a", "To increase internet speed"),
                ("b", "To isolate project dependencies"),
                ("c", "To compile Python into Java"),
                ("d", "To store database records"),
            ],
            "answer": "b"
        },

        {
            "question": "Which concept allows a Python class to inherit properties and methods from another class?",
            "choices": [
                ("a", "Encapsulation"),
                ("b", "Inheritance"),
                ("c", "Iteration"),
                ("d", "Recursion"),
            ],
            "answer": "b"
        },

        {
            "question": "Which Python library is commonly used for working with tabular data?",
            "choices": [
                ("a", "Pandas"),
                ("b", "Requests"),
                ("c", "Tkinter"),
                ("d", "Random"),
            ],
            "answer": "a"
        },

        {
            "question": "Which HTTP method is normally used to create a new resource through an API?",
            "choices": [
                ("a", "GET"),
                ("b", "POST"),
                ("c", "DELETE"),
                ("d", "HEAD"),
            ],
            "answer": "b"
        },

        {
            "question": "Which SQL command is commonly used to retrieve records from a database?",
            "choices": [
                ("a", "SELECT"),
                ("b", "INSERT"),
                ("c", "UPDATE"),
                ("d", "DROP"),
            ],
            "answer": "a"
        },

        {
            "question": "In Django, which component is mainly responsible for handling a web request and returning a response?",
            "choices": [
                ("a", "Model"),
                ("b", "View"),
                ("c", "Migration"),
                ("d", "Database"),
            ],
            "answer": "b"
        },

        {
            "question": "What should a developer generally do when an exception occurs in Python?",
            "choices": [
                ("a", "Ignore it completely"),
                ("b", "Use appropriate exception handling"),
                ("c", "Restart the computer"),
                ("d", "Delete the program"),
            ],
            "answer": "b"
        },

        {
            "question": "Which data structure is generally suitable when you need fast membership checking?",
            "choices": [
                ("a", "Set"),
                ("b", "List"),
                ("c", "String"),
                ("d", "Tuple"),
            ],
            "answer": "a"
        },

        {
            "question": "A Python developer receives a large problem that cannot be solved immediately. What is the best approach?",
            "choices": [
                ("a", "Write random code"),
                ("b", "Break the problem into smaller parts"),
                ("c", "Skip the problem"),
                ("d", "Copy code without understanding it"),
            ],
            "answer": "b"
        },
    ],


    "Java Developer": [

        {
            "question": "Which OOP concept allows a class to acquire properties and methods from another class?",
            "choices": [
                ("a", "Inheritance"),
                ("b", "Encapsulation"),
                ("c", "Abstraction"),
                ("d", "Compilation"),
            ],
            "answer": "a"
        },

        {
            "question": "Which collection does not allow duplicate elements?",
            "choices": [
                ("a", "List"),
                ("b", "Set"),
                ("c", "ArrayList"),
                ("d", "Vector"),
            ],
            "answer": "b"
        },

        {
            "question": "Which keyword is used to inherit a class in Java?",
            "choices": [
                ("a", "implements"),
                ("b", "extends"),
                ("c", "inherits"),
                ("d", "super"),
            ],
            "answer": "b"
        },

        {
            "question": "Which method is the entry point of a standard Java application?",
            "choices": [
                ("a", "run()"),
                ("b", "start()"),
                ("c", "main()"),
                ("d", "execute()"),
            ],
            "answer": "c"
        },

        {
            "question": "What is method overloading?",
            "choices": [
                ("a", "Same method name with different parameters"),
                ("b", "Creating multiple classes"),
                ("c", "Deleting a method"),
                ("d", "Using only static methods"),
            ],
            "answer": "a"
        },

        {
            "question": "Which keyword is used to handle exceptions?",
            "choices": [
                ("a", "try"),
                ("b", "check"),
                ("c", "error"),
                ("d", "catching"),
            ],
            "answer": "a"
        },

        {
            "question": "Which SQL operation is commonly required when Java applications retrieve data from related tables?",
            "choices": [
                ("a", "JOIN"),
                ("b", "DELETE"),
                ("c", "DROP"),
                ("d", "TRUNCATE"),
            ],
            "answer": "a"
        },

        {
            "question": "Which principle hides internal implementation details from the user?",
            "choices": [
                ("a", "Inheritance"),
                ("b", "Abstraction"),
                ("c", "Overloading"),
                ("d", "Iteration"),
            ],
            "answer": "b"
        },

        {
            "question": "Which data structure follows LIFO?",
            "choices": [
                ("a", "Queue"),
                ("b", "Stack"),
                ("c", "Graph"),
                ("d", "Tree"),
            ],
            "answer": "b"
        },

        {
            "question": "When solving a programming problem, what should a developer do before writing complex code?",
            "choices": [
                ("a", "Understand and break down the problem"),
                ("b", "Copy code from anywhere"),
                ("c", "Skip testing"),
                ("d", "Avoid thinking about edge cases"),
            ],
            "answer": "a"
        },
    ],
}