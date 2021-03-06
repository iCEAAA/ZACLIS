from django.shortcuts import render
from django.http import HttpResponse
from post.models import tag
from django.db.models import ObjectDoesNotExist
from post.views import generateList
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("123")

def tagsView(request,tag_name):
    try:   
        t=tag.objects.get(name=tag_name)
        postList=t.post_set.all()
        return render(request,'postList.html',{'postList':generateList(postList)})
    except ObjectDoesNotExist:
        return HttpResponse("Error: tag "+ tag_name +" does not exist!")
    #return render(render,'tagsView.html')