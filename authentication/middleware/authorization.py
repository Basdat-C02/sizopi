import jwt
from django.http import HttpResponseRedirect
from django.urls import reverse

from authentication.services.auth_service import AuthService
from authentication.utils.jwt_utils import decode_jwt, verify_jwt

class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = [
            reverse("authentication:landing"),
            reverse("authentication:login"),
            reverse("authentication:choose_role"),
            reverse("authentication:register_pengunjung"),
            reverse("authentication:register_dokter_hewan"),
            reverse("authentication:register_staff"),
        ]

    def __call__(self, request):
        if request.path.startswith("/__reload__"):
            return self.get_response(request)
        
        user = self.authenticate_user(request)
        
        if not user["is_authenticated"] and request.path not in self.exempt_urls:
            response = HttpResponseRedirect(reverse("authentication:landing"))
            response.delete_cookie("jwt")
            return response

        request.user = user
        return self.get_response(request)
    
    def authenticate_user(self, request):
        token = request.COOKIES.get("jwt")
        user = {"is_authenticated": False}
        
        if not token:
            return user
        
        try :
            username = verify_jwt(token)
            if username is None or username == "None":
                return user
            result = AuthService.get_user_by_username(username)
            if result == None:
                user['message'] = "User not found"
                return user
        except jwt.ExpiredSignatureError:
            user['message'] = "Token expired"
            return user
        except jwt.InvalidTokenError:
            user['message'] = "Invalid token"
            return user
        
        user = result
        user["is_authenticated"] = True
        return user
        