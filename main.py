contactos = []
while True:
    comando = input("")
    partes = comando.split()
    accion = partes[0].upper()
    if accion == "AGREGAR" and len(partes) == 4:
        nombre = partes[1]
        telefono = partes[2]
        correo = partes[3]
        contacto = {"nombre":nombre, "telefono":telefono, "correo":correo}
        contactos.append(contacto)
        print("Contacto agregado con exito.")
    elif accion == "ELIMINAR" and len(partes) == 2:
        nombre = partes[1]
        eliminarContacto = None
        for contacto in contactos:
            if contacto["nombre"] == nombre:
                eliminarContacto = contacto
                break
        if eliminarContacto:
            contactos.remove(eliminarContacto)
            print("Contacto eliminado con exito.")
    elif accion == "BUSCAR" and len(partes) == 2:
        parametro = partes[1]
        for contacto in contactos:
            if contacto["nombre"] == parametro or contacto["telefono"] == parametro or contacto["correo"] == parametro:
                print(f"Informacion del contacto {parametro}:")
                print(f" Nombre: {contacto['nombre']}")
                print(f" Teléfono: {contacto['telefono']}")
                print(f" Correo: {contacto['correo']}")
    elif accion == "ORGANIZAR":
        contactos.sort(key=lambda contacto: contacto["nombre"])
        print("Lista de contactos organizada:")
        for contacto in contactos:
            print(f" - {contacto['nombre']}")