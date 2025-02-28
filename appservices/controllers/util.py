from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from math import ceil
from datetime import datetime
from time import time
from superAdmin.models import *
from mongoengine.errors import NotUniqueError
from bson import ObjectId
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from math import ceil
from bson import ObjectId
from datetime import datetime
from time import time
from mongoengine.errors import NotUniqueError
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from math import ceil
from bson import ObjectId
from datetime import datetime
from time import time
from mongoengine.errors import NotUniqueError


templates = Jinja2Templates(directory="templates")