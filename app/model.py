from pydantic import BaseModel, Field

class Login(BaseModel):
    username : str = Field(..., example="admin@example.com")
    password : str = Field(..., example="admin")
    
class LoginArter(BaseModel):
    username : str
    password : str
    type : str
    
class UserList(BaseModel):
    username : str
    type : str

class Profile(BaseModel):
    username: str = Field(..., example="user@example.com")
    password: str = Field(..., example="user")
    type : str = Field(..., example='1')
    first_name : str = Field(..., example="first name")
    last_name : str = Field(..., example="last name")
    date_of_birth : str = Field(..., example="2000-12-31")
    address : str = Field(..., example="123 m.4")
    sub_district : str = Field(..., example="Rat Burana")
    district : str = Field(..., example="Rat Burana")
    province : str = Field(..., example="Bangkok")
    postcode : str = Field(..., example="10140")
    height : str = Field(..., example="170")
    weight : str = Field(..., example="60")
    pressure : str = Field(..., example="90")
    
class ProfileAdmin(BaseModel):
    username: str = Field(..., example="admin@example.com")
    password: str = Field(..., example="admin")
    type : str = Field(..., example='0')
    first_name : str = Field(..., example="first name")
    last_name : str = Field(..., example="last name")
    date_of_birth : str = Field(..., example="2000-12-31")
    address : str = Field(..., example="123 m.4")
    sub_district : str = Field(..., example="Rat Burana")
    district : str = Field(..., example="Rat Burana")
    province : str = Field(..., example="Bangkok")
    postcode : str = Field(..., example="10140")
    height : str = Field(..., example="170")
    weight : str = Field(..., example="60")
    pressure : str = Field(..., example="90")

class ProfileGet(BaseModel):
    id : int
    username: str = Field(..., example="admin@example.com")
    first_name : str = Field(..., example="first name")
    last_name : str = Field(..., example="last name")
    date_of_birth : str = Field(..., example="2000-12-31")
    address : str = Field(..., example="123 m.4")
    sub_district : str = Field(..., example="Rat Burana")
    district : str = Field(..., example="Rat Burana")
    province : str = Field(..., example="Bangkok")
    postcode : str = Field(..., example="10140")
    height : str = Field(..., example="170")
    weight : str = Field(..., example="60")
    pressure : str = Field(..., example="90")

class ProfileUpdate(BaseModel):
    id : int
    first_name : str = Field(..., example="first name")
    last_name : str = Field(..., example="last name")
    address : str = Field(..., example="123 m.4")
    sub_district : str = Field(..., example="Rat Burana")
    district : str = Field(..., example="Rat Burana")
    province : str = Field(..., example="Bangkok")
    postcode : str = Field(..., example="10140")
    height : str = Field(..., example="170")
    weight : str = Field(..., example="60")
    pressure : str = Field(..., example="90")

class ProfileDelete(BaseModel):
    id : int

class Dashboard(BaseModel):
    id : int
    username: str
    first_name : str
    last_name : str
    date_of_birth : str
    address : str
    sub_district : str
    district : str
    province : str
    postcode : str
    height : str
    weight : str
    pressure : str
