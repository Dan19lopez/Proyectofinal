import re
from datetime import datetime


class Validators:
    """
    Clase utilitaria para validaciones comunes del sistema
    """

    @staticmethod
    def validate_email(email):
        """
        Valida el formato de un email
        """
        if not email or email.strip() == "":
            return False, "El email no puede estar vacío"
        
        email = email.strip()
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(email_pattern, email):
            return False, "El formato del email no es válido"
        
        return True, "Email válido"

    @staticmethod
    def validate_phone(phone):
        """
        Valida el formato de un teléfono
        """
        if not phone or phone.strip() == "":
            return False, "El teléfono no puede estar vacío"
        
        phone = phone.strip()
        # Permite números con o sin espacios, guiones, paréntesis
        phone_pattern = r'^[\d\s\-\(\)\+]{7,15}$'
        
        if not re.match(phone_pattern, phone):
            return False, "El teléfono debe contener entre 7 y 15 dígitos"
        
        # Verificar que tenga al menos 7 dígitos
        digits_only = re.sub(r'[^\d]', '', phone)
        if len(digits_only) < 7:
            return False, "El teléfono debe contener al menos 7 dígitos"
        
        return True, "Teléfono válido"

    @staticmethod
    def validate_name(name, field_name="Nombre"):
        """
        Valida que un nombre no esté vacío y tenga longitud apropiada
        """
        if not name or name.strip() == "":
            return False, f"El {field_name.lower()} no puede estar vacío"
        
        name = name.strip()
        
        if len(name) < 2:
            return False, f"El {field_name.lower()} debe tener al menos 2 caracteres"
        
        if len(name) > 100:
            return False, f"El {field_name.lower()} no puede exceder 100 caracteres"
        
        # Verificar que solo contenga letras, espacios y algunos caracteres especiales
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\.\-\']+$', name):
            return False, f"El {field_name.lower()} solo puede contener letras, espacios, puntos, guiones y apostrofes"
        
        return True, f"{field_name} válido"

    @staticmethod
    def validate_description(description, max_length=255):
        """
        Valida una descripción
        """
        if not description or description.strip() == "":
            return False, "La descripción no puede estar vacía"
        
        description = description.strip()
        
        if len(description) < 3:
            return False, "La descripción debe tener al menos 3 caracteres"
        
        if len(description) > max_length:
            return False, f"La descripción no puede exceder {max_length} caracteres"
        
        return True, "Descripción válida"

    @staticmethod
    def validate_value(value_str):
        """
        Valida un valor monetario
        """
        if not value_str or value_str.strip() == "":
            return False, "El valor no puede estar vacío"
        
        try:
            value = float(value_str.strip())
            if value < 0:
                return False, "El valor no puede ser negativo"
            if value > 999999.99:
                return False, "El valor no puede exceder 999,999.99"
            return True, "Valor válido"
        except ValueError:
            return False, "El valor debe ser un número válido"

    @staticmethod
    def validate_date(date_str, date_format="%Y-%m-%d"):
        """
        Valida una fecha en formato específico
        """
        if not date_str or date_str.strip() == "":
            return False, "La fecha no puede estar vacía"
        
        try:
            date_obj = datetime.strptime(date_str.strip(), date_format)
            return True, "Fecha válida"
        except ValueError:
            return False, f"La fecha debe estar en formato {date_format}"

    @staticmethod
    def validate_future_date(date_str, date_format="%Y-%m-%d"):
        """
        Valida que una fecha sea futura
        """
        is_valid, message = Validators.validate_date(date_str, date_format)
        if not is_valid:
            return is_valid, message
        
        try:
            date_obj = datetime.strptime(date_str.strip(), date_format)
            if date_obj.date() <= datetime.now().date():
                return False, "La fecha debe ser futura"
            return True, "Fecha válida"
        except ValueError:
            return False, "Error al validar la fecha"

    @staticmethod
    def validate_choice(choice_str, valid_choices):
        """
        Valida que una opción esté dentro de las opciones válidas
        """
        if not choice_str or choice_str.strip() == "":
            return False, "Debe seleccionar una opción"
        
        try:
            choice = int(choice_str.strip())
            if choice not in valid_choices:
                return False, f"Opción inválida. Opciones válidas: {valid_choices}"
            return True, "Opción válida"
        except ValueError:
            return False, "Debe ingresar un número válido"

    @staticmethod
    def validate_address(address):
        """
        Valida una dirección
        """
        if not address or address.strip() == "":
            return False, "La dirección no puede estar vacía"
        
        address = address.strip()
        
        if len(address) < 5:
            return False, "La dirección debe tener al menos 5 caracteres"
        
        if len(address) > 200:
            return False, "La dirección no puede exceder 200 caracteres"
        
        return True, "Dirección válida"

    @staticmethod
    def validate_id(id_str, entity_name="ID"):
        """
        Valida un ID numérico
        """
        if not id_str or id_str.strip() == "":
            return False, f"El {entity_name} no puede estar vacío"
        
        try:
            id_value = int(id_str.strip())
            if id_value <= 0:
                return False, f"El {entity_name} debe ser un número positivo"
            return True, f"{entity_name} válido"
        except ValueError:
            return False, f"El {entity_name} debe ser un número válido"

    @staticmethod
    def get_validated_input(prompt, validator_func, *validator_args):
        """
        Solicita entrada del usuario con validación hasta que sea válida
        """
        while True:
            user_input = input(prompt)
            is_valid, message = validator_func(user_input, *validator_args)
            
            if is_valid:
                return user_input.strip()
            else:
                print(f"❌ Error: {message}")
                print("Por favor, inténtelo de nuevo.\n")