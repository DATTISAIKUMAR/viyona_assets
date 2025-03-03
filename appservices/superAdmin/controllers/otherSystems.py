from controllers.util import *


other_systems = APIRouter()


@other_systems.get('/other_systems_dashboard')
async def other_systems_dashboard(request:Request):
    try:
    
        total_systems = other_systemsdata.objects(status=1)
        assign_data = other_systemsdata.objects(othersystemStatus="Assigned",status=1)
        issue_data = other_systemsdata.objects(othersystemStatus="Issue",status=1)
        unassign_data = other_systemsdata.objects(othersystemStatus="Unassigned",status=1)

    

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
        message="exception occure.."
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})

@other_systems.post('/other_systems_add_systems', response_class=HTMLResponse)
async def handle_other_systems_add_systems(request: Request):
    # Extracting form data
    try:
        form_data = await request.form()
        other_systemsid = form_data.get('other_systemsid', '').upper()
        deviceid = form_data.get('deviceid', '').upper()
        productid = form_data.get('productid', '').upper()
        name = form_data.get('name', '').upper()
        manufacturer = form_data.get('manufacturer', '')
        model = form_data.get('model', '')
        configuration = form_data.get('configuration', '')
        date = datetime.now()
        status = form_data.get('status', '')
        required_fields=[other_systemsid,deviceid,productid,manufacturer,model,configuration,date,status]
        if(not all(required_fields)):
            message="Please enter valid fields.."
            return templates.TemplateResponse('other_systems_dashboard.html', {'request': request, 'message': message})
        

        # Check for existing records
        if other_systemsdata.objects(otherSystemsid=other_systemsid,status=1).first():
            message = "other_systems ID already exists..."
            return templates.TemplateResponse('other_systems_dashboard.html', {'request': request, 'message': message})

        if other_systemsdata.objects(productid=productid,status=1).first():
            message = "Product ID already exists..."
            return templates.TemplateResponse('other_systems_dashboard.html', {'request': request, 'message': message})

        try:
            # Save the other_systems data
            otherSystemsdata_id=other_systemsdata(
                otherSystemsid=other_systemsid,
                deviceid=deviceid,
                productid=productid,
                name=name,
                manufacturer=manufacturer,
                model=model,
                configuration=configuration,
                createdOn=date,
                othersystemStatus=status,
                status=1
            ).save()
            users=Logfiles_data.objects.order_by("-id")[0]

            # Save the history record
            HistoryField(
                otherSystemsdataid=otherSystemsdata_id.id,
                laptopid=other_systemsid,
                name=name,
                action="Create",
                admin=users.loginid.name,
                updatedDate=date,
                receivedBy='Rama Krishna sir',
                createdOn=date,
                status=1
            ).save()

            # Update unassigned other_systemss
            other_systemsdata.objects(name='').update(othersystemStatus="Unassigned")

        except NotUniqueError as e:
            # Handle unique constraint violations
            message = f"Error saving data: {str(e)}"
            return templates.TemplateResponse('other_systems_dashboard.html', {'request': request, 'message': message})

        except Exception as e:
            # General exception handling
            message = f"Unexpected error: {str(e)}"
            return templates.TemplateResponse('other_systems_dashboard.html', {'request': request, 'message': message})

        # Fetch data for the dashboard
        total_systems = other_systemsdata.objects(status=1)
        assign_data = other_systemsdata.objects(othersystemStatus="Assigned",status=1)
        issue_data = other_systemsdata.objects(othersystemStatus="Issue",status=1)
        unassign_data = other_systemsdata.objects(othersystemStatus="Unassigned",status=1)

        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': total_systems,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        }

        return templates.TemplateResponse('other_systems_dashboard.html', content)
    except Exception as e:
        message="exception occure.."
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})



@other_systems.get("/other_systems_assign_systems", response_class=HTMLResponse)
async def other_systems_assign_systems(request: Request):
    try:

        total_systems = other_systemsdata.objects(status=1)
        assign_data = other_systemsdata.objects(othersystemStatus="Assigned",status=1)
        issue_data = other_systemsdata.objects(othersystemStatus="Issue",status=1)
        unassign_data = other_systemsdata.objects(othersystemStatus="Unassigned",status=1)


        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': assign_data,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        }
        return templates.TemplateResponse('other_systems_dashboard.html', content)
    except Exception as e:
        message="exception occure.."
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})






@other_systems.get("/other_systems_issue_systems", response_class=HTMLResponse)
async def other_systems_issue_systems(request: Request):
    try:
        total_systems = other_systemsdata.objects(status=1)
        assign_data = other_systemsdata.objects(othersystemStatus="Assigned",status=1)
        issue_data = other_systemsdata.objects(othersystemStatus="Issue",status=1)
        unassign_data = other_systemsdata.objects(othersystemStatus="Unassigned",status=1)

    
        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': issue_data,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        }
        return templates.TemplateResponse('other_systems_dashboard.html', content)
    except Exception as e:
        message="exception occure.."
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})







@other_systems.get("/other_systems_unassign_systems", response_class=HTMLResponse)
async def other_systems_unassign_systems(request: Request):
    try:
        total_systems = other_systemsdata.objects(status=1)
        assign_data = other_systemsdata.objects(othersystemStatus="Assigned",status=1)
        issue_data = other_systemsdata.objects(othersystemStatus="Issue",status=1)
        unassign_data = other_systemsdata.objects(othersystemStatus="Unassigned",status=1)


        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': unassign_data,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        }
        return templates.TemplateResponse('other_systems_dashboard.html', content)
    except Exception as e:
        message="exception occure.."
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})






@other_systems.get("/other_systems_total_systems", response_class=HTMLResponse)
async def other_systems_total_systems(request: Request):
    try:
        total_systems = other_systemsdata.objects(status=1)
        assign_data = other_systemsdata.objects(othersystemStatus="Assigned",status=1)
        issue_data = other_systemsdata.objects(othersystemStatus="Issue",status=1)
        unassign_data = other_systemsdata.objects(othersystemStatus="Unassigned",status=1)

        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': total_systems,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        }
        return templates.TemplateResponse('other_systems_dashboard.html', content)
    except Exception as e:
        message="exception occure.."
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})



# other_systems edit delete and issue data 








@other_systems.post('/other_systems_edit_data/{data_id}', response_class=HTMLResponse)
async def handle_other_systems_systems(data_id,request: Request): 
    try:
        form_data = await request.form()
        other_systemsid = form_data.get('other_systemsid').upper()
        deviceid = form_data.get('deviceid').upper()
        productid = form_data.get('productid').upper()
        name = form_data.get('name').upper()
        manufacturer = form_data.get('manufacturer')
        model = form_data.get('model')
        configuration = form_data.get('configuration')
        date = datetime.now()
        otherstatus = form_data.get('status')
        required_fields=[other_systemsid,deviceid,productid,manufacturer,model,configuration,otherstatus]
        if(not all(required_fields)):
            message="Please enter valid fields.."
            return templates.TemplateResponse('other_systems_dashboard.html', {'request': request, 'message': message})
        data=other_systemsdata.objects(id=data_id).first()
        if data:
            receive=other_systemsdata.objects(id=data_id).first()
            users=Logfiles_data.objects.order_by("-id")[0]

            HistoryField(
            otherSystemsdataid=data_id,
            laptopid=other_systemsid,
            name=name,
            action="Edit",
            admin=users.loginid.name,
            updatedDate=date,
            receivedBy='Rama Krishna sir',
            createdOn=receive.createdOn,
            status=1
            ).save()
            data.update(
                otherSystemsid=other_systemsid,
                deviceid=deviceid,
                productid=productid,
                name=name,
                manufacturer=manufacturer,
                model=model,
                configuration=configuration,
                othersystemStatus=otherstatus,
                status=1
            )
            

        name_empty=other_systemsdata.objects(name='')
        if name_empty:
            name_empty.update(othersystemStatus="Unassigned")
        print(other_systemsid,deviceid)
        data1=other_systemsissue_data.objects(deviceId=other_systemsid,productid=deviceid,status=1)
        print(data1)
        if data1:
            data.update(othersystemStatus="Issue")


    
        total_systems = other_systemsdata.objects(status=1)
        assign_data = other_systemsdata.objects(othersystemStatus="Assigned",status=1)
        issue_data = other_systemsdata.objects(othersystemStatus="Issue",status=1)
        unassign_data = other_systemsdata.objects(othersystemStatus="Unassigned",status=1)

        content = {
            'request': request,
            'total_systems': len(total_systems),
            'assign_data': len(assign_data),
            'data': total_systems,
            'issue_data': len(issue_data),
            'unassign_data': len(unassign_data)
        }
        return templates.TemplateResponse('other_systems_dashboard.html', content)
    except Exception as e:
        message=f"exception occure..{e}"
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})



#issue data 
def pagenation_data(request):
    users=other_systemsissue_data.objects(status=1)

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
    return pagenation_data(request)

@other_systems.post('/other_systems_issue/{data_id}')
async def issue_data(data_id,request:Request):
    try:
        form_data = await request.form()
        other_systemsid = form_data.get('other_systemsid').upper()
        productid=form_data.get('deviceid').upper()
        name = form_data.get('name').upper()
        issue = form_data.get('issue')
        date =datetime.now()
        othersystemStatus = form_data.get('status')
        required_fields=[other_systemsid,productid,name,issue,othersystemStatus]
        if(not all(required_fields)):
            message="Please enter valid fields.."
            return templates.TemplateResponse('other_systems_dashboard.html', {'request': request, 'message': message})
        data=other_systemsissue_data.objects(deviceId=other_systemsid,productid=productid,status=1)
        if data:
            message="already this System is present in issue data..."
            return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})

        receive=other_systemsdata.objects(id=data_id).first()
        users=Logfiles_data.objects.order_by("-id")[0]

        HistoryField(
            otherSystemsdataid=data_id,
            laptopid=other_systemsid,
            name=name,
            action="Issue",
            admin=users.loginid.name,
            updatedDate=date,
            receivedBy='Rama Krishna sir',
            createdOn=receive.createdOn,
            status=1
        ).save()
        other_systemsissue_data(deviceId=other_systemsid,
                otherSystemsdataid=data_id,
                name=name,
                productid=productid,
                issue=issue,
                createdOn=date,
                othersystemStatus=othersystemStatus,
                status=1).save()
        
        
        data=other_systemsdata.objects(id=data_id).first()
        if data:
            data.update(othersystemStatus="Issue")


        total_systems = other_systemsdata.objects(status=1)
        assign_data = other_systemsdata.objects(othersystemStatus="Assigned",status=1)
        issue_data = other_systemsdata.objects(othersystemStatus="Issue",status=1)
        unassign_data = other_systemsdata.objects(othersystemStatus="Unassigned",status=1)

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
        message=f"exception occure..{e}"
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})



@other_systems.get('/other_systems_delete_issue/{data_id}')
async def delete_issue(data_id: str, request: Request):
    try:
        first = other_systemsissue_data.objects(id=data_id).first()
        if first:
            other_systemsdata_data = first.otherSystemsdataid 
            users=Logfiles_data.objects.order_by("-id")[0]

            HistoryField(
            otherSystemsdataid=data_id,
            laptopid=first.deviceId,
            name=first.name,
            action="Delete",
            admin=users.loginid.name,
            updatedDate=first.createdOn,
            receivedBy='Rama Krishna sir',
            createdOn=other_systemsdata_data.createdOn,
            status=1
            ).save()
            if other_systemsdata_data:
                other_systemsdata_data.update(status=2)
        
        other_systemsissue_data.objects(id=data_id).update(status=2)

        return pagenation_data(request)
    except Exception as e:
        message=f"exception occure..{e}"
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})




@other_systems.post('/other_systems_update_laptop_issue_data/{data_id}')
async def other_systems_update_laptop_issue_data(data_id,request:Request):
    try:
        form_data = await request.form()
        other_systemsid = form_data.get('other_systemsid').upper()
        deviceid = form_data.get('deviceid').upper()
        productid = form_data.get('productid').upper()
        name = form_data.get('name').upper()
        manufacturer = form_data.get('manufacturer')
        model = form_data.get('model')
        configuration = form_data.get('configuration')
        date = datetime.now()
        othersystemStatus = form_data.get('status')
        required_fields=[other_systemsid,deviceid,productid,manufacturer,model,configuration,othersystemStatus ]
        if(not all(required_fields)):
            message="Please enter valid fields.."
            return templates.TemplateResponse('other_systems_issues.html', {'request': request, 'message': message})
        update_data=other_systemsissue_data.objects(status=1) .first()
        print(update_data)
        # update_data=other_systemsissue_data.objects(id=ObjectId(data_id)) .first()
        if update_data:
            managedata=update_data.otherSystemsdataid
            if managedata and othersystemStatus  != "Issue":
                users=Logfiles_data.objects.order_by("-id")[0]

                HistoryField(
                    otherSystemsdataid=data_id,
                    laptopid=other_systemsid,
                    name=name,
                    action="Updated issue data",
                    admin=users.loginid.name,
                    updatedDate=date,
                    receivedBy='Rama Krishna sir',
                    createdOn=managedata.createdOn,
                    status=1
                ).save()
                managedata.update(othersystemStatus=othersystemStatus ,otherSystemsid=other_systemsid,deviceid=deviceid,productid=productid,name=name,manufacturer=manufacturer,model=model,configuration=configuration)
                
                update_data.update(status=2)
        return pagenation_data(request)
    except Exception as e:
        message=f"exception occure..{e}"
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})









# other_systems filters




@other_systems.get('/other_systems_other_systemsid')
async def other_systems_loginid(request:Request):
    try:
        form_data=request.query_params
        loginid=form_data.get('search_element').upper()
        total_systems=other_systemsdata.objects(otherSystemsid__icontains=loginid,status=1)
        assign_data=other_systemsdata.objects(othersystemStatus="Assigned",otherSystemsid__icontains=loginid,status=1)
        issue_data=other_systemsdata.objects(othersystemStatus="Issue",otherSystemsid__icontains=loginid,status=1)
        unassign_data=other_systemsdata.objects(othersystemStatus="Unassigned",otherSystemsid__icontains=loginid,status=1)
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
    except Exception as e:
        message=f"exception occure..{e}"
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})



@other_systems.get('/other_systems_name_filter')
async def other_systems_name_filter(request:Request):
    try:
        form_data=request.query_params
        loginid=form_data.get('search_element').upper()
        total_systems=other_systemsdata.objects(name__icontains=loginid,status=1)
        assign_data=other_systemsdata.objects(othersystemStatus="Assigned",name__icontains=loginid,status=1)
        issue_data=other_systemsdata.objects(othersystemStatus="Issue",name__icontains=loginid,status=1)
        unassign_data=other_systemsdata.objects(othersystemStatus="Unassigned",name__icontains=loginid,status=1)
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
    except Exception as e:
        message=f"exception occure..{e}"
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})




# pagenation data



@other_systems.get('/pagination_other_systems_issue/{page_num}',response_class=HTMLResponse)
async def pagination(page_num:int,request:Request):
    try:
        user=other_systemsissue_data.objects(status=1)
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
    except Exception as e:
        message="exception occure.."
        return templates.TemplateResponse('other_systems_dashboard.html',{'request':request,'message':message})
