
from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User
from .serializers import UserSerializer,CommentSerializer
# from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets 
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer,BrowsableAPIRenderer,JSONRenderer
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework import generics

def home(request):
    if request.method == "POST":  
        form = UserForm(request.POST) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/user-list/')  
            except:  
                pass  
    else:  
        form = UserForm()  
    return render(request,'home.html',{'form':form})

class HomeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(first_name__startswith = "A")
    count = queryset.count()
    # print(count)
    # template_name = "home.html"
    serializer_class = CommentSerializer
    

# class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):
#     queryset = User.objects.all()
#     def get_default_renderer(self, view):
#         return JSONRenderer()
    
    


@api_view(['GET'])
def UserList(request):
    serializer = UserSerializer(User.objects.all(), many=True).data
    context = {'users': serializer}
    return render(request, 'show.html',context)

# @api_view(['GET'])
# def UserDetail(request,pk):
#     user = User.objects.get(id=pk)
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def UserCreate(request):
#     serializer = UserSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

@api_view(['POST','GET'])
def UserUpdate(request,pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user,data=request.data)

    if serializer.is_valid():
        serializer.save()

        return redirect("/user-list/")  
    return render(request, 'edit.html', {'user': user})
    

@api_view(['DELETE','GET'])
def UserDelete(request,pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('/user-list/')   
    
# def home_view(request): 
#     if request.method == "POST":  
#         form = UserForm(request.POST)  
#         if form.is_valid():  
#             try:  
#                 form.save()  
#                 return redirect('/show/')  
#             except:  
#                 pass  
#     else:  
#         form = UserForm()  
#     return render(request,'home.html',{'form':form})

# def show(request):  
#     user = User.objects.all()  
#     return render(request,"show.html",{'user':user})  

# def delete(request, id):  
#     user = User.objects.get(id=id)  
#     user.delete()  
#     return redirect("/show/")  

# def update(request, id):  
#     user = User.objects.get(id=id)  
#     form = UserForm(request.POST, instance = user)  
#     if form.is_valid():  
#         form.save()  
#         return redirect("/show/")  
#     return render(request, 'edit.html', {'user': user})




class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'profiles': queryset})



# class ProfileDetail(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'profile_detail.html'

#     def get(self, request, pk):
#         profile = get_object_or_404(User, pk=pk)
#         serializer = UserSerializer(profile)
#         return Response({'serializer': serializer, 'profile': profile})

    # def post(self, request, pk):
    #     print("SFdsg")
    #     profile = get_object_or_404(User, pk=pk)
    #     serializer = UserSerializer(profile, data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'profile': profile})
    #     serializer.save()
    #     return redirect('users/')

class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'
    # style = {'template_pack': 'rest_framework/vertical/'}
   

    def get(self, request):
        serializer = UserSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return redirect("/user-list/")

        return Response({'serializer': serializer})

# class FileUploadView(APIView):
#     parser_classes = [FileUploadParser]

#     def put(self, request, filename, format=None):
#         file_obj = request.data['file']
#         print(file_obj)
#         # ...
#         # do some stuff with uploaded file
#         # ...
#         return Response(status=204)


# TemplateHTMLRenderer
class UserDetail(generics.RetrieveAPIView):
    """
    A view that returns a templated HTML representation of a given user.
    """
    queryset = User.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'users': self.object}, template_name='user_detail.html')

        