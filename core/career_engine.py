
# ==========================================
# AI CareerPath - Career Recommendation Engine
# ==========================================


# ==========================================
# CAREER REQUIREMENTS
# ==========================================

CAREER_REQUIREMENTS = {

    "AI / ML Engineer": {
        "python": 90,
        "dsa": 75,
        "sql": 70,
        "java": 40,
        "html_css": 30,
    },

    "Data Analyst": {
        "sql": 85,
        "python": 70,
        "dsa": 50,
        "java": 30,
        "html_css": 30,
    },

    "Data Scientist": {
        "python": 90,
        "sql": 80,
        "dsa": 60,
        "java": 30,
        "html_css": 20,
    },

    "Python Developer": {
        "python": 90,
        "dsa": 70,
        "sql": 60,
        "java": 30,
        "html_css": 40,
    },

    "Java Developer": {
        "java": 85,
        "dsa": 75,
        "sql": 70,
        "python": 40,
        "html_css": 40,
    },

    "Full Stack Developer": {
        "html_css": 85,
        "java": 70,
        "dsa": 70,
        "sql": 75,
        "python": 50,
    },

    "Cloud Engineer": {
        "python": 60,
        "dsa": 55,
        "sql": 50,
        "java": 50,
        "html_css": 30,
    },

    "Cybersecurity Analyst": {
        "python": 70,
        "sql": 65,
        "dsa": 60,
        "java": 40,
        "html_css": 25,
    },
}


# ==========================================
# CORE SKILLS
# ==========================================

CORE_SKILLS = {

    "AI / ML Engineer": [
        "python",
        "dsa",
    ],

    "Data Analyst": [
        "sql",
        "python",
    ],

    "Data Scientist": [
        "python",
        "sql",
    ],

    "Python Developer": [
        "python",
        "dsa",
    ],

    "Java Developer": [
        "java",
        "dsa",
    ],

    "Full Stack Developer": [
        "html_css",
        "java",
        "sql",
    ],

    "Cloud Engineer": [
        "python",
        "dsa",
    ],

    "Cybersecurity Analyst": [
        "python",
        "sql",
    ],
}


# ==========================================
# CAREER DESCRIPTIONS
# ==========================================

CAREER_DESCRIPTIONS = {

    "AI / ML Engineer":
        "Build AI and machine learning systems using Python, data and algorithms.",

    "Data Analyst":
        "Analyze data and create insights using SQL, Python and analytical tools.",

    "Data Scientist":
        "Use Python, SQL and statistical techniques to solve data-driven problems.",

    "Python Developer":
        "Build backend applications, automation tools and software using Python.",

    "Java Developer":
        "Build enterprise and backend applications using Java and object-oriented programming.",

    "Full Stack Developer":
        "Build complete web applications across frontend and backend technologies.",

    "Cloud Engineer":
        "Work with cloud infrastructure, automation, deployment and scalable systems.",

    "Cybersecurity Analyst":
        "Identify security risks, analyze systems and help protect applications and data.",
}


# ==========================================
# SKILL NAME NORMALIZATION
# ==========================================

def normalize_skill_name(skill):

    if not skill:
        return None

    skill = str(skill).strip().lower()

    aliases = {

        "python": "python",

        "java": "java",

        "sql": "sql",

        "dsa": "dsa",

        "html & css": "html_css",

        "html_css": "html_css",

        "html-css": "html_css",

        "html css": "html_css",
    }

    return aliases.get(
        skill,
        skill
    )


# ==========================================
# NORMALIZE STUDENT SKILLS
# ==========================================

def normalize_skills(skills):

    normalized = {}

    if not skills:
        return normalized

    for skill, score in skills.items():

        normalized_skill = normalize_skill_name(
            skill
        )

        if not normalized_skill:
            continue

        try:
            score = float(score or 0)

        except (TypeError, ValueError):
            score = 0

        score = max(
            0,
            min(score, 100)
        )

        normalized[normalized_skill] = score

    return normalized


# ==========================================
# CAREER RECOMMENDATION
# ==========================================

def recommend_career(skills):

    normalized_skills = normalize_skills(
        skills
    )

    career_scores = {}

    if not normalized_skills:
        return (
            "No Career Selected",
            {}
        )

    # ======================================
    # CALCULATE CAREER SCORES
    # ======================================

    for career, requirements in (
        CAREER_REQUIREMENTS.items()
    ):

        core_skills = CORE_SKILLS.get(
            career,
            []
        )

        assessed_core = [
            skill
            for skill in core_skills
            if skill in normalized_skills
        ]

        # No selected core skill
        if not assessed_core:

            career_scores[career] = 0

            continue

        total_score = 0
        total_weight = 0

        # ----------------------------------
        # ONLY STUDENT SELECTED SKILLS
        # ----------------------------------

        for skill, student_score in (
            normalized_skills.items()
        ):

            if skill not in requirements:
                continue

            required_score = requirements[
                skill
            ]

            if required_score <= 0:
                continue

            match = (
                student_score
                / required_score
            ) * 100

            match = min(
                match,
                100
            )

            if skill in core_skills:
                weight = 2
            else:
                weight = 1

            total_score += (
                match * weight
            )

            total_weight += weight

        if total_weight == 0:

            career_scores[career] = 0

            continue

        final_score = (
            total_score
            / total_weight
        )

        # ----------------------------------
        # MISSING CORE PENALTY
        # ----------------------------------

        missing_core = (
            len(core_skills)
            - len(assessed_core)
        )

        final_score -= (
            missing_core * 5
        )

        # ----------------------------------
        # WEAK CORE PENALTY
        # ----------------------------------

        weak_core_count = 0

        for core_skill in assessed_core:

            if (
                normalized_skills[
                    core_skill
                ] < 40
            ):

                weak_core_count += 1

        final_score -= (
            weak_core_count * 3
        )

        final_score = max(
            0,
            min(
                final_score,
                100
            )
        )

        career_scores[career] = round(
            final_score,
            1
        )

    # ======================================
    # SELECT BEST CAREER
    # ======================================

    eligible_careers = {

        career: score

        for career, score
        in career_scores.items()

        if score > 0
    }

    if not eligible_careers:

        return (
            "No Career Selected",
            career_scores
        )

    recommended_career = max(
        eligible_careers,
        key=eligible_careers.get
    )

    return (
        recommended_career,
        career_scores
    )


# ==========================================
# SKILL GAP ANALYSIS
# ==========================================

def analyze_skill_gap(
    skills,
    career
):
    """
    Returns skill gap information.

    IMPORTANT:
    This function returns requirements for the
    career. The views.py filters this to ONLY
    skills selected by the student.
    """

    requirements = (
        CAREER_REQUIREMENTS.get(
            career,
            {}
        )
    )

    normalized_skills = normalize_skills(
        skills
    )

    skill_gaps = {}

    # ======================================
    # ONLY PROCESS SELECTED SKILLS
    # ======================================

    for skill, current in (
        normalized_skills.items()
    ):

        # ----------------------------------
        # Ignore unknown skills
        # ----------------------------------

        if skill not in requirements:
            continue

        required = float(
            requirements[skill]
        )

        current = float(
            current
        )

        gap = max(
            required - current,
            0
        )

        # ----------------------------------
        # STATUS
        # ----------------------------------

        if current >= required:

            status = "Excellent"

        elif current >= required * 0.70:

            status = "Good"

        elif current >= required * 0.40:

            status = "Needs Improvement"

        else:

            status = "Beginner"

        skill_gaps[skill] = {

            "current":
                round(
                    current,
                    1
                ),

            "required":
                round(
                    required,
                    1
                ),

            "gap":
                round(
                    gap,
                    1
                ),

            "status":
                status,
        }

    return skill_gaps

