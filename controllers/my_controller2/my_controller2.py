from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

pen = robot.getDevice('pen')
pen.write(True)
pen.setInkColor(0x00FF00, 1.0) 

TIEMPO_LADO = 2.0
TIEMPO_GIRO_90 = 0.85 
inicio_cuadrado = 14.0 

while robot.step(timestep) != -1:
    tiempo = robot.getTime()
    
    if tiempo < 3.0:
        left_motor.setVelocity(4.0)
        right_motor.setVelocity(4.0)

    elif tiempo < 7.0:
        left_motor.setVelocity(5.0)
        right_motor.setVelocity(5.5)
        
    elif tiempo < 13.0:
        left_motor.setVelocity(4.0)
        right_motor.setVelocity(0.0)
        
    elif tiempo < inicio_cuadrado:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
        
    else:
        tiempo_relativo = tiempo - inicio_cuadrado
        duracion_ciclo = TIEMPO_LADO + TIEMPO_GIRO_90
        tiempo_en_ciclo = tiempo_relativo % duracion_ciclo
        ciclo_actual = int(tiempo_relativo / duracion_ciclo)
        
        if ciclo_actual < 4:
            if tiempo_en_ciclo < TIEMPO_LADO:
                left_motor.setVelocity(4.0)   
                right_motor.setVelocity(4.0)
            else:
                left_motor.setVelocity(-3.0) 
                right_motor.setVelocity(3.0)
        else:
            left_motor.setVelocity(0.0)       
            right_motor.setVelocity(0.0)
