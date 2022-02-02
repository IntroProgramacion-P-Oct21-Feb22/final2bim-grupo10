def crearFacebook():
 
    redSocial = "Facebook"
    print("\tCreando cuenta de ",redSocial)
    nombreUsuario = input("Nombre de usuario: ")
    edad = input("Edad: ")
    ciudad = input("Ciudad: ")
    pais = input("País: ")
    correoElectronico = input("Correo electrónico: ")
    
    resumenFacebook = f"Red: {redSocial}\nNombre de usuario: {nombreUsuario}\nEdad: {edad}\nCiudad: {ciudad}\nPaís: {pais}\nCorreo: {correoElectronico}"
    return resumenFacebook

def crearTwitter(datosCuentasCreadas: list):

    redSocial = "Twitter"
    print("\tCreando cuenta de ",redSocial)
    nombreUsuario = input("Nombre de usuario: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    edad = input("Edad: ")
    ciudad = input("Ciudad: ")
    pais = input("País: ")
    idioma = input("Idioma: ")
    correoElectronico = input("Correo electrónico: ")
    
    resumenTwitter = f"Red: {redSocial}\nNombre de usuario: {nombreUsuario}\nNombres: {nombres}\nApellidos: {apellidos}\nEdad: {edad}\nCiudad: {ciudad}\nPaís: {pais}\nIdioma: {idioma}\nCorreo: {correoElectronico}"
    datosCuentasCreadas.append(resumenTwitter)

def crearWhastapp():

    redSocial = "Whatsapp"
    print("\tCreando cuenta de ",redSocial)
    nombreUsuario = input("Nombre de usuario: ")
    numeroTelefono = input("Telefono: ")
    edad = input("Edad: ")
    ciudad = input("Ciudad: ")
    pais = input("País: ")
    
    resumenWhatsapp = f"Red: {redSocial}\nNombre de usuario: {nombreUsuario}\nNúmero teléfono: {numeroTelefono}\nEdad: {edad}+\nCiudad: {ciudad}+\nPaís: {pais}"
    return resumenWhatsapp

def crearTelegram(datosCuentasCreadas: list):

    redSocial = "Telegram"
    print("\tCreando cuenta de ",redSocial)
    nombreUsuario = input("Nombre de usuario: ")
    numeroTelefono = input("Telefono: ")    
    ciudad = input("Ciudad: ")
    pais = input("País: ")
    areaInteres = input("Área Interés: ")
  
    resumenTelegram = f"Red: {redSocial}\nNombre de usuario: {nombreUsuario}\nNúmero teléfono: {numeroTelefono}\nCiudad: {ciudad}\nPaís: {pais}\nÁrea Interés: {areaInteres}"
    datosCuentasCreadas.append(resumenTelegram)

def crearSignal():

    redSocial = "Signal"
    print("\tCreando cuenta de ",redSocial)
    nombreUsuario = input("Nombre de usuario: ")
    numeroTelefono = input("Telefono: ")   
    ciudad = input("Ciudad: ")
    pais = input("País: ")
    hobby = input("Hobby principal: ")
    
    resumenSignal = f"Red: {redSocial}\nNombre de usuario: {nombreUsuario}\nNúmero teléfono: {numeroTelefono}\nCiudad: {ciudad}+\nPaís: {pais}\nHobby Principal: {hobby}"
    return resumenSignal

def crearInstagram(datosCuentasCreadas: list):

    redSocial = "Instagram"
    print("\tCreando cuenta de ",redSocial)
    nombreUsuario = input("Nombre de usuario: ")
    ciudad = input("Ciudad: ") 
    edad = input("Edad: ")
    correoElectronico = input("Correo electrónico: ")
   
    resumenInstagram = f"Red: {redSocial}\nNombre de usuario: {nombreUsuario}\nCiudad: {ciudad}\nEdad: {edad}\nCorreo electrónico: {correoElectronico}"
    datosCuentasCreadas.append(resumenInstagram)

def crearFlickr():

    redSocial = "Flickr"
    print("\tCreando cuenta de ",redSocial)
    nombreUsuario = input("Nombre de usuario: ")
    correoElectronico = input("Correo electrónico: ")   
    
    resumenSignal = f"Red: {redSocial}\nNombre de usuario: {nombreUsuario}\nCorreo Electrónico: {correoElectronico}"
    return resumenSignal

def obtenerMensaje(numeroCuentas: int):
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    mensaje = " "
    if numeroCuentas>=1 and numeroCuentas<=5:
        mensaje = mensajeFinal[0]
    elif numeroCuentas>=6 and numeroCuentas<=15:
        mensaje = mensajeFinal[1]
    elif numeroCuentas>=16:
        mensaje = mensajeFinal[2]
    return mensaje

def main():
    bandera = True
    datosCuentasCreadas = []
    while bandera:
        opcion= 0
        print("\tEscoja una opción")
        print("1. Crear perfil de Facebook")
        print("2. Crear perfil de Twitter")
        print("3. Crear perfil de Whatsapp")
        print("4. Crear perfil de Telegram")
        print("5. Crear perfil de Signal")
        print("6. Crear perfil de Instagram")
        print("7. Crear perfil de Flickr")
        print("8. Terminar")
        opcion = int(input("Opción: "))

        if opcion==1:
            cuentaFacebook = crearFacebook()          
            datosCuentasCreadas.append(cuentaFacebook)
        elif opcion==2:
            crearTwitter(datosCuentasCreadas)            
        elif opcion==3:
            cuentaWhastapp = crearWhastapp()
            datosCuentasCreadas.append(cuentaWhastapp)
        elif opcion==4:
            crearTelegram(datosCuentasCreadas)           
        elif opcion==5:
            cuentaSignal = crearSignal()
            datosCuentasCreadas.append(cuentaSignal)
        elif opcion==6:
            crearInstagram(datosCuentasCreadas)          
        elif opcion==7:
            cuentaFlickr = crearFlickr()
            datosCuentasCreadas.append(cuentaFlickr)
        elif opcion==8:
            bandera=False
        else:
            print("\nIngrese una opción válida")
    print(obtenerMensaje(len(datosCuentasCreadas)))
main()