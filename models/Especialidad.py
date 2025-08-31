from pydantic import BaseModel, Field, constr
from typing import Optional

class Especialidad(BaseModel):
    id_especialidad: Optional[int] = Field(None, description="ID único de la especialidad")
    nombre: constr(strip_whitespace=True, min_length=3, max_length=100) = Field(..., description="Nombre de la especialidad")
    descripcion: Optional[constr(strip_whitespace=True, max_length=500)] = Field(None, description="Descripción de la especialidad")
    
    class Config:
        from_attributes = True
