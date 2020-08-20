from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from .models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
class BookListView(ListView):
    '''
        {
        "pan_number":""
        }
        '''
    template_name = "home.html"
    def get(self, request, *args, **kwargs,):

        ctx = {}
        response=''
        all_data = Book.objects.all()
        if all_data:
            ctx['all_Data']= all_data
            paginator = Paginator(all_data, 2)

            page = request.GET.get('page')
            try:
                response = paginator.page(page)
            except PageNotAnInteger:
                response = paginator.page(1)
            except EmptyPage:
                response = paginator.page(paginator.num_pages)
            ctx['paginator']=response

        base_url = 'booklist/'
        ctx['base_url']=base_url
        return render(request,self.template_name,ctx)

    def post(self,request,*args,**kwargs):
        ctx={}
        response = ''
        user_name = request.POST.get('book_name')
        all_data = Book.objects.filter(title__icontains=user_name)
        if all_data:
            ctx['all_Data'] = all_data
            paginator = Paginator(all_data, 2)

            page = request.GET.get('page')
            try:
                response = paginator.page(page)
            except PageNotAnInteger:
                response = paginator.page(1)
            except EmptyPage:
                response = paginator.page(paginator.num_pages)
            ctx['paginator'] = response

        base_url = 'booklist/'
        ctx['base_url'] = base_url
        return render(request, self.template_name, ctx)