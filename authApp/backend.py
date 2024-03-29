from authApp.models import CustomUser
from django.contrib.auth.hashers import check_password


class CustomUserBackend:
    def authenticate(self, request, username, password):
        if username and password:
            if '@' in username:
                kwargs = {'email': username}
            else:
                kwargs = {'username': username}
            try:
                user = CustomUser.objects.get(**kwargs)
                if check_password(password, user.password):
                    if user is not None:
                        return user
            except CustomUser.DoesNotExist:
                return None
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
