from django import forms

from .models import (
    StudentProfile,
    SkillAssessment,
    JobReadiness,
)


# =========================================================
# STUDENT PROFILE FORM
# =========================================================

class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile

        fields = [
            "name",
            "email",
            "college",
            "career_interest",
            "skills",
            "resume",
            "projects",
            "github_portfolio",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter your full name"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter your email"
                }
            ),

            "college": forms.TextInput(
                attrs={
                    "placeholder": "Enter your college name"
                }
            ),

            "career_interest": forms.TextInput(
                attrs={
                    "placeholder": "Example: Web Developer"
                }
            ),

            "skills": forms.TextInput(
                attrs={
                    "placeholder": "Example: Python, Java, SQL"
                }
            ),

            "projects": forms.Textarea(
                attrs={
                    "placeholder": "Enter your projects and technologies",
                    "rows": 5
                }
            ),

            "github_portfolio": forms.URLInput(
                attrs={
                    "placeholder": "https://github.com/yourusername"
                }
            ),
        }


# =========================================================
# SKILL QUESTION BANK
# =========================================================

SKILL_QUESTIONS = {

    # =====================================================
    # PYTHON
    # =====================================================

    "python": [

        {
            "question":
                "Which keyword is used to define a function in Python?",
            "choices": [
                ("a", "function"),
                ("b", "def"),
                ("c", "fun"),
                ("d", "define"),
            ],
            "answer": "b",
        },

        {
            "question":
                "Which of the following is immutable in Python?",
            "choices": [
                ("a", "List"),
                ("b", "Dictionary"),
                ("c", "Tuple"),
                ("d", "Set"),
            ],
            "answer": "c",
        },

        {
            "question":
                "What is the output of len([10, 20, 30])?",
            "choices": [
                ("a", "2"),
                ("b", "3"),
                ("c", "4"),
                ("d", "Error"),
            ],
            "answer": "b",
        },

        {
            "question":
                "Which symbol is used for comments in Python?",
            "choices": [
                ("a", "//"),
                ("b", "/*"),
                ("c", "#"),
                ("d", "--"),
            ],
            "answer": "c",
        },

        {
            "question":
                "Which data structure stores key-value pairs?",
            "choices": [
                ("a", "List"),
                ("b", "Tuple"),
                ("c", "Dictionary"),
                ("d", "Set"),
            ],
            "answer": "c",
        },
    ],


    # =====================================================
    # JAVA
    # =====================================================

    "java": [

        {
            "question":
                "Which keyword is used to create a class in Java?",
            "choices": [
                ("a", "class"),
                ("b", "Class"),
                ("c", "define"),
                ("d", "struct"),
            ],
            "answer": "a",
        },

        {
            "question":
                "Which concept allows the same method name with different parameters?",
            "choices": [
                ("a", "Inheritance"),
                ("b", "Encapsulation"),
                ("c", "Method Overloading"),
                ("d", "Abstraction"),
            ],
            "answer": "c",
        },

        {
            "question":
                "Which keyword is used to inherit a class?",
            "choices": [
                ("a", "implements"),
                ("b", "extends"),
                ("c", "inherits"),
                ("d", "super"),
            ],
            "answer": "b",
        },

        {
            "question":
                "Which method is the entry point of a Java program?",
            "choices": [
                ("a", "start()"),
                ("b", "run()"),
                ("c", "main()"),
                ("d", "execute()"),
            ],
            "answer": "c",
        },

        {
            "question":
                "Which OOP concept hides implementation details?",
            "choices": [
                ("a", "Inheritance"),
                ("b", "Polymorphism"),
                ("c", "Abstraction"),
                ("d", "Overloading"),
            ],
            "answer": "c",
        },
    ],


    # =====================================================
    # SQL
    # =====================================================

    "sql": [

        {
            "question":
                "Which SQL command is used to retrieve data?",
            "choices": [
                ("a", "GET"),
                ("b", "SELECT"),
                ("c", "FETCH"),
                ("d", "READ"),
            ],
            "answer": "b",
        },

        {
            "question":
                "Which clause is used to filter rows?",
            "choices": [
                ("a", "WHERE"),
                ("b", "FILTER"),
                ("c", "HAVING"),
                ("d", "CHECK"),
            ],
            "answer": "a",
        },

        {
            "question":
                "Which command removes a table?",
            "choices": [
                ("a", "DELETE"),
                ("b", "REMOVE"),
                ("c", "DROP"),
                ("d", "CLEAR"),
            ],
            "answer": "c",
        },

        {
            "question":
                "Which SQL function counts rows?",
            "choices": [
                ("a", "TOTAL()"),
                ("b", "COUNT()"),
                ("c", "NUMBER()"),
                ("d", "ROWS()"),
            ],
            "answer": "b",
        },

        {
            "question":
                "Which key uniquely identifies a row?",
            "choices": [
                ("a", "Foreign Key"),
                ("b", "Primary Key"),
                ("c", "Candidate Key"),
                ("d", "Index"),
            ],
            "answer": "b",
        },
    ],


    # =====================================================
    # HTML & CSS
    # =====================================================

    "html_css": [

        {
            "question":
                "Which HTML tag creates a hyperlink?",
            "choices": [
                ("a", "<link>"),
                ("b", "<a>"),
                ("c", "<href>"),
                ("d", "<url>"),
            ],
            "answer": "b",
        },

        {
            "question":
                "Which CSS property changes text color?",
            "choices": [
                ("a", "font-color"),
                ("b", "text-color"),
                ("c", "color"),
                ("d", "foreground"),
            ],
            "answer": "c",
        },

        {
            "question":
                "Which HTML tag is used for the largest heading?",
            "choices": [
                ("a", "<h6>"),
                ("b", "<head>"),
                ("c", "<h1>"),
                ("d", "<heading>"),
            ],
            "answer": "c",
        },

        {
            "question":
                "Which CSS property controls spacing inside an element?",
            "choices": [
                ("a", "margin"),
                ("b", "padding"),
                ("c", "spacing"),
                ("d", "inside"),
            ],
            "answer": "b",
        },

        {
            "question":
                "Which CSS layout system is useful for one-dimensional layouts?",
            "choices": [
                ("a", "Flexbox"),
                ("b", "SQL"),
                ("c", "DOM"),
                ("d", "AJAX"),
            ],
            "answer": "a",
        },
    ],


    # =====================================================
    # DSA
    # =====================================================

    "dsa": [

        {
            "question":
                "Which data structure follows FIFO?",
            "choices": [
                ("a", "Stack"),
                ("b", "Queue"),
                ("c", "Tree"),
                ("d", "Graph"),
            ],
            "answer": "b",
        },

        {
            "question":
                "Which data structure follows LIFO?",
            "choices": [
                ("a", "Queue"),
                ("b", "Array"),
                ("c", "Stack"),
                ("d", "Graph"),
            ],
            "answer": "c",
        },

        {
            "question":
                "Binary search requires the array to be:",
            "choices": [
                ("a", "Random"),
                ("b", "Sorted"),
                ("c", "Empty"),
                ("d", "Circular"),
            ],
            "answer": "b",
        },

        {
            "question":
                "Which data structure is commonly used for BFS?",
            "choices": [
                ("a", "Stack"),
                ("b", "Queue"),
                ("c", "Heap"),
                ("d", "Array"),
            ],
            "answer": "b",
        },

        {
            "question":
                "What is the average time complexity of binary search?",
            "choices": [
                ("a", "O(n)"),
                ("b", "O(n²)"),
                ("c", "O(log n)"),
                ("d", "O(1)"),
            ],
            "answer": "c",
        },
    ],
}


# =========================================================
# SKILL ASSESSMENT FORM
# =========================================================

class SkillAssessmentForm(forms.Form):

    def __init__(
        self,
        *args,
        selected_skills=None,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

        selected_skills = selected_skills or []

        for skill in selected_skills:

            questions = SKILL_QUESTIONS.get(
                skill,
                []
            )

            for index, question in enumerate(questions):

                self.fields[
                    f"{skill}_{index}"
                ] = forms.ChoiceField(

                    label=question["question"],

                    choices=question["choices"],

                    widget=forms.RadioSelect,

                    required=True,
                )


# =========================================================
# JOB READINESS QUESTION BANK
#
# ONLY 4 COMPONENTS:
# 1. CODING PRACTICE
# 2. APTITUDE
# 3. CS FUNDAMENTALS
# 4. SQL / DBMS
# =========================================================

JOB_READINESS_QUESTIONS = {

    # =====================================================
    # AI / ML ENGINEER
    # =====================================================

    "AI / ML Engineer": [

        # ---------- CODING PRACTICE ----------

        {
            "question":
                "Which Python library is commonly used for numerical computing?",
            "choices": [
                ("a", "NumPy"),
                ("b", "Bootstrap"),
                ("c", "Django"),
                ("d", "CSS"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        {
            "question":
                "Which Python library is commonly used for data manipulation?",
            "choices": [
                ("a", "Pandas"),
                ("b", "Bootstrap"),
                ("c", "JSP"),
                ("d", "Servlet"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        {
            "question":
                "Which algorithm is commonly used for classification?",
            "choices": [
                ("a", "Logistic Regression"),
                ("b", "Binary Search"),
                ("c", "Bubble Sort"),
                ("d", "HTML"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        # ---------- APTITUDE ----------

        {
            "question":
                "If a model processes 200 records per minute, how many records can it process in 5 minutes?",
            "choices": [
                ("a", "400"),
                ("b", "600"),
                ("c", "1000"),
                ("d", "1200"),
            ],
            "answer": "c",
            "component": "aptitude",
        },

        {
            "question":
                "A dataset contains 800 records. If 25% are used for testing, how many records are used for testing?",
            "choices": [
                ("a", "100"),
                ("b", "150"),
                ("c", "200"),
                ("d", "250"),
            ],
            "answer": "c",
            "component": "aptitude",
        },

        # ---------- CS FUNDAMENTALS ----------

        {
            "question":
                "What is overfitting?",
            "choices": [
                (
                    "a",
                    "Model performs well on training data but poorly on unseen data"
                ),
                ("b", "Model has no training data"),
                ("c", "Database duplication"),
                ("d", "CSS rendering"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        {
            "question":
                "Which data structure is commonly used for graph traversal using BFS?",
            "choices": [
                ("a", "Queue"),
                ("b", "Stack"),
                ("c", "Heap"),
                ("d", "Array"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        {
            "question":
                "What is the purpose of train/test splitting?",
            "choices": [
                ("a", "Evaluate performance on unseen data"),
                ("b", "Delete data"),
                ("c", "Create HTML"),
                ("d", "Change passwords"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        # ---------- SQL / DBMS ----------

        {
            "question":
                "What does SQL primarily help with in an ML system?",
            "choices": [
                ("a", "Retrieving and managing data"),
                ("b", "Designing CSS"),
                ("c", "Creating HTML headings"),
                ("d", "Changing monitor brightness"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },

        {
            "question":
                "Which SQL feature combines related tables?",
            "choices": [
                ("a", "JOIN"),
                ("b", "DROP"),
                ("c", "CLEAR"),
                ("d", "COMMENT"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },
    ],


    # =====================================================
    # DATA ANALYST
    # =====================================================

    "Data Analyst": [

        # ---------- CODING PRACTICE ----------

        {
            "question":
                "Which Python library is widely used for tabular data analysis?",
            "choices": [
                ("a", "Pandas"),
                ("b", "Django"),
                ("c", "Tkinter"),
                ("d", "Flask"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        {
            "question":
                "Which chart is commonly useful for comparing categories?",
            "choices": [
                ("a", "Bar chart"),
                ("b", "Paragraph text"),
                ("c", "CSS animation"),
                ("d", "Plain text only"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        # ---------- APTITUDE ----------

        {
            "question":
                "A report contains 120 records and 25% are invalid. How many valid records remain?",
            "choices": [
                ("a", "30"),
                ("b", "60"),
                ("c", "90"),
                ("d", "100"),
            ],
            "answer": "c",
            "component": "aptitude",
        },

        {
            "question":
                "If a data analyst processes 50 rows in 2 minutes, how many rows can be processed in 10 minutes at the same rate?",
            "choices": [
                ("a", "100"),
                ("b", "150"),
                ("c", "200"),
                ("d", "250"),
            ],
            "answer": "d",
            "component": "aptitude",
        },

        # ---------- CS FUNDAMENTALS ----------

        {
            "question":
                "What is data cleaning?",
            "choices": [
                ("a", "Fixing missing, invalid or inconsistent data"),
                ("b", "Deleting all data"),
                ("c", "Changing CSS"),
                ("d", "Creating HTML"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        {
            "question":
                "Which measure represents the average of a dataset?",
            "choices": [
                ("a", "Mean"),
                ("b", "Range"),
                ("c", "Mode only"),
                ("d", "Count"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        # ---------- SQL / DBMS ----------

        {
            "question":
                "Which SQL command retrieves data?",
            "choices": [
                ("a", "SELECT"),
                ("b", "DROP"),
                ("c", "DELETE"),
                ("d", "UPDATE"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },

        {
            "question":
                "Which SQL clause groups rows with the same values?",
            "choices": [
                ("a", "GROUP BY"),
                ("b", "ORDER BY"),
                ("c", "WHERE"),
                ("d", "JOIN"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },

        {
            "question":
                "Which SQL function calculates the average?",
            "choices": [
                ("a", "AVG()"),
                ("b", "COUNT()"),
                ("c", "SUMROW()"),
                ("d", "TOTALROW()"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },
    ],


    # =====================================================
    # DATA SCIENTIST
    # =====================================================

    "Data Scientist": [

        # ---------- CODING PRACTICE ----------

        {
            "question":
                "Which Python library is commonly used for numerical computation?",
            "choices": [
                ("a", "NumPy"),
                ("b", "Bootstrap"),
                ("c", "HTML"),
                ("d", "JSP"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        {
            "question":
                "Which library is widely used for data manipulation?",
            "choices": [
                ("a", "Pandas"),
                ("b", "Servlet"),
                ("c", "CSS"),
                ("d", "Bootstrap"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        {
            "question":
                "What is overfitting?",
            "choices": [
                (
                    "a",
                    "Excellent training performance but poor generalization"
                ),
                ("b", "No data"),
                ("c", "Fast SQL query"),
                ("d", "CSS error"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        # ---------- APTITUDE ----------

        {
            "question":
                "A dataset has 1000 rows. If 20% is used for testing, how many rows are used for testing?",
            "choices": [
                ("a", "100"),
                ("b", "150"),
                ("c", "200"),
                ("d", "250"),
            ],
            "answer": "c",
            "component": "aptitude",
        },

        {
            "question":
                "If a model runs 4 experiments in 10 minutes, how many experiments can it run in 30 minutes?",
            "choices": [
                ("a", "8"),
                ("b", "10"),
                ("c", "12"),
                ("d", "16"),
            ],
            "answer": "c",
            "component": "aptitude",
        },

        # ---------- CS FUNDAMENTALS ----------

        {
            "question":
                "What is the purpose of train/test splitting?",
            "choices": [
                ("a", "Evaluate model performance on unseen data"),
                ("b", "Delete data"),
                ("c", "Create HTML"),
                ("d", "Change database passwords"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        {
            "question":
                "What does standard deviation measure?",
            "choices": [
                ("a", "Spread of data"),
                ("b", "Number of tables"),
                ("c", "HTML size"),
                ("d", "Network speed"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        # ---------- SQL / DBMS ----------

        {
            "question":
                "Which SQL feature combines related tables?",
            "choices": [
                ("a", "JOIN"),
                ("b", "DROP"),
                ("c", "CLEAR"),
                ("d", "COMMENT"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },

        {
            "question":
                "Which SQL command retrieves records?",
            "choices": [
                ("a", "SELECT"),
                ("b", "INSERT"),
                ("c", "DROP"),
                ("d", "UPDATE"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },
    ],


    # =====================================================
    # PYTHON DEVELOPER
    # =====================================================

    "Python Developer": [

        # ---------- CODING PRACTICE ----------

        {
            "question":
                "Which Python structure stores key-value pairs?",
            "choices": [
                ("a", "List"),
                ("b", "Tuple"),
                ("c", "Dictionary"),
                ("d", "Set"),
            ],
            "answer": "c",
            "component": "coding_practice",
        },

        {
            "question":
                "Which mechanism handles exceptions in Python?",
            "choices": [
                ("a", "try-except"),
                ("b", "for-in"),
                ("c", "if-else"),
                ("d", "switch"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        {
            "question":
                "Which data structure follows LIFO?",
            "choices": [
                ("a", "Queue"),
                ("b", "Stack"),
                ("c", "Tree"),
                ("d", "Graph"),
            ],
            "answer": "b",
            "component": "coding_practice",
        },

        # ---------- APTITUDE ----------

        {
            "question":
                "If a program processes 80 requests per minute, how many requests can it process in 5 minutes?",
            "choices": [
                ("a", "200"),
                ("b", "300"),
                ("c", "400"),
                ("d", "500"),
            ],
            "answer": "c",
            "component": "aptitude",
        },

        {
            "question":
                "A Python application has 200 test cases and 10% fail. How many test cases pass?",
            "choices": [
                ("a", "180"),
                ("b", "190"),
                ("c", "200"),
                ("d", "170"),
            ],
            "answer": "a",
            "component": "aptitude",
        },

        # ---------- CS FUNDAMENTALS ----------

        {
            "question":
                "Which HTTP method is normally used to create a new resource?",
            "choices": [
                ("a", "GET"),
                ("b", "POST"),
                ("c", "HEAD"),
                ("d", "OPTIONS"),
            ],
            "answer": "b",
            "component": "cs_fundamentals",
        },

        {
            "question":
                "Which data structure follows FIFO?",
            "choices": [
                ("a", "Stack"),
                ("b", "Queue"),
                ("c", "Tree"),
                ("d", "Graph"),
            ],
            "answer": "b",
            "component": "cs_fundamentals",
        },

        # ---------- SQL / DBMS ----------

        {
            "question":
                "Which SQL command retrieves records?",
            "choices": [
                ("a", "INSERT"),
                ("b", "SELECT"),
                ("c", "UPDATE"),
                ("d", "DROP"),
            ],
            "answer": "b",
            "component": "sql_dbms",
        },

        {
            "question":
                "Which SQL feature retrieves related data from multiple tables?",
            "choices": [
                ("a", "JOIN"),
                ("b", "DROP"),
                ("c", "CLEAR"),
                ("d", "DELETE"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },
    ],


    # =====================================================
    # JAVA DEVELOPER
    # =====================================================

    "Java Developer": [

        # ---------- CODING PRACTICE ----------

        {
            "question":
                "Which concept allows a Java class to acquire another class's properties?",
            "choices": [
                ("a", "Inheritance"),
                ("b", "Iteration"),
                ("c", "Casting"),
                ("d", "Compilation"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        {
            "question":
                "Which collection stores unique values?",
            "choices": [
                ("a", "Set"),
                ("b", "List"),
                ("c", "ArrayList"),
                ("d", "Vector"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        {
            "question":
                "Same method name with different parameters is called?",
            "choices": [
                ("a", "Overloading"),
                ("b", "Overriding"),
                ("c", "Inheritance"),
                ("d", "Abstraction"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        # ---------- APTITUDE ----------

        {
            "question":
                "If a Java program processes 50 records per second, how many records can it process in 10 seconds?",
            "choices": [
                ("a", "100"),
                ("b", "250"),
                ("c", "500"),
                ("d", "1000"),
            ],
            "answer": "c",
            "component": "aptitude",
        },

        {
            "question":
                "A program has 80 test cases and 75% pass. How many pass?",
            "choices": [
                ("a", "40"),
                ("b", "50"),
                ("c", "60"),
                ("d", "70"),
            ],
            "answer": "c",
            "component": "aptitude",
        },

        # ---------- CS FUNDAMENTALS ----------

        {
            "question":
                "Which keyword is used for class inheritance?",
            "choices": [
                ("a", "implements"),
                ("b", "extends"),
                ("c", "inherits"),
                ("d", "superclass"),
            ],
            "answer": "b",
            "component": "cs_fundamentals",
        },

        {
            "question":
                "Which mechanism handles exceptions in Java?",
            "choices": [
                ("a", "try-catch"),
                ("b", "for-catch"),
                ("c", "loop-catch"),
                ("d", "switch-catch"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        # ---------- SQL / DBMS ----------

        {
            "question":
                "Which SQL command retrieves data?",
            "choices": [
                ("a", "SELECT"),
                ("b", "INSERT"),
                ("c", "DROP"),
                ("d", "UPDATE"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },

        {
            "question":
                "Which SQL feature retrieves related data from multiple tables?",
            "choices": [
                ("a", "JOIN"),
                ("b", "DROP"),
                ("c", "TRUNCATE"),
                ("d", "CLEAR"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },
    ],


    # =====================================================
    # FULL STACK DEVELOPER
    # =====================================================

    "Full Stack Developer": [

        # ---------- CODING PRACTICE ----------

        {
            "question":
                "Which HTML element creates a hyperlink?",
            "choices": [
                ("a", "<link>"),
                ("b", "<a>"),
                ("c", "<href>"),
                ("d", "<url>"),
            ],
            "answer": "b",
            "component": "coding_practice",
        },

        {
            "question":
                "Which CSS layout system is mainly one-dimensional?",
            "choices": [
                ("a", "Flexbox"),
                ("b", "SQL"),
                ("c", "DOM"),
                ("d", "AJAX"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        {
            "question":
                "Which technology makes web pages interactive?",
            "choices": [
                ("a", "JavaScript"),
                ("b", "SQL"),
                ("c", "MySQL"),
                ("d", "DNS"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        # ---------- APTITUDE ----------

        {
            "question":
                "A server handles 120 requests per minute. How many requests can it handle in 5 minutes?",
            "choices": [
                ("a", "300"),
                ("b", "500"),
                ("c", "600"),
                ("d", "700"),
            ],
            "answer": "c",
            "component": "aptitude",
        },

        {
            "question":
                "A website has 400 users and 25% are active. How many users are active?",
            "choices": [
                ("a", "50"),
                ("b", "100"),
                ("c", "150"),
                ("d", "200"),
            ],
            "answer": "b",
            "component": "aptitude",
        },

        # ---------- CS FUNDAMENTALS ----------

        {
            "question":
                "Which HTTP method retrieves data?",
            "choices": [
                ("a", "GET"),
                ("b", "POST"),
                ("c", "DELETE"),
                ("d", "PATCH"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        {
            "question":
                "Which HTTP status code means resource not found?",
            "choices": [
                ("a", "200"),
                ("b", "201"),
                ("c", "404"),
                ("d", "500"),
            ],
            "answer": "c",
            "component": "cs_fundamentals",
        },

        # ---------- SQL / DBMS ----------

        {
            "question":
                "Which SQL command retrieves records?",
            "choices": [
                ("a", "SELECT"),
                ("b", "INSERT"),
                ("c", "DROP"),
                ("d", "DELETE"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },

        {
            "question":
                "Which SQL feature combines related tables?",
            "choices": [
                ("a", "JOIN"),
                ("b", "DROP"),
                ("c", "CLEAR"),
                ("d", "COMMENT"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },
    ],


    # =====================================================
    # CLOUD ENGINEER
    # =====================================================

    "Cloud Engineer": [

        # ---------- CODING PRACTICE ----------

        {
            "question":
                "Which Python feature is useful for cloud automation scripts?",
            "choices": [
                ("a", "File handling and scripting"),
                ("b", "HTML tags"),
                ("c", "CSS selectors"),
                ("d", "SQL DROP only"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        {
            "question":
                "Which command is commonly used to list files in Linux?",
            "choices": [
                ("a", "ls"),
                ("b", "listfiles"),
                ("c", "show"),
                ("d", "dirsql"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        {
            "question":
                "Which tool is commonly used for version control?",
            "choices": [
                ("a", "Git"),
                ("b", "HTML"),
                ("c", "MySQL"),
                ("d", "CSS"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        # ---------- APTITUDE ----------

        {
            "question":
                "If a server handles 100 requests per minute, how many requests can it handle in 5 minutes?",
            "choices": [
                ("a", "100"),
                ("b", "300"),
                ("c", "500"),
                ("d", "1000"),
            ],
            "answer": "c",
            "component": "aptitude",
        },

        {
            "question":
                "A system has 99% uptime. Out of 1000 hours, approximately how many hours are unavailable?",
            "choices": [
                ("a", "1 hour"),
                ("b", "10 hours"),
                ("c", "50 hours"),
                ("d", "100 hours"),
            ],
            "answer": "b",
            "component": "aptitude",
        },

        # ---------- CS FUNDAMENTALS ----------

        {
            "question":
                "Which operating system is commonly used for cloud servers?",
            "choices": [
                ("a", "Linux"),
                ("b", "DOS"),
                ("c", "BIOS"),
                ("d", "HTML"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        {
            "question":
                "Which technology is commonly used to package applications into containers?",
            "choices": [
                ("a", "Docker"),
                ("b", "Photoshop"),
                ("c", "Bootstrap"),
                ("d", "Excel"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        {
            "question":
                "Which HTTP status code means a successful request?",
            "choices": [
                ("a", "404"),
                ("b", "500"),
                ("c", "200"),
                ("d", "403"),
            ],
            "answer": "c",
            "component": "cs_fundamentals",
        },

        {
            "question":
                "What does DNS primarily do?",
            "choices": [
                ("a", "Maps domain names to IP addresses"),
                ("b", "Stores passwords"),
                ("c", "Compiles Python"),
                ("d", "Creates databases"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        # ---------- SQL / DBMS ----------

        {
            "question":
                "Which SQL command retrieves records?",
            "choices": [
                ("a", "SELECT"),
                ("b", "DROP"),
                ("c", "DELETE"),
                ("d", "UPDATE"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },

        {
            "question":
                "Which SQL clause filters rows?",
            "choices": [
                ("a", "WHERE"),
                ("b", "FILTER"),
                ("c", "CHECK"),
                ("d", "SORT"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },
    ],


    # =====================================================
    # CYBERSECURITY ANALYST
    # =====================================================

    "Cybersecurity Analyst": [

        # ---------- CODING PRACTICE ----------

        {
            "question":
                "Which HTTP status code indicates a successful request?",
            "choices": [
                ("a", "200"),
                ("b", "404"),
                ("c", "500"),
                ("d", "403"),
            ],
            "answer": "a",
            "component": "coding_practice",
        },

        # ---------- APTITUDE ----------

        {
            "question":
                "A security system checks 200 events per minute. How many events can it check in 5 minutes?",
            "choices": [
                ("a", "500"),
                ("b", "800"),
                ("c", "1000"),
                ("d", "1200"),
            ],
            "answer": "c",
            "component": "aptitude",
        },

        {
            "question":
                "A monitoring system detects 90% of 500 suspicious events. How many events does it detect?",
            "choices": [
                ("a", "400"),
                ("b", "450"),
                ("c", "475"),
                ("d", "490"),
            ],
            "answer": "b",
            "component": "aptitude",
        },

        # ---------- CS FUNDAMENTALS ----------

        {
            "question":
                "Which principle ensures that only authorized users can access information?",
            "choices": [
                ("a", "Confidentiality"),
                ("b", "Compression"),
                ("c", "Compilation"),
                ("d", "Iteration"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        {
            "question":
                "Which attack attempts to trick users into revealing sensitive information?",
            "choices": [
                ("a", "Phishing"),
                ("b", "Sorting"),
                ("c", "Caching"),
                ("d", "Indexing"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        {
            "question":
                "What is the purpose of a firewall?",
            "choices": [
                ("a", "Control network traffic"),
                ("b", "Store passwords in plain text"),
                ("c", "Compile programs"),
                ("d", "Create HTML pages"),
            ],
            "answer": "a",
            "component": "cs_fundamentals",
        },

        # ---------- SQL / DBMS ----------

        {
            "question":
                "Which SQL command retrieves records from a database?",
            "choices": [
                ("a", "SELECT"),
                ("b", "DELETE"),
                ("c", "DROP"),
                ("d", "UPDATE"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },

        {
            "question":
                "Which type of vulnerability involves untrusted input being interpreted as part of a SQL query?",
            "choices": [
                ("a", "SQL Injection"),
                ("b", "DDoS"),
                ("c", "Phishing"),
                ("d", "Brute-force"),
            ],
            "answer": "a",
            "component": "sql_dbms",
        },
    ],
}


# =========================================================
# JOB READINESS FORM
# =========================================================

class JobReadinessForm(forms.Form):

    def __init__(
        self,
        *args,
        recommended_career=None,
        **kwargs
    ):
        super().__init__(
            *args,
            **kwargs
        )

        self.recommended_career = recommended_career

        questions = JOB_READINESS_QUESTIONS.get(
            recommended_career,
            []
        )

        for index, question in enumerate(questions):

            self.fields[
                f"job_{index}"
            ] = forms.ChoiceField(

                label=question["question"],

                choices=question["choices"],

                widget=forms.RadioSelect,

                required=True,
            )


# =========================================================
# INTERVIEW PREPARATION QUESTION BANK
# =========================================================

INTERVIEW_QUESTIONS = {

    # =====================================================
    # JAVA DEVELOPER
    # =====================================================

    "Java Developer": [

        {
            "question": "What is OOP in Java?",
            "choices": [
                ("a", "Object-Oriented Programming"),
                ("b", "Object Operating Process"),
                ("c", "Ordered Object Program"),
                ("d", "Open Operating Program"),
            ],
            "answer": "a",
        },

        {
            "question": "What is inheritance in Java?",
            "choices": [
                ("a", "Acquiring properties and behavior from another class"),
                ("b", "Deleting a class"),
                ("c", "Creating a database"),
                ("d", "Running a loop"),
            ],
            "answer": "a",
        },

        {
            "question": "What is method overloading?",
            "choices": [
                ("a", "Same method name with different parameters"),
                ("b", "Different method names with same parameters"),
                ("c", "Deleting a method"),
                ("d", "Calling a method once"),
            ],
            "answer": "a",
        },

        {
            "question": "Which keyword is used to inherit a class in Java?",
            "choices": [
                ("a", "implements"),
                ("b", "extends"),
                ("c", "inherits"),
                ("d", "super"),
            ],
            "answer": "b",
        },

        {
            "question": "What is exception handling?",
            "choices": [
                ("a", "Managing runtime errors"),
                ("b", "Creating objects"),
                ("c", "Creating CSS"),
                ("d", "Designing databases"),
            ],
            "answer": "a",
        },
    ],


    # =====================================================
    # PYTHON DEVELOPER
    # =====================================================

    "Python Developer": [

        {
            "question": "What is Python?",
            "choices": [
                ("a", "A high-level programming language"),
                ("b", "A database"),
                ("c", "An operating system"),
                ("d", "A web browser"),
            ],
            "answer": "a",
        },

        {
            "question": "Which keyword defines a function in Python?",
            "choices": [
                ("a", "function"),
                ("b", "define"),
                ("c", "def"),
                ("d", "fun"),
            ],
            "answer": "c",
        },

        {
            "question": "What is a dictionary in Python?",
            "choices": [
                ("a", "A key-value data structure"),
                ("b", "A sorting algorithm"),
                ("c", "A database server"),
                ("d", "A loop"),
            ],
            "answer": "a",
        },

        {
            "question": "Which structure handles exceptions in Python?",
            "choices": [
                ("a", "try-except"),
                ("b", "for-loop"),
                ("c", "if-switch"),
                ("d", "while-case"),
            ],
            "answer": "a",
        },

        {
            "question": "Which framework is commonly used for Python web development?",
            "choices": [
                ("a", "Django"),
                ("b", "Spring"),
                ("c", "JSP"),
                ("d", "Servlet"),
            ],
            "answer": "a",
        },
    ],


    # =====================================================
    # CLOUD ENGINEER
    # =====================================================

    "Cloud Engineer": [

        {
            "question": "What is cloud computing?",
            "choices": [
                ("a", "Delivery of computing resources over the internet"),
                ("b", "Only offline storage"),
                ("c", "Only database programming"),
                ("d", "Only website design"),
            ],
            "answer": "a",
        },

        {
            "question": "What does IaaS stand for?",
            "choices": [
                ("a", "Infrastructure as a Service"),
                ("b", "Internet as a System"),
                ("c", "Information as Software"),
                ("d", "Infrastructure as Software"),
            ],
            "answer": "a",
        },

        {
            "question": "Which is a major cloud service provider?",
            "choices": [
                ("a", "AWS"),
                ("b", "HTML"),
                ("c", "CSS"),
                ("d", "Bootstrap"),
            ],
            "answer": "a",
        },

        {
            "question": "Why is Linux important for cloud engineers?",
            "choices": [
                ("a", "Many cloud servers run Linux"),
                ("b", "It creates HTML automatically"),
                ("c", "It replaces SQL"),
                ("d", "It is a database"),
            ],
            "answer": "a",
        },

        {
            "question": "What is Docker mainly used for?",
            "choices": [
                ("a", "Containerization"),
                ("b", "Graphic design"),
                ("c", "Database normalization"),
                ("d", "Writing CSS"),
            ],
            "answer": "a",
        },
    ],


    # =====================================================
    # DATA ANALYST
    # =====================================================

    "Data Analyst": [

        {
            "question": "What is data cleaning?",
            "choices": [
                ("a", "Fixing inaccurate or inconsistent data"),
                ("b", "Deleting every row"),
                ("c", "Designing a website"),
                ("d", "Creating passwords"),
            ],
            "answer": "a",
        },

        {
            "question": "Which language is commonly used to query databases?",
            "choices": [
                ("a", "SQL"),
                ("b", "HTML"),
                ("c", "CSS"),
                ("d", "XML"),
            ],
            "answer": "a",
        },

        {
            "question": "Which Python library is widely used for data analysis?",
            "choices": [
                ("a", "Pandas"),
                ("b", "Django"),
                ("c", "Flask"),
                ("d", "Tkinter"),
            ],
            "answer": "a",
        },

        {
            "question": "What does GROUP BY do in SQL?",
            "choices": [
                ("a", "Groups rows based on values"),
                ("b", "Deletes rows"),
                ("c", "Creates tables"),
                ("d", "Changes passwords"),
            ],
            "answer": "a",
        },

        {
            "question": "What is the mean?",
            "choices": [
                ("a", "Average value"),
                ("b", "Largest value"),
                ("c", "Smallest value"),
                ("d", "Number of columns"),
            ],
            "answer": "a",
        },
    ],


    # =====================================================
    # DATA SCIENTIST
    # =====================================================

    "Data Scientist": [

        {
            "question": "What is machine learning?",
            "choices": [
                ("a", "A method where systems learn patterns from data"),
                ("b", "A database language"),
                ("c", "A CSS framework"),
                ("d", "An operating system"),
            ],
            "answer": "a",
        },

        {
            "question": "What is overfitting?",
            "choices": [
                ("a", "Good training performance but poor unseen-data performance"),
                ("b", "No training data"),
                ("c", "Database duplication"),
                ("d", "Network failure"),
            ],
            "answer": "a",
        },

        {
            "question": "Which Python library is commonly used for numerical computing?",
            "choices": [
                ("a", "NumPy"),
                ("b", "Django"),
                ("c", "Bootstrap"),
                ("d", "JSP"),
            ],
            "answer": "a",
        },

        {
            "question": "Why do we split data into training and testing sets?",
            "choices": [
                ("a", "To evaluate generalization on unseen data"),
                ("b", "To delete data"),
                ("c", "To create HTML"),
                ("d", "To change passwords"),
            ],
            "answer": "a",
        },

        {
            "question": "What is feature engineering?",
            "choices": [
                ("a", "Creating useful input features from raw data"),
                ("b", "Creating CSS pages"),
                ("c", "Deleting models"),
                ("d", "Creating databases only"),
            ],
            "answer": "a",
        },
    ],


    # =====================================================
    # FULL STACK DEVELOPER
    # =====================================================

    "Full Stack Developer": [

        {
            "question": "What does front-end development mainly involve?",
            "choices": [
                ("a", "Building the user interface"),
                ("b", "Managing only databases"),
                ("c", "Managing operating systems"),
                ("d", "Writing only server scripts"),
            ],
            "answer": "a",
        },

        {
            "question": "Which technology makes web pages interactive?",
            "choices": [
                ("a", "JavaScript"),
                ("b", "SQL"),
                ("c", "MySQL"),
                ("d", "DNS"),
            ],
            "answer": "a",
        },

        {
            "question": "What does REST API provide?",
            "choices": [
                ("a", "A way for applications to communicate through web services"),
                ("b", "Only CSS styling"),
                ("c", "Only image editing"),
                ("d", "Only database backups"),
            ],
            "answer": "a",
        },

        {
            "question": "Which HTTP method is commonly used to create a resource?",
            "choices": [
                ("a", "GET"),
                ("b", "POST"),
                ("c", "DELETE"),
                ("d", "HEAD"),
            ],
            "answer": "b",
        },

        {
            "question": "What is responsive web design?",
            "choices": [
                ("a", "Design that adapts to different screen sizes"),
                ("b", "Design for one fixed screen"),
                ("c", "Database optimization"),
                ("d", "Server monitoring"),
            ],
            "answer": "a",
        },
    ],


    # =====================================================
    # AI / ML ENGINEER
    # =====================================================

    "AI / ML Engineer": [

        {
            "question": "What is supervised learning?",
            "choices": [
                ("a", "Learning from labeled data"),
                ("b", "Learning without data"),
                ("c", "Learning only from databases"),
                ("d", "Learning CSS"),
            ],
            "answer": "a",
        },

        {
            "question": "What is classification?",
            "choices": [
                ("a", "Predicting categories or classes"),
                ("b", "Predicting only continuous values"),
                ("c", "Sorting files"),
                ("d", "Creating tables"),
            ],
            "answer": "a",
        },

        {
            "question": "What is overfitting?",
            "choices": [
                ("a", "Model learns training data too closely"),
                ("b", "Model has no data"),
                ("c", "Model has no features"),
                ("d", "Database error"),
            ],
            "answer": "a",
        },

        {
            "question": "Why is data preprocessing important?",
            "choices": [
                ("a", "To prepare clean and useful data for a model"),
                ("b", "To create HTML"),
                ("c", "To change passwords"),
                ("d", "To design CSS"),
            ],
            "answer": "a",
        },

        {
            "question": "Which library is commonly used for machine learning in Python?",
            "choices": [
                ("a", "Scikit-learn"),
                ("b", "Bootstrap"),
                ("c", "JSP"),
                ("d", "Servlet"),
            ],
            "answer": "a",
        },
    ],


    # =====================================================
    # CYBERSECURITY ANALYST
    # =====================================================

    "Cybersecurity Analyst": [

        {
            "question": "What is phishing?",
            "choices": [
                ("a", "A social engineering attack"),
                ("b", "A sorting algorithm"),
                ("c", "A database query"),
                ("d", "A CSS technique"),
            ],
            "answer": "a",
        },

        {
            "question": "What is a firewall?",
            "choices": [
                ("a", "A system that controls network traffic"),
                ("b", "A database"),
                ("c", "A programming language"),
                ("d", "A text editor"),
            ],
            "answer": "a",
        },

        {
            "question": "What is SQL injection?",
            "choices": [
                ("a", "An attack involving malicious SQL input"),
                ("b", "A sorting technique"),
                ("c", "A cloud service"),
                ("d", "A CSS attack"),
            ],
            "answer": "a",
        },

        {
            "question": "What does confidentiality mean in cybersecurity?",
            "choices": [
                ("a", "Only authorized users can access information"),
                ("b", "Everyone can access information"),
                ("c", "Information is deleted"),
                ("d", "Information is compressed"),
            ],
            "answer": "a",
        },

        {
            "question": "What is authentication?",
            "choices": [
                ("a", "Verifying the identity of a user"),
                ("b", "Deleting an account"),
                ("c", "Encrypting every file"),
                ("d", "Creating a database"),
            ],
            "answer": "a",
        },
    ],
}


# =========================================================
# INTERVIEW PREPARATION FORM
# =========================================================

class InterviewPreparationForm(forms.Form):

    def __init__(
        self,
        *args,
        recommended_career=None,
        **kwargs
    ):
        super().__init__(
            *args,
            **kwargs
        )

        self.recommended_career = recommended_career

        questions = INTERVIEW_QUESTIONS.get(
            recommended_career,
            []
        )

        for index, question in enumerate(questions):

            self.fields[
                f"interview_{index}"
            ] = forms.ChoiceField(

                label=question["question"],

                choices=question["choices"],

                widget=forms.RadioSelect,

                required=True,
            )