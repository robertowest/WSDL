
from zeep import Client
from zeep.exceptions import Fault
from zeep.transports import Transport

from SEOGA.models import ActoMedico, DetalleLiquidacion

T = TypeVar('T')


class SEOGA:
    def __init__(self, token=None):
        self.wsdl = 'https://www.seoga.es/ws/SEOGAPlataforma.svc?wsdl'
        self.token = token

    def conectar(self):
        self.client = Client(self.wsdl)

    def desconectar(self):
        self.client.transport.session.close()

    def _dataclass_from_dict(self, klass: Type[T], dikt: Dict[str, Any]) -> T:
        """Este es un método interno. No debería ser accedido desde fuera de la clase."""
        try:
            fieldtypes = {f.name: f.type for f in klass.__dataclass_fields__.values()}
            return klass(**{f: dikt[f] for f in fieldtypes.keys()})
        except Exception as e:
            print(f"Error al mapear datos a {klass.__name__}: {e}")
            raise

    def obtener_actividad_diaria(self, anyo, mes, dia) -> List[ActoMedico]:
        try:
            resultado = self.client.service.ObtenerActividadDiaria(self.token, anyo, mes, dia)
            # Verificar si la respuesta es una lista
            if isinstance(resultado, list):
                return [self._dataclass_from_dict(ActoMedico, item) for item in resultado]
        except Exception as e:
            raise e
        
    def obtener_detalle_liquidacion_mensual(self, anyo, mes) -> List[DetalleLiquidacion]:
        try:
            resultado = self.client.service.ObtenerDetalleLiquidacionMensual(self.token, anyo, mes)
            # Verificar si la respuesta es una lista
            if isinstance(resultado, list):
                return [self._dataclass_from_dict(DetalleLiquidacion, item) for item in resultado]
        except Exception as e:
            raise e


if __name__ == '__main__':
    # obtenemos el token ( select * from t_config where id=69 )
    cliente = SEOGA('TKS|vmpg66ZrjEgNaRYLNpX8aQVGQYViCnkDnSxsbHEPV9mFvd4P63n9Ht/BWp4vmlXwBEXzZPnMewXf0cREsojOfSzuinIrmy180pN7OrCiDZy+vKVUJa0cd1a74LI=')
    # abrir la conexión una sola vez
    cliente.conectar()
    try:
        # # realizar múltiples llamadas
        # for dia in range(1, 31):  # todos los días de mayo/2024
        #     actos_medicos = cliente.obtener_actividad_diaria(2024, 5, dia)
        #     if actos_medicos:
        #         for acto in actos_medicos:
        #             print(f"Paciente: {acto.Nombre_Paciente} {acto.Apellidos_Paciente}, Acto: {acto.Nombre_Acto}")
        actos_medicos = cliente.obtener_actividad_diaria(2024, 5, 1)
        if actos_medicos:
            for acto in actos_medicos:
                print(f"Paciente: {acto.Nombre_Paciente} {acto.Apellidos_Paciente}, Acto: {acto.Nombre_Acto}")

        # obtenemos el detalle de liquidación
        liquidacion = cliente.obtener_detalle_liquidacion_mensual(2024, 7)
        if liquidacion:
            print(f'Factura: {liquidacion.Numero_Autofactura}, Importe: {liquidacion.Importe_Cobrado}')

    except Fault as e:
        print(f'Error: {e}')

    except Exception as e:
        print(f'Error inesperado: {e}')

    finally:
        # Cerrar la conexión al finalizar todas las operaciones
        cliente.desconectar()
