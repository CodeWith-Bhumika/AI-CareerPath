from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from .forms import (
    StudentProfileForm,
    SkillAssessmentForm,
    JobReadinessForm,
    InterviewPreparationForm,
    SKILL_QUESTIONS,
    JOB_READINESS_QUESTIONS,
    INTERVIEW_QUESTIONS,
)

from .models import (
    StudentProfile,
    SkillAssessment,
    JobReadiness,
)

from .career_engine import (
    recommend_career,
    analyze_skill_gap,
)

from .roadmap import generate_roadmap
from .ai_advisor import generate_ai_advice


# ============================================================
# HELPER: SAFE NUMBER
# ============================================================

def safe_number(value, default=0):
    """
    Safely convert a value to float.
    """

    if value is None:
        return default

    try:
        return float(value)

    except (TypeError, ValueError):
        return default


# ============================================================
# HELPER: GET STUDENT SKILLS
# ============================================================

def get_student_skills(assessment):
    """
    Returns ONLY the skills selected by the student.
    """

    all_skills = {

        "python": (
            "Python",
            assessment.python,
        ),

        "java": (
            "Java",
            assessment.java,
        ),

        "sql": (
            "SQL",
            assessment.sql,
        ),

        "html_css": (
            "HTML & CSS",
            assessment.html_css,
        ),

        "dsa": (
            "DSA",
            assessment.dsa,
        ),
    }

    selected_string = (
        assessment.selected_skills or ""
    )

    selected_skills = []

    for skill in selected_string.split(","):

        skill = skill.strip().lower()

        if skill in all_skills:

            selected_skills.append(skill)

    selected_skills = list(
        dict.fromkeys(
            selected_skills
        )
    )

    skills = {}

    for skill in selected_skills:

        display_name, score = all_skills[skill]

        skills[display_name] = round(
            safe_number(score),
            2,
        )

    return skills


# ============================================================
# DISPLAY NAME -> ENGINE NAME
# ============================================================

def display_skill_to_engine_name(skill_name):

    mapping = {

        "Python": "python",

        "Java": "java",

        "SQL": "sql",

        "HTML & CSS": "html_css",

        "DSA": "dsa",
    }

    return mapping.get(
        skill_name,
        skill_name,
    )


# ============================================================
# ENGINE NAME -> DISPLAY NAME
# ============================================================

def engine_skill_to_display_name(skill_name):

    mapping = {

        "python": "Python",

        "java": "Java",

        "sql": "SQL",

        "html_css": "HTML & CSS",

        "dsa": "DSA",
    }

    return mapping.get(
        skill_name,
        skill_name,
    )


# ============================================================
# CAREER DATA
# ============================================================

def get_career_data(assessment):

    skills = get_student_skills(
        assessment
    )

    if not skills:

        return (
            {},
            "No Career Recommendation",
            {},
            {},
        )

    engine_skills = {}

    for display_name, score in skills.items():

        engine_name = (
            display_skill_to_engine_name(
                display_name
            )
        )

        engine_skills[engine_name] = (
            safe_number(score)
        )

    # --------------------------------------------------------
    # CAREER RECOMMENDATION
    # --------------------------------------------------------

    try:

        recommended_career, career_scores = (
            recommend_career(
                engine_skills
            )
        )

    except Exception as e:

        print(
            "CAREER ENGINE ERROR:",
            e,
        )

        recommended_career = (
            "No Career Recommendation"
        )

        career_scores = {}

    if not recommended_career:

        recommended_career = (
            "No Career Recommendation"
        )

    # --------------------------------------------------------
    # SKILL GAP
    # --------------------------------------------------------

    try:

        all_gaps = analyze_skill_gap(
            engine_skills,
            recommended_career,
        )

    except Exception as e:

        print(
            "SKILL GAP ERROR:",
            e,
        )

        all_gaps = {}

    skill_gaps = {}

    for engine_name, current_score in (
        engine_skills.items()
    ):

        display_name = (
            engine_skill_to_display_name(
                engine_name
            )
        )

        current = safe_number(
            current_score
        )

        data = {}

        if isinstance(all_gaps, dict):

            data = all_gaps.get(
                engine_name,
                {},
            )

            if not data:

                data = all_gaps.get(
                    display_name,
                    {},
                )

        if not isinstance(data, dict):

            data = {}

        required = data.get(
            "required"
        )

        if required is None:

            required = data.get(
                "target"
            )

        if (
            required is None
            or safe_number(required) <= 0
        ):

            required = 70

        required = safe_number(
            required,
            70,
        )

        gap = max(
            required - current,
            0,
        )

        if gap == 0:

            status = "Excellent"

        elif gap <= 10:

            status = "Good"

        elif gap <= 30:

            status = "Needs Improvement"

        else:

            status = "Major Gap"

        skill_gaps[display_name] = {

            "skill": display_name,

            "current": round(
                current,
                1,
            ),

            "required": round(
                required,
                1,
            ),

            "target": round(
                required,
                1,
            ),

            "gap": round(
                gap,
                1,
            ),

            "status": status,
        }

    return (
        skills,
        recommended_career,
        career_scores or {},
        skill_gaps,
    )


# ============================================================
# JOB READINESS COMPONENTS
# ============================================================

READINESS_COMPONENTS = [
    "coding_practice",
    "aptitude",
    "cs_fundamentals",
    "sql_dbms",
]


# ============================================================
# JOB READINESS: TOTAL QUIZ SCORE
# ============================================================

def calculate_quiz_score(
    form,
    recommended_career,
):

    questions = (
        JOB_READINESS_QUESTIONS.get(
            recommended_career,
            [],
        )
    )

    if not questions:

        return 0

    correct_answers = 0

    for index, question in enumerate(
        questions
    ):

        field_name = f"job_{index}"

        user_answer = (
            form.cleaned_data.get(
                field_name
            )
        )

        correct_answer = (
            question.get(
                "answer"
            )
        )

        if user_answer == correct_answer:

            correct_answers += 1

    score = (
        correct_answers
        / len(questions)
    ) * 100

    return round(
        score,
        2,
    )


# ============================================================
# JOB READINESS: COMPONENT SCORES
# ============================================================

def calculate_component_scores(
    form,
    recommended_career,
):

    questions = (
        JOB_READINESS_QUESTIONS.get(
            recommended_career,
            [],
        )
    )

    component_questions = {
        component: []
        for component in READINESS_COMPONENTS
    }

    for index, question in enumerate(
        questions
    ):

        component = question.get(
            "component"
        )

        if component in component_questions:

            component_questions[
                component
            ].append(
                (
                    index,
                    question,
                )
            )

    scores = {}

    for component in READINESS_COMPONENTS:

        questions_for_component = (
            component_questions.get(
                component,
                [],
            )
        )

        if not questions_for_component:

            scores[component] = 0.0

            continue

        correct = 0

        for index, question in (
            questions_for_component
        ):

            field_name = f"job_{index}"

            user_answer = (
                form.cleaned_data.get(
                    field_name
                )
            )

            correct_answer = (
                question.get(
                    "answer"
                )
            )

            if user_answer == correct_answer:

                correct += 1

        score = (
            correct
            / len(
                questions_for_component
            )
        ) * 100

        scores[component] = round(
            score,
            2,
        )

    return scores


# ============================================================
# FINAL JOB READINESS SCORE
# ONLY 4 COMPONENTS
# ============================================================

def calculate_final_readiness_score(
    component_scores,
):

    total = 0

    for component in READINESS_COMPONENTS:

        score = component_scores.get(
            component,
            0,
        )

        total += safe_number(
            score,
            0,
        )

    final_score = (
        total
        / len(READINESS_COMPONENTS)
    )

    return round(
        final_score,
        2,
    )


# ============================================================
# READINESS STATUS
# ============================================================

def get_readiness_status(score):

    score = safe_number(
        score
    )

    if score >= 80:

        return "Job Ready"

    elif score >= 60:

        return "Almost Ready"

    elif score >= 40:

        return "Developing"

    else:

        return "Beginner"


# ============================================================
# PROFILE
# ============================================================

def profile(request):

    if request.method == "POST":

        form = StudentProfileForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            student = form.save()

            request.session[
                "student_id"
            ] = student.id

            request.session.pop(
                "job_readiness_id",
                None,
            )

            request.session.pop(
                "interview_score",
                None,
            )

            return redirect(
                "assessment"
            )

    else:

        form = StudentProfileForm()

    return render(
        request,
        "profile.html",
        {
            "form": form,
        },
    )


# ============================================================
# SUCCESS
# ============================================================

def success(request):

    return redirect(
        "assessment"
    )


# ============================================================
# SKILL ASSESSMENT
# ============================================================

def assessment(request):

    student_id = (
        request.session.get(
            "student_id"
        )
    )

    if not student_id:

        return redirect(
            "profile"
        )

    student = get_object_or_404(
        StudentProfile,
        id=student_id,
    )

    selected_skills = []

    student_skills = (
        student.skills or ""
    )

    for skill in student_skills.split(","):

        skill = skill.strip().lower()

        if skill in SKILL_QUESTIONS:

            selected_skills.append(
                skill
            )

    selected_skills = list(
        dict.fromkeys(
            selected_skills
        )
    )

    if request.method == "POST":

        form = SkillAssessmentForm(
            request.POST,
            selected_skills=selected_skills,
        )

        if form.is_valid():

            assessment_obj = (
                SkillAssessment()
            )

            assessment_obj.student = (
                student
            )

            assessment_obj.selected_skills = (
                ",".join(
                    selected_skills
                )
            )

            skill_scores = {}

            for skill in selected_skills:

                questions = (
                    SKILL_QUESTIONS.get(
                        skill,
                        [],
                    )
                )

                total_questions = len(
                    questions
                )

                correct_answers = 0

                for index, question in enumerate(
                    questions
                ):

                    field_name = (
                        f"{skill}_{index}"
                    )

                    user_answer = (
                        form.cleaned_data.get(
                            field_name
                        )
                    )

                    correct_answer = (
                        question.get(
                            "answer"
                        )
                    )

                    if (
                        user_answer
                        == correct_answer
                    ):

                        correct_answers += 1

                if total_questions:

                    score = (
                        correct_answers
                        / total_questions
                    ) * 100

                else:

                    score = 0

                skill_scores[skill] = round(
                    score,
                    2,
                )

            assessment_obj.python = (
                skill_scores.get(
                    "python",
                    0,
                )
            )

            assessment_obj.java = (
                skill_scores.get(
                    "java",
                    0,
                )
            )

            assessment_obj.sql = (
                skill_scores.get(
                    "sql",
                    0,
                )
            )

            assessment_obj.html_css = (
                skill_scores.get(
                    "html_css",
                    0,
                )
            )

            assessment_obj.dsa = (
                skill_scores.get(
                    "dsa",
                    0,
                )
            )

            assessment_obj.save()

            request.session.pop(
                "job_readiness_id",
                None,
            )

            request.session.pop(
                "interview_score",
                None,
            )

            return redirect(
                "result",
                assessment_id=assessment_obj.id,
            )

    else:

        form = SkillAssessmentForm(
            selected_skills=selected_skills
        )

    return render(
        request,
        "assessment.html",
        {
            "form": form,
            "student": student,
            "selected_skills": selected_skills,
        },
    )


# ============================================================
# JOB READINESS
# ============================================================

def job_readiness(
    request,
    assessment_id,
):

    student_id = (
        request.session.get(
            "student_id"
        )
    )

    if not student_id:

        return redirect(
            "profile"
        )

    student = get_object_or_404(
        StudentProfile,
        id=student_id,
    )

    assessment = get_object_or_404(
        SkillAssessment,
        id=assessment_id,
        student=student,
    )

    (
        skills,
        recommended_career,
        career_scores,
        skill_gaps,
    ) = get_career_data(
        assessment
    )

    if request.method == "POST":

        form = JobReadinessForm(
            request.POST,
            recommended_career=(
                recommended_career
            ),
        )

        if form.is_valid():

            component_scores = (
                calculate_component_scores(
                    form,
                    recommended_career,
                )
            )

            final_readiness_score = (
                calculate_final_readiness_score(
                    component_scores
                )
            )

            readiness_status = (
                get_readiness_status(
                    final_readiness_score
                )
            )

            # Delete previous readiness record.
            JobReadiness.objects.filter(
                student=student
            ).delete()

            readiness = JobReadiness(

                student=student,

                readiness_score=(
                    final_readiness_score
                ),

                readiness_status=(
                    readiness_status
                ),

                coding_practice=(
                    component_scores.get(
                        "coding_practice",
                        0,
                    )
                ),

                aptitude=(
                    component_scores.get(
                        "aptitude",
                        0,
                    )
                ),

                cs_fundamentals=(
                    component_scores.get(
                        "cs_fundamentals",
                        0,
                    )
                ),

                sql_dbms=(
                    component_scores.get(
                        "sql_dbms",
                        0,
                    )
                ),

                projects=None,

                resume=None,

                github_portfolio=None,

                interview_preparation=None,
            )

            readiness.save()

            request.session[
                "job_readiness_id"
            ] = readiness.id

            # A new Job Readiness attempt means
            # the old interview score should be cleared.
            request.session.pop(
                "interview_score",
                None,
            )

            return redirect(
                "result",
                assessment_id=assessment.id,
            )

    else:

        form = JobReadinessForm(
            recommended_career=(
                recommended_career
            )
        )

    return render(
        request,
        "job_readiness.html",
        {
            "form": form,
            "student": student,
            "assessment": assessment,
            "recommended_career": recommended_career,
            "career_scores": career_scores,
            "skill_gaps": skill_gaps,
        },
    )


# ============================================================
# INTERVIEW PREPARATION
# ============================================================

def interview_preparation(
    request,
    assessment_id,
):

    student_id = (
        request.session.get(
            "student_id"
        )
    )

    if not student_id:

        return redirect(
            "profile"
        )

    student = get_object_or_404(
        StudentProfile,
        id=student_id,
    )

    assessment = get_object_or_404(
        SkillAssessment,
        id=assessment_id,
        student=student,
    )

    (
        skills,
        recommended_career,
        career_scores,
        skill_gaps,
    ) = get_career_data(
        assessment
    )

    if request.method == "POST":

        form = InterviewPreparationForm(
            request.POST,
            recommended_career=(
                recommended_career
            ),
        )

        if form.is_valid():

            questions = (
                INTERVIEW_QUESTIONS.get(
                    recommended_career,
                    [],
                )
            )

            correct_answers = 0

            for index, question in enumerate(
                questions
            ):

                field_name = (
                    f"interview_{index}"
                )

                user_answer = (
                    form.cleaned_data.get(
                        field_name
                    )
                )

                correct_answer = (
                    question.get(
                        "answer"
                    )
                )

                if user_answer == correct_answer:

                    correct_answers += 1

            if questions:

                interview_score = (
                    correct_answers
                    / len(questions)
                ) * 100

            else:

                interview_score = 0

            interview_score = round(
                interview_score,
                2,
            )

            # ------------------------------------------------
            # SAVE SESSION
            # ------------------------------------------------

            request.session[
                "interview_score"
            ] = interview_score

            request.session.modified = True

            # ------------------------------------------------
            # SAVE DATABASE
            # ------------------------------------------------

            readiness_id = (
                request.session.get(
                    "job_readiness_id"
                )
            )

            if readiness_id:

                readiness = (
                    JobReadiness.objects
                    .filter(
                        id=readiness_id,
                        student=student,
                    )
                    .first()
                )

                if readiness:

                    readiness.interview_preparation = (
                        interview_score
                    )

                    readiness.save(
                        update_fields=[
                            "interview_preparation"
                        ]
                    )

            return redirect(
                "result",
                assessment_id=assessment.id,
            )

    else:

        form = InterviewPreparationForm(
            recommended_career=(
                recommended_career
            )
        )

    return render(
        request,
        "interview_preparation.html",
        {
            "form": form,
            "student": student,
            "assessment": assessment,
            "recommended_career": recommended_career,
            "career_scores": career_scores,
            "skill_gaps": skill_gaps,
        },
    )


# ============================================================
# DASHBOARD
# ============================================================

def dashboard(request):

    student_id = (
        request.session.get(
            "student_id"
        )
    )

    if not student_id:

        return redirect(
            "profile"
        )

    student = get_object_or_404(
        StudentProfile,
        id=student_id,
    )

    # Get latest skill assessment.
    assessment = (
        SkillAssessment.objects
        .filter(
            student=student
        )
        .order_by("-created_at", "-id")
        .first()
    )

    if not assessment:

        return redirect(
            "profile"
        )

    (
        skills,
        recommended_career,
        career_scores,
        skill_gaps,
    ) = get_career_data(
        assessment
    )

    # --------------------------------------------------------
    # TECHNICAL SCORE
    # --------------------------------------------------------

    if skills:

        percentage = (
            sum(
                safe_number(score)
                for score in skills.values()
            )
            / len(skills)
        )

    else:

        percentage = 0

    percentage = round(
        percentage,
        2,
    )

    # --------------------------------------------------------
    # STRONGEST SKILL
    # --------------------------------------------------------

    if skills:

        strongest_skill = max(
            skills,
            key=lambda skill:
                safe_number(
                    skills[skill]
                ),
        )

    else:

        strongest_skill = "None"

    # --------------------------------------------------------
    # ROADMAP
    # --------------------------------------------------------

    try:

        roadmap = generate_roadmap(
            skill_gaps
        )

    except Exception as e:

        print(
            "DASHBOARD ROADMAP ERROR:",
            e,
        )

        roadmap = []

    # --------------------------------------------------------
    # JOB READINESS
    # --------------------------------------------------------

    readiness_obj = (
        JobReadiness.objects
        .filter(
            student=student
        )
        .order_by("-created_at", "-id")
        .first()
    )

    if readiness_obj:

        readiness_score = safe_number(
            readiness_obj.readiness_score
        )

        job_readiness_data = {

            "score": round(
                readiness_score,
                2,
            ),

            "status": (
                readiness_obj.readiness_status
                or get_readiness_status(
                    readiness_score
                )
            ),

            "components": {

                "coding_practice": safe_number(
                    readiness_obj.coding_practice,
                    0,
                ),

                "aptitude": safe_number(
                    readiness_obj.aptitude,
                    0,
                ),

                "cs_fundamentals": safe_number(
                    readiness_obj.cs_fundamentals,
                    0,
                ),

                "sql_dbms": safe_number(
                    readiness_obj.sql_dbms,
                    0,
                ),
            },
        }

        interview_score = (
            readiness_obj.interview_preparation
        )

    else:

        job_readiness_data = {

            "score": 0,

            "status": "Not Assessed",

            "components": {

                "coding_practice": None,

                "aptitude": None,

                "cs_fundamentals": None,

                "sql_dbms": None,
            },
        }

        interview_score = None

    # --------------------------------------------------------
    # SESSION FALLBACK FOR INTERVIEW
    # --------------------------------------------------------

    if interview_score is None:

        interview_score = (
            request.session.get(
                "interview_score"
            )
        )

    if interview_score is not None:

        interview_score = round(
            safe_number(
                interview_score,
                0,
            ),
            2,
        )

    # --------------------------------------------------------
    # AI ADVISOR
    # --------------------------------------------------------

    try:

        ai_advice = generate_ai_advice(
            student.name,
            skills,
            recommended_career,
            skill_gaps,
        )

    except Exception as e:

        print(
            "DASHBOARD AI ADVISOR ERROR:",
            e,
        )

        ai_advice = {

            "career":
                recommended_career,

            "why_career":
                f"{recommended_career} is recommended based on your current assessed skills.",

            "strongest_skills": [
                f"{skill}: {score}/100"
                for skill, score in skills.items()
            ],

            "biggest_gaps": [
                (
                    f"{skill}: "
                    f"{data.get('current', 0)}/100 "
                    f"-> "
                    f"{data.get('required', 0)}/100 "
                    f"(gap {data.get('gap', 0)})"
                )
                for skill, data
                in skill_gaps.items()
            ],

            "what_to_learn_first": [
                "Strengthen your skill gaps.",
                "Practice coding regularly.",
                "Build practical projects.",
                "Prepare for interviews.",
            ],

            "projects": [],

            "placement_action_plan": {

                "learn":
                    "Focus on your highest-priority skill gaps.",

                "practice":
                    "Practice coding and technical questions regularly.",

                "build":
                    "Build practical projects related to your target career.",

                "interview":
                    "Prepare technical and HR interview questions.",
            },
        }

    return render(
        request,
        "dashboard.html",
        {

            "student":
                student,

            "assessment":
                assessment,

            "skills":
                skills,

            "percentage":
                percentage,

            "strongest_skill":
                strongest_skill,

            "recommended_career":
                recommended_career,

            "career_scores":
                career_scores,

            "skill_gaps":
                skill_gaps,

            "roadmap":
                roadmap,

            "job_readiness":
                job_readiness_data,

            "interview_score":
                interview_score,

            "ai_advice":
                ai_advice,

        },
    )


# ============================================================
# RESULT
# ============================================================

def result(
    request,
    assessment_id,
):

    student_id = (
        request.session.get(
            "student_id"
        )
    )

    if not student_id:

        return redirect(
            "profile"
        )

    assessment = get_object_or_404(
        SkillAssessment,
        id=assessment_id,
        student_id=student_id,
    )

    (
        skills,
        recommended_career,
        career_scores,
        skill_gaps,
    ) = get_career_data(
        assessment
    )

    # ========================================================
    # OVERALL TECHNICAL SCORE
    # ========================================================

    if skills:

        percentage = (
            sum(
                safe_number(score)
                for score in skills.values()
            )
            / len(skills)
        )

    else:

        percentage = 0

    percentage = round(
        percentage,
        2,
    )

    # ========================================================
    # STRONGEST / WEAKEST SKILL
    # ========================================================

    if skills:

        strongest_skill = max(
            skills,
            key=lambda skill:
                safe_number(
                    skills[skill]
                ),
        )

        weakest_skill = min(
            skills,
            key=lambda skill:
                safe_number(
                    skills[skill]
                ),
        )

    else:

        strongest_skill = "None"

        weakest_skill = "None"

    # ========================================================
    # ROADMAP
    # ========================================================

    try:

        roadmap = generate_roadmap(
            skill_gaps
        )

    except Exception as e:

        print(
            "ROADMAP ERROR:",
            e,
        )

        roadmap = []

    # ========================================================
    # JOB READINESS
    # ========================================================

    readiness_id = (
        request.session.get(
            "job_readiness_id"
        )
    )

    readiness_obj = None

    if readiness_id:

        readiness_obj = (
            JobReadiness.objects
            .filter(
                id=readiness_id,
                student=assessment.student,
            )
            .first()
        )

    # Fallback to latest readiness record
    if not readiness_obj:

        readiness_obj = (
            JobReadiness.objects
            .filter(
                student=assessment.student
            )
            .order_by("-created_at", "-id")
            .first()
        )

    # ========================================================
    # JOB READINESS DATA
    # ========================================================

    if readiness_obj:

        readiness_score = safe_number(
            readiness_obj.readiness_score
        )

        job_readiness_data = {

            "id":
                readiness_obj.id,

            "score":
                round(
                    readiness_score,
                    2,
                ),

            "status": (
                readiness_obj.readiness_status
                or get_readiness_status(
                    readiness_score
                )
            ),

            "components": {

                "coding_practice":
                    readiness_obj.coding_practice,

                "aptitude":
                    readiness_obj.aptitude,

                "cs_fundamentals":
                    readiness_obj.cs_fundamentals,

                "sql_dbms":
                    readiness_obj.sql_dbms,
            },
        }

    else:

        job_readiness_data = {

            "id":
                None,

            "score":
                0,

            "status":
                "Not Assessed",

            "components": {

                "coding_practice":
                    None,

                "aptitude":
                    None,

                "cs_fundamentals":
                    None,

                "sql_dbms":
                    None,
            },
        }

    # ========================================================
    # INTERVIEW PREPARATION SCORE
    # ========================================================

    interview_score = None

    # DATABASE FIRST
    if readiness_obj:

        if (
            readiness_obj.interview_preparation
            is not None
        ):

            interview_score = safe_number(
                readiness_obj.interview_preparation,
                0,
            )

    # SESSION FALLBACK
    if interview_score is None:

        interview_score = (
            request.session.get(
                "interview_score"
            )
        )

    if interview_score is not None:

        interview_score = round(
            safe_number(
                interview_score,
                0,
            ),
            2,
        )

    # ========================================================
    # AI CAREER ADVISOR
    # ========================================================

    try:

        ai_advice = generate_ai_advice(
            assessment.student.name,
            skills,
            recommended_career,
            skill_gaps,
        )

    except Exception as e:

        print(
            "AI ADVISOR ERROR:",
            e,
        )

        ai_advice = {

            "career":
                recommended_career,

            "why_career": (
                f"{recommended_career} is "
                f"recommended based on your "
                f"current assessed skills."
            ),

            "strongest_skills": [

                f"{skill}: {score}/100"

                for skill, score
                in skills.items()
            ],

            "biggest_gaps": [

                (
                    f"{skill}: "
                    f"{data.get('current', 0)}/100 "
                    f"-> "
                    f"{data.get('required', 0)}/100 "
                    f"(gap {data.get('gap', 0)})"
                )

                for skill, data
                in skill_gaps.items()
            ],

            "what_to_learn_first": [

                "Strengthen your current technical skills.",

                "Practice coding and problem solving.",

                "Build practical projects.",

                "Prepare for technical interviews.",
            ],

            "projects": [],

            "placement_action_plan": {

                "learn":
                    "Focus on the fundamental technical skills required for your target career.",

                "practice":
                    "Practice coding and problem solving regularly.",

                "build":
                    "Complete practical projects and add them to your portfolio.",

                "interview":
                    "Prepare technical interview questions.",
            },
        }

    # ========================================================
    # RESULT PAGE
    # ========================================================

    return render(
        request,
        "result.html",
        {

            "assessment":
                assessment,

            "assessment_id":
                assessment.id,

            "student":
                assessment.student,

            "skills":
                skills,

            "percentage":
                percentage,

            "strongest_skill":
                strongest_skill,

            "weakest_skill":
                weakest_skill,

            "recommended_career":
                recommended_career,

            "career_scores":
                career_scores,

            "skill_gaps":
                skill_gaps,

            "roadmap":
                roadmap,

            "job_readiness":
                job_readiness_data,

            "interview_score":
                interview_score,

            "job_readiness_assessment_id":
                assessment.id,

            "ai_advice":
                ai_advice,
        },
    )