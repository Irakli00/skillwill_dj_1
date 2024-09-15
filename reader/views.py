from django.shortcuts import render
from pysss import password

from .form import UserForm

# def reader_input(request):
#     return render(request,'reader_form.html',{'form':UserForm})


def reader_input(request):
    if request.method == 'POST':
        form = UserForm(request.POST)  # Bind form with POST data
        if form.is_valid():
            # Access form data
            username = form.cleaned_data['username']
            user_password = form.cleaned_data['password']

            if username == 'ira' and user_password =='123':
                return render(request, 'success_form.html', {'username': username})

    else:
        form = UserForm()  # Show an empty form

    return render(request, 'reader_form.html', {'form': form})