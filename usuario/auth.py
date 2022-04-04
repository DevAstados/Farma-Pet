import logging

from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password

from usuario.models import CustomUser


class SettingsBackend:
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """

    def authenticate(self, request, username=None, password=None):

            try:
                # Try to find a user matching your username
                user = CustomUser.objects.get(username=username)

                #  Check the password is the reverse of the username
                if CustomUser.check_password(password, user.password):
                    # Yes? return the Django user object
                    return user
                else:
                    # No? return None - triggers default login failed
                    return None
            except CustomUser.DoesNotExist:
                # No user was found, return None - triggers default login failed
                return None


    def get_user(self, user_id):
        logging.error('get_user')
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None

    def has_perm(self, user_obj, perm, obj=None):
        return user_obj.username == settings.ADMIN_LOGIN