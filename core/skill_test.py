# ==========================================
# AI CareerPath - Skill Test Question Bank
# ==========================================

SKILL_TESTS = {

    "python": {
        "name": "Python",
        "questions": [
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["function", "def", "func", "define"],
                "answer": "def",
            },
            {
                "question": "Which data type stores key-value pairs?",
                "options": ["List", "Tuple", "Dictionary", "Set"],
                "answer": "Dictionary",
            },
            {
                "question": "What is the output of len([10, 20, 30])?",
                "options": ["2", "3", "4", "10"],
                "answer": "3",
            },
            {
                "question": "Which symbol is used for comments in Python?",
                "options": ["//", "#", "/*", "<!--"],
                "answer": "#",
            },
            {
                "question": "Which keyword is used to create a class?",
                "options": ["object", "class", "struct", "define"],
                "answer": "class",
            },
        ],
    },

    "java": {
        "name": "Java",
        "questions": [
            {
                "question": "Which keyword is used to create a class in Java?",
                "options": ["class", "Class", "define", "object"],
                "answer": "class",
            },
            {
                "question": "Which method is the entry point of a Java program?",
                "options": ["start()", "run()", "main()", "execute()"],
                "answer": "main()",
            },
            {
                "question": "Which concept allows the same method name with different parameters?",
                "options": [
                    "Inheritance",
                    "Encapsulation",
                    "Method Overloading",
                    "Abstraction"
                ],
                "answer": "Method Overloading",
            },
            {
                "question": "Which keyword is used for inheritance?",
                "options": ["inherits", "extends", "implements", "super"],
                "answer": "extends",
            },
            {
                "question": "Which type of language is Java?",
                "options": [
                    "Procedural only",
                    "Object-Oriented",
                    "Markup",
                    "Assembly"
                ],
                "answer": "Object-Oriented",
            },
        ],
    },

    "sql": {
        "name": "SQL",
        "questions": [
            {
                "question": "Which command is used to retrieve data?",
                "options": ["GET", "SELECT", "FETCH", "OPEN"],
                "answer": "SELECT",
            },
            {
                "question": "Which command is used to remove a table?",
                "options": ["DELETE", "REMOVE", "DROP", "CLEAR"],
                "answer": "DROP",
            },
            {
                "question": "Which clause filters rows?",
                "options": ["WHERE", "FILTER", "HAVING", "CHECK"],
                "answer": "WHERE",
            },
            {
                "question": "Which key uniquely identifies a row?",
                "options": [
                    "Foreign Key",
                    "Primary Key",
                    "Candidate Key",
                    "Index"
                ],
                "answer": "Primary Key",
            },
            {
                "question": "Which SQL command adds a new row?",
                "options": ["ADD", "INSERT", "UPDATE", "CREATE"],
                "answer": "INSERT",
            },
        ],
    },

    "dsa": {
        "name": "DSA",
        "questions": [
            {
                "question": "Which data structure follows LIFO?",
                "options": ["Queue", "Stack", "Array", "Tree"],
                "answer": "Stack",
            },
            {
                "question": "Which data structure follows FIFO?",
                "options": ["Stack", "Queue", "Tree", "Graph"],
                "answer": "Queue",
            },
            {
                "question": "What is the average time complexity of binary search?",
                "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
                "answer": "O(log n)",
            },
            {
                "question": "Which structure consists of nodes connected by edges?",
                "options": ["Array", "Stack", "Graph", "Queue"],
                "answer": "Graph",
            },
            {
                "question": "Which sorting algorithm repeatedly swaps adjacent elements?",
                "options": [
                    "Merge Sort",
                    "Quick Sort",
                    "Bubble Sort",
                    "Binary Sort"
                ],
                "answer": "Bubble Sort",
            },
        ],
    },

    "html_css": {
        "name": "HTML & CSS",
        "questions": [
            {
                "question": "Which tag creates a hyperlink?",
                "options": ["<link>", "<a>", "<href>", "<url>"],
                "answer": "<a>",
            },
            {
                "question": "Which language is used for webpage styling?",
                "options": ["HTML", "CSS", "SQL", "Python"],
                "answer": "CSS",
            },
            {
                "question": "Which CSS property changes text color?",
                "options": ["font", "text-color", "color", "foreground"],
                "answer": "color",
            },
            {
                "question": "Which HTML tag creates a paragraph?",
                "options": ["<p>", "<para>", "<text>", "<paragraph>"],
                "answer": "<p>",
            },
            {
                "question": "Which CSS property changes background color?",
                "options": [
                    "background-color",
                    "bg-color",
                    "color-background",
                    "background"
                ],
                "answer": "background-color",
            },
        ],
    },
}