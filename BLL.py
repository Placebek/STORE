from DAL import DataAccessor

class BusinessLogic:
    def __init__(self) -> None:
        self.data_accessor = DataAccessor()

    def get_user_by_login_password(self, login, password):
        if user:
            return True
        else:
            return False
        return self.data_accessor.get_user_by_login_password(login, password)
