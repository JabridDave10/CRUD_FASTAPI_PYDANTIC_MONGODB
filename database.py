from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from typing import Optional, Dict, List, Any
import os
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de MongoDB
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE")
}

# Variable global para la conexión
client = None
db = None

def get_connection():
    """Obtiene una conexión a MongoDB"""
    global client, db
    
    try:
        # Construir la URI de conexión
        if DB_CONFIG["host"].startswith("mongodb+srv://"):
            # Para MongoDB Atlas
            uri = DB_CONFIG["host"]
        else:
            # Para MongoDB local
            uri = f"mongodb://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}"
        
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        db = client[DB_CONFIG["database"]]
        
        # Verificar conexión
        client.admin.command('ping')
        print("✅ Conexión a MongoDB establecida")
        return True
        
    except (ConnectionFailure, ServerSelectionTimeoutError) as e:
        print(f"❌ Error conectando a MongoDB: {e}")
        return False

def get_database():
    """Obtiene la instancia de la base de datos"""
    global db
    if db is None:
        get_connection()
    return db

def get_collection(collection_name: str):
    """Obtiene una colección específica"""
    database = get_database()
    return database[collection_name]

def insert_document(collection_name: str, document: Dict[str, Any]) -> Optional[str]:
    """Inserta un documento en una colección y retorna el ID"""
    try:
        collection = get_collection(collection_name)
        # Agregar timestamp de creación
        document["created_at"] = datetime.utcnow()
        result = collection.insert_one(document)
        return str(result.inserted_id)
    except Exception as e:
        print(f"❌ Error insertando documento en {collection_name}: {e}")
        return None

def find_documents(collection_name: str, filter_dict: Dict[str, Any] = None) -> List[Dict[str, Any]]:
    """Busca documentos en una colección"""
    try:
        collection = get_collection(collection_name)
        filter_dict = filter_dict or {}
        documents = list(collection.find(filter_dict))
        
        # Convertir ObjectId a string para serialización JSON
        for doc in documents:
            if "_id" in doc:
                doc["_id"] = str(doc["_id"])
        
        return documents
    except Exception as e:
        print(f"❌ Error buscando documentos en {collection_name}: {e}")
        return []

def find_document_by_id(collection_name: str, document_id: str) -> Optional[Dict[str, Any]]:
    """Busca un documento por ID"""
    try:
        from bson import ObjectId
        collection = get_collection(collection_name)
        document = collection.find_one({"_id": ObjectId(document_id)})
        
        if document and "_id" in document:
            document["_id"] = str(document["_id"])
        
        return document
    except Exception as e:
        print(f"❌ Error buscando documento por ID en {collection_name}: {e}")
        return None

def update_document(collection_name: str, document_id: str, update_data: Dict[str, Any]) -> bool:
    """Actualiza un documento por ID"""
    try:
        from bson import ObjectId
        collection = get_collection(collection_name)
        
        # Agregar timestamp de actualización
        update_data["updated_at"] = datetime.utcnow()
        
        result = collection.update_one(
            {"_id": ObjectId(document_id)},
            {"$set": update_data}
        )
        return result.modified_count > 0
    except Exception as e:
        print(f"❌ Error actualizando documento en {collection_name}: {e}")
        return False

def delete_document(collection_name: str, document_id: str) -> bool:
    """Elimina un documento por ID"""
    try:
        from bson import ObjectId
        collection = get_collection(collection_name)
        result = collection.delete_one({"_id": ObjectId(document_id)})
        return result.deleted_count > 0
    except Exception as e:
        print(f"❌ Error eliminando documento en {collection_name}: {e}")
        return False

def initialize_database():
    """Inicializa la base de datos MongoDB creando las colecciones y datos de ejemplo"""
    print("🗄️  Inicializando base de datos MongoDB...")
    
    if not get_connection():
        return False
    
    try:
        database = get_database()
        
        # Crear colecciones si no existen
        collections = ["paciente", "especialidad", "doctor", "historial", "cita"]
        
        for collection_name in collections:
            if collection_name not in database.list_collection_names():
                database.create_collection(collection_name)
                print(f"✅ Colección '{collection_name}' creada")
        
        # Verificar si ya existen datos de ejemplo
        especialidad_count = database.especialidad.count_documents({})
        
        if especialidad_count == 0:
            print("📝 Insertando datos de ejemplo...")
            
            # Insertar especialidades de ejemplo
            especialidad = [
                {
                    "nombre": "Cardiología",
                    "descripcion": "Especialidad médica que se encarga del diagnóstico y tratamiento de las enfermedades del corazón"
                },
                {
                    "nombre": "Dermatología", 
                    "descripcion": "Especialidad médica que se encarga del diagnóstico y tratamiento de las enfermedades de la piel"
                },
                {
                    "nombre": "Pediatría",
                    "descripcion": "Especialidad médica que se encarga del cuidado de la salud de los niños"
                },
                {
                    "nombre": "Ginecología",
                    "descripcion": "Especialidad médica que se encarga de la salud del sistema reproductor femenino"
                },
                {
                    "nombre": "Ortopedia",
                    "descripcion": "Especialidad médica que se encarga del diagnóstico y tratamiento de lesiones y enfermedades del sistema musculoesquelético"
                }
            ]
            
            for especialidad in especialidad:
                insert_document("especialidad", especialidad)
            
            # Obtener IDs de especialidades para crear doctor
            especialidad_docs = find_documents("especialidad")
            
            # Insertar doctores de ejemplo
            doctor = [
                {
                    "nombre": "María",
                    "apellido": "García",
                    "telefono": "3001234567",
                    "email": "maria.garcia@clinica.com",
                    "id_especialidad": especialidad_docs[0]["_id"]
                },
                {
                    "nombre": "Carlos",
                    "apellido": "Rodríguez", 
                    "telefono": "3002345678",
                    "email": "carlos.rodriguez@clinica.com",
                    "id_especialidad": especialidad_docs[1]["_id"]
                },
                {
                    "nombre": "Ana",
                    "apellido": "López",
                    "telefono": "3003456789", 
                    "email": "ana.lopez@clinica.com",
                    "id_especialidad": especialidad_docs[2]["_id"]
                },
                {
                    "nombre": "Luis",
                    "apellido": "Martínez",
                    "telefono": "3004567890",
                    "email": "luis.martinez@clinica.com", 
                    "id_especialidad": especialidad_docs[3]["_id"]
                },
                {
                    "nombre": "Patricia",
                    "apellido": "Hernández",
                    "telefono": "3005678901",
                    "email": "patricia.hernandez@clinica.com",
                    "id_especialidad": especialidad_docs[4]["_id"]
                }
            ]
            
            for doctor in doctor:
                insert_document("doctor", doctor)
            
            # Insertar paciente de ejemplo
            paciente = [
                {
                    "nombre": "Juan",
                    "apellido": "Pérez",
                    "fecha_nacimiento": "1990-05-15",
                    "telefono": "3001111111",
                    "email": "juan.perez@email.com",
                    "direccion": "Calle 123 #45-67"
                },
                {
                    "nombre": "María",
                    "apellido": "González",
                    "fecha_nacimiento": "1985-08-22",
                    "telefono": "3002222222", 
                    "email": "maria.gonzalez@email.com",
                    "direccion": "Carrera 78 #90-12"
                },
                {
                    "nombre": "Pedro",
                    "apellido": "Sánchez",
                    "fecha_nacimiento": "1995-03-10",
                    "telefono": "3003333333",
                    "email": "pedro.sanchez@email.com",
                    "direccion": "Avenida 5 #23-45"
                },
                {
                    "nombre": "Ana",
                    "apellido": "Ramírez",
                    "fecha_nacimiento": "1988-12-05",
                    "telefono": "3004444444",
                    "email": "ana.ramirez@email.com",
                    "direccion": "Calle 67 #89-01"
                },
                {
                    "nombre": "Luis",
                    "apellido": "Torres",
                    "fecha_nacimiento": "1992-07-18",
                    "telefono": "3005555555",
                    "email": "luis.torres@email.com",
                    "direccion": "Carrera 34 #56-78"
                }
            ]
            
            for paciente in paciente:
                insert_document("paciente", paciente)
            
            print("✅ Datos de ejemplo insertados")
        else:
            print("ℹ️  Los datos de ejemplo ya existen")
        
        # Crear índices para optimizar consultas
        try:
            database.cita.create_index("fecha_hora")
            database.cita.create_index("id_paciente")
            database.cita.create_index("id_doctor")
            database.historial.create_index("id_paciente")
            database.historial.create_index("fecha")
            database.doctor.create_index("id_especialidad")
            print("✅ Índices creados/verificados")
        except Exception as e:
            print(f"⚠️  Advertencia creando índices: {e}")
        
        print("🎉 Base de datos MongoDB inicializada correctamente")
        return True
        
    except Exception as e:
        print(f"❌ Error inicializando base de datos MongoDB: {e}")
        return False

def close_connection():
    """Cierra la conexión a MongoDB"""
    global client
    if client:
        client.close()
        print("🔌 Conexión a MongoDB cerrada")
