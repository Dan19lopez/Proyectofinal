from domain.Friend import Friend
from repository.FriendRepository import FriendRepository
from repository.FriendRepositoryDB import FriendRepositoryDB
from utils.Validators import Validators


class  FriendService:


    def __init__(self):
        self.friendObject = Friend(None, None, None, None, None, None)
        self.friendRepository = FriendRepository()
        self.friendRepositoryDB = FriendRepositoryDB()



    def createUser(self):

        print("\n=== CREAR NUEVO AMIGO ===")

        # Validar nombre
        name = Validators.get_validated_input(
            "Nombre del amigo: ", 
            Validators.validate_name, 
            "Nombre"
        )
        self.friendObject.name = name
        
        # Validar teléfono
        phone = Validators.get_validated_input(
            "Teléfono: ", 
            Validators.validate_phone
        )
        self.friendObject.phone = phone
        
        # Validar email
        mail = Validators.get_validated_input(
            "Email: ", 
            Validators.validate_email
        )
        
        # Verificar si el email ya existe
        existing_friends = self.friendRepositoryDB.select_friends()
        for friend in existing_friends:
            if friend.mail.lower() == mail.lower():
                print("❌ Error: Ya existe un amigo con este email")
                return
        
        self.friendObject.mail = mail
        
        # Validar dirección
        adress = Validators.get_validated_input(
            "Dirección: ", 
            Validators.validate_address
        )
        self.friendObject.adress = adress
        
        # Validar rol
        print("Roles disponibles:")
        print("1. Amigo")
        print("2. Familiar") 
        print("3. Compañero")
        
        rol = int(Validators.get_validated_input(
            "Seleccione el rol (1-3): ", 
            Validators.validate_choice, 
            [1, 2, 3]
        ))
        self.friendObject.rol = rol

        # Set id to None since it will be auto-generated
        self.friendObject.id = None

        print(f"Creando amigo: {name}, {phone}, {mail}, {adress}, {rol}")

        try:
            # Only save to database, don't use the dictionary repository for new friends
            self.friendRepositoryDB.createFriendDB(self.friendObject)
            print("✅ Amigo creado exitosamente")
        except Exception as e:
            print(f"❌ Error al crear el amigo: {e}")


    def selectUser(self):
        self.friendRepository.printFriend()
        return self.friendRepositoryDB.select_friends()


    def updateFriend(self , id_friend):
        friend = []


        if self.friendRepository.friends.get(id_friend):

            id = int(input("Id Amigo: "))
            self.friendObject.id = id
            name = input("Nombre amigo:")
            self.friendObject._name = name
            phone = input("Telefono: ")
            self.friendObject._phone = phone
            mail = input("Email: ")
            self.friendObject._mail = phone
            adress = (input("Direccion: "))
            self.friendObject._adress = adress
            rol = input("rol: ")
            self.friendObject._rol = adress

            friend.append(id)  # 1
            friend.append(name)  # pepito
            friend.append(phone)  # 3214567890
            friend.append(mail)  # pp@mail.com
            friend.append(adress)  # medellin
            friend.append(rol)  # amigo

            print(f"friend{friend}")

            self.friendRepository.createFriendDict(id, friend)
        else:
            print("Usuario no existe")



    def select_friend_by_id(self, id_friend):
        return self.friendRepositoryDB.select_user_by_id(id_friend)


    def update_friend(self):
        print("\n=== ACTUALIZAR AMIGO ===")
        
        # Validar ID
        id_str = Validators.get_validated_input(
            "Ingrese el ID del amigo a modificar: ", 
            Validators.validate_id, 
            "ID del amigo"
        )
        id = int(id_str)
        
        friend = self.friendRepositoryDB.select_user_by_id(id)
        
        if not friend:
            print("❌ Amigo no encontrado")
            return
        
        print(f"Amigo actual: {friend}")
        print("\nDeje en blanco para mantener el valor actual:")
        
        # Validar nombre si se proporciona uno nuevo
        new_name = input(f"Nombre amigo (actual: {friend.name}): ").strip()
        if new_name:
            is_valid, message = Validators.validate_name(new_name, "Nombre")
            if not is_valid:
                print(f"❌ Error en el nombre: {message}")
                return
            friend.name = new_name
        
        # Validar teléfono si se proporciona uno nuevo
        new_phone = input(f"Teléfono (actual: {friend.phone}): ").strip()
        if new_phone:
            is_valid, message = Validators.validate_phone(new_phone)
            if not is_valid:
                print(f"❌ Error en el teléfono: {message}")
                return
            friend.phone = new_phone
        
        # Validar email si se proporciona uno nuevo
        new_mail = input(f"Email (actual: {friend.mail}): ").strip()
        if new_mail:
            is_valid, message = Validators.validate_email(new_mail)
            if not is_valid:
                print(f"❌ Error en el email: {message}")
                return
            
            # Verificar si el email ya existe en otro amigo
            existing_friends = self.friendRepositoryDB.select_friends()
            for existing_friend in existing_friends:
                if existing_friend.id != friend.id and existing_friend.mail.lower() == new_mail.lower():
                    print("❌ Error: Ya existe otro amigo con este email")
                    return
            
            friend.mail = new_mail
        
        # Validar dirección si se proporciona una nueva
        new_adress = input(f"Dirección (actual: {friend.adress}): ").strip()
        if new_adress:
            is_valid, message = Validators.validate_address(new_adress)
            if not is_valid:
                print(f"❌ Error en la dirección: {message}")
                return
            friend.adress = new_adress
        
        # Validar rol si se proporciona uno nuevo
        new_rol = input(f"Rol - 1:Amigo, 2:Familiar, 3:Compañero (actual: {friend.rol}): ").strip()
        if new_rol:
            is_valid, message = Validators.validate_choice(new_rol, [1, 2, 3])
            if not is_valid:
                print(f"❌ Error en el rol: {message}")
                return
            friend.rol = int(new_rol)

        try:
            self.friendRepositoryDB.updateFriend(friend)
            print("✅ Amigo actualizado exitosamente")
        except Exception as e:
            print(f"❌ Error al actualizar el amigo: {e}")


    def removeFriend(self, id_friend):
        """self.friendRepository.removeFriendDict(id_friend)"""
        self.friendRepositoryDB.delete_friend_by_id(id_friend)
