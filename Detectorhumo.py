print("****Bienvenidos****")
print("Sistema Automático de Detección de Incendios para el Hogar")
import time

def leer_sensor_humo():
    entrada = input("Ingrese el valor del sensor de humo (0 = no humo, 1 = humo detectado): ")
    return entrada.strip() == '1'

def activar_alertas():
    print("¡Alerta! Humo detectado")
    print("Buzzer activado")
    print("LED encendido")
    print("Mensaje en LCD: '¡Fuego detectado!'")
    time.sleep(5)
    print("Buzzer apagado")
    print("LED apagado")

def main():
    print("Detector de humo iniciado. Presione Ctrl+C para salir.")
    try:
        while True:
            humo_detectado = leer_sensor_humo()
            if humo_detectado:
                activar_alertas()
            else:
                print("No se detecta humo")

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDetector de humo detenido.")

if __name__ == "__main__":
    main()
