
# ==========================================
# AI CareerPath - AI Career Advisor
# ==========================================

import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai


# ------------------------------------------
# LOAD ENVIRONMENT
# ------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


# ------------------------------------------
# GEMINI CLIENT
# ------------------------------------------

API_KEY = os.getenv("GEMINI_API_KEY")

client = None

if API_KEY:
    client = genai.Client(
        api_key=API_KEY
    )


# ==========================================
# HELPER: SAFE NUMBER
# ==========================================

def safe_number(value, default=0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


# ==========================================
# GENERATE AI CAREER ADVICE
# ==========================================

def generate_ai_advice(
    student_name,
    skills,
    recommended_career,
    skill_gaps
):
    """
    Generate structured AI career advice.

    IMPORTANT:
    - Only selected skills are used.
    - Unselected skills are never treated as zero.
    - AI does not change the recommended career.
    - Returns a dictionary suitable for result.html.
    """

    # --------------------------------------
    # SAFETY CHECK
    # --------------------------------------

    if not skills:

        return {
            "why_career": (
                "Please complete the skill assessment "
                "to receive personalized career advice."
            ),
            "strongest_skills": [],
            "biggest_gaps": [],
            "what_to_learn_first": [],
            "projects": [],
            "placement_action_plan": {
                "learn": "",
                "practice": "",
                "build": "",
                "interview": "",
            },
            "career": recommended_career,
            "student_name": student_name,
        }


    # --------------------------------------
    # NORMALIZE SKILL DATA
    # --------------------------------------

    clean_skills = {}

    for skill, score in skills.items():

        clean_skills[skill] = round(
            safe_number(score),
            2
        )


    # --------------------------------------
    # STRONGEST SKILLS
    # --------------------------------------

    sorted_skills = sorted(
        clean_skills.items(),
        key=lambda item: item[1],
        reverse=True
    )

    strongest_skills = sorted_skills[:3]


    strongest_text = "\n".join(
        f"- {skill}: {score}/100"
        for skill, score in strongest_skills
    )


    # --------------------------------------
    # SKILL GAPS
    # --------------------------------------

    improvement_skills = []
    completed_skills = []

    for skill, data in (skill_gaps or {}).items():

        if not isinstance(data, dict):
            continue

        current = data.get("current")
        required = data.get("required")
        gap = data.get("gap")
        status = data.get("status")

        if current is None:
            continue

        current = safe_number(current)
        required = safe_number(required)

        gap = max(
            required - current,
            0
        )

        if gap > 0:

            improvement_skills.append({
                "skill": skill,
                "current": round(current, 2),
                "required": round(required, 2),
                "gap": round(gap, 2),
                "status": status or "Needs Improvement",
            })

        else:

            completed_skills.append(
                f"- {skill}: "
                f"{round(current, 2)}/100 "
                f"(target {round(required, 2)}/100)"
            )


    # Biggest gaps first
    improvement_skills.sort(
        key=lambda item: item["gap"],
        reverse=True
    )


    # --------------------------------------
    # FORMAT GAPS
    # --------------------------------------

    if improvement_skills:

        gaps_text = "\n".join(
            f'- {item["skill"]}: '
            f'{item["current"]}/100 → '
            f'{item["required"]}/100 '
            f'(gap {item["gap"]})'
            for item in improvement_skills
        )

    else:

        gaps_text = (
            "No selected skill is currently below "
            "its required target."
        )


    # --------------------------------------
    # COMPLETED SKILLS
    # --------------------------------------

    if completed_skills:

        completed_text = "\n".join(
            completed_skills
        )

    else:

        completed_text = (
            "No selected skill has reached its "
            "target yet."
        )


    # --------------------------------------
    # AI PROMPT
    # --------------------------------------

    prompt = f"""
You are the AI Career Advisor inside a college
student career guidance application called
AI CareerPath.

The application's career engine has already
selected the recommended career.

You MUST NOT change the recommended career.

Use ONLY the information provided below.

Do NOT invent:
- experience
- internships
- certifications
- achievements
- projects already completed
- skills that were not assessed

IMPORTANT:

1. CURRENT SELECTED SKILLS are the only skills
   actually assessed.

2. An unselected skill must NOT be treated as
   score 0.

3. Do not describe an unselected skill as a
   current skill.

4. If a career requires a skill that was not
   assessed, say "Not assessed yet".

5. Do not tell the student to improve a skill
   that already meets its target.

6. Keep advice realistic for a college student.

7. Prioritize fundamentals before advanced topics.

8. Recommend exactly THREE practical projects.

9. Projects must be realistic and resume-friendly.

10. At least ONE project must combine an existing
    selected skill with a weaker/missing skill.

11. Keep the response concise.

------------------------------------------
STUDENT
------------------------------------------

Name:
{student_name}

Recommended Career:
{recommended_career}

------------------------------------------
CURRENT SELECTED SKILLS
------------------------------------------

{clean_skills}

------------------------------------------
STRONGEST SELECTED SKILLS
------------------------------------------

{strongest_text}

------------------------------------------
SKILLS ALREADY MEETING TARGET
------------------------------------------

{completed_text}

------------------------------------------
SKILL GAPS
------------------------------------------

{gaps_text}

------------------------------------------
RESPONSE FORMAT
------------------------------------------

Return ONLY valid JSON.

Use exactly this structure:

{{
    "why_career": "short explanation",

    "strongest_skills": [
        "Skill: score/100"
    ],

    "biggest_gaps": [
        "Skill: current/100 -> target/100 (gap X)"
    ],

    "what_to_learn_first": [
        "Priority 1",
        "Priority 2",
        "Priority 3"
    ],

    "projects": [
        {{
            "name": "Project name",
            "technology": "Technology",
            "description": "What to build",
            "skill": "Skill improved",
            "why": "Why it helps the career"
        }},
        {{
            "name": "Project name",
            "technology": "Technology",
            "description": "What to build",
            "skill": "Skill improved",
            "why": "Why it helps the career"
        }},
        {{
            "name": "Project name",
            "technology": "Technology",
            "description": "What to build",
            "skill": "Skill improved",
            "why": "Why it helps the career"
        }}
    ],

    "placement_action_plan": {{
        "learn": "practical learning action",
        "practice": "practical practice action",
        "build": "practical project action",
        "interview": "practical interview action"
    }}
}}

Do not add any other JSON fields.
"""


    # --------------------------------------
    # GEMINI NOT CONFIGURED
    # --------------------------------------

    if client is None:

        return {
            "why_career": (
                f"{recommended_career} connects with "
                "the skills you selected in your assessment."
            ),

            "strongest_skills": [
                f"{skill}: {score}/100"
                for skill, score in strongest_skills
            ],

            "biggest_gaps": [
                (
                    f'{item["skill"]}: '
                    f'{item["current"]}/100 -> '
                    f'{item["required"]}/100 '
                    f'(gap {item["gap"]})'
                )
                for item in improvement_skills
            ],

            "what_to_learn_first": [
                "Strengthen your biggest assessed skill gap.",
                "Practice the core concepts of your target career.",
                "Build one practical resume project.",
            ],

            "projects": [],

            "placement_action_plan": {
                "learn": (
                    "Study the fundamentals required "
                    "for your recommended career."
                ),
                "practice": (
                    "Practice coding and review your mistakes."
                ),
                "build": (
                    "Build practical projects using your "
                    "current and weaker skills."
                ),
                "interview": (
                    "Prepare technical and HR questions "
                    "and practice explaining your projects."
                ),
            },

            "career": recommended_career,
            "student_name": student_name,
        }


    # --------------------------------------
    # GENERATE RESPONSE
    # --------------------------------------

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        response_text = response.text.strip()


        # --------------------------------------
        # REMOVE MARKDOWN JSON FENCES
        # --------------------------------------

        if response_text.startswith("```"):

            response_text = (
                response_text
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )


        # --------------------------------------
        # PARSE JSON
        # --------------------------------------

        import json

        data = json.loads(
            response_text
        )


        # --------------------------------------
        # ENSURE REQUIRED FIELDS
        # --------------------------------------

        data.setdefault(
            "why_career",
            ""
        )

        data.setdefault(
            "strongest_skills",
            []
        )

        data.setdefault(
            "biggest_gaps",
            []
        )

        data.setdefault(
            "what_to_learn_first",
            []
        )

        data.setdefault(
            "projects",
            []
        )

        data.setdefault(
            "placement_action_plan",
            {}
        )


        # --------------------------------------
        # ENSURE EXACTLY THREE PROJECTS
        # --------------------------------------

        projects = data.get(
            "projects",
            []
        )

        if not isinstance(projects, list):
            projects = []

        data["projects"] = projects[:3]


        # --------------------------------------
        # PLACEMENT PLAN
        # --------------------------------------

        placement_plan = data.get(
            "placement_action_plan",
            {}
        )

        if not isinstance(
            placement_plan,
            dict
        ):
            placement_plan = {}

        placement_plan.setdefault(
            "learn",
            ""
        )

        placement_plan.setdefault(
            "practice",
            ""
        )

        placement_plan.setdefault(
            "build",
            ""
        )

        placement_plan.setdefault(
            "interview",
            ""
        )

        data["placement_action_plan"] = (
            placement_plan
        )


        # --------------------------------------
        # NEVER TRUST AI TO CHANGE CAREER
        # --------------------------------------

        data["career"] = recommended_career
        data["student_name"] = student_name


        return data


    # --------------------------------------
    # AI ERROR
    # --------------------------------------

    except Exception as e:

        print(
            "AI CAREER ADVISOR ERROR:",
            repr(e)
        )

        return {
            "why_career": (
                f"{recommended_career} is the career "
                "recommended by your assessment. "
                "Focus on strengthening the assessed "
                "skills and building practical projects "
                "for this career."
            ),

            "strongest_skills": [
                f"{skill}: {score}/100"
                for skill, score in strongest_skills
            ],

            "biggest_gaps": [
                (
                    f'{item["skill"]}: '
                    f'{item["current"]}/100 -> '
                    f'{item["required"]}/100 '
                    f'(gap {item["gap"]})'
                )
                for item in improvement_skills
            ],

            "what_to_learn_first": [
                "Strengthen your biggest skill gap.",
                "Practice the fundamentals of the recommended career.",
                "Build practical projects and prepare for interviews.",
            ],

            "projects": [],

            "placement_action_plan": {
                "learn": (
                    "Study the core concepts required "
                    "for the recommended career."
                ),
                "practice": (
                    "Practice coding regularly and "
                    "review mistakes."
                ),
                "build": (
                    "Build practical projects that "
                    "improve your weak areas."
                ),
                "interview": (
                    "Practice technical, project and "
                    "HR interview questions."
                ),
            },

            "career": recommended_career,
            "student_name": student_name,
        }

