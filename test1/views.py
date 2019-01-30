#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView

# Create your views here.
from django.http import HttpResponse
from django.template import loader
#
from test1.models import Book, Impression
from test1.forms import BookForm, ImpressionForm

#
def index(request):
    return HttpResponse('Hello World ,from test1')

#
def book_list(request):
    """書籍の一覧"""
#    return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by('id')
    return render(request,
                  'test1/book_list.html',     # 使用するテンプレート
                  {'books': books})         # テンプレートに渡すデータ
#
def book_edit(request, book_id=None):
    """書籍の編集"""
    if book_id:   # book_id が指定されている (修正時)
        book = get_object_or_404(Book, pk=book_id)
    else:         # book_id が指定されていない (追加時)
        book = Book()
#    print(book.name )

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            book = form.save(commit=False)
            book.save()
            return redirect('test1:book_list')
    else:    # GET の時
        form = BookForm(instance=book)  # book インスタンスからフォームを作成

#    return render(request, 'test1/book_edit.html', dict(form=form, book_id=book_id))
    return render(request, 'test1/book_edit.html', dict(book=book, book_id=book_id))


def book_del(request, book_id):
    """書籍の削除"""
#    return HttpResponse('書籍の削除')
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('test1:book_list')

#
def book_test(request ):
    return render(request, 'test1/book_test.html')