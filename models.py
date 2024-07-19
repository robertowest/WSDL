from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional

@dataclass
class ActoMedico:
    Apellidos_Paciente: str
    Codigo_Acto: str
    Codigo_Acto_Liquidacion: Optional[str]
    Codigo_Especialidad: str
    Codigo_ListaActos: str
    Conciliado: bool
    DNI_Paciente: str
    Episodio: str
    Estado_Incidencia: Optional[str]
    Fecha: datetime
    Fecha_Creacion: datetime
    Fecha_Liquidacion: Optional[datetime]
    Fecha_Registro_Liquidacion: Optional[datetime]
    Id_Acto: int
    Id_ActoVisita: int
    Id_Companhia: int
    Id_Incidencia: Optional[int]
    Id_Paciente: int
    Id_Sede: int
    Id_Tarifa: Optional[int]
    Id_Visita: int
    Importe_Cobrado: Optional[Decimal]
    Importe_Esperado: Decimal
    Incidencia_Detectada: bool
    Info_Complementaria: str
    Nombre_Acto: str
    Nombre_Acto_Liquidacion: Optional[str]
    Nombre_Companhia: str
    Nombre_Especialidad: str
    Nombre_Paciente: str
    Nombre_Sede: str
    Nombre_Tarifa: Optional[str]
    NumeroHCPaciente: str
    Numero_Operacion: str
    Numero_Tarjeta: Optional[str]
    Observaciones: Optional[str]
    Reclamable_Incidencia: Optional[str]
    Tipo_Incidencia: Optional[str]


@dataclass
class DetalleLiquidacion:
    Apellidos_Paciente: str
    Codigo_Acto: int
    Codigo_Acto_Liquidacion: str
    Codigo_Especialidad: int
    Codigo_ListaActos: Optional[int]
    DNI_Paciente: str
    Episodio: str
    Estado_Incidencia: int
    Fecha: datetime
    Fecha_Creacion: datetime
    Fecha_Liquidacion: datetime
    Fecha_Registro_Liquidacion: datetime
    Id_Acto: int
    Id_ActoVisita: int
    Id_Companhia: int
    Id_Incidencia: int
    Id_Paciente: int
    Id_Sede: int
    Id_Tarifa: Optional[int]
    Id_Visita: int
    Importe_Cobrado: Decimal
    Importe_Esperado: Decimal
    Incidencia_Detectada: bool
    Info_Complementaria: str
    Nombre_Acto: str
    Nombre_Acto_Liquidacion: str
    Nombre_Companhia: str
    Nombre_Especialidad: str
    Nombre_Paciente: str
    Nombre_Sede: str
    Nombre_Tarifa: Optional[int]
    NumeroHCPaciente: str
    Numero_Autofactura: str
    Numero_Operacion: int
    Numero_Tarjeta: str
    Observaciones: Optional[str]
    Observaciones_Companhia: Optional[str]
    Reclamable_Incidencia: bool
    Referencia_Facturacion_Centro: Optional[str]
    Referencia_Facturacion_Companhia: Optional[str]
    Referencia_Liquidacion: str
    Tipo_Incidencia: int
    Tramitado_Seoga: bool
