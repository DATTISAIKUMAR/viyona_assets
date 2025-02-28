from controllers.util import *


other_systems = APIRouter()



@other_systems.get('/other_systems_dashboard')
async def other_systems_dashboard(request:Request):
    try:
    
        total_systems = other_systemsdata.objects()
        assign_data = other_systemsdata.objects(status="Assigned")
        issue_data = other_systemsdata.objects(status="Issue")
        unassign_data = other_systemsdata.objects(status="Unassigned")

    

        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': total_systems,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        }

        return templates.TemplateResponse('other_systems_dashboard.html',content)
    except Exception as e:
        message="exception accure.."
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})

@other_systems.post('/other_systems_add_systems', response_class=HTMLResponse)
async def handle_other_systems_add_systems(request: Request):
    # Extracting form data
    form_data = await request.form()
    other_systemsid = form_data.get('other_systemsid', '').upper()
    deviceid = form_data.get('deviceid', '').upper()
    productid = form_data.get('productid', '').upper()
    name = form_data.get('name', '').upper()
    manufacturer = form_data.get('manufacturer', '')
    model = form_data.get('model', '')
    configuration = form_data.get('configuration', '')
    date = form_data.get('date', '')
    status = form_data.get('status', '')
    required_fields=[other_systemsid,deviceid,productid,manufacturer,model,configuration,date,status]
    if(not all(required_fields)):
        message="Please enter valid fields.."
        return templates.TemplateResponse('other_systems_dashboard.html', {'request': request, 'message': message})
    

    # Check for existing records
    if other_systemsdata.objects(other_systemsid=other_systemsid).first():
        message = "other_systems ID already exists..."
        return templates.TemplateResponse('other_systems_dashboard.html', {'request': request, 'message': message})

    if other_systemsdata.objects(productid=productid).first():
        message = "Product ID already exists..."
        return templates.TemplateResponse('other_systems_dashboard.html', {'request': request, 'message': message})

    try:
        # Save the other_systems data
        other_systemsdata(
            other_systemsid=other_systemsid,
            deviceid=deviceid,
            productid=productid,
            name=name,
            manufacturer=manufacturer,
            model=model,
            configuration=configuration,
            date=date,
            status=status
        ).save()
        users=Logfiles_data.objects.order_by("-id")[0]

        # Save the history record
        HistoryField(
            laptopid=other_systemsid,
            name=name,
            action="Create",
            admin=users.loginid.name,
            updated_date=date,
            received_by='Rama Krishna sir',
            received_date=date
        ).save()

        # Update unassigned other_systemss
        other_systemsdata.objects(name='').update(status="Unassigned")

    except NotUniqueError as e:
        # Handle unique constraint violations
        message = f"Error saving data: {str(e)}"
        return templates.TemplateResponse('other_systems_dashboard.html', {'request': request, 'message': message})

    except Exception as e:
        # General exception handling
        message = f"Unexpected error: {str(e)}"
        return templates.TemplateResponse('other_systems_dashboard.html', {'request': request, 'message': message})

    # Fetch data for the dashboard
    total_systems = other_systemsdata.objects()
    assign_data = other_systemsdata.objects(status="Assigned")
    issue_data = other_systemsdata.objects(status="Issue")
    unassign_data = other_systemsdata.objects(status="Unassigned")

    content = {
        'request': request,
        'total_systems': len(total_systems),
        'assign_data': len(assign_data),
        'data': total_systems,
        'issue_data': len(issue_data),
        'unassign_data': len(unassign_data)
    }

    return templates.TemplateResponse('other_systems_dashboard.html', content)



@other_systems.get("/other_systems_assign_systems", response_class=HTMLResponse)
async def other_systems_assign_systems(request: Request):

    total_systems = other_systemsdata.objects()
    assign_data = other_systemsdata.objects(status="Assigned")
    issue_data = other_systemsdata.objects(status="Issue")
    unassign_data = other_systemsdata.objects(status="Unassigned")


    content = {
        'request': request,
        'total_systems': len(total_systems),
        'assign_data': len(assign_data),
        'data': assign_data,
        'issue_data': len(issue_data),
        'unassign_data': len(unassign_data)
    }
    return templates.TemplateResponse('other_systems_dashboard.html', content)






@other_systems.get("/other_systems_issue_systems", response_class=HTMLResponse)
async def other_systems_issue_systems(request: Request):

    total_systems = other_systemsdata.objects()
    assign_data = other_systemsdata.objects(status="Assigned")
    issue_data = other_systemsdata.objects(status="Issue")
    unassign_data = other_systemsdata.objects(status="Unassigned")

  
    content = {
        'request': request,
        'total_systems': len(total_systems),
        'assign_data': len(assign_data),
        'data': issue_data,
        'issue_data': len(issue_data),
        'unassign_data': len(unassign_data)
    }
    return templates.TemplateResponse('other_systems_dashboard.html', content)







@other_systems.get("/other_systems_unassign_systems", response_class=HTMLResponse)
async def other_systems_unassign_systems(request: Request):
   
    total_systems = other_systemsdata.objects()
    assign_data = other_systemsdata.objects(status="Assigned")
    issue_data = other_systemsdata.objects(status="Issue")
    unassign_data = other_systemsdata.objects(status="Unassigned")


    content = {
        'request': request,
        'total_systems': len(total_systems),
        'assign_data': len(assign_data),
        'data': unassign_data,
        'issue_data': len(issue_data),
        'unassign_data': len(unassign_data)
    }
    return templates.TemplateResponse('other_systems_dashboard.html', content)






@other_systems.get("/other_systems_total_systems", response_class=HTMLResponse)
async def other_systems_total_systems(request: Request):
    total_systems = other_systemsdata.objects()
    assign_data = other_systemsdata.objects(status="Assigned")
    issue_data = other_systemsdata.objects(status="Issue")
    unassign_data = other_systemsdata.objects(status="Unassigned")

    content = {
        'request': request,
        'total_systems': len(total_systems),
        'assign_data': len(assign_data),
        'data': total_systems,
        'issue_data': len(issue_data),
        'unassign_data': len(unassign_data)
    }
    return templates.TemplateResponse('other_systems_dashboard.html', content)



# other_systems edit delete and issue data 








@other_systems.post('/other_systems_edit_data/{data_id}', response_class=HTMLResponse)
async def handle_other_systems_systems(data_id,request: Request): 
    form_data = await request.form()
    other_systemsid = form_data.get('other_systemsid').upper()
    deviceid = form_data.get('deviceid').upper()
    productid = form_data.get('productid').upper()
    name = form_data.get('name').upper()
    manufacturer = form_data.get('manufacturer')
    model = form_data.get('model')
    configuration = form_data.get('configuration')
    date = form_data.get('date')
    status = form_data.get('status')
    required_fields=[other_systemsid,deviceid,productid,manufacturer,model,configuration,date,status]
    if(not all(required_fields)):
        message="Please enter valid fields.."
        return templates.TemplateResponse('other_systems_dashboard.html', {'request': request, 'message': message})
    data=other_systemsdata.objects(id=data_id).first()
    if data:
        receive=other_systemsdata.objects(id=data_id).first()
        users=Logfiles_data.objects.order_by("-id")[0]

        HistoryField(
        other_systemsdataid=data_id,
        laptopid=other_systemsid,
        name=name,
        action="Edit",
        admin=users.loginid.name,
        updated_date=date,
        received_by='Rama Krishna sir',
        received_date=receive.date
        ).save()
        data.update(
            other_systemsid=other_systemsid,
            deviceid=deviceid,
            productid=productid,
            name=name,
            manufacturer=manufacturer,
            model=model,
            configuration=configuration,
            date=date,
            status=status
        )
        



    name_empty=other_systemsdata.objects(name='')
    if name_empty:
        name_empty.update(status="Unassigned")
    data1=other_systemsissue_data.objects(other_systemsdataid=data_id,productid=productid)
    if data1:
        data.update(status="Issue")


   
    total_systems = other_systemsdata.objects()
    assign_data = other_systemsdata.objects(status="Assigned")
    issue_data = other_systemsdata.objects(status="Issue")
    unassign_data = other_systemsdata.objects(status="Unassigned")

    content = {
        'request': request,
        'total_systems': len(total_systems),
        'assign_data': len(assign_data),
        'data': total_systems,
        'issue_data': len(issue_data),
        'unassign_data': len(unassign_data)
    }
    return templates.TemplateResponse('other_systems_dashboard.html', content)



#issue data 
def error_function(request):
    users=other_systemsissue_data.objects()

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
    return templates.TemplateResponse('other_systems_issues.html',content)


@other_systems.get('/other_systems_issue')
async def other_systems_report_page(request:Request):
    return error_function(request)

@other_systems.post('/other_systems_issue/{data_id}')
async def issue_data(data_id,request:Request):
    form_data = await request.form()
    other_systemsid = form_data.get('other_systemsid').upper()
    productid=form_data.get('deviceid').upper()
    name = form_data.get('name').upper()
    issue = form_data.get('issue')
    date = form_data.get('date')
    status = form_data.get('status')
    required_fields=[other_systemsid,productid,name,issue,date,status]
    if(not all(required_fields)):
        message="Please enter valid fields.."
        return templates.TemplateResponse('other_systems_dashboard.html', {'request': request, 'message': message})
    data=other_systemsissue_data.objects(deviceId=other_systemsid,productid=productid)
    if data:
        message="already this System is present in issue data..."
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})

    receive=other_systemsdata.objects(id=data_id).first()
    users=Logfiles_data.objects.order_by("-id")[0]

    HistoryField(
        other_systemsdataid=data_id,
        laptopid=other_systemsid,
        name=name,
        action="Issue",
        admin=users.loginid.name,
        updated_date=date,
        received_by='Rama Krishna sir',
        received_date=receive.date
    ).save()
    other_systemsissue_data(deviceId=other_systemsid,
               other_systemsdataid=data_id,
               name=name,
               productid=productid,
               issue=issue,
               date=date,
               status=status).save()
    
    
    data=other_systemsdata.objects(id=data_id).first()
    if data:
        data.update(status="Issue")


    total_systems = other_systemsdata.objects()
    assign_data = other_systemsdata.objects(status="Assigned")
    issue_data = other_systemsdata.objects(status="Issue")
    unassign_data = other_systemsdata.objects(status="Unassigned")

    content = {
        'request': request,
        'total_systems': len(total_systems),
        'assign_data': len(assign_data),
        'data': total_systems,
        'issue_data': len(issue_data),
        'unassign_data': len(unassign_data)
    }
    return templates.TemplateResponse('other_systems_dashboard.html',content)



@other_systems.get('/other_systems_delete_issue/{data_id}')
async def delete_issue(data_id: str, request: Request):
    first = other_systemsissue_data.objects(id=data_id).first()
    if first:
        other_systemsdata_data = first.other_systemsdataid 
        users=Logfiles_data.objects.order_by("-id")[0]

        HistoryField(
        other_systemsdataid=data_id,
        laptopid=first.deviceId,
        name=first.name,
        action="Delete",
        admin=users.loginid.name,
        updated_date=first.date,
        received_by='Rama Krishna sir',
        received_date=other_systemsdata_data.date
        ).save()
        if other_systemsdata_data:
            other_systemsdata_data.delete()
    
    other_systemsissue_data.objects(id=data_id).delete()

    return error_function(request)




@other_systems.post('/other_systems_update_laptop_issue_data/{data_id}')
async def other_systems_update_laptop_issue_data(data_id,request:Request):
    form_data = await request.form()
    other_systemsid = form_data.get('other_systemsid').upper()
    deviceid = form_data.get('deviceid').upper()
    productid = form_data.get('productid').upper()
    name = form_data.get('name').upper()
    manufacturer = form_data.get('manufacturer')
    model = form_data.get('model')
    configuration = form_data.get('configuration')
    date = form_data.get('date')
    status = form_data.get('status')
    required_fields=[other_systemsid,deviceid,productid,manufacturer,model,configuration,date,status]
    if(not all(required_fields)):
        message="Please enter valid fields.."
        return templates.TemplateResponse('other_systems_issues.html', {'request': request, 'message': message})
    update_data=other_systemsissue_data.objects() .first()
    print(update_data)
    # update_data=other_systemsissue_data.objects(id=ObjectId(data_id)) .first()
    if update_data:
        managedata=update_data.other_systemsdataid
        if managedata and status != "Issue":
            users=Logfiles_data.objects.order_by("-id")[0]

            HistoryField(
                other_systemsdataid=data_id,
                laptopid=other_systemsid,
                name=name,
                action="Updated issue data",
                admin=users.loginid.name,
                updated_date=date,
                received_by='Rama Krishna sir',
                received_date=managedata.date
            ).save()
            managedata.update(status=status,other_systemsid=other_systemsid,deviceid=deviceid,productid=productid,name=name,manufacturer=manufacturer,model=model,configuration=configuration)
            
            update_data.delete()
    return error_function(request)









# other_systems filters




@other_systems.get('/other_systems_other_systemsid')
async def other_systems_loginid(request:Request):
    form_data=request.query_params
    loginid=form_data.get('search_element').upper()
    total_systems=other_systemsdata.objects(other_systemsid__icontains=loginid)
    assign_data=other_systemsdata.objects(status="Assigned",other_systemsid__icontains=loginid)
    issue_data=other_systemsdata.objects(status="Issue",other_systemsid__icontains=loginid)
    unassign_data=other_systemsdata.objects(status="Unassigned",other_systemsid__icontains=loginid)
    content={
        'request':request,
        'total_systems':len(total_systems),
        'assign_data':len(assign_data),
        'data':total_systems,
        'issue_data':len(issue_data),
        'unassign_data':len(unassign_data),
        'search_element':loginid
    }
    return templates.TemplateResponse('other_systems_dashboard.html',content)



@other_systems.get('/other_systems_name_filter')
async def other_systems_name_filter(request:Request):
    form_data=request.query_params
    loginid=form_data.get('search_element').upper()
    total_systems=other_systemsdata.objects(name__icontains=loginid)
    assign_data=other_systemsdata.objects(status="Assigned",name__icontains=loginid)
    issue_data=other_systemsdata.objects(status="Issue",name__icontains=loginid)
    unassign_data=other_systemsdata.objects(status="Unassigned",name__icontains=loginid)
    content={
        'request':request,
        'total_systems':len(total_systems),
        'assign_data':len(assign_data),
        'data':total_systems,
        'issue_data':len(issue_data),
        'unassign_data':len(unassign_data),
        "search_element1":loginid
    }
    return templates.TemplateResponse('other_systems_dashboard.html',content)




# pagenation data



@other_systems.get('/pagination_other_systems_issue/{page_num}',response_class=HTMLResponse)
async def pagination(page_num:int,request:Request):
    user=other_systemsissue_data.objects()
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
    return templates.TemplateResponse('other_systems_issues.html',content)
