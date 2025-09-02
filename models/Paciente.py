from pydantic import BaseModel, Field, constr
from typing import Optional
from datetime import datetime

class Paciente(BaseModel):
    id_paciente: int = Field(..., description="ID único del paciente")
    nombre: constr(strip_whitespace=True, min_length=2, max_length=50) = Field(..., description="Nombre del paciente")
    apellido: constr(strip_whitespace=True, min_length=2, max_length=50) = Field(..., description="Apellido del paciente")
    fecha_nacimiento: datetime = Field(..., description="Fecha de nacimiento del paciente")
    telefono: Optional[constr(strip_whitespace=True, max_length=20)] = Field(None, description="Teléfono del paciente")
    email: constr(strip_whitespace=True, max_length=100) = Field(..., description="Email del paciente")
    direccion: constr(strip_whitespace=True, max_length=200) = Field(..., description="Dirección del paciente")
    
    class Config:
        from_attributes = True
