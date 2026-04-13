from controller import Robot
import math

robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

left_sensor = robot.getDevice('left wheel sensor')
right_sensor = robot.getDevice('right wheel sensor')
left_sensor.enable(timestep)
right_sensor.enable(timestep)

RADIO_RUEDA = 0.0205
DISTANCIA_RUEDAS = 0.053

fase_actual = "RECTA"
lados_dibujados = 0
tiempo_inicio_recta = 16.0
angulo_al_empezar_giro = 0.0

etapa_actual = 0  

while robot.step(timestep) != -1:
    tiempo = robot.getTime()
    
    pos_izq = left_sensor.getValue()
    pos_der = right_sensor.getValue()
    
    dist_izq = pos_izq * RADIO_RUEDA
    dist_der = pos_der * RADIO_RUEDA
    
    angulo_rad = (dist_der - dist_izq) / DISTANCIA_RUEDAS
    angulo_grados = angulo_rad * (180.0 / math.pi)

    if tiempo < 16.0:
        if tiempo < 3.0:
            if etapa_actual == 0:
                print(f"\nETAPA {etapa_actual + 1}: LÍNEA RECTA")
                etapa_actual += 1
            left_motor.setVelocity(4.0)
            right_motor.setVelocity(4.0)
            
        elif tiempo < 7.0:
            if etapa_actual == 1:
                print(f"\nETAPA {etapa_actual + 1}: CURVA")
                etapa_actual += 1
            left_motor.setVelocity(5.0)
            right_motor.setVelocity(5.5)
            
        else:
            if etapa_actual == 2:
                    print(f"\nETAPA {etapa_actual + 1}: CÍRCULO")
                    etapa_actual += 1
            left_motor.setVelocity(4.0)
            right_motor.setVelocity(0.0)
            
    else:
        if etapa_actual == 3:
            print(f"\nETAPA {etapa_actual + 1}: CUADRADO")
            etapa_actual += 1
            
        if lados_dibujados < 4:
            
            if fase_actual == "RECTA":
                left_motor.setVelocity(4.0)
                right_motor.setVelocity(4.0)
                
                if tiempo - tiempo_inicio_recta >= 2.0:
                    fase_actual = "GIRO"
                    angulo_al_empezar_giro = angulo_grados
                    print(f"    Iniciando Giro {lados_dibujados + 1}")
            
            elif fase_actual == "GIRO":
                delta_angulo = abs(angulo_grados - angulo_al_empezar_giro)
                
                if delta_angulo > 85.0:
                    left_motor.setVelocity(-0.1)
                    right_motor.setVelocity(0.1)
                else:
                    left_motor.setVelocity(-3.0)
                    right_motor.setVelocity(3.0)
                
                if delta_angulo >= 90.0:
                    fase_actual = "RECTA"
                    print(f"    - Giro {lados_dibujados + 1} COMPLETADO | Giró exactamente: {delta_angulo:.2f}°")
                    lados_dibujados += 1
                    tiempo_inicio_recta = tiempo 
        
        else:
            left_motor.setVelocity(0.0)
            right_motor.setVelocity(0.0)
            print("\nFinalizó el recorrido del Robot :)")
            break
