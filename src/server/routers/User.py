import fastapi
from src.server.resolvers import Users
from src.server.database.models import Users
from typing import List

router = fastapi.APIRouter(prefix='/user', tags=['Users'])


@router.get('/get_all')
def get_all() -> List[Users] | dict:
    return get_all()


@router.get('/user/{user_id}')
def get(user_id: int) -> Users:
    return Users.get(user_id)


@router.post('/create/')
def create(new_user: Users) -> Users | dict:
    return Users.create(new_user)


@router.put('/update/{user_id}')
def update(user_id: int, new_data: Users):
    return Users.update(user_id, new_data)


@router.delete('/delete/{user_id}')
def delete(user_id: int):
    return Users.delete(user_id)
