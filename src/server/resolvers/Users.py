from src.server.database.db_manager import db_manager
from src.server.database.models import Users
from typing import List


def login(login: str, password: str) -> Users:
    res = db_manager.execute_query(query="SELECT id FROM Users WHERE login = (?) and password = (?)",
                                   args=(login, password))
    return get(res[0]) if res else {'Error': 'incorrect login or password'}


def get(user_id: int) -> Users:
    res = db_manager.execute_query(query='SELECT * FROM Users WHERE id = (?)', args=user_id)

    return None if not res else Users(
        id=res[0],
        FIO=res[1],
        login=res[2],
        password=''
    )


def get_all() -> List[Users] | dict:
    user_list = db_manager.execute_query(query='SELECT * FROM Users', fetchone=False)
    res = []
    if user_list:
        for Users in user_list:
            res.append(Users(
                id=Users[0],
                FIO=Users[1],
                login=Users[2],
                password=''
            ))

    return res


def create(new_user: Users) -> int | dict:
    res = db_manager.execute_query(query='INSERT INTO Users(FIO,login,password) VALUES (?,?,?) returning id',
                                   args=(new_user.FIO, new_user.login, new_user.password))
    if type != dict:
        res = get(res[0])

    return res


def update(user_id: int, new_data: Users) -> None:
    return db_manager.execute_query(query='UPDATE Users SET (FIO, login, password) = (?,?,?) WHERE id = (?)',
                                    arqs=(new_data.FIO, new_data.login, new_data.password, user_id))


def delete(user_id: int) -> int:
    return db_manager.execute_query(query='DELETE FROM Users WHERE id = (?)', args=user_id)
