
from controllers.util import *

desktop = APIRouter()




@desktop.get('/desktop_dashboard')
async def desktop_dashboard(request:Request):
    try:
        total_systems = Desktopdata.objects(status=1)
        assign_data = Desktopdata.objects(desktopstatus="Assigned",status=1)
        issue_data = Desktopdata.objects(desktopstatus="Issue",status=1)
        unassign_data = Desktopdata.objects(desktopstatus="Unassigned",status=1)
        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': total_systems,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        
        }

        return templates.TemplateResponse('desktop_dashboard.html',content)
    except Exception as e:
        return templates.TemplateResponse('desktop_dashboard.html',{'message':e,"request":request})

@desktop.post('/desktop_add_systems', response_class=HTMLResponse)
async def handle_desktop_add_systems(request: Request):
    # Extracting form data
    try:
        form_data = await request.form()
        desktopid = form_data.get('desktopid', '').upper()
        deviceid = form_data.get('deviceid', '').upper()
        productid = form_data.get('productid', '').upper()
        name = form_data.get('name', '').upper()
        manufacturer = form_data.get('manufacturer', '')
        model = form_data.get('model', '')
        configuration = form_data.get('configuration', '')
        createdOn = datetime.now()
        desktopstatus = form_data.get('status', '')
        required_fields=[desktopid,deviceid,productid,manufacturer,model,configuration,desktopstatus]
        if(not all(required_fields)):
            message="Please enter valid fields.."
            return templates.TemplateResponse('desktop_dashboard.html', {'request': request, 'message': message})
        
        users=Logfiles_data.objects.order_by("-id")[0]

        # Check for existing records
        if Desktopdata.objects(desktopid=desktopid,status=1).first():
            message = "Desktop ID already exists..."
            return templates.TemplateResponse('desktop_dashboard.html', {'request': request, 'message': message})

        if Desktopdata.objects(productid=productid,status=1).first():
            message = "Product ID already exists..."
            return templates.TemplateResponse('desktop_dashboard.html', {'request': request, 'message': message})

        try:
            # Save the desktop data
            desktop_dataId=Desktopdata(
                desktopid=desktopid,
                deviceid=deviceid,
                productid=productid,
                name=name,
                manufacturer=manufacturer,
                model=model,
                configuration=configuration,
                createdOn=createdOn,
                desktopstatus=desktopstatus,
                status=1
            ).save()
            print(desktop_dataId.id,"+++++++++++++++++++++++")
            HistoryField(
                desktopdataid=desktop_dataId.id,
                laptopid=desktopid,
                name=name,
                action="Create",
                admin=users.loginid.name,
                updatedDate=createdOn,
                receivedBy='Rama Krishna sir',
                createdOn=createdOn,
                status=1
            ).save()
            print("+++++++++++++++++++")

            # Update unassigned desktops
            Desktopdata.objects(name='').update(desktopstatus="Unassigned")

        except NotUniqueError as e:
            # Handle unique constraint violations
            message = f"Error saving data: {str(e)}"
            return templates.TemplateResponse('desktop_dashboard.html', {'request': request, 'message': message})

        except Exception as e:
            # General exception handling
            message = f"Unexpected error: {str(e)}"
            return templates.TemplateResponse('desktop_dashboard.html', {'request': request, 'message': message})

        # Fetch data for the dashboard
        total_systems = Desktopdata.objects(status=1)
        assign_data = Desktopdata.objects(desktopstatus="Assigned",status=1)
        issue_data = Desktopdata.objects(desktopstatus="Issue",status=1)
        unassign_data = Desktopdata.objects(desktopstatus="Unassigned",status=1)

        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': total_systems,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        }

        return templates.TemplateResponse('desktop_dashboard.html', content)
    except Exception as e:
        return templates.TemplateResponse('desktop_dashboard.html',{'message':e,"request":request})



@desktop.get("/dasktop_assign_systems", response_class=HTMLResponse)
async def desktop_assign_systems(request: Request):
    try:
        total_systems = Desktopdata.objects(status=1)
        assign_data = Desktopdata.objects(desktopstatus="Assigned",status=1)
        issue_data = Desktopdata.objects(desktopstatus="Issue",status=1)
        unassign_data = Desktopdata.objects(desktopstatus="Unassigned",status=1)

        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': assign_data,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        }
        return templates.TemplateResponse('desktop_dashboard.html', content)
    except Exception as e:
        return templates.TemplateResponse('desktop_dashboard.html',{'message':e,"request":request})






@desktop.get("/dasktop_issue_systems", response_class=HTMLResponse)
async def desktop_issue_systems(request: Request):
    try:

        total_systems = Desktopdata.objects(status=1)
        assign_data = Desktopdata.objects(desktopstatus="Assigned",status=1)
        issue_data = Desktopdata.objects(desktopstatus="Issue",status=1)
        unassign_data = Desktopdata.objects(desktopstatus="Unassigned",status=1)

    
        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': issue_data,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        }
        return templates.TemplateResponse('desktop_dashboard.html', content)
    except Exception as e:
        return templates.TemplateResponse('desktop_dashboard.html',{'message':e,"request":request})







@desktop.get("/dasktop_unassign_systems", response_class=HTMLResponse)
async def desktop_unassign_systems(request: Request):
    try:
   
        total_systems = Desktopdata.objects(status=1)
        assign_data = Desktopdata.objects(desktopstatus="Assigned",status=1)
        issue_data = Desktopdata.objects(desktopstatus="Issue",status=1)
        unassign_data = Desktopdata.objects(desktopstatus="Unassigned",status=1)


        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': unassign_data,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        }
        return templates.TemplateResponse('desktop_dashboard.html', content)
    except Exception as e:
        return templates.TemplateResponse('desktop_dashboard.html',{'message':e,"request":request})






@desktop.get("/desktop_total_systems", response_class=HTMLResponse)
async def desktop_total_systems(request: Request):
    try:
        total_systems = Desktopdata.objects(status=1)
        assign_data = Desktopdata.objects(desktopstatus="Assigned",status=1)
        issue_data = Desktopdata.objects(desktopstatus="Issue",status=1)
        unassign_data = Desktopdata.objects(desktopstatus="Unassigned",status=1)

        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': total_systems,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        }
        return templates.TemplateResponse('desktop_dashboard.html', content)
    except Exception as e:
        return templates.TemplateResponse('desktop_dashboard.html',{'message':e,"request":request})



# desktop edit delete and issue data 








@desktop.post('/desktop_edit_data/{data_id}', response_class=HTMLResponse)
async def handle_desktop_systems(data_id,request: Request):
    try: 
        form_data = await request.form()
        desktopid = form_data.get('desktopid').upper()
        deviceid = form_data.get('deviceid').upper()
        productid = form_data.get('productid').upper()
        name = form_data.get('name').upper()
        manufacturer = form_data.get('manufacturer')
        model = form_data.get('model')
        configuration = form_data.get('configuration')
        createdOn=datetime.now()
        desktopstatus = form_data.get('status')
        required_fields=[desktopid,deviceid,productid,manufacturer,model,configuration,desktopstatus]
        users=Logfiles_data.objects.order_by("-id")[0]

        if(not all(required_fields)):
            message="Please enter valid fields.."
            return templates.TemplateResponse('desktop_dashboard.html', {'request': request, 'message': message})
        data=Desktopdata.objects(id=data_id).first()
        if data:
            receive=Desktopdata.objects(id=data_id).first()
            HistoryField(
            desktopdataid=data_id,
            laptopid=desktopid,
            name=name,
            action="Edit",
            admin=users.loginid.name,
            updatedDate=createdOn,
            receivedBy='Rama Krishna sir',
            createdOn=receive.createdOn,
            status=1
            ).save()
            data.update(
            desktopid=desktopid,
            deviceid=deviceid,
            productid=productid,
            name=name,
            manufacturer=manufacturer,
            model=model,
            configuration=configuration,
            desktopstatus=desktopstatus,
            status=1
            )
            
        name_empty=Desktopdata.objects(name='')
        if name_empty:
            name_empty.update(desktoptatus="Unassigned")
        print(desktopid,productid)
        data1=Desktopissue_data.objects(desktopid=desktopid,productid=deviceid,status=1)
        print(data1)
        if data1:
            data.update(desktopstatus="Issue")


    
        total_systems = Desktopdata.objects(status=1)
        assign_data = Desktopdata.objects(desktopstatus="Assigned",status=1)
        issue_data = Desktopdata.objects(desktopstatus="Issue",status=1)
        unassign_data = Desktopdata.objects(desktopstatus="Unassigned",status=1)

        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': total_systems,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        }
        return templates.TemplateResponse('desktop_dashboard.html', content)
    except Exception as e:
        return templates.TemplateResponse('desktop_dashboard.html',{'message':e,"request":request})



#issue data 
def pagenation_data(request):
    users=Desktopissue_data.objects(status=1)
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
    return templates.TemplateResponse('desktop_issues.html',content)


@desktop.get('/desktop_issue')
async def desktop_report_page(request:Request):
    return pagenation_data(request)

@desktop.post('/desktop_issue/{data_id}')
async def issue_data(data_id,request:Request):
    try:
        form_data = await request.form()
        desktopid = form_data.get('desktopid').upper()
        productid=form_data.get('deviceid').upper()
        name = form_data.get('name').upper()
        issue = form_data.get('issue')
        date = datetime.now()
        desktopstatus = form_data.get('status')
        required_fields=[desktopid,productid,name,issue,desktopstatus]
        if(not all(required_fields)):
            message="Please enter valid fields.."
            return templates.TemplateResponse('desktop_dashboard.html', {'request': request, 'message': message})
        data=Desktopissue_data.objects(desktopid=desktopid,productid=productid,status=1)
        if data:
            message="already this System is present in issue data..."
            return templates.TemplateResponse('desktop_dashboard.html',{'request':request,'message':message})
        users=Logfiles_data.objects.order_by("-id")[0]

        receive=Desktopdata.objects(id=data_id).first()
        HistoryField(
            desktopdataid=data_id,
            laptopid=desktopid,
            name=name,
            action="Issue",
            admin=users.loginid.name,
            updatedDate=date,
            receivedBy='Rama Krishna sir',
            createdOn=receive.createdOn,
            status=1
        ).save()
        print("+++++++++++++++++++++++")
        Desktopissue_data(desktopid=desktopid,
                desktopdataid=data_id,
                name=name,
                productid=productid,
                issue=issue,
                createdOn=date,
                desktopstatus=desktopstatus,
                status=1).save()
        
        
        data=Desktopdata.objects(id=data_id).first()
        print(data)
        if data:
            data.update(desktopstatus="Issue")


        total_systems = Desktopdata.objects(status=1)
        assign_data = Desktopdata.objects(desktopstatus="Assigned",status=1)
        issue_data = Desktopdata.objects(desktopstatus="Issue",status=1)
        unassign_data = Desktopdata.objects(desktopstatus="Unassigned",status=1)

        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': total_systems,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        }
        return templates.TemplateResponse('desktop_dashboard.html',content)
    except Exception as e:
        return templates.TemplateResponse('desktop_dashboard.html',{'message':e,"request":request})



@desktop.get('/desktop_delete_issue/{data_id}')
async def delete_issue(data_id: str, request: Request):
    try:
        first = Desktopissue_data.objects(id=data_id).first()
        users=Logfiles_data.objects.order_by("-id")[0]

        if first:
            Desktopdata_data = first.desktopdataid 
            HistoryField(
            desktopdataid=data_id,
            laptopid=first.desktopid,
            name=first.name,
            action="Delete",
            admin=users.loginid.name,
            updatedDate=datetime.now(),
            receivedBy='Rama Krishna sir',
            createdOn=Desktopdata_data.createdOn,
            status=1
            ).save()
            if Desktopdata_data:
                Desktopdata_data.update(status=2)
        
        Desktopissue_data.objects(id=data_id).update(status=2)

        return pagenation_data(request)
    except Exception as e:
        return templates.TemplateResponse('desktop_dashboard.html',{'message':e,"request":request})




@desktop.post('/desktop_update_laptop_issue_data/{data_id}')
async def desktop_update_laptop_issue_data(data_id,request:Request):
    try:
        form_data = await request.form()
        desktopid = form_data.get('desktopid').upper()
        deviceid = form_data.get('deviceid').upper()
        productid = form_data.get('productid').upper()
        name = form_data.get('name').upper()
        manufacturer = form_data.get('manufacturer')
        model = form_data.get('model')
        configuration = form_data.get('configuration')
        date = datetime.now()
        desktopstatus = form_data.get('status')
        required_fields=[desktopid,deviceid,productid,manufacturer,model,configuration,desktopstatus]
        users=Logfiles_data.objects.order_by("-id")[0]

        if(not all(required_fields)):
            message="Please enter valid fields.."
            return templates.TemplateResponse('desktop_issues.html', {'request': request, 'message': message})
        update_data=Desktopissue_data.objects(id=data_id).first()
        if update_data:
            managedata=update_data.desktopdataid
            if managedata and desktopstatus != "Issue":
                HistoryField(
                    desktopdataid=data_id,
                    laptopid=desktopid,
                    name=name,
                    action="Updated issue data",
                    admin=users.loginid.name,
                    updatedDate=date,
                    receivedBy='Rama Krishna sir',
                    createdOn=managedata.createdOn,
                    status=1
                ).save()
                managedata.update(desktopstatus=desktopstatus,desktopid=desktopid,deviceid=deviceid,productid=productid,name=name,manufacturer=manufacturer,model=model,configuration=configuration)
                
                update_data.update(status=2)
        return pagenation_data(request)
    except Exception as e:
        return templates.TemplateResponse('desktop_dashboard.html',{'message':e,"request":request})









# desktop filters




@desktop.get('/desktop_desktopid')
async def desktop_loginid(request:Request):
    try:
        form_data=request.query_params
        loginid=form_data.get('search_element').upper()
        total_systems=Desktopdata.objects(desktopid__icontains=loginid,status=1)
        assign_data=Desktopdata.objects(desktopstatus="Assigned",desktopid__icontains=loginid,status=1)
        issue_data=Desktopdata.objects(desktopstatus="Issue",desktopid__icontains=loginid,status=1)
        unassign_data=Desktopdata.objects(desktopstatus="Unassigned",desktopid__icontains=loginid,status=1)
        content={
            'request':request,
            'total_systems':len(total_systems),
            'assign_data':len(assign_data),
            'data':total_systems,
            'issue_data':len(issue_data),
            'unassign_data':len(unassign_data),
            'search_element':loginid
        }
        return templates.TemplateResponse('desktop_dashboard.html',content)
    except Exception as e:
        return templates.TemplateResponse('desktop_dashboard.html',{'message':e,"request":request})



@desktop.get('/desktop_name_filter')
async def desktop_name_filter(request:Request):
    try:
        form_data=request.query_params
        loginid=form_data.get('search_element').upper()
        total_systems=Desktopdata.objects(name__icontains=loginid,status=1)
        assign_data=Desktopdata.objects(desktopstatus="Assigned",name__icontains=loginid,status=1)
        issue_data=Desktopdata.objects(desktopstatus="Issue",name__icontains=loginid,status=1)
        unassign_data=Desktopdata.objects(desktopstatus="Unassigned",name__icontains=loginid,status=1)
        content={
            'request':request,
            'total_systems':len(total_systems),
            'assign_data':len(assign_data),
            'data':total_systems,
            'issue_data':len(issue_data),
            'unassign_data':len(unassign_data),
            "search_element1":loginid
        }
        return templates.TemplateResponse('desktop_dashboard.html',content)
    except Exception as e:
        return templates.TemplateResponse('desktop_dashboard.html',{'message':e,"request":request})




# pagenation data



@desktop.get('/pagination_desktop_issue/{page_num}',response_class=HTMLResponse)
async def pagination(page_num:int,request:Request):
    try:
        user=Desktopissue_data.objects()
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
        return templates.TemplateResponse('desktop_issues.html',content)
    except Exception as e:
        return templates.TemplateResponse('desktop_dashboard.html',{'message':e,"request":request})
