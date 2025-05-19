def user_context(request):
    user = request.user if hasattr(request, "user") else {}
    return {
        "is_authenticated": user.get("is_authenticated", False),
        "user_role": user.get("role", ""),
        "is_adopter": user.get("is_adopter", False),
    }
