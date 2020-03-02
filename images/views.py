from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from django.shortcuts import get_object_or_404
from .models import Image


@login_required
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            # assign current user to the item将当前用户分配给项
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            # redirect to new created item detail view重定向到新创建的项目详细信息视图
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET使用书签工具通过GET提供的数据构建表单
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})


def image_detail(request, image_id, slug):
    image = get_object_or_404(Image, id=image_id, slug=slug)
    return render(request, 'images/image/detail.html', {'section': 'images', 'image': image})
