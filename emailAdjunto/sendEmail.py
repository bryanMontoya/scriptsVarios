# Módulo de importación
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#Descrpción: Clase responsable de generar un objeto de tipo email.
class Email:
   def __init__(self, poolCorreos, asuntoMensaje, cuerpoMensaje, userFrom, userPass, path):        
      self.poolCorreos = poolCorreos
      self.asuntoMensaje = asuntoMensaje
      self.cuerpoMensaje = cuerpoMensaje        
      self.userFrom = userFrom
      self.userPass = userPass                               
      self.path = path

   #Descripción: Método responsable de enviar un email a un pool de direcciones con un archivo adjunto.
   def sendEmail(self): 
        #Descripción: Verifica si se tiene conectividad haciendo una petición http.
        try:
            requests.get("http://www.google.com", timeout=5)
        except (requests.ConnectionError, requests.Timeout):
            return "Problemas de conexión de red."        

        server = smtplib.SMTP_SSL("smtp.gmail.com")                     
        try:
            server.login(self.userFrom, self.userPass)
        except:
            return "Usuario o contraseña incorrectas."
        else:      
            try:                
                att  =  MIMEApplication(open(self.path,'rb').read(),'utf-8')  
                att.add_header('Content-Disposition', 'attachment', filename = 'Archivo adjunto.%s'%(self.path.split(".")[1])) 

                for correo in self.poolCorreos:
                    msg  = MIMEMultipart()
                    msg['to'] = correo
                    msg['from'] = self.userFrom
                    msg['subject'] = self.asuntoMensaje
                    part = MIMEText(self.cuerpoMensaje)  
                    msg.attach(part)                
                    msg.attach(att)                
                    server.sendmail(msg['from'], msg['to'], msg.as_string())

                server.close()   
            except:
                return "La ruta especificada o el archivo no existe."

        return "Correo enviado con éxito!" 