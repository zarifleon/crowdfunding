from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse # For basic responses
from django.views.decorators.csrf import csrf_exempt # For simplicity in examples, consider CSRF protection for production
from django.contrib.auth.hashers import make_password, check_password
import json # For parsing JSON request bodies

from .models import CrowdUsuario, CrowdCatalogoUsuarioTipo, CrowdUsuarioNivel, CrowdCaso, CrowdCategoria, CrowdCatalogoEstatus, SistemaMunicipalPrograma # Import necessary models

# TODO: Consider creating Django Forms for validation and HTML rendering assistance.

@csrf_exempt # REMOVE/REPLACE with proper CSRF for production
def registrar_usuario_vista(request):
    if request.method == 'POST':
        try:
            # Asumiendo que los datos vienen como JSON
            # En una aplicación web tradicional, vendrían de request.POST (form data)
            data = json.loads(request.body)

            id_morelia = data.get('id_morelia')
            email = data.get('email')
            raw_password = data.get('password')
            first_name = data.get('first_name')
            last_name = data.get('last_name')

            # Campos opcionales o con default
            usuario_tipo_id = data.get('usuario_tipo_id') # ID del tipo de usuario
            nivel_id = data.get('nivel_id') # ID del nivel de usuario

            # Validación básica (Django Forms es mejor para esto)
            if not all([id_morelia, email, raw_password, first_name, last_name]):
                return JsonResponse({'error': 'Faltan campos requeridos.'}, status=400)

            if CrowdUsuario.objects.filter(id_morelia=id_morelia).exists():
                return JsonResponse({'error': 'El ID Morelia ya está registrado.'}, status=400)

            if CrowdUsuario.objects.filter(email=email).exists():
                return JsonResponse({'error': 'El correo electrónico ya está registrado.'}, status=400)

            # Hashear la contraseña
            hashed_password = make_password(raw_password)

            # Obtener instancias de FK si se proporcionan IDs
            usuario_tipo_inst = None
            if usuario_tipo_id:
                try:
                    usuario_tipo_inst = CrowdCatalogoUsuarioTipo.objects.get(id=usuario_tipo_id)
                except CrowdCatalogoUsuarioTipo.DoesNotExist:
                    return JsonResponse({'error': f'Tipo de usuario con ID {usuario_tipo_id} no encontrado.'}, status=400)

            nivel_inst = None
            if nivel_id:
                try:
                    nivel_inst = CrowdUsuarioNivel.objects.get(id=nivel_id)
                except CrowdUsuarioNivel.DoesNotExist:
                    return JsonResponse({'error': f'Nivel de usuario con ID {nivel_id} no encontrado.'}, status=400)

            # Crear el nuevo usuario
            nuevo_usuario = CrowdUsuario.objects.create(
                id_morelia=id_morelia,
                email=email,
                password=hashed_password,
                first_name=first_name,
                last_name=last_name,
                usuario_tipo=usuario_tipo_inst,
                nivel=nivel_inst
                # fecha_creacion y activo tienen defaults en el modelo
            )

            # Podríamos serializar el usuario creado y devolverlo, o solo un mensaje de éxito.
            return JsonResponse({
                'mensaje': 'Usuario registrado exitosamente.',
                'usuario': {
                    'id_morelia': nuevo_usuario.id_morelia,
                    'email': nuevo_usuario.email,
                    'first_name': nuevo_usuario.first_name,
                    'last_name': nuevo_usuario.last_name,
                }
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Cuerpo de la solicitud JSON inválido.'}, status=400)
        except Exception as e:
            # Loggear el error e
            return JsonResponse({'error': f'Ocurrió un error en el servidor: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Método no permitido. Solo POST es aceptado.'}, status=405)


# --- Gestión de Casos ---

# Vista para listar todos los casos (Read)
def listar_casos_vista(request):
    if request.method == 'GET':
        casos = CrowdCaso.objects.all() # Podríamos añadir filtros, paginación, etc.

        # Serializar los datos del caso. Esto es una serialización manual simple.
        # Para APIs más complejas, Django REST framework (DRF) es muy útil.
        casos_data = []
        for caso_obj in casos:
            casos_data.append({
                'id': caso_obj.id,
                'creador': caso_obj.creador.id_morelia, # Mostrar el ID del creador
                'titulo': caso_obj.exposicion_titulo,
                'quien_soy': caso_obj.exposicion_quien_soy,
                'que_necesito': caso_obj.exposicion_que_necesito,
                'porque': caso_obj.exposicion_porque,
                'detalles_adicionales': caso_obj.exposicion_detalles_adicionales,
                'texto_promocional': caso_obj.exposicion_promocional,
                'video_promocional': caso_obj.video_promocional.url if caso_obj.video_promocional else None,
                'imagen_promocional': caso_obj.imagen_promocional.url if caso_obj.imagen_promocional else None,
                'categoria': caso_obj.categoria.nombre if caso_obj.categoria else None,
                'cantidad_requerida': caso_obj.cantidad_requerida,
                'cantidad_obtenida': caso_obj.cantidad_obtenida,
                'estatus': caso_obj.estatus.nombre if caso_obj.estatus else None,
                'fecha_publicacion': caso_obj.fecha_publicacion.isoformat() if caso_obj.fecha_publicacion else None,
                'fecha_creacion': caso_obj.fecha_creacion.isoformat(),
                'fecha_fin': caso_obj.fecha_fin.isoformat() if caso_obj.fecha_fin else None,
                'programa_municipal': caso_obj.programa_municipal.descripcion_nombre if caso_obj.programa_municipal else None,
                # Podríamos añadir artículos asociados aquí si es necesario
            })
        return JsonResponse(casos_data, safe=False) # safe=False es para permitir listas en la raíz del JSON

    return JsonResponse({'error': 'Método no permitido. Solo GET es aceptado.'}, status=405)


# Vista para crear un nuevo caso (Create)
@csrf_exempt # REMOVE/REPLACE con proper CSRF for production
def crear_caso_vista(request):
    if request.method == 'POST':
        # Aquí se necesitaría autenticación para saber quién es el creador.
        # Por ahora, asumiremos que el 'creador_id_morelia' viene en el request body o form data.
        # En una implementación real, se tomaría de request.user después de la autenticación.
        try:
            # Si se envían archivos, los datos de texto vendrán en request.POST, no en request.body (JSON)
            # Esto es típico para multipart/form-data.
            # Si no hay archivos, se podría seguir esperando JSON, o estandarizar a form-data.
            # Por simplicidad, asumiremos que si hay archivos, todo es form-data.
            # Si no hay archivos, se podría intentar parsear JSON, o requerir form-data siempre.

            # Intentar obtener datos de request.POST (form-data) primero
            # Si se usa DRF, esto se maneja de forma más transparente.
            data = request.POST
            if not data: # Si request.POST está vacío, intentar leer JSON (para clientes que no envían archivos)
                try:
                    data = json.loads(request.body)
                except json.JSONDecodeError:
                    # Si no es JSON y POST está vacío, y el método es POST, algo anda mal.
                    if not request.FILES: # Si tampoco hay archivos, entonces el cuerpo está mal o vacío.
                        return JsonResponse({'error': 'Cuerpo de la solicitud vacío o en formato incorrecto. Se espera form-data o JSON.'}, status=400)
                    # Si hay archivos pero no data en POST, igual se usa un dict vacío para data y se procede.
                    data = {}


            # Campos requeridos para crear un caso (ejemplo, ajustar según necesidad)
            creador_id_morelia = data.get('creador_id_morelia') # TEMPORAL: Debería venir de request.user
            exposicion_titulo = data.get('exposicion_titulo')
            exposicion_quien_soy = data.get('exposicion_quien_soy')
            exposicion_que_necesito = data.get('exposicion_que_necesito')
            exposicion_porque = data.get('exposicion_porque')
            categoria_id = data.get('categoria_id') # ID de la categoría
            cantidad_requerida = data.get('cantidad_requerida')
            fecha_publicacion = data.get('fecha_publicacion') # Formato YYYY-MM-DD
            fecha_fin = data.get('fecha_fin') # Formato YYYY-MM-DD

            # Validación básica (Django Forms o DRF Serializers son mejores)
            # Asegurarse de que los campos requeridos no sean None o string vacío si vienen de form data
            required_fields_map = {
                "creador_id_morelia": creador_id_morelia, "exposicion_titulo": exposicion_titulo,
                "exposicion_quien_soy": exposicion_quien_soy, "exposicion_que_necesito": exposicion_que_necesito,
                "exposicion_porque": exposicion_porque, "categoria_id": categoria_id,
                "cantidad_requerida": cantidad_requerida, "fecha_publicacion": fecha_publicacion,
                "fecha_fin": fecha_fin
            }
            missing_fields = [key for key, value in required_fields_map.items() if not value]
            if missing_fields:
                return JsonResponse({'error': f'Faltan campos requeridos: {", ".join(missing_fields)}'}, status=400)


            try:
                creador_inst = CrowdUsuario.objects.get(id_morelia=creador_id_morelia)
            except CrowdUsuario.DoesNotExist:
                return JsonResponse({'error': 'El usuario creador especificado no existe.'}, status=400)

            try:
                categoria_inst = CrowdCategoria.objects.get(id=int(categoria_id)) # Convertir a int si viene de form-data
            except (CrowdCategoria.DoesNotExist, ValueError):
                return JsonResponse({'error': 'La categoría especificada no existe o ID inválido.'}, status=400)

            # Campos opcionales
            exposicion_detalles_adicionales = data.get('exposicion_detalles_adicionales', '')
            exposicion_promocional = data.get('exposicion_promocional', '')
            # Files from request.FILES
            video_promocional_file = request.FILES.get('video_promocional')
            imagen_promocional_file = request.FILES.get('imagen_promocional')

            estatus_id = data.get('estatus_id')
            programa_municipal_id = data.get('programa_municipal_id')

            estatus_inst = None
            if estatus_id:
                try:
                    estatus_inst = CrowdCatalogoEstatus.objects.get(id=int(estatus_id))
                except CrowdCatalogoEstatus.DoesNotExist:
                    return JsonResponse({'error': 'El estatus especificado no existe.'}, status=400)

            programa_municipal_inst = None
            if programa_municipal_id:
                try:
                    programa_municipal_inst = SistemaMunicipalPrograma.objects.get(id=programa_municipal_id)
                except SistemaMunicipalPrograma.DoesNotExist:
                    return JsonResponse({'error': 'El programa municipal especificado no existe.'}, status=400)

            nuevo_caso = CrowdCaso.objects.create(
                creador=creador_inst,
                exposicion_titulo=exposicion_titulo,
                exposicion_quien_soy=exposicion_quien_soy,
                exposicion_que_necesito=exposicion_que_necesito,
                exposicion_porque=exposicion_porque,
                exposicion_detalles_adicionales=exposicion_detalles_adicionales,
                exposicion_promocional=exposicion_promocional,
                video_promocional=video_promocional_file, # Asignar el archivo subido
                imagen_promocional=imagen_promocional_file, # Asignar el archivo subido
                categoria=categoria_inst,
                cantidad_requerida=float(cantidad_requerida),
                # cantidad_obtenida tiene default 0.0
                estatus=estatus_inst, # Puede ser None si no se provee y el modelo lo permite
                fecha_publicacion=fecha_publicacion,
                # fecha_creacion tiene default timezone.now
                fecha_fin=fecha_fin,
                programa_municipal=programa_municipal_inst # Puede ser None
            )

            return JsonResponse({
                'mensaje': 'Caso creado exitosamente.',
                'caso_id': nuevo_caso.id
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Cuerpo de la solicitud JSON inválido.'}, status=400)
        except ValueError as ve: # Para errores de conversión como float()
            return JsonResponse({'error': f'Error en el valor de un campo: {str(ve)}'}, status=400)
        except Exception as e:
            # Loggear el error e
            return JsonResponse({'error': f'Ocurrió un error en el servidor: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Método no permitido. Solo POST es aceptado.'}, status=405)


# Vista para obtener detalles de un caso específico (Read by ID)
def detalle_caso_vista(request, caso_id):
    if request.method == 'GET':
        try:
            caso_obj = CrowdCaso.objects.select_related(
                'creador', 'categoria', 'estatus', 'programa_municipal'
            ).get(id=caso_id) # Usar select_related para optimizar obtención de FKs

            # Serializar los datos del caso
            caso_data = {
                'id': caso_obj.id,
                'creador': { # Serializar datos del creador
                    'id_morelia': caso_obj.creador.id_morelia,
                    'nombre_completo': f"{caso_obj.creador.first_name} {caso_obj.creador.last_name}",
                    'email': caso_obj.creador.email, # Considerar si se debe exponer públicamente
                },
                'titulo': caso_obj.exposicion_titulo,
                'quien_soy': caso_obj.exposicion_quien_soy,
                'que_necesito': caso_obj.exposicion_que_necesito,
                'porque': caso_obj.exposicion_porque,
                'detalles_adicionales': caso_obj.exposicion_detalles_adicionales,
                'texto_promocional': caso_obj.exposicion_promocional,
                'video_promocional': caso_obj.video_promocional.url if caso_obj.video_promocional else None,
                'imagen_promocional': caso_obj.imagen_promocional.url if caso_obj.imagen_promocional else None,
                'categoria': caso_obj.categoria.nombre if caso_obj.categoria else None,
                'cantidad_requerida': caso_obj.cantidad_requerida,
                'cantidad_obtenida': caso_obj.cantidad_obtenida,
                'estatus': caso_obj.estatus.nombre if caso_obj.estatus else None,
                'fecha_publicacion': caso_obj.fecha_publicacion.isoformat() if caso_obj.fecha_publicacion else None,
                'fecha_creacion': caso_obj.fecha_creacion.isoformat(),
                'fecha_fin': caso_obj.fecha_fin.isoformat() if caso_obj.fecha_fin else None,
                'programa_municipal': caso_obj.programa_municipal.descripcion_nombre if caso_obj.programa_municipal else None,
                'articulos': [ # Incluir artículos asociados al caso
                    {
                        'id': articulo.id,
                        'descripcion': articulo.descripcion,
                        'recibo_tipo': articulo.recibo_tipo,
                        'precio': articulo.precio,
                    } for articulo in caso_obj.articulos.all() # Usando related_name 'articulos'
                ]
            }
            return JsonResponse(caso_data)

        except CrowdCaso.DoesNotExist:
            return JsonResponse({'error': 'Caso no encontrado.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Ocurrió un error en el servidor: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Método no permitido. Solo GET es aceptado.'}, status=405)


# Vista para actualizar un caso existente (Update)
@csrf_exempt # REMOVE/REPLACE con proper CSRF for production
def actualizar_caso_vista(request, caso_id):
    if request.method == 'PUT' or request.method == 'PATCH': # PUT para reemplazo total, PATCH para parcial
        try:
            caso_obj = CrowdCaso.objects.get(id=caso_id)

            # --- INICIO Bloque de Autorización (Conceptual) ---
            # En una implementación real con autenticación:
            # if not request.user.is_authenticated:
            #     return JsonResponse({'error': 'Autenticación requerida.'}, status=401)
            # if caso_obj.creador != request.user: # Asumiendo que request.user es una instancia de CrowdUsuario
            #     # O si hay roles/permisos más complejos:
            #     # if not request.user.has_perm('nucleo_crowdfunding.change_crowdcaso', caso_obj) and caso_obj.creador != request.user :
            #     return JsonResponse({'error': 'No tiene permiso para modificar este caso.'}, status=403)
            # --- FIN Bloque de Autorización ---

            # Por ahora, para prueba, permitiremos la actualización sin auth real,
            # pero el bloque anterior muestra dónde iría la lógica de permisos.
            # Se podría requerir 'creador_id_morelia' en el payload para una pseudo-verificación temporal si no hay auth.

            data = json.loads(request.body) # Asume JSON para simplicidad, necesitaría manejar multipart si se actualizan archivos por esta vía

            # Actualizar campos. Si es PATCH, solo se actualizan los campos presentes.
            # Si es PUT, se podrían esperar todos los campos o manejar ausencias como errores o borrado (según la semántica deseada).

            # Campos actualizables (ejemplo, expandir según necesidad)
            if 'exposicion_titulo' in data:
                caso_obj.exposicion_titulo = data['exposicion_titulo']
            if 'exposicion_quien_soy' in data:
                caso_obj.exposicion_quien_soy = data['exposicion_quien_soy']
            if 'exposicion_que_necesito' in data:
                caso_obj.exposicion_que_necesito = data['exposicion_que_necesito']
            if 'exposicion_porque' in data:
                caso_obj.exposicion_porque = data['exposicion_porque']
            if 'exposicion_detalles_adicionales' in data:
                caso_obj.exposicion_detalles_adicionales = data['exposicion_detalles_adicionales']
            if 'exposicion_promocional' in data: # Este es NOT NULL en el modelo (como TextField)
                caso_obj.exposicion_promocional = data['exposicion_promocional']

            # Manejo de archivos para actualización
            video_promocional_file = request.FILES.get('video_promocional')
            if video_promocional_file:
                caso_obj.video_promocional = video_promocional_file
            elif 'video_promocional' in data and data.get('video_promocional') is None:
                # Permitir borrar el video enviando null/None para el campo (si el campo del modelo permite null)
                caso_obj.video_promocional = None

            imagen_promocional_file = request.FILES.get('imagen_promocional')
            if imagen_promocional_file:
                caso_obj.imagen_promocional = imagen_promocional_file
            elif 'imagen_promocional' in data and data.get('imagen_promocional') is None:
                 # Permitir borrar la imagen enviando null/None
                caso_obj.imagen_promocional = None


            if 'categoria_id' in data:
                try:
                    categoria_inst = CrowdCategoria.objects.get(id=data['categoria_id'])
                    caso_obj.categoria = categoria_inst
                except CrowdCategoria.DoesNotExist:
                    return JsonResponse({'error': 'Categoría no encontrada.'}, status=400)

            if 'cantidad_requerida' in data:
                try:
                    caso_obj.cantidad_requerida = float(data['cantidad_requerida'])
                except ValueError:
                     return JsonResponse({'error': 'Cantidad requerida debe ser un número.'}, status=400)

            # cantidad_obtenida usualmente no se actualiza directamente por el usuario.

            if 'estatus_id' in data:
                if data['estatus_id'] is None:
                    caso_obj.estatus = None
                else:
                    try:
                        estatus_inst = CrowdCatalogoEstatus.objects.get(id=data['estatus_id'])
                        caso_obj.estatus = estatus_inst
                    except CrowdCatalogoEstatus.DoesNotExist:
                        return JsonResponse({'error': 'Estatus no encontrado.'}, status=400)

            if 'fecha_publicacion' in data:
                caso_obj.fecha_publicacion = data['fecha_publicacion'] # Asumir formato YYYY-MM-DD
            if 'fecha_fin' in data:
                caso_obj.fecha_fin = data['fecha_fin'] # Asumir formato YYYY-MM-DD

            if 'programa_municipal_id' in data:
                if data['programa_municipal_id'] is None:
                    caso_obj.programa_municipal = None
                else:
                    try:
                        programa_inst = SistemaMunicipalPrograma.objects.get(id=data['programa_municipal_id'])
                        caso_obj.programa_municipal = programa_inst
                    except SistemaMunicipalPrograma.DoesNotExist:
                        return JsonResponse({'error': 'Programa municipal no encontrado.'}, status=400)

            caso_obj.save() # Guardar los cambios

            # Devolver el objeto actualizado (o solo un mensaje de éxito)
            # Reutilizar la serialización de detalle_caso_vista sería ideal para consistencia.
            # Por brevedad, un mensaje simple:
            return JsonResponse({'mensaje': 'Caso actualizado exitosamente.', 'caso_id': caso_obj.id})

        except CrowdCaso.DoesNotExist:
            return JsonResponse({'error': 'Caso no encontrado.'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Cuerpo de la solicitud JSON inválido.'}, status=400)
        except ValueError as ve: # Para errores de conversión como float()
             return JsonResponse({'error': f'Error en el valor de un campo: {str(ve)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Ocurrió un error en el servidor: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Método no permitido. Solo PUT o PATCH son aceptados.'}, status=405)


# Vista para eliminar un caso existente (Delete)
@csrf_exempt # REMOVE/REPLACE con proper CSRF for production
def eliminar_caso_vista(request, caso_id):
    if request.method == 'DELETE':
        try:
            caso_obj = CrowdCaso.objects.get(id=caso_id)

            # --- INICIO Bloque de Autorización (Conceptual) ---
            # En una implementación real con autenticación:
            # if not request.user.is_authenticated:
            #     return JsonResponse({'error': 'Autenticación requerida.'}, status=401)
            # if caso_obj.creador != request.user: # Asumiendo que request.user es una instancia de CrowdUsuario
            #     return JsonResponse({'error': 'No tiene permiso para eliminar este caso.'}, status=403)
            # --- FIN Bloque de Autorización ---

            caso_obj.delete()
            return JsonResponse({'mensaje': 'Caso eliminado exitosamente.'}, status=200) # O 204 No Content

        except CrowdCaso.DoesNotExist:
            return JsonResponse({'error': 'Caso no encontrado.'}, status=404)
        except Exception as e:
            # Loggear el error e
            return JsonResponse({'error': f'Ocurrió un error en el servidor: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Método no permitido. Solo DELETE es aceptado.'}, status=405)


# Placeholder para la vista de login
@csrf_exempt # REMOVE/REPLACE con proper CSRF for production
def login_usuario_vista(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_morelia_o_email = data.get('id_morelia_o_email') # Permitir login con ID Morelia o email
            password_ingresada = data.get('password')

            if not all([id_morelia_o_email, password_ingresada]):
                return JsonResponse({'error': 'Se requiere ID Morelia/email y contraseña.'}, status=400)

            usuario_encontrado = None
            if '@' in id_morelia_o_email: # Asumimos que es un email
                try:
                    usuario_encontrado = CrowdUsuario.objects.get(email=id_morelia_o_email)
                except CrowdUsuario.DoesNotExist:
                    pass # El error se maneja abajo
            else: # Asumimos que es ID Morelia
                try:
                    usuario_encontrado = CrowdUsuario.objects.get(id_morelia=id_morelia_o_email)
                except CrowdUsuario.DoesNotExist:
                    pass # El error se maneja abajo

            if usuario_encontrado and check_password(password_ingresada, usuario_encontrado.password):
                if not usuario_encontrado.activo:
                     return JsonResponse({'error': 'La cuenta no está activa.'}, status=403) # 403 Forbidden

                # Aquí se manejaría la sesión. Para una API sin estado, se podría devolver un token (JWT).
                # Para Django con sesiones:
                # from django.contrib.auth import login
                # login(request, usuario_encontrado) # Esto requiere que CrowdUsuario sea compatible con el backend de auth de Django
                # Por ahora, solo devolvemos un mensaje de éxito. La gestión de sesión/token es un paso adicional.

                return JsonResponse({
                    'mensaje': 'Inicio de sesión exitoso.',
                    'usuario': {
                        'id_morelia': usuario_encontrado.id_morelia,
                        'email': usuario_encontrado.email,
                        'first_name': usuario_encontrado.first_name,
                        'last_name': usuario_encontrado.last_name,
                        # No devolver la contraseña hasheada ni información sensible no necesaria.
                    }
                })
            else:
                return JsonResponse({'error': 'Credenciales inválidas.'}, status=401) # 401 Unauthorized

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Cuerpo de la solicitud JSON inválido.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Ocurrió un error en el servidor: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Método no permitido. Solo POST es aceptado.'}, status=405)
