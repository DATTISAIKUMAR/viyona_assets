from mongoengine import *
 
 
connect('dashboard',host="mongodb+srv://dattisai02:Dkumar02@cluster0.efrhv.mongodb.net/",ssl=True)
 
 
 
 
class Signup(Document):
    name=StringField()
    email=StringField()
    password=StringField()
    role=StringField()
    reason=StringField()
    status=IntField()
    createdOn=DateTimeField()
 
 
 
class Managedata(Document):
    laptopid=StringField()
    name=StringField()
    serial_no=StringField()
    product=StringField()
    configuration=StringField()
    received_by=StringField(default=None)
    createdOn=DateTimeField()
    status=IntField()
    laptopStatus=StringField()
 
 
 
class Issue_data(Document):
    managedataId=ReferenceField(Managedata)
    laptopid=StringField()
    name=StringField()
    serial_no=StringField()
    issue=StringField()
    createdOn=DateTimeField()
    status=IntField()
    laptopStatus=StringField()
 
 
 
   
class other_systemsdata(Document):
    other_systemsid=StringField()
    deviceid=StringField()
    productid=StringField()
    manufacturer=StringField()
    name=StringField()
    model=StringField()
    configuration=StringField()
    date=StringField(default=None)
    status=StringField()
 
class other_systemsissue_data(Document):
    other_systemsdataid=ReferenceField(other_systemsdata)
    deviceId = StringField()
    productid=StringField()
    name=StringField()
    issue=StringField()
    date=StringField()
    status=StringField()
 
 
 
 
 
class Logfiles_data(Document):
    loginid=ReferenceField(Signup)
    createdOn=StringField()
    status=IntField()
 
 
class Super_admin(Document):
    email=StringField()
    password=StringField()
    status=IntField()
 
 
 
 
class Desktopdata(Document):
    desktopid=StringField()
    deviceid=StringField()
    productid=StringField()
    manufacturer=StringField()
    model=StringField()
    configuration=StringField()
    name=StringField()
    date=StringField()
    status=StringField()
 
 
class Desktopissue_data(Document):
    desktopdataid=ReferenceField(Desktopdata)
    desktopid=StringField()
    productid=StringField()
    name=StringField()
    issue=StringField()
    date=StringField(default=None)
    status=StringField()
 
 
 
class HistoryField(Document):
    desktopdataid=ReferenceField(Desktopdata)
    laptopdataid=ReferenceField(Managedata)
    other_systemsdataid=ReferenceField(other_systemsdata)
    desktopid=StringField()
    laptopid=StringField()
    name=StringField()
    admin=StringField()
    action=StringField()
    updated_date=StringField()
    createdOn=DateTimeField()
    received_by=StringField()
 
   
 