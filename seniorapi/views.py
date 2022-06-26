from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status, filters
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser,ParseError
from rest_framework import generics, mixins, viewsets
from .models import number, users, car, Stream, pat_ref, patterns
from .serializers import numberSerializer, usersSerializer, StreamSerializer, carSerializer, pat_ref_Serializer

#number api 

class number_List(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = number.objects.all()
    serializer_class = numberSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


# register api
class register_List(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = users.objects.all()
    serializer_class = usersSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

#stream api
@api_view(['GET','POST'])
def stream_api(request):
    # GET
    if request.method == 'GET':
        query = Stream.objects.all()
        serializer = StreamSerializer(query, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = StreamSerializer(data= request.data, many=True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

#car api
class car_List(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = car.objects.all()
    serializer_class = carSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class pat_ref_List(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = pat_ref.objects.all()
    serializer_class = pat_ref_Serializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)



#all patterns api
@api_view(['GET'])
def patternsid(request,pk):

    data = pat_ref.objects.all().filter(user=pk)

    response = {
        
        'all patterns by user-id ' : list(data.values('user','time','startp_lat','startp_lon','endp_lat','endp_lon','cluster'))

    }
    return JsonResponse(response)


#show user-id of user by cluster  
@api_view(['GET'])
def clusterid(request,pk):

    data = pat_ref.objects.all().filter(cluster=pk)
    

    response = {
        
        'info user by cluster ' : list(data.values('user'))
        
    }
    return JsonResponse(response)

#show information user by user id from table car and user and number 
@api_view(['GET'])
def informationid(request,pk):

    data = users.objects.all().filter(user_id=pk)
    data1 = car.objects.all().filter(user=pk)
    data2 = number.objects.all().filter(user_id=pk)
    

    response = {
        
        'info user by cluster ' : list(data.values('firstname', 'secondname','profilepic'))
                                  +list(data1.values('Vehicle_Type', 'car_number'))
                                  +list(data2.values('phone'))
        
    }
    return JsonResponse(response)


#show dashboard 1
@api_view(['GET'])
def dashbord_all(request):

    data = users.objects.all()
    data1 =  car.objects.all()
    data2 = number.objects.all()
    response = {
        
        'information_for_user': list(data.values('firstname', 'secondname','fathername','dateofbirth', 'gender','profilepic','cardpic', 'car','user_id'))
                                + list(data1.values('Vehicle_Type','car_number','user'))
                                + list (data2.values('user_id','phone','activated'))
    }
    return JsonResponse(response)

 
@api_view(['GET'])
def dashbord_all_id(request,pk):

    data = users.objects.all().filter(user_id=pk)
    data1 = car.objects.all().filter(user=pk)
    data2 = number.objects.all().filter(user_id=pk)
    response = {
        
        'information_for_user': list(data.values('firstname', 'secondname','fathername','dateofbirth', 'gender','profilepic','cardpic', 'car','user_id'))
                                + list(data1.values('Vehicle_Type','car_number','user'))
                                + list (data2.values('user_id','phone','activated'))
    }
    return JsonResponse(response)

# edit activate api
class  editactive(APIView):
    def get_object(self, pk):
        try:
            return number.objects.get(user_id=pk)
        except number.DoesNotExists:
            raise Http404
    def get(self, request, pk):
        query = self.get_object(pk)
        serializer = numberSerializer(query)
        return Response(serializer.data)
    def put(self, request, pk):
        query = self.get_object(pk)
        serializer = numberSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def streamofid(request,pk):

    data1 = Stream.objects.all().filter(user=pk)

    response = {
        
        'information_stream_of _user' : list(data1.values('user','lat','lon','time'))

    }
    return JsonResponse(response)

@api_view(['GET'])
def streamoftime(request,time):

    data1 = Stream.objects.all().filter(time=time)

    response = {
        
        'information_stream_of _time' : list(data1.values('user','lat','lon','time'))

    }
    return JsonResponse(response)

@api_view(['GET'])
def idandtime(request,pk,time):

    data1 = Stream.objects.filter(user=pk , time=time)

    response = {
        
        'information_stream_of _time' : list(data1.values('user','lat','lon','time'))

    }
    return JsonResponse(response)   