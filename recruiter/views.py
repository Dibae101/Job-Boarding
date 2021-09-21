from django.core import paginator
from accounts.models import Account
from designer.models import ProjectDescriptionModel, ProjectTagsModel, DesignerRegister
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import RecruiterRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from .models import RecruiterRegister
from django.contrib import messages
from designer.models import DesignerEducation, DesignerExperience, DesignerRegister
from accounts.models import Account
from django.core.paginator import Paginator
from designer.models import DesignerRegister

# signup

def recruiter_check(request):
    return request.is_recruiter

@login_required(login_url='login')
@user_passes_test(recruiter_check, login_url='login')
def register(request):
    if request.method == 'POST':
        form = RecruiterRegisterForm(request.POST, request.FILES)
        print("form:", form)
        if form.is_valid():
            form.instance.user = request.user
            request.user.is_profile_completed = True
            request.user.save()
            # form.instance.is_profile_completed = True
            try:
                recruiter_reg_instance = RecruiterRegister.objects.get(user=request.user)
                recruiter_reg_instance.delete()
            except:
                pass
            form.instance.is_profile_completed = True
            form.save()
            messages.success(request, "Recruiter profile sucessfully created")
            return redirect('dashboard')
        else:
            return render(request, 'register.html', {"form":form})
    else:
        form = RecruiterRegisterForm()
    
    context = {
        "form": form
    }
    return render(request, 'register.html', context)

# recruiter_dashboard
@login_required(login_url='login')
@user_passes_test(recruiter_check, login_url='login')
def dashboard(request):
    project_description = ProjectDescriptionModel.objects.all()
    designer_register =  DesignerRegister.objects.all()
    project_tags = ProjectTagsModel.objects.all()
    paginator = Paginator(designer_register,3)
    page = request.GET.get('page')
    designer_register=paginator.get_page(page)
    context = {
        'project_description': project_description,
        'project_tags': project_tags,
        'designer_register': designer_register,
    }
    return render(request, 'dashboard.html', context)

# recruiter profile
@login_required(login_url='login')
@user_passes_test(recruiter_check, login_url='login')
def recruiter_profile(request):
    rec_profile = RecruiterRegister.objects.filter(user=request.user)
    context = {
        'rec_profile': rec_profile,
    }
    return render(request, 'recruiter-profile.html', context)

#designer_profile view
@login_required(login_url='login')
# @user_passes_test(recruiter_check, login_url='login')
def designer_profile(request, user_id):
    designer = Account.objects.get(pk=user_id)
    projects = ProjectDescriptionModel.objects.filter(user=designer)
    experiences = DesignerExperience.objects.filter(user=designer)
    educations = DesignerEducation.objects.filter(user=designer)
    designer_details = DesignerRegister.objects.get(user=designer)
    top_skills = designer_details.top_skills.split(",")
    user_experiences = designer_details.experience.split(",")
    tools_of_choice = designer_details.tools_of_choice.split(",")
    projects = ProjectDescriptionModel.objects.filter(user=designer)

    context={
        "designer":designer,
        "projects":projects,
        "experiences":experiences,
        "educations":educations,
        "top_skills":top_skills,
        "user_experiences":user_experiences,
        "tools_of_choice":tools_of_choice,
        "projects":projects,
    }
    return render(request, 'designer-profile.html', context)

# service_plan
def services(request):
    if request.method == "POST":
        message_name = request.POST["message-name"]
        message_email = request.POST["message-email"]
        message = request.POST["message"]
        # send email
        send_mail(
            message_name,
            message,
            message_email,
            ["devdjango101@gmail.com"],
            fail_silently=False,
        )
        return render(request, "services.html", {"message_name": message_name})
    else:
        return render(request, "services.html")
    







