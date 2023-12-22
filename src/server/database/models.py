from pydantic import BaseModel
from typing import Optional


class ModifyBaseModel(BaseModel):
    id: Optional[int]


class Posts(ModifyBaseModel):
    title: str


class Departments(ModifyBaseModel):
    title: str


class Staff(ModifyBaseModel):
    FIO: str
    id_post: int
    id_department: int


class Roles(ModifyBaseModel):
    title: str


class Users(ModifyBaseModel):
    FIO: str
    login: str
    password: str


class Type_of_treatments(ModifyBaseModel):
    title: str


class Status_Requests(ModifyBaseModel):
    title: str


class Requests(ModifyBaseModel):
    add_data: str
    id_status_req: int
    id_user: int


class Type_of_diseases(ModifyBaseModel):
    title: str


class Diseases(ModifyBaseModel):
    title: str
    descriptions: Optional[str]
    id_type_of_disease: int


class Receptions(ModifyBaseModel):
    id_req: int
    id_staff: int
    id_disease: int
    id_type_of_treatment: int
    description_of_treatment: str


class Treatment_status(ModifyBaseModel):
    title: str


class Patients(ModifyBaseModel):
    id_reception: int
    id_status: int
    data_of_discharge: str