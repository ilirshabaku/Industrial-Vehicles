from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render


@login_required
@permission_required('auth.change_group', raise_exception=True)
def assign_user_group(request):
    # Logic for assigning users to groups
    return render(request, 'permissions/admin.html')