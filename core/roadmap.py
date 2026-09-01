# ==========================================
# AI CareerPath - Personalized Roadmap
# ==========================================


# ==========================================
# TOPICS FOR EACH SKILL
# ==========================================

SKILL_TOPICS = {

    "python": [
        "Python Basics",
        "Variables, Data Types & Operators",
        "Conditions and Loops",
        "Functions",
        "OOP in Python",
        "Exception Handling",
        "File Handling",
        "NumPy",
        "Pandas",
        "Data Processing",
    ],

    "dsa": [
        "Arrays",
        "Strings",
        "Searching",
        "Sorting",
        "Linked Lists",
        "Stacks",
        "Queues",
        "Hashing",
        "Trees",
        "Basic Recursion",
    ],

    "sql": [
        "SELECT Queries",
        "WHERE and Filtering",
        "ORDER BY",
        "GROUP BY",
        "Aggregate Functions",
        "JOINS",
        "Subqueries",
        "Views",
        "Database Design",
    ],

    "java": [
        "Java Basics",
        "Variables and Data Types",
        "Classes and Objects",
        "OOP Concepts",
        "Inheritance",
        "Polymorphism",
        "Exception Handling",
        "Collections",
        "Java 8 Basics",
    ],

    "html_css": [
        "HTML Basics",
        "Forms",
        "Semantic HTML",
        "CSS Basics",
        "Selectors and Box Model",
        "Flexbox",
        "Grid",
        "Responsive Design",
        "Bootstrap",
    ],
}


# ==========================================
# DISPLAY NAMES
# ==========================================

SKILL_DISPLAY_NAMES = {

    "python": "Python",
    "dsa": "DSA",
    "sql": "SQL",
    "java": "Java",
    "html_css": "HTML & CSS",
}


# ==========================================
# NUMBER OF TOPICS TO SHOW
# ==========================================

TOPIC_LIMITS = {

    "python": 7,
    "dsa": 7,
    "sql": 7,
    "java": 7,
    "html_css": 7,
}


# ==========================================
# NORMALIZE SKILL NAME
# ==========================================

def normalize_skill_name(skill):

    if not skill:
        return None

    skill = str(skill).strip().lower()

    aliases = {

        "python": "python",

        "dsa": "dsa",
        "data structures": "dsa",
        "data structures and algorithms": "dsa",

        "sql": "sql",
        "mysql": "sql",

        "java": "java",

        "html": "html_css",
        "css": "html_css",
        "html css": "html_css",
        "html & css": "html_css",
        "html-css": "html_css",
        "html_css": "html_css",
    }

    return aliases.get(
        skill,
        skill
    )


# ==========================================
# SAFE FLOAT
# ==========================================

def safe_float(value, default=0):

    try:
        return float(value)

    except (TypeError, ValueError):

        return default


# ==========================================
# GENERATE PERSONALIZED ROADMAP
# ==========================================

def generate_roadmap(skill_gaps):

    roadmap = []

    # ==========================================
    # NO DATA
    # ==========================================

    if not skill_gaps:

        return roadmap


    # ==========================================
    # COLLECT VALID GAPS
    # ==========================================

    valid_gaps = []

    for skill, data in skill_gaps.items():

        if not isinstance(data, dict):

            continue


        # --------------------------------------
        # GET VALUES
        # --------------------------------------

        current = data.get(
            "current"
        )

        required = data.get(
            "required"
        )

        gap = data.get(
            "gap"
        )

        status = data.get(
            "status"
        )


        # --------------------------------------
        # SKIP UNASSESSED
        # --------------------------------------

        if current is None:

            continue


        # --------------------------------------
        # CONVERT NUMBERS
        # --------------------------------------

        current = safe_float(
            current,
            0
        )

        required = safe_float(
            required,
            0
        )


        # --------------------------------------
        # CALCULATE GAP IF NECESSARY
        # --------------------------------------

        if gap is None:

            gap = max(
                required - current,
                0
            )

        else:

            gap = safe_float(
                gap,
                max(
                    required - current,
                    0
                )
            )


        # --------------------------------------
        # SKIP TARGET-REACHED SKILLS
        # --------------------------------------

        if gap <= 0:

            continue


        # --------------------------------------
        # ADD VALID GAP
        # --------------------------------------

        valid_gaps.append({

            "skill": skill,

            "current": round(
                current,
                1
            ),

            "required": round(
                required,
                1
            ),

            "gap": round(
                gap,
                1
            ),

            "status": (
                status
                or "Needs Improvement"
            ),

        })


    # ==========================================
    # SORT BIGGEST GAP FIRST
    # ==========================================

    valid_gaps.sort(

        key=lambda item: item["gap"],

        reverse=True

    )


    # ==========================================
    # CREATE ROADMAP IN SERIAL ORDER
    # ==========================================

    for index, item in enumerate(
        valid_gaps
    ):

        skill = item["skill"]

        current = item["current"]

        required = item["required"]

        gap = item["gap"]

        status = item["status"]


        # ======================================
        # NORMALIZE SKILL
        # ======================================

        normalized_skill = (
            normalize_skill_name(
                skill
            )
        )


        # ======================================
        # GET DISPLAY NAME
        # ======================================

        display_skill = (
            SKILL_DISPLAY_NAMES.get(
                normalized_skill,
                str(skill).title()
            )
        )


        # ======================================
        # GET TOPICS
        # ======================================

        topics = SKILL_TOPICS.get(

            normalized_skill,

            []

        )


        # ======================================
        # LIMIT TOPICS
        # ======================================

        limit = TOPIC_LIMITS.get(

            normalized_skill,

            5

        )


        topics = topics[:limit]


        # ======================================
        # PRIORITY BY SERIAL POSITION
        # ======================================

        if index == 0:

            priority = "HIGH"

        elif index <= 2:

            priority = "MEDIUM"

        else:

            priority = "LOW"


        # ======================================
        # ROADMAP ITEM
        # ======================================

        roadmap.append({

            "step": index + 1,

            "skill": skill,

            "display_name": display_skill,

            "current": current,

            "required": required,

            "gap": gap,

            "status": status,

            "topics": topics,

            "priority": priority,

        })


    # ==========================================
    # RETURN
    # ==========================================

    return roadmap