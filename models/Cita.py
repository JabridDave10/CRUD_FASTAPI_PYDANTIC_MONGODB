from pydantic import BaseModel, Field, constr, conint
from typing import Optional
from datetime import datetime

class Cita(BaseModel):
    id_cita: Optional[int] = Field(None, description="ID único de la cita")
    fecha_hora: datetime = Field(..., description="Fecha y hora de la cita")
    motivo: Optional[constr(strip_whitespace=True, max_length=500)] = Field(None, description="Motivo de la cita")
    id_paciente: conint(gt=0) = Field(..., description="ID del paciente")
    id_doctor: conint(gt=0) = Field(..., description="ID del doctor")
    
    class Config:
        from_attributes = True
