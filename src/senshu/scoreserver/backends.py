from django.contrib.auth import get_user_model
User = get_user_model()

class UserBackend(object):
    """
    This is custom backend for authenticating user.
    """

    def authenticate(self, username=None, password=None):
        """
        Use the login name, and a hash of the password. For example:

        ADMIN_LOGIN = 'admin'
        ADMIN_PASSWORD = 'pbkdf2_sha256$...'
        :param username:
        :param password:
        :return:
        """
        print("Use custom authenticate backend.")
        user = None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            print("There is no specified user.")
        if user is not None:
            password_valid = user.check_password(password)
            if password_valid:
                return user
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None






















































































