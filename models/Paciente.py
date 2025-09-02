from pydantic import BaseModel, Field, constr, validator
from typing import Optional
from datetime import datetime
import re

class Paciente(BaseModel):
    id_paciente: int = Field(..., description="ID único del paciente")
    nombre: constr(strip_whitespace=True, min_length=2, max_length=50) = Field(..., description="Nombre del paciente")
    apellido: constr(strip_whitespace=True, min_length=2, max_length=50) = Field(..., description="Apellido del paciente")
    fecha_nacimiento: datetime = Field(..., description="Fecha de nacimiento del paciente")
    telefono: Optional[constr(strip_whitespace=True, max_length=20)] = Field(None, description="Teléfono del paciente")
    email: constr(strip_whitespace=True, max_length=100) = Field(..., description="Email del paciente")
    direccion: constr(strip_whitespace=True, max_length=200) = Field(..., description="Dirección del paciente")
    
    @validator('nombre')
    def validar_nombre(cls, v):
        # Solo permite letras, espacios y algunos caracteres especiales comunes en nombres
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\'-]+$', v):
            raise ValueError('El nombre solo puede contener letras, espacios, guiones y apóstrofes')
        return v.strip()
    
    @validator('apellido')
    def validar_apellido(cls, v):
        # Solo permite letras, espacios y algunos caracteres especiales comunes en apellidos
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\'-]+$', v):
            raise ValueError('El apellido solo puede contener letras, espacios, guiones y apóstrofes')
        return v.strip()
    
    class Config:
        from_attributes = True
