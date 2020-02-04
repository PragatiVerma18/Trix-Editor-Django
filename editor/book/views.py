# views.py

from django.shortcuts import render

from .forms import BookForm


def create_book(request):
    template_name = 'book/create.html'
    form = BookForm(request.GET)
    # do further processing here
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # usual way, in which other form fields are processed
            description = form.cleaned_data.get('description')

    return render(request, template_name, {'form': form})