from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Specialist
from .serializers import CategorySerializer, SpecialistSerializer


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(instance=category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(serializer.instance, request.data)
            return Response(serializer.data)
        return Response({'error': serializer.errors})
    elif request.method == 'DELETE':
        category.delete()
        return Response({'deleted': True})


class SpecialistListAPIView(APIView):
    def get(self, request):
        specialists = Specialist.objects.all()
        serializer = SpecialistSerializer(specialists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SpecialistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_object(specialist_id):
    try:
        return Specialist.objects.get(id=specialist_id)
    except Specialist.DoesNotExist as e:
        return Response({'error': str(e)})


def get(request, specialist_id):
    specialist = get_object(specialist_id)
    serializer = SpecialistSerializer(specialist)
    return Response(serializer.data)


class SpecialistDetailAPIView(APIView):
    def get_object(self, specialist_id):
        try:
            return Specialist.objects.get(id=specialist_id)
        except Specialist.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, specialist_id):
        specialist = self.get_object(specialist_id)
        serializer = SpecialistSerializer(specialist)
        return Response(serializer.data)

    def put(self, request, specialist_id):
        specialist = get_object(specialist_id)
        serializer = SpecialistSerializer(instance=specialist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors})

    def delete(self, request, specialist_id):
        specialist = get_object(specialist_id)
        specialist.delete()

        return Response({'deleted': True})


class SpecialistByCategoryAPIView(APIView):
    def get(self, request, category_id):
        specialists = Specialist.objects.filter(category=category_id)
        serializer = SpecialistSerializer(specialists, many=True)
        return Response(serializer.data)


class TopTenSpecialistsAPIView(APIView):
    def get(self, request):
        top_ten = Specialist.objects.order_by('likes')[:10]
        serializer = SpecialistSerializer(top_ten, many=True)
        return Response(serializer.data)