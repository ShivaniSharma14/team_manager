from django.shortcuts import render , get_object_or_404 , redirect
from .forms import ResourceForm
from .models import Resource
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .permissions import can_modify_resource, can_delete_resource




# list View
@login_required
def ListResourceView(request):

    objects = Resource.objects.all()
    context={'objects':objects}
    return render(request, 'resources/resources_list.html' , context)




# DetailView
@login_required

def DetailResourceView(request , id):
    obj = get_object_or_404(Resource , id=id)

    context={'object':obj}
    return render(request, 'resources/resources_detail.html' , context)




# CreateView
@login_required

def CreateResourceView(request):


    

    if request.method == 'POST':
        form = ResourceForm(request.POST)

        if form.is_valid():
            resource = form.save(commit=False)
            resource.created_by = request.user
            resource.save()
            messages.success(request, "Post is made successfully!")
            return redirect('resource-detail', id=resource.id)
    
                    
    form = ResourceForm()
    context={'form':form}
    return render(request, 'resources/resources_create.html' , context)




# Update View
@login_required

def UpdateResourceView(request , id):

    obj = get_object_or_404(Resource , id=id)

    if not can_modify_resource(request.user ,obj):
        raise PermissionDenied


    form = ResourceForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('resource-detail' , id=obj.id)
      
        
    context={'form':form}
    
    return render(request, 'resources/resources_update.html' , context)



# Delete View
@login_required

def DeleteResourceView(request , id):

    obj = get_object_or_404(Resource, id=id)

    if not can_delete_resource(request.user ,obj):
        raise PermissionDenied

    else:
        if request.method == 'POST':
          obj.delete()
          return redirect('resource-page')

    context={'object':obj}
    return render(request, 'resources/resources_delete.html' ,context)