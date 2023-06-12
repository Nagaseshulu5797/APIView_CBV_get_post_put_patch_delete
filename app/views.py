from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@permission_classes([IsAuthenticated])
class class_data(APIView):
    def get(self,request,id):
        PQS=Product.objects.all()
        JDMS=Product_CategoryData(PQS,many=True)
        return Response(JDMS.data)

    def post(self,request,id):
        PMSD=Product_CategoryData(data=request.data)
        if PMSD.is_valid():
            SPO=PMSD.save()
            return Response({'massage':'Product is created'})
        else:
            return Response({'Failed':'Product is not created'})

    def put(self,request,id):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        PMSD=Product_CategoryData(PO,data=request.data)
        if PMSD.is_valid():
            SPO=PMSD.save()
            return Response({'massage':'Product is Updated'})
        else:
            return Response({'Failed':'Product is not Updated'})

    def patch(self,request,id):
        id=request.data["id"]
        PO=Product.objects.get(id=id)
        PO.Pid=request.data['Pid']
        PO.save()
        return Response({"Update":"Partial Upadate successfully"})

    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'delete':'Delete success'})






    