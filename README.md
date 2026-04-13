# LABORATORIO 1 ROBÓTICA
---
Integrantes:
- Vicente Aburto Falcón
- Yamil Soleman Fernandez
- Vicente Nills Quezada Gallardo
- Sebastián García Valdebenito
- Ignacio Matus de la Parra
---

## Contenidos del documento

1. [Descripción del Laboratorio](#1-descripción-del-laboratorio)
2. [¿Cómo ejecutar la simulación en Webots?](#2-cómo-ejecutar-la-simulación-en-webots)
3. [Resultados Obtenidos](#3-resultados-obtenidos)
4. [Preguntas de análisis](#4-preguntas-de-análisis)
---

## 1. Descripción del Laboratorio

El Laboratorio 1 se centra en la simulación interactiva de un robot móvil diferencial (modelo e-puck) utilizando el entorno Webots. El objetivo principal es comprender y validar el comportamiento cinemático del robot mediante la programación de un controlador en Python que manipula de forma independiente la velocidad de sus dos ruedas motrices. 

Al alterar las velocidades de los actuadores (vl​ y vr​), el sistema ejecuta diversas trayectorias secuenciales —tales como líneas rectas, curvas, círculos y rotaciones estáticas para dibujar un cuadrado— evidenciando la relación directa entre la formulación matemática y el desplazamiento físico.

---
## 2. ¿Cómo ejecutar la simulación en Webots?

Para ejecutar nuestra simulacion de manera correcta y observar el comportamiento cinemático del robot, se deben seguir los siguientes pasos en el entorno de desarrollo:

  1. Cargar el Entorno: Abrir el software Webots y cargar el archivo del mundo (.wbt) que contiene la pista de pruebas y el robot diferencial (en este caso, el modelo e-puck).
  2. Configurar el Controlador: En el panel izquierdo (Árbol de Escena o Scene Tree), desplegar las propiedades del robot e-puck, buscar el campo controller y seleccionar el script de Python desarrollado para este laboratorio ('my_controller2'). Este paso es muy importante para asegurar que el robot ejecute nuestra lógica y no un comportamiento por defecto.
  3. Parámetros de Velocidad: Dentro del código del controlador (Python), se deben definir o ajustar las variables de velocidad para cada actuador: $v_l$ para el motor izquierdo y $v_r$ para el motor derecho. Dependiendo del experimento que se desee ejecutar (movimiento recto, curva o rotación), estas velocidades deberán ser iguales, diferentes u opuestas.
  4. Ejecución: Presionar el botón de "Play" (o "Step" para un análisis paso a paso) en la interfaz superior de Webots.

Si al darle "Play" el robot no se mueve o la consola Webots arroja un error indicando que no se reconoce el comando, es probable que Webots no esté detectando la versión de Python instalada. Para solucionarlo:
  - Ir al menú superior y seleccionar Tools > Preferences.
  - Buscar el apartado que dice Python command.
  - Ingresar el comando exacto o la ruta del ejecutable de Python de su dispositivo (se recomienda python 3.11.0).
  - Aplicar los cambios, recargar el mundo y volver a ejecutar la simulación.


---
## 3. Resultados Obtenidos

Tras implementar el controlador en Python y ejecutar la simulación en Webots, se validaron experimentalmente los principios del modelo cinemático del robot diferencial. Los resultados se dividen en los desafios propuestos:

  - ### A. Validación de Movimientos Básicos
    Se logró controlar el desplazamiento del robot manipulando las velocidades lineales de los motores izquierdo ($v_l$) y derecho ($v_r$):
      - Línea Recta: Al configurar $v_l = 4.0$ y $v_r = 4.0$, el robot mantuvo una trayectoria rectilínea. Esto confirma que cuando $v_l = v_r$, la velocidad angular $\omega$ es $0$.
      - Trayectoria Curva: Con $v_l = 5.0$ y $v_r = 5.5$, se observó un arco suave inclinado hacia la izquierda, validando que el robot pivota hacia el lado de la rueda más lenta.
      - Círculo: Se configuró $v_l = 4.0$ y $v_r = 0.0$. Al dejar una rueda estática, el robot tiene una trayectoria circular perfecta con un radio dependiente de la distancia entre ruedas $L$.

  - ### B. Ejecución del Desafío Opcional: Cuadrado
    Para simular la trayectoria de un cuadrado de forma precisa, se implementó una lógica de control basada en odimetría:
      - Fase de Avance: Durante un intervalo de $2.0$ segundos, el robot avanzó a una velocidad constante de $4.0$.
      - Fase de Giro (Con odimetría): Se utilizaron los sensores de posición de las ruedas para calcular el ángulo de rotación de forma bastante precisa en tiempo real. Mediante la fórmula de cinemática y el uso de la librería `math`, el robot tiene una rotación estática sobre el propio eje configurando velocidades opuestas ($v_l = -3.0$, $v_r = 3.0$) hasta que el diferencial de posición marca 85° o más, donde cambian estos valores a ($v_l = -0.1$, $v_r = 0.1$), de modo que el robot rota más lentamente para alcanzar a detectarse cuando el diferencial de posición marca 90° aproximadamente, momento en el cual se detiene la rotación y vuelve a la Fase de Avance en caso de no haber completado el cuadrado aún.
      - Resultado: El robot completó un cuadrado practicamente perfecto con un margen de error < 0.05° en cada ángulo recto.
   
    - ### C. Comparación de la Trayectoria con y sin Perturbaciones
    Para visualizar el comportamiento del robot en un entorno más realista, se introdujeron perturbaciones aleatorias (`random.uniform`) en las velocidades de los motores. 
    
    Como se observa en la comparación visual, el modelo cinemático ideal (izquierda) finaliza su trayectoria exactamente en la posición calculada. Sin embargo, al aplicar perturbaciones (derecha), el robot sufre una clara desviación geométrica (drift). Esto demuestra el principio fundamental de que pequeñas variaciones en las velocidades generan grandes cambios acumulativos en la posición final del robot.

### Video de Muestra:

>https://github.com/user-attachments/assets/c6eb3f55-d192-45d5-ae45-f7dd25ba4fcb

---
## 4. Preguntas de análisis

- **¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?**
  - Cuando ambas ruedas operan a la misma velocidad, el robot se desplaza en línea recta porque ambos lados recorren la misma distancia simultáneamente, anulando cualquier desvío. Si las velocidades son distintas, la trayectoria se vuelve curva hacia el lado de la rueda más lenta, ya que la rueda con mayor velocidad obliga al eje a pivotar sobre la otra al recorrer un arco más largo. En el caso de que las ruedas giren en sentidos opuestos con la misma magnitud, el robot realiza una rotación sobre su propio eje, debido a que el desplazamiento lineal se anula y solo queda el cambio de orientación en el mismo punto. Finalmente, para dibujar un círculo, es necesario mantener estas velocidades asimétricas de forma constante, lo que asegura un radio de giro estable hasta completar la circunferencia.
  
- **¿Cómo cambia la trayectoria cuando las velocidades son diferentes?**
  - Cuando existe una disparidad entre las velocidades de ambas ruedas, la trayectoria del robot deja de ser rectilínea y se vuelve curva, inclinándose siempre hacia el lado de la rueda que se desplaza más lento. Esto sucede porque la rueda con mayor velocidad recorre una distancia superior en el mismo intervalo de tiempo, lo que genera un momento de giro que obliga al chasis del robot a pivotar sobre el lado de menor tracción, modificando gradualmente su orientación de manera constante.

- **¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?**
  - Cuando una rueda gira en una dirección y la otra en el sentido contrario con la misma intensidad, el robot pierde su capacidad de avanzar o retroceder de forma lineal, realizando en su lugar una rotación estática sobre su propio eje central. Esto ocurre porque los desplazamientos de ambas ruedas se anulan mutuamente respecto al avance del chasis, pero al tirar de los extremos del robot en direcciones opuestas, generan un par de giro continuo que obliga al sistema a pivotar en el mismo punto, permitiendo cambiar la orientación sin modificar la posición en el espacio.

- **¿Qué tipo de movimiento permite dibujar un círculo?**
  - Para que el robot logre dibujar un círculo perfecto, es estrictamente necesario ejecutar un movimiento curvo manteniendo velocidades asimétricas pero constantes a lo largo de todo el trayecto. Al configurar una rueda para que gire más rápido que la otra (o incluso deteniendo una por completo), el robot tiende a inclinarse hacia el lado de menor velocidad; si esta diferencia de tracción no sufre ninguna alteración con el tiempo, el radio de giro se mantendrá completamente estable e invariable, obligando al chasis a trazar una curva continua que eventualmente se cerrará sobre sí misma completando la circunferencia.
