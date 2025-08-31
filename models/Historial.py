from pydantic import BaseModel, Field, constr, conint
from typing import Optional
from datetime import date

class Historial(BaseModel):
    id_historial: Optional[int] = Field(None, description="ID único del historial")
    fecha: date = Field(..., description="Fecha del historial médico")
    diagnostico: Optional[constr(strip_whitespace=True, max_length=1000)] = Field(None, description="Diagnóstico del paciente")
    tratamiento: Optional[constr(strip_whitespace=True, max_length=1000)] = Field(None, description="Tratamiento aplicado")
    observaciones: Optional[constr(strip_whitespace=True, max_length=2000)] = Field(None, description="Observaciones adicionales")
    id_paciente: conint(gt=0) = Field(..., description="ID del paciente")
    id_doctor: conint(gt=0) = Field(..., description="ID del doctor")
    
    class Config:
        from_attributes = True
