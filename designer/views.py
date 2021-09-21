from django.http.response import HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import DesignerEducationForm, DesignerExperienceForm, DesignerRegisterForm, ProjectDescriptionForm, ProjectTagsForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import DesignerEducation, DesignerExperience, DesignerRegister, ProjectDescriptionModel

# Create your views here.

def designer_check(request):
    return request.is_designer


@login_required(login_url='login')
@user_passes_test(designer_check, login_url='login')
def register(request):
    if request.method == 'POST':
        form = DesignerRegisterForm(request.POST, request.FILES)
        print("form:", form)
        if form.is_valid():
            form.instance.user = request.user
            request.user.is_profile_completed = True
            request.user.save()
            # form.instance.is_profile_completed = True
            try:
                designer_reg_instance = DesignerRegister.objects.get(user=request.user)
                designer_reg_instance.delete()
            except:
                pass
            form.instance.is_profile_completed = True
            form.save()
            messages.success(request, "Designer information sucessfully added")
            return redirect('designer-profile')
        else:
            return render(request, 'designer/register.html', {"form":form})
    else:
        form = DesignerRegisterForm()
    
    context = {
        "form": form
    }
    return render(request, 'designer/register.html', context)




@login_required(login_url='login')
@user_passes_test(designer_check, login_url='login')
def project_description(request):
    
    if request.method == 'POST':
        form = ProjectDescriptionForm(request.POST)
        
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            print(form.instance.project_link)
            # messages.success(request, "Project description successfully added.")
            
            project_id = ProjectDescriptionModel.objects.get(user = request.user, project_link=form.instance.project_link).id
       
            return redirect('project-tags', project_id=project_id)
            

        else:
            return render(request, 'designer/project-description.html', {"form":form})
    else:
        form = ProjectDescriptionForm()
    
    context = {
        "form": form
    }
    return render(request, 'designer/project-description.html', context=context)


@login_required(login_url='login')

def project_detail(request, project_id):
    project = ProjectDescriptionModel.objects.get( pk=project_id)
    context={
        "project":project,
    }
    return render(request, 'designer/project_detail.html', context)


@login_required(login_url='login')
@user_passes_test(designer_check, login_url='login')
def project_update(request, project_id):
    user = request.user
    project = ProjectDescriptionModel.objects.get(user=user, pk=project_id)
    
    form = ProjectDescriptionForm(None, instance=project)
    if request.method == 'POST':
        if form.is_valid():
            project_desc_instance = ProjectDescriptionModel(user=user, pk=project_id)
            project_desc_instance.delete()
            form.save() 
            messages.success(request, "Project Details Updated.")
            return redirect('project-tags', project_id=project_id)

    return render(request, 'designer/project-description.html', {"form":form})



@login_required(login_url='login')
@user_passes_test(designer_check, login_url='login')
def project_delete(request, project_id):
    user = request.user
    project = ProjectDescriptionModel.objects.get(user=user, pk=project_id)
    if request.method == 'POST':
        project.delete()
        messages.success(request,str( project.project_name+ " Project Deleted"))
        return redirect('designer-profile')

    return render(request, 'designer/delete-project.html', {'project': project})

@login_required(login_url='login')
@user_passes_test(designer_check, login_url='login')
def project_tags(request, project_id):
    project_name = ProjectDescriptionModel.objects.get(user=request.user, pk=project_id)
    project_id = project_id
    if request.method == 'POST':
        
        
        form = ProjectTagsForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            
            # project_name = ProjectDescriptionModel.objects.get(user=request.user, pk=project_id).project_name
            form.instance.project_name = project_name
            form.save()
            messages.success(request, "Project tags Sucessfully added")
            return redirect('home')
        else:
            return render(request, 'project-tags.html', {"form":form})
    else:
        form = ProjectTagsForm()
    
    context = {
        "form": form,
        # "project_name": project_name,
        "project_id": project_id,
    }
    return render(request, 'designer/project-tags.html', context=context)

@login_required(login_url='login')
@user_passes_test(designer_check, login_url='login')
def my_profile(request):
    projects = ProjectDescriptionModel.objects.filter(user=request.user)
    experiences = DesignerExperience.objects.filter(user=request.user)
    educations = DesignerEducation.objects.filter(user=request.user)
    designer_details = DesignerRegister.objects.get(user=request.user)
    top_skills = designer_details.top_skills.split(",")
    user_experiences = designer_details.experience.split(",")
    tools_of_choice = designer_details.tools_of_choice.split(",")
    projects = ProjectDescriptionModel.objects.filter(user=request.user)

    context={
        "projects":projects,
        "experiences":experiences,
        "educations":educations,
        "top_skills":top_skills,
        "user_experiences":user_experiences,
        "tools_of_choice":tools_of_choice,
        "projects":projects,
    }
    return render(request, 'designer/designer-profile.html', context)


@login_required(login_url='login')
@user_passes_test(designer_check, login_url='login')
def profile_update(request):
    profile = request.user.designerregister
    form = DesignerRegisterForm(request.POST or None, instance=profile)
    if form.is_valid():
        designer_reg_instance = DesignerRegister.objects.get(user=request.user)
        designer_reg_instance.delete()
        form.save()
        return redirect('home')
    return render(request, 'designer/register.html', {"form":form})




@login_required(login_url='login')
@user_passes_test(designer_check, login_url='login')
def designer_experience(request):
    
    if request.method == 'POST':
        form = DesignerExperienceForm(request.POST)
        
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            print("saved sucessfully")
            messages.success(request, "Your experience was successfully added.")
            return redirect('home')
        
        else:
            return render(request, 'designer/designer-experience.html', {"form":form})
    else:
        form = DesignerExperienceForm()
    
    context = {
        "form": form
    }
    return render(request, 'designer/designer-experience.html', context=context)

@login_required(login_url='login')
@user_passes_test(designer_check, login_url='login')
def experience_update(request, experience_id):
    user = request.user
    experience = DesignerExperience.objects.get(user=user, pk=experience_id)
    form = DesignerExperienceForm(None, instance=experience)
    if request.method == 'POST':
        if form.is_valid():
            experience_desc_instance = ProjectDescriptionModel(user=user, pk=experience_id)
            experience_desc_instance.delete()
            form.save() 
            messages.success(request, "Your experience has been Updated.")
            return redirect('designer-profile')

    return render(request, 'designer/designer-experience.html', {"form":form})

@login_required(login_url='login')
@user_passes_test(designer_check, login_url='login')
def experience_delete(request, experience_id):
    user = request.user
    experience = DesignerExperience.objects.get(user=user, pk=experience_id)
    if request.method == 'POST':
        experience.delete()
        messages.success(request,str( experience.work_title+ " Deleted"))
        return redirect('designer-profile')

    return render(request, 'designer/delete-experience.html', {'experience': experience})




@login_required(login_url='login')
@user_passes_test(designer_check, login_url='login')
def designer_education(request):
    
    if request.method == 'POST':
        form = DesignerEducationForm(request.POST)
        
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            print("saved sucessfully")
            messages.success(request, "Your experience was successfully added.")
            return redirect('home')
        
        else:
            return render(request, 'designer/designer-experience.html', {"form":form})
    else:
        form = DesignerEducationForm()
    
    context = {
        "form": form
    }
    return render(request, 'designer/designer-education.html', context=context)


@login_required(login_url='login')
@user_passes_test(designer_check,login_url='login')
def education_update(request, education_id):
    education = DesignerEducation.objects.get(user=request.user, pk=education_id)
    form = DesignerEducationForm(request.POST or None, instance=education)
    if request.method == 'POST':
        if form.is_valid():
            education_instance= DesignerEducation.objects.get(user=request.user, pk=education_id)
            education_instance.delete()
            form.save()
            return redirect('designer-profile')
    context= {
        "form":form,
    }
        
    return render(request, 'designer/designer-education.html', context)

@login_required(login_url='login')
@user_passes_test(designer_check, login_url='login')
def education_delete(request, education_id):
    education = DesignerEducation.objects.get(user=request.user, pk=education_id)
    if request.method == 'POST':
        education.delete()
        messages.success(request, f'Education details of {education.title} successfully deleted.')
        return redirect('designer-profile')
    context={
        "education":education,
    }
    return render(request, 'designer/delete-education.html', context)


def temp(request):
    return render(request,'designer/temp.html')