from controllers.util import *

dashboard = APIRouter()

@dashboard.get("/")
async def read_dashboard(request:Request):
    return templates.TemplateResponse('login.html',{'request':request})

@dashboard.get('/add_systems', response_class=HTMLResponse)
async def add_systems(request: Request):
    return templates.TemplateResponse('manage.html', {'request': request})


@dashboard.get('/dashboard', response_class=HTMLResponse)
async def add_systems(request: Request):
    return templates.TemplateResponse('dashboard.html', {'request': request})

@dashboard.post('/add_systems', response_class=HTMLResponse)
async def handle_add_systems(request: Request): 
    form_data = await request.form()
    laptopid = form_data.get('laptopid').upper()
    name = form_data.get('name').upper()
    serial_no = form_data.get('serial_no')
    product = form_data.get('product')
    configuration = form_data.get('configuration')
    receiver = form_data.get('receiver')
    date = form_data.get('date')
    status = form_data.get('status')

    data=Managedata.objects(laptopid=laptopid)
    data1=Managedata.objects(serial_no=serial_no)
    required_fields=[laptopid,serial_no,product,configuration,receiver,date,status]


    if(data):
        message='laptopid already exits...'
        return templates.TemplateResponse('dashboard.html',{'request':request,'message':message})
    if(data1):
        message='serial number already exits...'
        return templates.TemplateResponse('dashboard.html',{'request':request,'message':message})
    if(all(required_fields)):
        Managedata(
        laptopid=laptopid,
        name=name,
        serial_no=serial_no,
        product=product,
        configuration=configuration,
        received_by=receiver,
        date=date,
        status=status
        ).save()
        users=Logfiles_data.objects.order_by("-id")[0]

        HistoryField(
        laptopid=laptopid,
        name=name,
        action="Create",
        admin=users.loginid.name,
        updated_date=date,
        received_by=receiver,
        received_date=date
        ).save()
    
        name_empty=Managedata.objects(name='')
        if name_empty:
            name_empty.update(status="Unassigned")


   
        total_systems = Managedata.objects()
        assign_data = Managedata.objects(status="Assigned")
        issue_data = Managedata.objects(status="Issue")
        unassign_data = Managedata.objects(status="Unassigned")

 

        content = {
        'request': request,
        'total_systems': len(total_systems),
        'assign_data': len(assign_data),
        'data': total_systems,
        'issue_data': len(issue_data),
        'unassign_data': len(unassign_data)
    
        }
        return templates.TemplateResponse('dashboard.html', content)
    else:
        message="Please enter valid fields.."
        return templates.TemplateResponse('dashboard.html', {'request': request, 'message': message})



@dashboard.get("/assign_systems", response_class=HTMLResponse)
async def assign_systems(request: Request):

    total_systems = Managedata.objects()
    assign_data = Managedata.objects(status="Assigned")
    issue_data = Managedata.objects(status="Issue")
    unassign_data = Managedata.objects(status="Unassigned")


    content = {
        'request': request,
        'total_systems': len(total_systems),
        'assign_data': len(assign_data),
        'data': assign_data,
        'issue_data': len(issue_data),
        'unassign_data': len(unassign_data)
    }
    return templates.TemplateResponse('dashboard.html', content)






@dashboard.get("/issue_systems", response_class=HTMLResponse)
async def issue_systems(request: Request):

    total_systems = Managedata.objects()
    assign_data = Managedata.objects(status="Assigned")
    issue_data = Managedata.objects(status="Issue")
    unassign_data = Managedata.objects(status="Unassigned")

  
    content = {
        'request': request,
        'total_systems': len(total_systems),
        'assign_data': len(assign_data),
        'data': issue_data,
        'issue_data': len(issue_data),
        'unassign_data': len(unassign_data)
    }
    return templates.TemplateResponse('dashboard.html', content)







@dashboard.get("/unassign_systems", response_class=HTMLResponse)
async def unassign_systems(request: Request):
   
    total_systems = Managedata.objects()
    assign_data = Managedata.objects(status="Assigned")
    issue_data = Managedata.objects(status="Issue")
    unassign_data = Managedata.objects(status="Unassigned")


    content = {
        'request': request,
        'total_systems': len(total_systems),
        'assign_data': len(assign_data),
        'data': unassign_data,
        'issue_data': len(issue_data),
        'unassign_data': len(unassign_data)
    }
    return templates.TemplateResponse('dashboard.html', content)






@dashboard.get("/total_systems", response_class=HTMLResponse)
async def total_systems(request: Request):
    total_systems = Managedata.objects()
    assign_data = Managedata.objects(status="Assigned")
    issue_data = Managedata.objects(status="Issue")
    unassign_data = Managedata.objects(status="Unassigned")

    content = {
        'request': request,
        'total_systems': len(total_systems),
        'assign_data': len(assign_data),
        'data': total_systems,
        'issue_data': len(issue_data),
        'unassign_data': len(unassign_data)
    }
    return templates.TemplateResponse('dashboard.html', content)











@dashboard.get('/laptopid')
async def loginid(request:Request):
    form_data=request.query_params
    loginid=form_data.get('search_element').upper()
    total_systems=Managedata.objects(laptopid__icontains=loginid)
    assign_data=Managedata.objects(status="Assigned",laptopid__icontains=loginid)
    issue_data=Managedata.objects(status="Issue",laptopid__icontains=loginid)
    unassign_data=Managedata.objects(status="Unassigned",laptopid__icontains=loginid)
    content={
        'request':request,
        'total_systems':len(total_systems),
        'assign_data':len(assign_data),
        'data':total_systems,
        'issue_data':len(issue_data),
        'unassign_data':len(unassign_data),
        'search_element':loginid
    }
    return templates.TemplateResponse('dashboard.html',content)



@dashboard.get('/name_filter')
async def name_filter(request:Request):
    form_data=request.query_params
    loginid=form_data.get('search_element').upper()
    total_systems=Managedata.objects(name__icontains=loginid)
    assign_data=Managedata.objects(status="Assigned",name__icontains=loginid)
    issue_data=Managedata.objects(status="Issue",name__icontains=loginid)
    unassign_data=Managedata.objects(status="Unassigned",name__icontains=loginid)
    content={
        'request':request,
        'total_systems':len(total_systems),
        'assign_data':len(assign_data),
        'data':total_systems,
        'issue_data':len(issue_data),
        'unassign_data':len(unassign_data),
        "search_element1":loginid
    }
    return templates.TemplateResponse('dashboard.html',content)









#history filter
def error_function(request):
    users=HistoryField.objects.order_by('-id')
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
    return templates.TemplateResponse('history.html',content)


@dashboard.get('/history')
async def history(request:Request):
    return error_function(request)


@dashboard.get('/history_laptopid')
async def loginid(request:Request):
    form_data=request.query_params
    loginid=form_data.get('search_element').upper()
    data=HistoryField.objects(laptopid__icontains=loginid)
    content = {
        'request': request,
        'data':data
        
    }
    return templates.TemplateResponse('history.html',content)




@dashboard.get('/history_name_filter')
async def name_filter(request:Request):
    form_data=request.query_params
    loginid=form_data.get('search_element').upper()
    data=HistoryField.objects(name__icontains=loginid)
    content = {
        'request': request,
         'data':data
        
    }
    return templates.TemplateResponse('history.html',content)




@dashboard.get('/pagination1/{page_num}',response_class=HTMLResponse)
async def pagination(page_num:int,request:Request):
    user=HistoryField.objects()
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
    return templates.TemplateResponse('history.html',content)








def error_function(request):
    users=Issue_data.objects()
    page = 1
    per_page = 5
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
    return templates.TemplateResponse('report_issue.html',content)

@dashboard.post('/edit_data/{data_id}', response_class=HTMLResponse)
async def handle_edit_systems(data_id,request: Request): 
    form_data = await request.form()
    laptopid = form_data.get('laptopid').upper()
    name = form_data.get('name').upper()
    serial_no = form_data.get('serial_no')
    product = form_data.get('product')
    configuration = form_data.get('configuration')
    date = form_data.get('date')
    status = form_data.get('status')
    data=Managedata.objects(id=data_id).first()
    required_fields=[laptopid,serial_no,product,configuration,date,status]
    if data:
        if(not all(required_fields)):
            message="Please enter valid fields.."
            return templates.TemplateResponse('dashboard.html', {'request': request, 'message': message})
        receive=Managedata.objects(id=data_id).first()
        users=Logfiles_data.objects.order_by("-id")[0]

        HistoryField(
        laptopdataid=data_id,
        laptopid=laptopid,
        name=name,
        action="Edit",
        admin=users.loginid.name,
        updated_date=date,
        received_by=receive.received_by,
        received_date=receive.date
        ).save()
        data.update(
        laptopid=laptopid,
        name=name,
        serial_no=serial_no,
        product=product,
        configuration=configuration,
        status=status
        )
        

    name_empty=Managedata.objects(name='')
    if name_empty:
        name_empty.update(status="Unassigned")
    data1=Issue_data.objects(laptopid=laptopid,serial_no=serial_no)
    if data1:
        data.update(status="Issue")


   
    total_systems = Managedata.objects()
    assign_data = Managedata.objects(status="Assigned")
    issue_data = Managedata.objects(status="Issue")
    unassign_data = Managedata.objects(status="Unassigned")

    content = {
        'request': request,
        'total_systems': len(total_systems),
        'assign_data': len(assign_data),
        'data': total_systems,
        'issue_data': len(issue_data),
        'unassign_data': len(unassign_data)
    }
    return templates.TemplateResponse('dashboard.html', content)


@dashboard.get('/issue')
async def report_page(request:Request):
    return error_function(request)

@dashboard.post('/issue/{data_id}')
async def issue_data(data_id,request:Request):
    form_data = await request.form()
    laptopid = form_data.get('laptopid').upper()
    name = form_data.get('name').upper()
    serial_no = form_data.get('serial_no')
    issue = form_data.get('issue')
    date = form_data.get('date')
    status = form_data.get('status')
    required_fields=[laptopid,name,serial_no,issue,date,status]
    data=Issue_data.objects(laptopid=laptopid,serial_no=serial_no).first()
    if data:
        message="already this System is present in issue data..."
        return templates.TemplateResponse('dashboard.html',{'request':request,'message':message})
    if(not all(required_fields)):
            message="Please enter valid fields.."
            return templates.TemplateResponse('dashboard.html', {'request': request, 'message': message})

    receive=Managedata.objects(id=data_id).first()
    users=Logfiles_data.objects.order_by("-id")[0]

    HistoryField(
        laptopdataid=data_id,
        laptopid=laptopid,
        name=name,
        action="Issue",
        admin=users.loginid.name,
        updated_date=date,
        received_by=receive.received_by,
        received_date=receive.date
        ).save()
    Issue_data(laptopid=laptopid,
               managedataId=data_id,
               name=name,
               serial_no=serial_no,
               issue=issue,
               date=date,
               status=status).save()
    
    
    
    data=Managedata.objects(id=data_id).first()
    if data:
        data.update(status="Issue")


    total_systems = Managedata.objects()
    assign_data = Managedata.objects(status="Assigned")
    issue_data = Managedata.objects(status="Issue")
    unassign_data = Managedata.objects(status="Unassigned")

    content = {
        'request': request,
        'total_systems': len(total_systems),
        'assign_data': len(assign_data),
        'data': total_systems,
        'issue_data': len(issue_data),
        'unassign_data': len(unassign_data)
    }
    return templates.TemplateResponse('dashboard.html',content)



@dashboard.get('/delete_issue/{data_id}')
async def delete_issue(data_id: str, request: Request):
    first = Issue_data.objects(id=data_id).first()
    if first:
        managedata_data = first.managedataId
        users=Logfiles_data.objects.order_by("-id")[0]

        HistoryField(
        laptopdataid=data_id,
        laptopid=first.laptopid,
        name=first.name,
        action="Delete",
        admin=users.loginid.name,
        updated_date=first.date,
        received_by=managedata_data.received_by,
        received_date=managedata_data.date
        ).save()
        if managedata_data:
            managedata_data.delete()
    
    Issue_data.objects(id=data_id).delete()

    return error_function(request)



@dashboard.post('/update_laptop_issue_data/{data_id}')
async def update_laptop_issue_data(data_id,request:Request):
    form_data = await request.form()
    laptopid = form_data.get('laptopid').upper()
    name = form_data.get('name').upper()
    serial_no = form_data.get('serial_no')
    product = form_data.get('product')
    configuration = form_data.get('configuration')
    date = form_data.get('date')
    status = form_data.get('status')
    required_fields=[laptopid,name,serial_no,product,configuration,date,status]
    if(not all(required_fields)):
        message="Please enter valid fields.."
        return templates.TemplateResponse('report_issue.html', {'request': request, 'message': message})
    update_data=Issue_data.objects(id=data_id).first()
    if update_data:
        managedata=update_data.managedataId
        if managedata and status != "Issue":
            users=Logfiles_data.objects.order_by("-id")[0]

            HistoryField(
                laptopdataid=data_id,
                laptopid=laptopid,
                name=name,
                action="Update issue data",
                admin=users.loginid.name,
                updated_date=date,
                received_by=managedata.received_by,
                received_date=managedata.date
                ).save()
            managedata.update(status=status,laptopid=laptopid,name=name,serial_no=serial_no,product=product,configuration=configuration)
            
            update_data.delete()
    return error_function(request)





@dashboard.get('/pagination_laptop_issue/{page_num}',response_class=HTMLResponse)
async def pagination(page_num:int,request:Request):
    user=Issue_data.objects()
    page = page_num
    per_page = 5
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
    return templates.TemplateResponse('report_issue.html',content)

