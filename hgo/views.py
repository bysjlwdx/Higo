# coding='utf-8'
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

# 添加Django自带的分页插件 paginator
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# 包装csrf请求，避免django认为其实跨站攻击脚本
from django.views.decorators.csrf import csrf_exempt
from .models import Stu
from Higo.forms import StuFrom


# Create your views here.
# 显示所有数据,并分页

def hgo_list(request):
    keyword = request.POST.get("name")
    if keyword:
        articles = Stu.objects.all().filter(name=keyword).order_by('id')
    else:
        # articles = Stu.objects.get_queryset().order_by('id')
        articles = Stu.objects.all()
    paginator = Paginator(articles, 5)   # 分页，10篇文章一页
    page = int(request.GET.get('page', 1))  # 获取请求的文章页码，默认为第一页
    contacts = paginator.get_page(page)  # 返回指定页码的页面
    return render(request, 'index.html', {'contacts': contacts})

    # 添加的方法
def hgo_insert(requset):
    if requset.method == "POST":
        stu_form = StuFrom(requset.POST)
        if stu_form.is_valid():
            stu_form.save()
        return HttpResponseRedirect("/show/")
    else:
        return render(requset, "insert.html")

    # 删除的方法


def delById(request):
    id = request.GET["id"];
    str = Stu.objects.get(id=id)
    str.delete()
    return HttpResponseRedirect("/show/")


# 查看的方法
def queryById(request):
    id = request.GET["id"];
    if id == "":
        return HttpResponseRedirect("/show/")
    stuu = Stu.objects.get(id=id)
    return render_to_response("curd.html", {"d": stuu})


# 修改数据的方法
@csrf_exempt
def upById(request):
    id = request.POST["id"];
    print(id)
    name = request.POST["name"];
    gender = request.POST["gender"];
    age = request.POST["age"];
    address = request.POST["address"];
    st = Stu()
    if len(id) > 0:
        st.id = id;
    st.age = age;
    st.name = name;
    st.gender = gender;
    st.address = address;
    st.save()
    return HttpResponseRedirect("/show/")