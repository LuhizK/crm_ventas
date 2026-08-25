import jwt
import datetime
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from ..models import Usuario

# Llave secreta para firmar el token (usamos la misma llave robusta de Django)
SECRET_KEY = settings.SECRET_KEY 

# --------------------------------------------------------
# ENDPOINT DE LOGIN (Generación del Token JWT)
# --------------------------------------------------------
@api_view(['POST'])
def login_usuario(request):
    username = request.data.get('username')
    password_ingresada = request.data.get('password')

    try:
        # 1. Buscamos el usuario en la tabla
        usuario = Usuario.objects.get(username=username)
        
        # 2. Verificamos la contraseña encriptada
        if check_password(password_ingresada, usuario.password_hash):
            
            # 3. Generamos el Payload (los datos que viajan en el token)
            payload = {
                'id_usuario': usuario.id_usuario,
                'rol': usuario.id_rol.nombre_rol,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2) # Expira en 2 horas
            }
            
            # 4. Firmamos el Token (Requisito de la Sesión 1)
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            
            return Response({
                'mensaje': 'Autenticación exitosa',
                'token': token
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
            
    except Usuario.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

# --------------------------------------------------------
# MIDDLEWARE DE PROTECCIÓN (El Candado)
# --------------------------------------------------------
def validar_token(view_func):
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        
        # Verificamos si envió el token y si tiene el formato "Bearer <token>"
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response({'error': 'Acceso denegado. Token no proporcionado o formato incorrecto.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Extraemos solo el token (quitamos la palabra Bearer)
        token = auth_header.split(' ')[1]
        
        try:
            # Intentamos decodificarlo
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            # Si es válido, guardamos la info del usuario en la petición y lo dejamos pasar
            request.usuario_auth = payload
            return view_func(request, *args, **kwargs)
            
        except jwt.ExpiredSignatureError:
            return Response({'error': 'El token ha expirado. Inicia sesión nuevamente.'}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidTokenError:
            return Response({'error': 'Token inválido.'}, status=status.HTTP_401_UNAUTHORIZED)
            
    return wrapper