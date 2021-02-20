import serial

comPort = "COM4"
port = 9600


def serialTest():
    conn = serial.Serial(comPort, port)
    print("Port status: " + str(conn.isOpen()))
    print("Port name: " + conn.name)
    print("Iniciando a transmissão de dados: ")
    print("API_HCSR04 - Sensor Ultrassonico: ")
    print("Aguardando conexao " + str(conn.readline()))
    
    
    while True:
        print("Dado lido: " + str(conn.readline()))   
   
 
serialTest()