from django.shortcuts import render
from django.contrib import messages
from email_validator import validate_email, EmailNotValidError


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email-address')

        context = {
            'email': email
        }

        try:
            email_object = validate_email(email)

            messages.success(request, f'{email} if valid email address!!')

            return render(request, 'verifier/index.html', context)

        except EmailNotValidError as e:
            messages.warning(request, f'{e} ')
            return render(request, 'verifier/index.html', context)

    return render(request, 'verifier/index.html')


