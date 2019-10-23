from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer,MemberSerializer,AuthorSerializer,BorrowsSerializer
from .models import Book,Member,Author,Borrows

class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class MemberView(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class AuthorView(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BorrowsView(viewsets.ModelViewSet):
    serializer_class = BorrowsSerializer
    queryset = Borrows.objects.all()


@api_view(['GET',])
def api_library_list_view(request):
    library = Book.objects.all()
    if request.method == 'GET':
        serializer = BookSerializer(library, many=True)
        return Response(serializer.data)


@api_view(['GET',])
def api_library_details_view(request,pk):
    try:
        library = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BookSerializer(library)
        return Response(serializer.data)


@api_view(['GET',])
def api_member_list_view(request):
    member = Member.objects.all()
    if request.method == 'GET':
        serializer=MemberSerializer(member,many=True)

        return Response(serializer.data)


@api_view(['GET',])
def api_member_details_view(request,pk):
    try:
        member = Member.objects.get(id=pk)
    except Member.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MemberSerializer(member)
        return Response(serializer.data)


@api_view(['GET',])
def api_author_list_view(request):
    author = Author.objects.all()
    if request.method == 'GET':
        serializer=AuthorSerializer(author,many=True)

        return Response(serializer.data)


@api_view(['GET',])
def api_author_details_view(request,pk):
    try:
        author = Author.objects.get(id=pk)
    except Author.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)


@api_view(['GET',])
def api_borrows_list_view(request):
    borrows = Borrows.objects.all()
    if request.method == 'GET':
        serializer=BorrowsSerializer(borrows,many=True)

        return Response(serializer.data)


@api_view(['GET',])
def api_borrows_details_view(request,pk):
    try:
        borrows = Borrows.objects.get(id=pk)
    except Borrows.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BorrowsSerializer(borrows)
        return Response(serializer.data)


@api_view(['PUT', ])
def api_library_update_list_view(request,pk):
    try:
        library = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BookSerializer(library,data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = "Update Successful"
            return Response(serializer.data)

        return Response(serializer.error,status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_404_NOT_FOUND)


@api_view(['PUT', ])
def api_member_update_list_view(request,pk):
    try:
        member = Member.objects.get(id=pk)
    except Member.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = MemberSerializer(member,data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = "Update Successful"
            return Response(serializer.data)

        return Response(serializer.error,status.HTTP_400_BAD_REQUEST)
    return Response(status.HTTP_404_NOT_FOUND)



@api_view(['DELETE', ])
def api_library_delete_view(request,pk):
    try:
        library = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = library.delete()
        data = {}
        if operation:
            data['success'] = "Delete Succesfull"
        else:
            data['failure'] = "Unsuccessfull"
            return Response(data,status.HTTP_200_OK)
        return Response(data,status.HTTP_404_NOT_FOUND)



@api_view(['POST', ])
def api_library_post_view(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

