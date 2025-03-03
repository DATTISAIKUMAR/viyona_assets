
from controllers.util import *

router = APIRouter()


def data_In_dict(data):
    data_dict={}
    mongoData=data.objects(status=1)
    for i in mongoData:
        
        data_dict["email"]=i.email
        data_dict["password"]=i.password
    return data_dict

def pagination_data(request):
    users=Logfiles_data.objects.order_by("-id")
    page = 1
    per_page = 10
    start = (page - 1) * per_page
    end = start + per_page
    total_pages = ceil(len(users) / per_page)
    paginated_data = users[start:end]
    content= {
        "start":start,
        "total_pages": total_pages,
        "request":request,
        'data':paginated_data
    }
    return templates.TemplateResponse('loginfiles.html',content)


@router.get('/login',response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})


@router.get('/signup',response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse('signup.html', {'request': request})


@router.post('/login1',response_class=HTMLResponse)
async def login_page(request:Request):
    try:
        form_data=await request.form()
        email=form_data.get('email')
        password=form_data.get('password')
        date=datetime.now()
        data=Signup.objects(email=email,password=password).first()
    
        if not data or ('@' not in email[2:-5] and '.' not in email[-5::]):
            message="Invalid Password or Email..."
            return templates.TemplateResponse('login.html',{'request':request,'message':message})
        Logfiles_data(loginid=data.id,createdOn=date,status=1).save() 
        print("++++++++++++++++++++",data.id)  
        name_empty=Managedata.objects(name='')
        if name_empty:
            name_empty.update(laptopStatus="Unassigned")
        total_systems=Managedata.objects()
        desktop_total=Desktopdata.objects()
        other_systems=other_systemsdata.objects()
    
        content = {
            'request': request,
            'total_systems': len(total_systems),
            'desktop_total':len(desktop_total),
            'other_systems':len(other_systems)
        }
        return templates.TemplateResponse('asserts.html',content)
    except Exception as e:
        message="exception has occured.."
        return templates.TemplateResponse('asserts.html', {'request': request, 'message': message})

@router.post('/signup',response_class=HTMLResponse)
async def admin_signup(request: Request):
    try:
        form_data = await request.form()
        name = form_data.get('name')
        email = form_data.get('email')
        password = form_data.get('password')
        password1 = form_data.get('password1')
        role = form_data.get('role')
        reason=form_data.get('reason')
        createdOn= datetime.now()
        required_fields=[name,email,password,password1,role,reason]
        if password != password1:
            message = "Passwords do not match!"
            return templates.TemplateResponse('logfile.html', {'request': request, 'message': message})
        if('@' not in email[2:-5] and '.' not in email[-5::]):
            message='Invalid email.....'
            return templates.TemplateResponse('logfile.html', {'request': request, 'message': message})
        data=Signup.objects(email=email, password=password,status=1).first()
        if(data):
            message="user already exits.."
            return templates.TemplateResponse('logfile.html', {'request': request, 'message': message})
        if(all(required_fields)):
            Signup(name=name, email=email, password=password, role=role,reason=reason,createdOn=createdOn,status=1).save()
        else:
            message="Please enter valid fields.."
            return templates.TemplateResponse('logfile.html', {'request': request, 'message': message})

        return RedirectResponse('/logfile1', status_code=303)
    except Exception as e:
        message="exception has occured.."
        return templates.TemplateResponse('logfile.html', {'request': request, 'message': message})
    
@router.get('/logfile1')
async def adminfiles(request:Request):
    admins=Signup.objects(status=1)
    return templates.TemplateResponse('logfile.html',{'request':request,"data":admins})




@router.post('/logfile')
async def admin_data_file(request:Request):
    try:
        form_data=await request.form()
        email=form_data.get('email')
        password=form_data.get('password')
        data=Super_admin.objects(email=email,password=password,status=1).first()
        if not data:
            return templates.TemplateResponse('super_admin.html',{'request':request,'message':"Invalid details..."})
        
        admins=Signup.objects(status=1)
        return templates.TemplateResponse('logfile.html',{'request':request,'data':admins})
    except Exception as e:
        message="exception occure.."
        return templates.TemplateResponse('logfile.html',{'request':request,'message':message})

@router.get('/super_admin')
async def super_admin(request:Request):
    return templates.TemplateResponse('super_admin.html',{'request':request})



@router.post('/super_admin_signup')
async def super_admin_sinup(email:str,password:str,request:Request):
    if('@' not in email[2:-3]) and ('.' not in email[-4::]):
        return 1
    Super_admin(email=email,password=password,status=1).save()
    Signup(name="admin",email=email, password=password,createdOn=datetime.now(),status=1).save()
    return "success"




@router.get('/login_files')
async def login_detail_page(request:Request):
    return pagination_data(request)



@router.get('/delete/{id}')
async def delete_page(id,request:Request):
    try:
        login_data=Logfiles_data.objects(loginid=id).first()
        admin_data=Signup.objects(id=id).first()
        login_data.update(status=2)
        admin_data.update(status=2)
        data=Signup.objects(status=1)
        return templates.TemplateResponse('logfile.html',{'request':request,'data':data})
    except Exception as e:
        return templates.TemplateResponse('logfile.html',{'request':request,'message':"Exception Occure..."})

        
    

@router.get('/asserts_dashboard')
async def dashboard(request:Request):
    try:
        total_systems=Managedata.objects(status=1)
        desktop_total=Desktopdata.objects(status=1)
        other_systems=other_systemsdata.objects(status=1)
        
        return templates.TemplateResponse('asserts.html',{'request': request,'total_systems': len(total_systems),'desktop_total':len(desktop_total),'other_systems':len(other_systems)})
    except Exception as e:
         return templates.TemplateResponse('asserts.html',{'request':request,'message':f"Exception Occure...{e}"})




@router.get('/pagination/{page_num}',response_class=HTMLResponse)
async def pagination(page_num:int,request:Request):
    try:
        user=Logfiles_data.objects.order_by("-id")
        page = page_num
        per_page = 10
        start = (page - 1) * per_page
        end = start + per_page
        total_pages = ceil(len(user) / per_page)
        paginated_data = user[start:end]
        content= {
            "start":start,
            "total_pages": total_pages,
            "request":request,
            'data':paginated_data
        }
        return templates.TemplateResponse('loginfiles.html',content)
    except Exception as e:
        return templates.TemplateResponse('loginfiles.html',{'request':request,'message':"Exception Occure..."})
