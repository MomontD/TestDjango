from django.shortcuts import render, redirect

from governments.forms import add_governmentForm


def governments(request):
    return render(request, '')


def add_government(request):
    error = ''
    if request.method == "POST":
        form = add_governmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operations')
        else:
            error = 'Data not accepted! Invalid data in form!'

    form = add_governmentForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'governments/add_government.html', data)
