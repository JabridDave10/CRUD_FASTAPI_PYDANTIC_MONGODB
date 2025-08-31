from pydantic import BaseModel, Field, constr, conint
from typing import Optional

class Doctor(BaseModel):
    id_doctor: Optional[int] = Field(None, description="ID único del doctor")
    nombre: constr(strip_whitespace=True, min_length=2, max_length=50) = Field(..., description="Nombre del doctor")
    apellido: constr(strip_whitespace=True, min_length=2, max_length=50) = Field(..., description="Apellido del doctor")
    telefono: Optional[constr(strip_whitespace=True, max_length=20)] = Field(None, description="Teléfono del doctor")
    email: Optional[constr(strip_whitespace=True, max_length=100)] = Field(None, description="Email del doctor")
    id_especialidad: conint(gt=0) = Field(..., description="ID de la especialidad del doctor")
    
    class Config:
        from_attributes = True
