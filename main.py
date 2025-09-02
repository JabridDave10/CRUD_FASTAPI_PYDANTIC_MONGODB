from fastapi import FastAPI, HTTPException
import sys
import os
from typing import Dict, Any

# Agregar el directorio models al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'models'))

from Paciente import Paciente
from Especialidad import Especialidad
from Doctor import Doctor
from Historial import Historial
from Cita import Cita

# Importar servicio de MongoDB
import service_mongo as service

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc")

# ===========================================
# CRUD Paciente
# ===========================================
@app.post("/paciente")
def crear_paciente(paciente: Paciente):
    paciente_id = service.crear_paciente(paciente.model_dump())
    if paciente_id:
        return {
            "message": "Paciente creado exitosamente",
            "id_paciente": paciente_id,
            "data": paciente.model_dump()
        }
    raise HTTPException(status_code=400, detail="Error al crear el paciente")

@app.get("/paciente")
def obtener_pacientes():
    pacientes = service.obtener_pacientes()
    return {
        "message": "Lista de pacientes",
        "data": pacientes
    }

@app.get("/paciente/{paciente_id}")
def obtener_paciente(paciente_id: str):
    paciente = service.obtener_paciente(paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return {
        "message": f"Paciente {paciente_id}",
        "data": paciente
    }

@app.put("/paciente/{paciente_id}")
def actualizar_paciente(paciente_id: str, paciente: Paciente):
    if service.actualizar_paciente(paciente_id, paciente.model_dump()):
        return {
            "message": f"Paciente {paciente_id} actualizado exitosamente",
            "data": paciente.model_dump()
        }
    raise HTTPException(status_code=404, detail="Paciente no encontrado")

@app.patch("/paciente/{paciente_id}")
def actualizar_paciente_parcial(paciente_id: str, paciente_data: Dict[str, Any]):
    """Actualizar solo campos específicos del paciente"""
    if service.actualizar_paciente(paciente_id, paciente_data):
        return {
            "message": f"Paciente {paciente_id} actualizado parcialmente exitosamente",
            "data": paciente_data
        }
    raise HTTPException(status_code=404, detail="Paciente no encontrado")

@app.delete("/paciente/{paciente_id}")
def eliminar_paciente(paciente_id: str):
    if service.eliminar_paciente(paciente_id):
        return {
            "message": f"Paciente {paciente_id} eliminado exitosamente"
        }
    raise HTTPException(status_code=404, detail="Paciente no encontrado")

# ===========================================
# CRUD Especialidad
# ===========================================
@app.post("/especialidad")
def crear_especialidad(especialidad: Especialidad):
    especialidad_id = service.crear_especialidad(especialidad.model_dump())
    if especialidad_id:
        return {
            "message": "Especialidad creada exitosamente",
            "id_especialidad": especialidad_id,
            "data": especialidad.model_dump()
        }
    raise HTTPException(status_code=400, detail="Error al crear la especialidad")

@app.get("/especialidad")
def obtener_especialidades():
    especialidades = service.obtener_especialidades()
    return {
        "message": "Lista de especialidades",
        "data": especialidades
    }

@app.get("/especialidad/{especialidad_id}")
def obtener_especialidad(especialidad_id: str):
    especialidad = service.obtener_especialidad(especialidad_id)
    if not especialidad:
        raise HTTPException(status_code=404, detail="Especialidad no encontrada")
    return {
        "message": f"Especialidad {especialidad_id}",
        "data": especialidad
    }

@app.put("/especialidad/{especialidad_id}")
def actualizar_especialidad(especialidad_id: str, especialidad: Especialidad):
    if service.actualizar_especialidad(especialidad_id, especialidad.model_dump()):
        return {
            "message": f"Especialidad {especialidad_id} actualizada exitosamente",
            "data": especialidad.model_dump()
        }
    raise HTTPException(status_code=404, detail="Especialidad no encontrada")

@app.patch("/especialidad/{especialidad_id}")
def actualizar_especialidad_parcial(especialidad_id: str, especialidad_data: Dict[str, Any]):
    """Actualizar solo campos específicos de la especialidad"""
    if service.actualizar_especialidad(especialidad_id, especialidad_data):
        return {
            "message": f"Especialidad {especialidad_id} actualizada parcialmente exitosamente",
            "data": especialidad_data
        }
    raise HTTPException(status_code=404, detail="Especialidad no encontrada")

@app.delete("/especialidad/{especialidad_id}")
def eliminar_especialidad(especialidad_id: str):
    if service.eliminar_especialidad(especialidad_id):
        return {
            "message": f"Especialidad {especialidad_id} eliminada exitosamente"
        }
    raise HTTPException(status_code=404, detail="Especialidad no encontrada")

# ===========================================
# CRUD Doctor
# ===========================================
@app.post("/doctor")
def crear_doctor(doctor: Doctor):
    doctor_id = service.crear_doctor(doctor.model_dump())
    if doctor_id:
        return {
            "message": "Doctor creado exitosamente",
            "id_doctor": doctor_id,
            "data": doctor.model_dump()
        }
    raise HTTPException(status_code=400, detail="Error al crear el doctor")

@app.get("/doctor")
def obtener_doctores():
    doctores = service.obtener_doctores()
    return {
        "message": "Lista de doctores",
        "data": doctores
    }

@app.get("/doctor/{doctor_id}")
def obtener_doctor(doctor_id: str):
    doctor = service.obtener_doctor(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return {
        "message": f"Doctor {doctor_id}",
        "data": doctor
    }

@app.put("/doctor/{doctor_id}")
def actualizar_doctor(doctor_id: str, doctor: Doctor):
    if service.actualizar_doctor(doctor_id, doctor.model_dump()):
        return {
            "message": f"Doctor {doctor_id} actualizado exitosamente",
            "data": doctor.model_dump()
        }
    raise HTTPException(status_code=404, detail="Doctor no encontrado")

@app.patch("/doctor/{doctor_id}")
def actualizar_doctor_parcial(doctor_id: str, doctor_data: Dict[str, Any]):
    """Actualizar solo campos específicos del doctor"""
    if service.actualizar_doctor(doctor_id, doctor_data):
        return {
            "message": f"Doctor {doctor_id} actualizado parcialmente exitosamente",
            "data": doctor_data
        }
    raise HTTPException(status_code=404, detail="Doctor no encontrado")

@app.delete("/doctor/{doctor_id}")
def eliminar_doctor(doctor_id: str):
    if service.eliminar_doctor(doctor_id):
        return {
            "message": f"Doctor {doctor_id} eliminado exitosamente"
        }
    raise HTTPException(status_code=404, detail="Doctor no encontrado")

# ===========================================
# CRUD Historial
# ===========================================
@app.post("/historial")
def crear_historial(historial: Historial):
    historial_id = service.crear_historial(historial.model_dump())
    if historial_id:
        return {
            "message": "Historial creado exitosamente",
            "id_historial": historial_id,
            "data": historial.model_dump()
        }
    raise HTTPException(status_code=400, detail="Error al crear el historial")

@app.get("/historial")
def obtener_historiales():
    historiales = service.obtener_historiales()
    return {
        "message": "Lista de historiales",
        "data": historiales
    }

@app.get("/historial/{historial_id}")
def obtener_historial(historial_id: str):
    historial = service.obtener_historial(historial_id)
    if not historial:
        raise HTTPException(status_code=404, detail="Historial no encontrado")
    return {
        "message": f"Historial {historial_id}",
        "data": historial
    }

@app.put("/historial/{historial_id}")
def actualizar_historial(historial_id: str, historial: Historial):
    if service.actualizar_historial(historial_id, historial.model_dump()):
        return {
            "message": f"Historial {historial_id} actualizado exitosamente",
            "data": historial.model_dump()
        }
    raise HTTPException(status_code=404, detail="Historial no encontrado")

@app.patch("/historial/{historial_id}")
def actualizar_historial_parcial(historial_id: str, historial_data: Dict[str, Any]):
    """Actualizar solo campos específicos del historial"""
    if service.actualizar_historial(historial_id, historial_data):
        return {
            "message": f"Historial {historial_id} actualizado parcialmente exitosamente",
            "data": historial_data
        }
    raise HTTPException(status_code=404, detail="Historial no encontrado")

@app.delete("/historial/{historial_id}")
def eliminar_historial(historial_id: str):
    if service.eliminar_historial(historial_id):
        return {
            "message": f"Historial {historial_id} eliminado exitosamente"
        }
    raise HTTPException(status_code=404, detail="Historial no encontrado")

# ===========================================
# CRUD Cita
# ===========================================
@app.post("/cita")
def crear_cita(cita: Cita):
    cita_id = service.crear_cita(cita.model_dump())
    if cita_id:
        return {
            "message": "Cita creada exitosamente",
            "id_cita": cita_id,
            "data": cita.model_dump()
        }
    raise HTTPException(status_code=400, detail="Error al crear la cita")

@app.get("/cita")
def obtener_citas():
    citas = service.obtener_citas()
    return {
        "message": "Lista de citas",
        "data": citas
    }

@app.get("/cita/{cita_id}")
def obtener_cita(cita_id: str):
    cita = service.obtener_cita(cita_id)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return {
        "message": f"Cita {cita_id}",
        "data": cita
    }

@app.put("/cita/{cita_id}")
def actualizar_cita(cita_id: str, cita: Cita):
    if service.actualizar_cita(cita_id, cita.model_dump()):
        return {
            "message": f"Cita {cita_id} actualizada exitosamente",
            "data": cita.model_dump()
        }
    raise HTTPException(status_code=404, detail="Cita no encontrada")

@app.patch("/cita/{cita_id}")
def actualizar_cita_parcial(cita_id: str, cita_data: Dict[str, Any]):
    """Actualizar solo campos específicos de la cita"""
    if service.actualizar_cita(cita_id, cita_data):
        return {
            "message": f"Cita {cita_id} actualizada parcialmente exitosamente",
            "data": cita_data
        }
    raise HTTPException(status_code=404, detail="Cita no encontrada")

@app.delete("/cita/{cita_id}")
def eliminar_cita(cita_id: str):
    if service.eliminar_cita(cita_id):
        return {
            "message": f"Cita {cita_id} eliminada exitosamente"
        }
    raise HTTPException(status_code=404, detail="Cita no encontrada")
