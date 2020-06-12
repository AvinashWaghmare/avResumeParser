from django.shortcuts import render, redirect, get_object_or_404
from pyresparser import ResumeParser
from .models import Resume, UploadResumeModelForm
from django.contrib import messages
from django.conf import settings
from django.db import IntegrityError
from django.http import HttpResponse, FileResponse, Http404
from rest_framework.response import Response
import os
import json


def homepage(request):
    if request.method == 'POST':
        Resume.objects.all().delete()
        file_form = UploadResumeModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('resume')

        resumes_data = []

        if file_form.is_valid():
            for file in files:
                try:
                    # saving the file
                    resume = Resume(resume=file)
                    resume.save()

                    # extracting resume entities
                    parser = ResumeParser(os.path.join(settings.MEDIA_ROOT, resume.resume.name))
                    data = parser.get_extracted_data()
                    r_data = {
                        "name": data["name"],
                        "email": data["email"],
                        "mobile_number": data["mobile_number"],
                        "skills": data["skills"],
                        "college_name": data["college_name"],
                        "degree": data["degree"],
                        'designation': data["designation"],
                        "experience": data["experience"],
                        "company_names": data["company_names"],
                        'total_experience': data["total_experience"]
                    }
                    print(type(r_data))
                    print(r_data)
                    resumes_data.append(r_data)
                    resume.name = r_data.get("name")
                    resume.email = r_data.get("email")
                    resume.mobile_number = r_data.get("mobile_number")
                    if r_data.get("degree") is not None:
                        resume.education = ', '.join(r_data.get("degree"))
                    else:
                        resume.education = None
                    resume.company_names = r_data.get("company_names")
                    resume.college_name = r_data.get("college_name")
                    resume.designation = r_data.get("designation")
                    resume.total_experience = r_data.get("total_experience")
                    if r_data.get("skills") is not None:
                        resume.skills = ', '.join(r_data.get("skills"))
                    else:
                        resume.skills = None
                    if r_data.get("experience") is not None:
                        resume.experience = ','.join(r_data.get("experience"))
                    else:
                        resume.experience = None
                    resume.save()

                except IntegrityError:
                    messages.warning(request, "Duplicate resume found:", file.name)
                    return redirect("homepage")
            resumes = Resume.objects.all()
            messages.success(request, "Resumes uploaded!")
            context = {
                "resumes": resumes,
            }
            return render(request, "base.html", context)
    else:
        form = UploadResumeModelForm()
        context = {
            "form": form
        }
    return render(request, "base.html", context)
