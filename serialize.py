from fastapi import FastAPI, Request, Response, Depends
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import RedirectResponse

from pydantic import BaseModel

app = FastAPI()
"""
When you return data from a FastAPI endpoint, 
it automatically serializes (converts) the Python object into JSON using jsonable_encoder under the hood.
----------------------------------------------------------
Python Type  -->    JSON Equivalent   --> jsonable_encoder
----------------------------------------------------------
dict         -->    object  {"name": "Avinash"} → {"name": "Avinash"}
list         -->    array   ["apple", "banana"] → ["apple", "banana"]
tuple        -->    array   ("a", "b") → ["a", "b"]
set          -->    array   {"a", "b"} → ["a", "b"]
str          -->    string  "Avinash" → "Avinash"
int, float   -->    number  42 → 42
bool         -->    boolean True → true, False → false
None         -->    null    None → null

Pydantic models are automatically JSON-serializable — FastAPI calls .model_dump()
Pydantic Model / dataclass  -->   object  User(name="Avinash") → {"name": "Avinash"}
Custom Class (non-Pydantic) -->   Not JSON serializable  --> You must convert it manually (e.g. return my_obj.__dict__)
datetime, date, time        -->   string (ISO format)    --> datetime(2025, 10, 27) → "2025-10-27T00:00:00"
Decimal, UUID               -->   string or number (depending) --> Decimal("2.5") → 2.5, UUID("...") → "..."


response.text	 -->  str	-->   Raw response body as a string
response.json()	 -->  dict, list, int, float, bool, or None  --> Parsed JSON converted to Python type
"""

# Defining a Pydantic model
class AvinashModel(BaseModel):
    name: str

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return RedirectResponse(url="/")
    return RedirectResponse(url=f"/error/{exc.status_code}")

@app.get("/")
def welcome():
    return "Welcome to API Development"

# 1) Integer Data
@app.get("/intdata")
def intdata():
    return 100

# 2) float Data
@app.get("/floatdata")
def floatdata():
    return 2.3

# 3) String Data
@app.get("/stringdata")
def stringdata():
    return "Avinash in string data"

# 4) Bool Data -  also sending as list
# Python value True , False  --> JSON output  true, false
@app.get("/booldata")
def booldata():
    return True

# 5) List Data
@app.get("/listdata")
def listdata():
    return ['avinash_in_list', 33]

# 6) tuple Data -  also sending as list
@app.get("/tupledata")
def tupledata():
    return ('avinash in tuple', 33)

# 7) Set Data -  also sending as list
@app.get("/setdata")
def setdata():
    return {'avinash in set data', 33}

# 8) Dict Data
@app.get("/dictdata")
def dictdata():
    return {'name': 'avinash', 'age': 33}

# 9) Nonetype Data  --> returning Null
# Python value None  --> JSON output null
@app.get("/nonedata")
def nonedata():
    return None

# 10) Returns nothing
@app.get("/returnnothing")
def returnnothing():
    return Response(status_code=204)

# 11) pydantic modeldata
# Creating a dependency function
def get_data(name: str) -> AvinashModel:
    return AvinashModel(name=name)

# calling with querry params http://127.0.0.1:8000/modeldata?name=Avinash
@app.get("/modeldata")
def modeldata(data: AvinashModel = Depends(get_data)):
    return data









