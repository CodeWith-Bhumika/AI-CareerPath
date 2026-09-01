from django.urls import path
from . import views


urlpatterns = [

    # ==========================================
    # PROFILE
    # ==========================================

    path(
        "",
        views.profile,
        name="profile"
    ),

    path(
        "profile/",
        views.profile,
        name="profile"
    ),


    # ==========================================
    # SUCCESS
    # ==========================================

    path(
        "success/",
        views.success,
        name="success"
    ),


    # ==========================================
    # DASHBOARD
    # ==========================================

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),


    # ==========================================
    # SKILL ASSESSMENT
    # ==========================================

    path(
        "assessment/",
        views.assessment,
        name="assessment"
    ),


    # ==========================================
    # JOB READINESS
    # ==========================================

    path(
        "job-readiness/<int:assessment_id>/",
        views.job_readiness,
        name="job_readiness"
    ),


    # ==========================================
    # INTERVIEW PREPARATION
    # ==========================================

    path(
        "interview-preparation/<int:assessment_id>/",
        views.interview_preparation,
        name="interview_preparation"
    ),


    # ==========================================
    # RESULT
    # ==========================================

    path(
        "result/<int:assessment_id>/",
        views.result,
        name="result"
    ),

]