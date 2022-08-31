from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
# import jwt

from typing import List
from passlib.context import CryptContext

from app.db import database, users
import app.model as model

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECERT_KEY = "YOUR_FAST_API_SECRET_KEY"
ALGORITHM ="HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 800

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# ! Users
@app.get("/api/user", response_model=List[model.UserList], tags=["Users"])
async def find_all_users():
    query = users.select().where(users.c.type == '1')
    return await database.fetch_all(query)


# ! Login
# login
@app.post("/api/login/", tags=["Login"])
async def get_login(user: model.Login):
    
    
    query = users.select().where(users.c.username == user.username).limit(1)
    data = await database.fetch_all(query)
    
    data_id = data[0].id
    data_username = data[0].username
    data_password = data[0].password
    data_type = data[0].type
    
    if (pwd_context.verify(user.password, data_password)):
        return { 
                'message' : {
                    'id' : data_id,
                    'username' : data_username,
                    }
                }
    else:
        return {
                'message' : {
                    'username' : "login failed",
                    'type' : '-1'
                    }
                }


# ! Register
@app.post("/api/register/", tags=["Register"])
async def get_register(profile: model.Profile):
    query = users.insert().values(
        username        = profile.username,
        password        = pwd_context.hash(profile.password),
        type            = profile.type,
        first_name      = profile.first_name,
        last_name       = profile.last_name,
        date_of_birth   = profile.date_of_birth,
        address         = profile.address,
        sub_district    = profile.sub_district,
        district        = profile.district,
        province        = profile.province,
        postcode        = profile.postcode,
        height          = profile.height,
        weight          = profile.weight,
        pressure        = profile.pressure,
    ) 

    await database.execute(query)
    
    return { profile.type }


# ! Dashboard
@app.get("/api/dashboard/", tags=["Dashboard"], response_model=List[model.Dashboard])
async def get_dashboard():
    query = users.select().where(users.c.type == '1')
    return await database.fetch_all(query)


# ! Profile
@app.get("/api/profile/{userId}", tags=["Profile"], response_model=List[model.ProfileGet])
async def get_profile(userId: int):
    query = users.select().where(users.c.id == userId)
    return await database.fetch_all(query)

@app.put("/api/profile/", tags=["Profile"], response_model=List[model.ProfileGet])
async def update_profile(user: model.ProfileUpdate):
    query = users.update().\
        where(users.c.id == user.id).\
        values(
            first_name = user.first_name,
            last_name  = user.last_name,
            address = user.address,
            sub_district = user.sub_district,
            district = user.district,
            province = user.province,
            postcode = user.postcode,
            height = user.height,
            weight = user.weight,
            pressure = user.pressure
        )
    await database.execute(query)

    return await get_profile(user.id)

@app.delete("/api/profile/{userId}/", tags=["Profile"])
async def delete_profile(userId):
    
    query = users.delete().where(users.c.id == int(userId))
    await database.execute(query)
    
    return {
        "status" : True,
        "message": "This user has been deleted successfully." 
    }
    
    
# ! Admin
@app.get("/api/register-admin/", tags=["Admin"])
async def get_register_admin(user: model.Login):
    query = users.insert().values(
        username        = user.username,
        password        = pwd_context.hash(user.password),
        type            = "0",
        first_name      = "admin",
        last_name       = "admin",
        date_of_birth   = "1990-12-31",
        address         = "123 m.4",
        sub_district    = "Rat Burana",
        district        = "Rat Burana",
        province        = "Bangkok",
        postcode        = "10140",
        height          = "170",
        weight          = "60",
        pressure        = "95",
    ) 

    await database.execute(query)
    
    return { 
        "username" : "admin@example.com",
        "password" : "admin"
    }



@app.get("/init/register-admin/", tags=["Admin"])
async def get_register_admin():
    query = users.insert().values(
        username        = "admin@example.com",
        password        = pwd_context.hash("admin"),
        type            = "0",
        first_name      = "admin",
        last_name       = "admin",
        date_of_birth   = "1990-12-31",
        address         = "123 m.4",
        sub_district    = "Rat Burana",
        district        = "Rat Burana",
        province        = "Bangkok",
        postcode        = "10140",
        height          = "170",
        weight          = "60",
        pressure        = "95",
    ) 

    await database.execute(query)
    
    return { 
        "username" : "admin@example.com",
        "password" : "admin"
    }