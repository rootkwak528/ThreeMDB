from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
	
    if '0' <= username[0] <= '9':
        return Response({'error': 'ID는 숫자로 시작할 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    if not 4 <= len(username) <= 12:
        return Response({'error': 'ID는 4~12자의 영문, 숫자, _로만 작성될 수 있습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    for ch in username:
        if not (
            '0' <= ch <= '9' or 
            'a' <= ch <= 'z' or 
            'A' <= ch <= 'Z' or
            ch == '_'):
            return Response({'error': 'ID는 4~12자의 영문, 숫자, _로만 작성될 수 있습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if len(password) <= 8:
        return Response({'error': '비밀번호는 8자 이상이어야 합니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)