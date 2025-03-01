from mongoengine import *
 
 
connect('viyonaAssets',host="mongodb+srv://dattisai02:Dkumar02@cluster0.efrhv.mongodb.net/",ssl=True)
 
 
 
 
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
    createdOn=DateTimeField()
    othersystemStatus=StringField()
    status=IntField()
 
class other_systemsissue_data(Document):
    other_systemsdataid=ReferenceField(other_systemsdata)
    deviceId = StringField()
    productid=StringField()
    name=StringField()
    issue=StringField()
    createdOn=DateTimeField()
    othersystemStatus=StringField()
    status=IntField()
 
 
 
 
 
class Logfiles_data(Document):
    loginid=ReferenceField("Signup")
    createdOn=DateTimeField()
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
    createdOn=DateTimeField()
    desktopstatus=StringField()
    status=IntField()
 
 
class Desktopissue_data(Document):
    desktopdataid=ReferenceField(Desktopdata)
    desktopid=StringField()
    productid=StringField()
    name=StringField()
    issue=StringField()
    createdOn=DateTimeField()
    desktopstatus=StringField()
    status=IntField()
 
 
 
class HistoryField(Document):
    desktopdataid=ReferenceField(Desktopdata)
    laptopdataid=ReferenceField(Managedata)
    other_systemsdataid=ReferenceField(other_systemsdata)
    desktopid=StringField()
    laptopid=StringField()
    name=StringField()
    admin=StringField()
    action=StringField()
    updatedDate=DateTimeField()
    createdOn=DateTimeField()
    receivedBy=StringField()
    status=IntField()
 
   
 