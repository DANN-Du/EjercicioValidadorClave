from abc import ABC, abstractmethod


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave):
        return any(char.isupper() for char in clave)

    def _contiene_minuscula(self, clave):
        return any(char.islower() for char in clave)

    def _contiene_numero(self, clave):
        return any(char.isdigit() for char in clave)

    @abstractmethod
    def es_valida(self, clave):
        pass
class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=8)

    def _contiene_caracter_especial(self, clave):
        especiales = '@_#$%'
        return any(char in especiales for char in clave)

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise Exception("La clave debe tener una longitud de más de 8 caracteres")
        if not self._contiene_mayuscula(clave):
            raise Exception("La clave debe contener al menos una letra mayúscula")
        if not self._contiene_minuscula(clave):
            raise Exception("La clave debe contener al menos una letra minúscula")
        if not self._contiene_numero(clave):
            raise Exception("La clave debe contener al menos un número")
        if not self._contiene_caracter_especial(clave):
            raise Exception("La clave debe contener al menos un caracter especial (@, _, #, $, %)")
        return True

