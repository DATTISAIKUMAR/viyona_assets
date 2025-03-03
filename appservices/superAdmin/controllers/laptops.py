from controllers.util import *
 
laptops = APIRouter()
 
 
@laptops.get("/")
async def read_dashboard(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
 
 
@laptops.get("/dashboard", response_class=HTMLResponse)
async def add_systems(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
 
 
@laptops.get("/add_systems", response_class=HTMLResponse)
async def add_systems(request: Request):
    return templates.TemplateResponse("manage.html", {"request": request})
 
 
@laptops.post("/add_systems", response_class=HTMLResponse)
async def handle_add_systems(request: Request):
    try:
        form_data = await request.form()
        laptopid = form_data.get("laptopid").upper()
        name = form_data.get("name").upper()
        serialNo = form_data.get("serialNo")
        product = form_data.get("product")
        configuration = form_data.get("configuration")
        receiver = form_data.get("receiver")
        createdOn = datetime.now()
        laptopStatus = form_data.get("status")
 
        data = Managedata.objects(laptopid=laptopid, status=1)
        data1 = Managedata.objects(serialNo=serialNo, status=1)
        required_fields = [
            laptopid,
            serialNo,
            product,
            configuration,
            receiver,
            laptopStatus,
        ]
 
        if data:
            message = "laptopid already exits..."
            return templates.TemplateResponse(
                "dashboard.html", {"request": request, "message": message}
            )
        if data1:
            message = "serial number already exits..."
            return templates.TemplateResponse(
                "dashboard.html", {"request": request, "message": message}
            )
        if all(required_fields):
            laptopAddData = Managedata(
                laptopid=laptopid,
                name=name,
                serialNo=serialNo,
                product=product,
                configuration=configuration,
                receivedBy=receiver,
                createdOn=createdOn,
                status=1,
                laptopStatus=laptopStatus,
            ).save()
            users = Logfiles_data.objects(status=1).order_by("-id")[0]
 
            historyAddData = HistoryField(
                laptopdataid=laptopAddData.id,
                laptopid=laptopid,
                name=name,
                action="Create",
                admin=users.loginid.name,
                updatedDate=createdOn,
                receivedBy=receiver,
                createdOn=datetime.now(),
                status=1,
            ).save()
 
            name_empty = Managedata.objects(name="")
            if name_empty:
                name_empty.update(laptopStatus="Unassigned")
 
            total_systems = Managedata.objects(status=1)
            assign_data = Managedata.objects(laptopStatus="Assigned", status=1)
            issue_data = Managedata.objects(laptopStatus="Issue", status=1)
            unassign_data = Managedata.objects(laptopStatus="Unassigned", status=1)
 
            content = {
                "request": request,
                "total_systems": len(total_systems),
                "assign_data": len(assign_data),
                "data": total_systems,
                "issue_data": len(issue_data),
                "unassign_data": len(unassign_data),
            }
            return templates.TemplateResponse("dashboard.html", content)
        else:
            message = "Please enter valid fields.."
            return templates.TemplateResponse(
                "dashboard.html", {"request": request, "message": message}
            )
    except Exception as e:
        message = f"exception has occured.. {e}"
        return templates.TemplateResponse(
            "dashboard.html", {"request": request, "message": message}
        )
 
 
# assigned laptops
@laptops.get("/assign_systems", response_class=HTMLResponse)
async def assign_systems(request: Request):
    try:
        total_systems = Managedata.objects(status=1)
        assign_data = Managedata.objects(laptopStatus="Assigned", status=1)
        issue_data = Managedata.objects(laptopStatus="Issue", status=1)
        unassign_data = Managedata.objects(laptopStatus="Unassigned", status=1)
 
        content = {
            "request": request,
            "total_systems": len(total_systems),
            "assign_data": len(assign_data),
            "data": assign_data,
            "issue_data": len(issue_data),
            "unassign_data": len(unassign_data),
        }
        return templates.TemplateResponse("dashboard.html", content)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "dashboard.html", {"request": request, "message": message}
        )
 
 
# laptop with issue
@laptops.get("/issue_systems", response_class=HTMLResponse)
async def issue_systems(request: Request):
    try:
        total_systems = Managedata.objects(status=1)
        assign_data = Managedata.objects(laptopStatus="Assigned", status=1)
        issue_data = Managedata.objects(laptopStatus="Issue", status=1)
        unassign_data = Managedata.objects(laptopStatus="Unassigned", status=1)
 
        content = {
            "request": request,
            "total_systems": len(total_systems),
            "assign_data": len(assign_data),
            "data": issue_data,
            "issue_data": len(issue_data),
            "unassign_data": len(unassign_data),
        }
        return templates.TemplateResponse("dashboard.html", content)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "dashboard.html", {"request": request, "message": message}
        )
 
 
# unassigned laptops
@laptops.get("/unassign_systems", response_class=HTMLResponse)
async def unassign_systems(request: Request):
    try:
        total_systems = Managedata.objects(status=1)
        assign_data = Managedata.objects(laptopStatus="Assigned", status=1)
        issue_data = Managedata.objects(laptopStatus="Issue", status=1)
        unassign_data = Managedata.objects(laptopStatus="Unassigned", status=1)
 
        content = {
            "request": request,
            "total_systems": len(total_systems),
            "assign_data": len(assign_data),
            "data": unassign_data,
            "issue_data": len(issue_data),
            "unassign_data": len(unassign_data),
        }
        return templates.TemplateResponse("dashboard.html", content)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "dashboard.html", {"request": request, "message": message}
        )
 
 
# display all in laptops
@laptops.get("/total_systems", response_class=HTMLResponse)
async def total_systems(request: Request):
    try:
        total_systems = Managedata.objects(status=1)
        assign_data = Managedata.objects(laptopStatus="Assigned",status=1 )
        issue_data = Managedata.objects(laptopStatus="Issue", status=1)
        unassign_data = Managedata.objects(laptopStatus="Unassigned", status=1)
 
        content = {
            "request": request,
            "total_systems": len(total_systems),
            "assign_data": len(assign_data),
            "data": total_systems,
            "issue_data": len(issue_data),
            "unassign_data": len(unassign_data),
        }
        return templates.TemplateResponse("dashboard.html", content)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "dashboard.html", {"request": request, "message": message}
        )
 
 
# searchAPI in laptop
@laptops.get("/laptopid")
async def laptopid_Search(request: Request):
    try:
        form_data = request.query_params
        loginid = form_data.get("search_element").upper()
        total_systems = Managedata.objects(laptopid__icontains=loginid, status=1)
        assign_data = Managedata.objects(
            laptopStatus="Assigned", laptopid__icontains=loginid, status=1
        )
        issue_data = Managedata.objects(
            laptopStatus="Issue", laptopid__icontains=loginid, status=1
        )
        unassign_data = Managedata.objects(
            laptopStatus="Unassigned", laptopid__icontains=loginid, status=1
        )
        content = {
            "request": request,
            "total_systems": len(total_systems),
            "assign_data": len(assign_data),
            "data": total_systems,
            "issue_data": len(issue_data),
            "unassign_data": len(unassign_data),
            "search_element": loginid,
        }
        return templates.TemplateResponse("dashboard.html", content)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "dashboard.html", {"request": request, "message": message}
        )
 
 
# filter using employee name
@laptops.get("/name_filter")
async def name_filter(request: Request):
    try:
 
        form_data = request.query_params
        loginid = form_data.get("search_element").upper()
        total_systems = Managedata.objects(name__icontains=loginid, status=1)
        assign_data = Managedata.objects(
            laptopStatus="Assigned", name__icontains=loginid, status=1
        )
        issue_data = Managedata.objects(laptopStatus="Issue", name__icontains=loginid, status=1)
        unassign_data = Managedata.objects(
            laptopStatus="Unassigned", name__icontains=loginid, status=1
        )
        content = {
            "request": request,
            "total_systems": len(total_systems),
            "assign_data": len(assign_data),
            "data": total_systems,
            "issue_data": len(issue_data),
            "unassign_data": len(unassign_data),
            "search_element1": loginid,
        }
        return templates.TemplateResponse("dashboard.html", content)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "dashboard.html", {"request": request, "message": message}
        )
 
 
# history filter
def history_function(request):
    try:
        users = HistoryField.objects(status=1).order_by("-id")
        page = 1
        per_page = 10
        start = (page - 1) * per_page
        end = start + per_page
        total_pages = ceil(len(users) / per_page)
        paginated_data = users[start:end]
        content = {
            "start": start,
            "total_pages": total_pages,
            "request": request,
            "data": paginated_data,
        }
        return templates.TemplateResponse("history.html", content)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "history.html", {"request": request, "message": message}
        )
 
 
@laptops.get("/history")
async def history(request: Request):
    return history_function(request)
 
 
@laptops.get("/history_laptopid")
async def history_laptopid(request: Request):
    try:
        form_data = request.query_params
        loginid = form_data.get("search_element").upper()
        data = HistoryField.objects(laptopid__icontains=loginid, status=1)
        content = {"request": request, "data": data}
        return templates.TemplateResponse("history.html", content)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "history.html", {"request": request, "message": message}
        )
 
 
@laptops.get("/history_name_filter")
async def name_filter(request: Request):
    try:
        form_data = request.query_params
        loginid = form_data.get("search_element").upper()
        data = HistoryField.objects(name__icontains=loginid, status=1)
        content = {"request": request, "data": data}
        return templates.TemplateResponse("history.html", content)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "history.html", {"request": request, "message": message}
        )
 
 
@laptops.get("/pagination1/{page_num}", response_class=HTMLResponse)
async def pagination(page_num: int, request: Request):
    try:
        user = HistoryField.objects(status=1)
        page = page_num
        per_page = 10
        start = (page - 1) * per_page
        end = start + per_page
        total_pages = ceil(len(user) / per_page)
        paginated_data = user[start:end]
        content = {
            "start": start,
            "total_pages": total_pages,
            "request": request,
            "data": paginated_data,
        }
        return templates.TemplateResponse("history.html", content)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "history.html", {"request": request, "message": message}
        )
 
 
def response_issue(request):
    try:
        users = Issue_data.objects(status=1)
        page = 1
        per_page = 5
        start = (page - 1) * per_page
        end = start + per_page
        total_pages = ceil(len(users) / per_page)
        paginated_data = users[start:end]
        content = {
            "start": start,
            "total_pages": total_pages,
            "request": request,
            "data": paginated_data,
        }
        return templates.TemplateResponse("report_issue.html", content)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "report_issue.html", {"request": request, "message": message}
        )
 
 
@laptops.post("/edit_data/{data_id}", response_class=HTMLResponse)
async def handle_edit_systems(data_id, request: Request):
    try:
        form_data = await request.form()
        laptopid = form_data.get("laptopid").upper()
        name = form_data.get("name").upper()
        serialNo = form_data.get("serialNo")
        product = form_data.get("product")
        configuration = form_data.get("configuration")
        createdOn = datetime.now()
        laptopStatus = form_data.get("status")
        data = Managedata.objects(id=data_id, status=1).first()
        required_fields = [
            laptopid,
            serialNo,
            product,
            configuration,
            createdOn,
            laptopStatus,
        ]
        if data:
            if not all(required_fields):
                message = "Please enter valid fields.."
                return templates.TemplateResponse(
                    "dashboard.html", {"request": request, "message": message}
                )
            receive = Managedata.objects(id=data_id, status=1).first()
            users = Logfiles_data.objects(status=1).order_by("-id")[0]
            HistoryField(
                laptopdataid=data_id,
                laptopid=laptopid,
                name=name,
                action="Edit",
                admin=users.loginid.name,
                updatedDate=createdOn,
                receivedBy=receive.receivedBy,
                createdOn=receive.createdOn,
                status=1,
            ).save()
            data.update(
                laptopid=laptopid,
                name=name,
                serialNo=serialNo,
                product=product,
                configuration=configuration,
                laptopStatus=laptopStatus,
                status=1,
            )
 
        name_empty = Managedata.objects(name="")
        if name_empty:
            name_empty.update(laptopStatus="Unassigned")
        data1 = Issue_data.objects(laptopid=laptopid, serialNo=serialNo, status=1)
        if data1:
            data.update(laptopStatus="Issue")
 
        total_systems = Managedata.objects(status=1)
        assign_data = Managedata.objects(laptopStatus="Assigned", status=1)
        issue_data = Managedata.objects(laptopStatus="Issue", status=1)
        unassign_data = Managedata.objects(laptopStatus="Unassigned", status=1)
 
        content = {
            "request": request,
            "total_systems": len(total_systems),
            "assign_data": len(assign_data),
            "data": total_systems,
            "issue_data": len(issue_data),
            "unassign_data": len(unassign_data),
        }
        return templates.TemplateResponse("dashboard.html", content)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "dashboard.html", {"request": request, "message": message}
        )
 
 
@laptops.get("/issue")
async def report_page(request: Request):
    return response_issue(request)
 
 
@laptops.post("/issue/{data_id}")
async def issue_data(data_id, request: Request):
    try:
        form_data = await request.form()
        print(form_data, "---")
        laptopid = form_data.get("laptopid").upper()
        name = form_data.get("name").upper()
        serialNo = form_data.get("serialNo")
        issue = form_data.get("issue")
        createdOn = datetime.now()
        laptopStatus = form_data.get("status")
        required_fields = [laptopid, name, serialNo, issue, createdOn, laptopStatus]
        data = Issue_data.objects(laptopid=laptopid, serialNo=serialNo, status=1).first()
        if data:
            message = "already this System is present in issue data..."
            return templates.TemplateResponse(
                "dashboard.html", {"request": request, "message": message}
            )
        if not all(required_fields):
            message = "Please enter valid fields.."
            return templates.TemplateResponse(
                "dashboard.html", {"request": request, "message": message}
            )
 
        receive = Managedata.objects(id=data_id, status=1).first()
        users = Logfiles_data.objects(status=1).order_by("-id")[0]
 
        HistoryField(
            laptopdataid=data_id,
            laptopid=laptopid,
            name=name,
            action="Issue",
            admin=users.loginid.name,
            updatedDate=createdOn,
            receivedBy=receive.receivedBy,
            createdOn=receive.createdOn,
            status=1,
        ).save()
        Issue_data(
            laptopid=laptopid,
            managedataId=data_id,
            name=name,
            serialNo=serialNo,
            issue=issue,
            createdOn=createdOn,
            laptopStatus=laptopStatus,
            status=1,
        ).save()
 
        data = Managedata.objects(id=data_id, status=1).first()
        if data:
            data.update(laptopStatus="Issue")
 
        total_systems = Managedata.objects(status=1)
        assign_data = Managedata.objects(laptopStatus="Assigned", status=1)
        issue_data = Managedata.objects(laptopStatus="Issue", status=1)
        unassign_data = Managedata.objects(laptopStatus="Unassigned", status=1)
 
        content = {
            "request": request,
            "total_systems": len(total_systems),
            "assign_data": len(assign_data),
            "data": total_systems,
            "issue_data": len(issue_data),
            "unassign_data": len(unassign_data),
        }
        return templates.TemplateResponse("dashboard.html", content)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "dashboard.html", {"request": request, "message": message}
        )
 
 
@laptops.get("/delete_issue/{data_id}")
async def delete_issue(data_id: str, request: Request):
    try:
        first = Issue_data.objects(id=data_id, status=1).first()
        if first:
            managedata_data = first.managedataId
            users = Logfiles_data.objects(status=1).order_by("-id")[0]
 
            HistoryField(
                laptopdataid=data_id,
                laptopid=first.laptopid,
                name=first.name,
                action="Delete",
                admin=users.loginid.name,
                updatedDate=first.createdOn,
                receivedBy=managedata_data.receivedBy,
                createdOn=managedata_data.createdOn,
                status=1,
            ).save()
            if managedata_data:
                managedata_data.update(status=2)
 
        Issue_data.objects(id=data_id).update(status=2)
 
        return response_issue(request)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "dashboard.html", {"request": request, "message": message}
        )
 
 
@laptops.post("/update_laptop_issue_data/{data_id}")
async def update_laptop_issue_data(data_id, request: Request):
    try:
        form_data = await request.form()
        laptopid = form_data.get("laptopid").upper()
        name = form_data.get("name").upper()
        serialNo = form_data.get("serialNo")
        product = form_data.get("product")
        configuration = form_data.get("configuration")
        createdOn = datetime.now()
        laptopStatus = form_data.get("status")
        required_fields = [
            laptopid,
            name,
            serialNo,
            product,
            configuration,
            createdOn,
            laptopStatus,
        ]
        if not all(required_fields):
            message = "Please enter valid fields.."
            return templates.TemplateResponse(
                "report_issue.html", {"request": request, "message": message}
            )
        update_data = Issue_data.objects(id=data_id, status=1).first()
        if update_data:
            managedata = update_data.managedataId
            if managedata and laptopStatus != "Issue":
                users = Logfiles_data.objects(status=1).order_by("-id")[0]
 
                HistoryField(
                    laptopdataid=data_id,
                    laptopid=laptopid,
                    name=name,
                    action="Update issue data",
                    admin=users.loginid.name,
                    updatedDate=createdOn,
                    receivedBy=managedata.receivedBy,
                    createdOn=managedata.createdOn,
                    status=1,
                ).save()
                managedata.update(
                    laptopStatus=laptopStatus,
                    laptopid=laptopid,
                    name=name,
                    serialNo=serialNo,
                    product=product,
                    configuration=configuration,
                    status=1,
                )
 
                update_data.update(status=2)
        return response_issue(request)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "dashboard.html", {"request": request, "message": message}
        )
 
 
@laptops.get("/pagination_laptop_issue/{page_num}", response_class=HTMLResponse)
async def pagination(page_num: int, request: Request):
    try:
        user = Issue_data.objects(status=1)
        page = page_num
        per_page = 5
        start = (page - 1) * per_page
        end = start + per_page
        total_pages = ceil(len(user) / per_page)
        paginated_data = user[start:end]
        content = {
            "start": start,
            "total_pages": total_pages,
            "request": request,
            "data": paginated_data,
        }
        return templates.TemplateResponse("report_issue.html", content)
    except Exception as e:
        message = f"exception has occured..{e}"
        return templates.TemplateResponse(
            "dashboard.html", {"request": request, "message": message}
        )
 
 
 