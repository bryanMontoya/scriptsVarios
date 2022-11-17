from sendEmail import Email

def main():
    #Credenciales de correo de origen: Importante: Habilitar acceso con apps menos seguras!! 
    userFrom = "email@gmail.com"
    userPass = "password"
    #Ruta para archivo a adjuntar:(xlsx, docx, png, jpg ...)    
    path ='C:/Users/.../archivo.docx'        
    asuntoMensaje = "Asunto del mensaje."   
    cuerpoMensaje = "Cuerpo del mensaje."     
    #Correos de destino:
    poolCorreos = ['email1@gmail.com','email2@gmail.com']

    m1 = Email(poolCorreos, asuntoMensaje, cuerpoMensaje, userFrom, userPass, path)
    print(m1.sendEmail())    

main()