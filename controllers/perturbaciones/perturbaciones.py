import random
from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

etapa_actual = 0  

while robot.step(timestep) != -1:
    tiempo = robot.getTime()
    vl_base = 0.0
    vr_base = 0.0
    aplicar_ruido = True
    
    if tiempo < 3.0:
        if etapa_actual == 0:
            print(f"\nETAPA {etapa_actual + 1}: LÍNEA RECTA (Con ruido)")
            etapa_actual += 1
        vl_base = 4.0
        vr_base = 4.0
        
    elif tiempo < 7.0:
        if etapa_actual == 1:
            print(f"\nETAPA {etapa_actual + 1}: CURVA (Con ruido)")
            etapa_actual += 1
        vl_base = 5.0
        vr_base = 5.5
        
    elif tiempo < 13.0:
        if etapa_actual == 2:
            print(f"\nETAPA {etapa_actual + 1}: CÍRCULO (Con ruido)")
            etapa_actual += 1
        vl_base = 4.0
        vr_base = 0.0
        
    else:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
        print("\n\nFinalizó el recorrido con perturbaciones :)")
        break

    if aplicar_ruido:
        vl_base += random.uniform(-0.1, 0.1)
        vr_base += random.uniform(-0.1, 0.1)

    left_motor.setVelocity(vl_base)
    right_motor.setVelocity(vr_base)
