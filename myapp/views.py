import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from myapp.models import Student, Company, Internship, Complaint, Application, Task, Report


def registrationGet(request):
    return render(request, 'registration.html')
def loginGet(request):
    return render(request,'login.html')
def login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    print(request.POST,"==========================")
    if not username or not password:
        messages.error(request,'Username or password is required')
        return redirect('/myapp/loginGet/')

    user = authenticate(request, username=username, password=password)
    if user is not None:
            if user.groups.filter(name='admin').exists():
                login(request, user)
                return redirect('/myapp/adminHome/')

            elif user.groups.filter(name='company').exists():
                login(request,user)
                cc=request.user
                mm=Company.objects.get(USER_id=cc)
                if mm.status == "approved":
                    return redirect('/myapp/companyHome/')
                else :
                    messages.error(request, 'Invalid User')
                    return redirect('/myapp/loginGet/')


            elif user.groups.filter(name='user').exists():
                print("ccccccccccccccccccccc")

                login(request, user)
                return redirect('/myapp/userHome/')
            else:
                messages.error(request,'Invalid user')
                return redirect('/myapp/loginGet/')


    else:
        messages.error(request,'Username or password is incorrect')
        return redirect('/myapp/loginGet/')




def adminHome(request):
    return render(request,'admins/index.html')

def landingPage(request):
    return render(request,'landingpage.html')

def adm_add_statistics(request):
    return render(request,'admins/add_statistics.html')

def adm_manage_company(request):
    return render(request, 'admins/manage_company.html')

def adm_manage_intern(request):
    return render(request, 'admins/manage_intern.html')

def adm_view_approved_company(request):
    data = Company.objects.filter(status='approved')
    return render(request,'admins/view_approved_company.html',{'data':data})


def adm_view_company(request):
    data=Company.objects.filter(status='pending')
    return render(request, 'admins/view_company.html',{'data':data})

def approve_company(request,id):
    Company.objects.filter(id=id).update(status='approved')
    return redirect('/myapp/adm_view_company/')

def reject_company(request,id):
    Company.objects.filter(id=id).update(status='rejected')
    return redirect('/myapp/adm_view_company/')

def adm_change_password(request):
    return render(request,'admins/adm_change_password.html')


def adm_view_internship(request):
    data=Internship.objects.filter(status='pending')
    return render(request, 'admins/view_internship.html',{'data':data})

def adm_approve_internship(request,id):
    Internship.objects.filter(id=id).update(status='approved')
    return redirect('/myapp/adm_view_internship/')

def adm_reject_internship(request,id):
    Internship.objects.filter(id=id).update(status='rejected')
    return redirect('/myapp/adm_view_internship/')


def adm_view_approved_internship(request):
    data = Internship.objects.filter(status='approved')
    return render(request,'admins/view_approved_internship.html',{'data':data})


def adm_view_rejected_company(request):
    data = Company.objects.filter(status='rejected')
    return render(request,'admins/view_rejected_company.html',{'data':data})

def adm_view_rejected_internship(request):
    data = Internship.objects.filter(status='rejected')
    return render(request,'admins/view_rejected_internship.html',{'data':data})


#=======Company====================================

def companyHome(request):
    return render (request,'company/cindex.html')

def c_add_certificate(request):
    return render(request,'company/add_certificate.html')

def c_add_internship(request):
    return render(request,'company/add_internship.html')

def c_add_internship_post(request):
    internship_id=request.POST['internshipId']
    title=request.POST['title']
    description=request.POST['description']
    status=request.POST['status']
    type=request.POST['type']
    cc = request.user

    i=Internship()
    i.name=internship_id
    i.title=title
    i.description=description
    i.i_status=status
    i.status='pending'
    i.type=type
    i.COMPANY=Company.objects.get(USER=cc)
    i.save()
    messages.success(request,'Adding internship is successful')
    return redirect('/myapp/c_add_internship/')


def c_view_internship(request):
    cc = request.user
    data=Internship.objects.filter(COMPANY__USER=cc)
    return render(request,'company/view_internship.html',{'data':data})



def c_view_internship_post(request):
    # internship_id = request.POST['internshipId']
    # company_name = request.POST['companyname']
    # title = request.POST['title']
    # approval_date = request.POST['approval date']
    # status = request.POST['status']
    return


def c_add_task(request,id):
    t=Task.objects.filter(INTERNSHIP__COMPANY__USER=request.user)
    data=Application.objects.get(id=id)
    from datetime import datetime
    date= datetime.now().today()
    return render(request,'company/add_task.html',{'data':data,'t':t,'date':date})



def c_delete_task(request,id):
    Task.objects.filter(id=id).delete()
    return redirect('/myapp/c_view_applicationGet/')


def c_add_task_post(request):
    aid=request.POST['aid']
    internshipId = request.POST['internshipId']
    title=request.POST['title']
    description=request.POST['description']
    assigned_date=request.POST['assigned_date']
    due_date=request.POST['due_date']
    cc=request.user

    t=Task()
    t.INTERNSHIP_id=internshipId
    t.title=title
    t.description=description

    t.assigned_date=assigned_date
    t.due_date=due_date
    t.APPLICATION_id=aid
    t.save()
    messages.success(request, 'Adding task is successful')
    return redirect('/myapp/c_view_applicationGet/')

def c_view_task(request,id):
    data=Task.objects.filter(INTERNSHIP_id=id)
    return render(request,'company/c_view_task.html',{'data':data})




def c_datesearch(request):
    return render(request,'company/datesearch.html')

def c_registration(request):
    return render(request,'company/registration.html')

def c_registration_post(request):
    name=request.POST['name']
    year=request.POST['year']
    icon = request.FILES['icon']
    email = request.POST['email']
    phone = request.POST['phone']
    place=request.POST['place']
    city = request.POST['city']
    pincode = request.POST['pincode']
    password = request.POST['password']
    confirm_password = request.POST['confirm password']
    license=request.POST['license']

    from datetime import datetime
    date = datetime.now().strftime("%y%m%d-%H%M%S") + ".jpg"
    fs = FileSystemStorage()
    fs.save(date,icon)
    path = fs.url(date)

    if User.objects.filter(username=email).exists():
        messages.error(request,'Email already exist')
        return redirect('/myapp/c_registration/')

    elif password==confirm_password:

        user=User.objects.create_user(username=email,password=confirm_password)
        user.groups.add(Group.objects.get(name="company"))
        user.save()


        c=Company()
        c.name = name
        c.year=year
        c.icon = path
        c.email =email
        c.phone_number = phone
        c.place =place
        c.city  = city
        c.pincode = pincode
        c.license =license
        c.USER=user
        c.save()
        messages.success(request,'Registered Successfully, please wait for the confirmation')
        return redirect('/myapp/loginGet/')
    else:
        messages.error(request,'Invalid credential')
        return redirect('/myapp/c_registration/')


def c_view_application(request):
    return render(request,'company/view_application.html')

def c_view_applicationGet(request):
    data=Application.objects.filter(INTERNSHIP__COMPANY__USER=request.user)
    return render(request,'company/view_application.html',{'data':data})

def c_approved_applicationGet(request,app_id):
    Application.objects.filter(id=app_id).update(status="approved")
    return redirect('/myapp/c_view_applicationGet/')


def c_rejected_applicationGet(request,app_id):
    Application.objects.filter(id=app_id).update(status="rejected")
    return redirect('/myapp/c_view_applicationGet/')





def c_view_daily_reports(request):
    data=Report.objects.all()
    return render(request,'company/view_daily_reports.html',{'data':data})

def c_view_complaints(request):
    data=Complaint.objects.all()
    return render(request,'company/view_complaints.html',{'data':data})

def c_sent_reply(request,id):
    return render(request,'company/c_sent_reply.html',{'id':id})
def c_sent_reply_post(request):
    id=request.POST['id']
    reply=request.POST['reply']
    Complaint.objects.filter(id=id).update(reply=reply)
    return redirect('/myapp/c_view_complaints/')

def c_view_user(request):
    data=Application.objects.filter(INTERNSHIP__COMPANY__USER=request.user)
    return render(request,'company/view_user.html',{'data':data})

def c_change_password(request):
    return render(request,'company/c_change_password.html')


#===========User===================

def u_ratingandreview(request):
    return render (request,'user/ratingandreview.html')
def u_registration(request):
    return render (request,'user/registration.html')


def registration_post(request):
    full_name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    email=request.POST['email']
    phone_number=request.POST['phone']
    place=request.POST['place']
    city=request.POST['city']
    pincode=request.POST['pincode']
    state=request.POST['state']
    photo=request.FILES['photo']
    from datetime import datetime
    date=datetime.now().strftime("%y%m%d-%H%M%S")+".jpg"
    fs=FileSystemStorage()
    fs.save(date,photo)
    path=fs.url(date)
    password=request.POST['password']
    confirm_password=request.POST['confirmPassword']
    if User.objects.filter(username=email).exists():
        messages.error(request,'Email already exists')
        return redirect('/myapp/registrationGet/')
    else:
        user=User.objects.create_user(username=email,password=confirm_password)
        user.groups.add(Group.objects.get(name='user'))
        user.save()

        uobj=Student()
        uobj.name=full_name
        uobj.date_of_birth=dob
        uobj.gender=gender
        uobj.date = date
        uobj.email = email
        uobj.phone_number = phone_number
        uobj.place = place
        uobj.city = city
        uobj.pincode = pincode
        uobj.state=state
        uobj.upload_photo = path
        uobj.USER=user
        uobj.save()
        return redirect('/myapp/loginGet/')



def u_sentcomplaints(request):
    return render(request, 'user/sentcomplaints.html')
def u_sentcomplaints_post(request):
    complaint=request.POST['complaint']
    c=Complaint()
    c.complaint=complaint
    c.reply="pending"
    c.date=datetime.datetime.now()
    c.STUDENT=Student.objects.get(USER=request.user)
    c.save()
    return redirect('/myapp/u_sentcomplaints/')

def u_view_complaints(request):
    data=Complaint.objects.filter(STUDENT=Student.objects.get(USER=request.user))
    return render(request, 'user/view_complaints.html',{'data':data})




def u_view_application_status(request):
    data=Application.objects.filter(STUDENT__USER=request.user)

    return render(request,'user/view_application_status.html',{'data':data})

def u_certificate(request):
    return render(request,'user/view_certificate.html')

def u_view_internship(request):
    data=Internship.objects.filter(status="approved")
    l=[]
    for i in data:
        if Application.objects.filter(INTERNSHIP_id=i.id,STUDENT__USER=request.user.id).exists():
            l.append({
                'id':i.id,
                'name':i.name,'cname':i.COMPANY.name,'title':i.title,'description':i.description,'i_status':i.i_status,'type':i.type,
                'rstatus':'yes'
            })
        else:
            l.append({
                'id': i.id,
                'name': i.name, 'cname': i.COMPANY.name, 'title': i.title, 'description': i.description,
                'i_status': i.i_status, 'type': i.type,
                'rstatus': 'no'
            })


    return render(request,'user/view_internship.html',{'data':l})

def u_apply(request,internship_id):
    a=Application()
    a.applied_date=datetime.datetime.now()
    a.status="pending"
    a.INTERNSHIP_id=internship_id
    a.STUDENT=Student.objects.get(USER=request.user)
    a.save()
    messages.success(request,'Applied Successfully')
    return  redirect('/myapp/u_view_internship/')


def u_view_task(request,id):
    data=Task.objects.filter(INTERNSHIP_id=id)
    request.session['i_id']=id
    return render(request,'user/view_task.html',{'data':data})

def u_edit_task(request,id):
    return render (request,'user/edit_task.html',{'id':id})

def u_edit_task_post(request):
    title=request.POST['title']
    content=request.POST['content']
    id=request.POST['id']

    r=Report()
    r.title=title
    r.content=content
    r.report_date=datetime.datetime.now()
    r.STUDENT=Student.objects.get(USER=request.user)
    r.TASK=Task.objects.get(id=id)
    r.save()
    return redirect(f"/myapp/u_view_task/{request.session['i_id']}")


def u_change_password(request):
    return render(request,'user/u_change_password.html')

def userHome(request):
    return render(request,'user/newindex.html')

