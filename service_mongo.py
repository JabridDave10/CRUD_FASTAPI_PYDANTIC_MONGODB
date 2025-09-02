import database
from typing import List, Optional, Dict, Any
from datetime import datetime

# ===========================================
# CRUD para Paciente
# ===========================================
def crear_paciente(paciente_data: Dict[str, Any]) -> Optional[str]:
    """Crear un nuevo paciente"""
    try:
        # Convertir fecha_nacimiento a datetime si es date o string
        if 'fecha_nacimiento' in paciente_data:
            from datetime import datetime, date
            fecha_valor = paciente_data['fecha_nacimiento']
            
            if isinstance(fecha_valor, date):
                # Convertir date a datetime (MongoDB no soporta date directamente)
                paciente_data['fecha_nacimiento'] = datetime.combine(fecha_valor, datetime.min.time())
            elif isinstance(fecha_valor, str):
                try:
                    # Intentar parsear la fecha en formato ISO (YYYY-MM-DD)
                    fecha = datetime.fromisoformat(fecha_valor)
                    paciente_data['fecha_nacimiento'] = fecha
                except ValueError:
                    # Si falla, intentar con otros formatos comunes
                    try:
                        fecha = datetime.strptime(fecha_valor, '%d/%m/%Y')
                        paciente_data['fecha_nacimiento'] = fecha
                    except ValueError:
                        print(f"Error: Formato de fecha inválido: {fecha_valor}")
                        return None
        
        paciente_id = database.insert_document("paciente", paciente_data)
        return paciente_id
    except Exception as e:
        print(f"Error creando paciente: {e}")
        return None

def obtener_pacientes() -> List[Dict[str, Any]]:
    """Obtener todos los pacientes"""
    return database.find_documents("paciente")

def obtener_paciente(paciente_id: str) -> Optional[Dict[str, Any]]:
    """Obtener un paciente por ID"""
    return database.find_document_by_id("paciente", paciente_id)

def actualizar_paciente(paciente_id: str, paciente_data: Dict[str, Any]) -> bool:
    """Actualizar un paciente"""
    try:
        # Convertir fecha_nacimiento a datetime si es date o string
        if 'fecha_nacimiento' in paciente_data:
            from datetime import datetime, date
            fecha_valor = paciente_data['fecha_nacimiento']
            
            if isinstance(fecha_valor, date):
                # Convertir date a datetime (MongoDB no soporta date directamente)
                paciente_data['fecha_nacimiento'] = datetime.combine(fecha_valor, datetime.min.time())
            elif isinstance(fecha_valor, str):
                try:
                    # Intentar parsear la fecha en formato ISO (YYYY-MM-DD)
                    fecha = datetime.fromisoformat(fecha_valor)
                    paciente_data['fecha_nacimiento'] = fecha
                except ValueError:
                    # Si falla, intentar con otros formatos comunes
                    try:
                        fecha = datetime.strptime(fecha_valor, '%d/%m/%Y')
                        paciente_data['fecha_nacimiento'] = fecha
                    except ValueError:
                        print(f"Error: Formato de fecha inválido: {fecha_valor}")
                        return False
        
        return database.update_document("paciente", paciente_id, paciente_data)
    except Exception as e:
        print(f"Error actualizando paciente: {e}")
        return False

def eliminar_paciente(paciente_id: str) -> bool:
    """Eliminar un paciente"""
    return database.delete_document("paciente", paciente_id)

# ===========================================
# CRUD para Especialidad
# ===========================================
def crear_especialidad(especialidad_data: Dict[str, Any]) -> Optional[str]:
    """Crear una nueva especialidad"""
    try:
        especialidad_id = database.insert_document("especialidades", especialidad_data)
        return especialidad_id
    except Exception as e:
        print(f"Error creando especialidad: {e}")
        return None

def obtener_especialidades() -> List[Dict[str, Any]]:
    """Obtener todas las especialidades"""
    return database.find_documents("especialidades")

def obtener_especialidad(especialidad_id: str) -> Optional[Dict[str, Any]]:
    """Obtener una especialidad por ID"""
    return database.find_document_by_id("especialidades", especialidad_id)

def actualizar_especialidad(especialidad_id: str, especialidad_data: Dict[str, Any]) -> bool:
    """Actualizar una especialidad"""
    try:
        return database.update_document("especialidades", especialidad_id, especialidad_data)
    except Exception as e:
        print(f"Error actualizando especialidad: {e}")
        return False

def eliminar_especialidad(especialidad_id: str) -> bool:
    """Eliminar una especialidad"""
    return database.delete_document("especialidades", especialidad_id)

# ===========================================
# CRUD para Doctor
# ===========================================
def crear_doctor(doctor_data: Dict[str, Any]) -> Optional[str]:
    """Crear un nuevo doctor"""
    try:
        doctor_id = database.insert_document("doctor", doctor_data)
        return doctor_id
    except Exception as e:
        print(f"Error creando doctor: {e}")
        return None

def obtener_doctores() -> List[Dict[str, Any]]:
    """Obtener todos los doctores"""
    return database.find_documents("doctor")

def obtener_doctor(doctor_id: str) -> Optional[Dict[str, Any]]:
    """Obtener un doctor por ID"""
    return database.find_document_by_id("doctor", doctor_id)

def actualizar_doctor(doctor_id: str, doctor_data: Dict[str, Any]) -> bool:
    """Actualizar un doctor"""
    try:
        return database.update_document("doctor", doctor_id, doctor_data)
    except Exception as e:
        print(f"Error actualizando doctor: {e}")
        return False

def eliminar_doctor(doctor_id: str) -> bool:
    """Eliminar un doctor"""
    return database.delete_document("doctores", doctor_id)

# ===========================================
# CRUD para Historial
# ===========================================
def crear_historial(historial_data: Dict[str, Any]) -> Optional[str]:
    """Crear un nuevo historial"""
    try:
        # Convertir fecha a string si es date
        if hasattr(historial_data, 'fecha'):
            historial_data['fecha'] = str(historial_data['fecha'])
        
        historial_id = database.insert_document("historiales", historial_data)
        return historial_id
    except Exception as e:
        print(f"Error creando historial: {e}")
        return None

def obtener_historiales() -> List[Dict[str, Any]]:
    """Obtener todos los historiales"""
    return database.find_documents("historiales")

def obtener_historial(historial_id: str) -> Optional[Dict[str, Any]]:
    """Obtener un historial por ID"""
    return database.find_document_by_id("historiales", historial_id)

def actualizar_historial(historial_id: str, historial_data: Dict[str, Any]) -> bool:
    """Actualizar un historial"""
    try:
        # Convertir fecha a string si es date
        if hasattr(historial_data, 'fecha'):
            historial_data['fecha'] = str(historial_data['fecha'])
        
        return database.update_document("historiales", historial_id, historial_data)
    except Exception as e:
        print(f"Error actualizando historial: {e}")
        return False

def eliminar_historial(historial_id: str) -> bool:
    """Eliminar un historial"""
    return database.delete_document("historiales", historial_id)

# ===========================================
# CRUD para Cita
# ===========================================
def crear_cita(cita_data: Dict[str, Any]) -> Optional[str]:
    """Crear una nueva cita"""
    try:
        # Convertir fecha_hora a string si es datetime
        if hasattr(cita_data, 'fecha_hora'):
            cita_data['fecha_hora'] = str(cita_data['fecha_hora'])
        
        cita_id = database.insert_document("cita", cita_data)
        return cita_id
    except Exception as e:
        print(f"Error creando cita: {e}")
        return None

def obtener_citas() -> List[Dict[str, Any]]:
    """Obtener todas las citas"""
    return database.find_documents("cita")

def obtener_cita(cita_id: str) -> Optional[Dict[str, Any]]:
    """Obtener una cita por ID"""
    return database.find_document_by_id("cita", cita_id)

def actualizar_cita(cita_id: str, cita_data: Dict[str, Any]) -> bool:
    """Actualizar una cita"""
    try:
        # Convertir fecha_hora a string si es datetime
        if hasattr(cita_data, 'fecha_hora'):
            cita_data['fecha_hora'] = str(cita_data['fecha_hora'])
        
        return database.update_document("cita", cita_id, cita_data)
    except Exception as e:
        print(f"Error actualizando cita: {e}")
        return False

def eliminar_cita(cita_id: str) -> bool:
    """Eliminar una cita"""
    return database.delete_document("cita", cita_id)
