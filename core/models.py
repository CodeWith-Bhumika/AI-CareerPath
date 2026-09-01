from django.db import models


# ============================================================
# STUDENT PROFILE
# ============================================================

class StudentProfile(models.Model):

    name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    college = models.CharField(
        max_length=200,
        blank=True,
        default=""
    )

    career_interest = models.CharField(
        max_length=150,
        blank=True,
        default=""
    )

    skills = models.TextField(
        blank=True,
        default=""
    )

    # ========================================================
    # CAREER PROFILE
    # ========================================================

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True
    )

    projects = models.TextField(
        blank=True,
        default=""
    )

    github_portfolio = models.URLField(
        blank=True,
        default=""
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


# ============================================================
# SKILL ASSESSMENT
# ============================================================

class SkillAssessment(models.Model):

    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name="skill_assessments"
    )

    selected_skills = models.TextField(
        blank=True,
        default=""
    )

    # --------------------------------------------------------
    # SKILL SCORES
    # --------------------------------------------------------

    # NULL = skill was NOT selected/assessed
    # 0 = skill WAS assessed but score was 0

    python = models.FloatField(
        null=True,
        blank=True
    )

    java = models.FloatField(
        null=True,
        blank=True
    )

    sql = models.FloatField(
        null=True,
        blank=True
    )

    html_css = models.FloatField(
        null=True,
        blank=True
    )

    dsa = models.FloatField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.student.name} - "
            f"Assessment {self.id}"
        )


# ============================================================
# JOB READINESS
# ============================================================

class JobReadiness(models.Model):

    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name="job_readiness"
    )

    # --------------------------------------------------------
    # OVERALL READINESS
    # --------------------------------------------------------

    readiness_score = models.FloatField(
        default=0
    )

    readiness_status = models.CharField(
        max_length=50,
        default="Not Assessed"
    )

    # --------------------------------------------------------
    # READINESS COMPONENTS
    # --------------------------------------------------------

    coding_practice = models.FloatField(
        null=True,
        blank=True
    )

    aptitude = models.FloatField(
        null=True,
        blank=True
    )

    cs_fundamentals = models.FloatField(
        null=True,
        blank=True
    )

    sql_dbms = models.FloatField(
        null=True,
        blank=True
    )

    # --------------------------------------------------------
    # OLD READINESS FIELDS
    # --------------------------------------------------------
    # Kept unchanged so your existing code/database does not
    # break. These are currently NOT used in the final score.

    projects = models.FloatField(
        null=True,
        blank=True
    )

    resume = models.FloatField(
        null=True,
        blank=True
    )

    github_portfolio = models.FloatField(
        null=True,
        blank=True
    )

    interview_preparation = models.FloatField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.student.name} - "
            f"{self.readiness_score}%"
        )

    # ============================================================
# INTERVIEW PREPARATION QUESTIONS
# ============================================================

INTERVIEW_QUESTIONS = {

    "Java Developer": [
        {
            "question": "What is inheritance in Java?",
            "options": [
                "Acquiring properties of another class",
                "Deleting a class",
                "Creating a database",
                "Running a loop"
            ],
            "answer": "Acquiring properties of another class"
        },
        {
            "question": "What is method overloading?",
            "options": [
                "Same method name with different parameters",
                "Same method name in two files",
                "Deleting a method",
                "Calling a method repeatedly"
            ],
            "answer": "Same method name with different parameters"
        },
        {
            "question": "Which keyword is used for inheritance in Java?",
            "options": [
                "extends",
                "implements",
                "inherits",
                "super"
            ],
            "answer": "extends"
        },
        {
            "question": "Which collection stores unique values?",
            "options": [
                "Set",
                "List",
                "ArrayList",
                "Vector"
            ],
            "answer": "Set"
        },
        {
            "question": "What is exception handling used for?",
            "options": [
                "Handling runtime errors",
                "Creating classes",
                "Connecting CSS",
                "Sorting arrays"
            ],
            "answer": "Handling runtime errors"
        }
    ],

    "Python Developer": [
        {
            "question": "Which keyword defines a function in Python?",
            "options": [
                "def",
                "function",
                "func",
                "define"
            ],
            "answer": "def"
        },
        {
            "question": "Which data type stores key-value pairs?",
            "options": [
                "Dictionary",
                "List",
                "Tuple",
                "Set"
            ],
            "answer": "Dictionary"
        },
        {
            "question": "Which library is commonly used for numerical computing?",
            "options": [
                "NumPy",
                "Django",
                "Bootstrap",
                "CSS"
            ],
            "answer": "NumPy"
        },
        {
            "question": "Which keyword is used to handle exceptions?",
            "options": [
                "try",
                "catch",
                "exception",
                "handle"
            ],
            "answer": "try"
        },
        {
            "question": "Which framework is commonly used for Python web development?",
            "options": [
                "Django",
                "Spring",
                "JSP",
                "Servlet"
            ],
            "answer": "Django"
        }
    ],

    "Cloud Engineer": [
        {
            "question": "What does cloud computing provide?",
            "options": [
                "On-demand computing resources",
                "Only offline storage",
                "Only desktop applications",
                "Only databases"
            ],
            "answer": "On-demand computing resources"
        },
        {
            "question": "Which service model provides virtual machines?",
            "options": [
                "IaaS",
                "SaaS",
                "PaaS",
                "DBaaS"
            ],
            "answer": "IaaS"
        },
        {
            "question": "Which platform is a major cloud provider?",
            "options": [
                "AWS",
                "HTML",
                "CSS",
                "Bootstrap"
            ],
            "answer": "AWS"
        },
        {
            "question": "What is cloud scalability?",
            "options": [
                "Ability to increase or decrease resources",
                "Deleting servers",
                "Changing passwords",
                "Writing HTML"
            ],
            "answer": "Ability to increase or decrease resources"
        },
        {
            "question": "Which technology is commonly used for containerization?",
            "options": [
                "Docker",
                "Excel",
                "Bootstrap",
                "JQuery"
            ],
            "answer": "Docker"
        }
    ],

    "Data Analyst": [
        {
            "question": "Which language is commonly used for querying databases?",
            "options": [
                "SQL",
                "HTML",
                "CSS",
                "XML"
            ],
            "answer": "SQL"
        },
        {
            "question": "Which Python library is commonly used for data manipulation?",
            "options": [
                "Pandas",
                "Django",
                "Bootstrap",
                "JSP"
            ],
            "answer": "Pandas"
        },
        {
            "question": "Which visualization library is commonly used in Python?",
            "options": [
                "Matplotlib",
                "Django",
                "Flask",
                "Servlet"
            ],
            "answer": "Matplotlib"
        },
        {
            "question": "Which SQL command retrieves data?",
            "options": [
                "SELECT",
                "INSERT",
                "DROP",
                "UPDATE"
            ],
            "answer": "SELECT"
        },
        {
            "question": "What does GROUP BY do in SQL?",
            "options": [
                "Groups rows based on a column",
                "Deletes rows",
                "Creates a database",
                "Changes passwords"
            ],
            "answer": "Groups rows based on a column"
        }
    ]
}