from flask import Flask
import datetime
import email_to
import pytz

app = Flask(__name__)

def generateFibonacci():

    """Función encargada de generar la serie de Fibonacci."""

    hora = datetime.datetime.now(pytz.timezone('America/Bogota'))
    hora = hora.strftime('%H:%M:%S')
    hour = hora.split(':')

    x = int(hour[1][0])
    y = int(hour[1][1])
    n = int(hour[2])

    fib = str(x) + ", "
    for i in range(n):
        x, y = y, (x + y)
        fib = fib + str(x) + ", "

    x, y = y, (x + y)
    fib = fib + str(x)
    
    return hora, fib

def sendEmail(hora, fibSeries):

    """Función encargada de enviar email."""

    server = email_to.EmailServer('smtp.gmail.com', 587, 'reportesgi@clinicasomer.com', 'ReportesGI2020*')
    server.quick_email('bmontoyaosorios@gmail.com', 'Fibonacci, Hora: ' + str(hora) ,
                   ['Serie de Fibonacci: ' + fibSeries])

@app.route('/fibonacci')
def fibonacci():

    """Función encargada de recibir la petición para la serie de Fibonacci."""

    hora, fibSeries = generateFibonacci()
    sendEmail(hora = hora, fibSeries = fibSeries)

    return "Hora: " + hora + " Serie de Fibonnaci: " + fibSeries

app.run(host = "0.0.0.0", debug = True)
#serve(app, host = "0.0.0.0") 