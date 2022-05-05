from django.shortcuts import render, redirect, get_object_or_404
from .models import task, data, Test, Book
from .forms import BookCreate
from django.http import HttpResponse
def home(request):
    tasks = task.objects.all()
    return render(request, 'main/home.html',{'title': 'hello', 'tasks':tasks})
def carla(request):
    return render(request, 'main/carla.html')

    return render(request, 'main/index.html',{'sport':length})
def about(request):
    hobby =Test.objects.all()
    return render(request, 'main/about.html',{'hobby':hobby})
def last(request):
    name = data.objects.all()
    age = data.objects.all()
    weight = data.objects.all()
    return render(request, 'main/last.html',{'name': name,'age': age, 'weight':weight })

def fifth(request):
    return render(request, 'main/fifth.html')

def sixth(request):
    return render(request, 'main/sixth.html')

def seventh(request):
    return render(request, 'main/seventh.html')

def eighth(request):
    return render(request, 'main/eighth.html')
def index(request):
    shelf = Book.objects.all()
    return render(request, 'main/page.html', {'shelf': shelf})
def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'main/end.html', {'upload_form':upload})
def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('index')
    return render(request, 'main/end.html', {'upload_form':book_form})
def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')


def show_post(request):
    post = get_object_or_404(Posts, pk=post_id)
    context = {'post': post}
    return render(request, 'project/post.html', context=context)

def add_emp(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request, "myapp/from.html", {"form": form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            return redirect('/admin')
        else:
            clear_errors = form.errors.get("all")
            return render(request, "myapp/from.html", {"form": form, "clear_errors": clear_errors})




# Create your views here.
def book(request):
    object_list = Book.objects.all()
    student_list = Book.objects.all()

    search_query = request.POST.get('search')

    if not search_query:
        search_query = ""
    if request.method == 'POST':
        object_list = Book.objects.filter(student_name__icontains=search_query)

    return render(request, 'polls/book.html', {'object_list': object_list})
