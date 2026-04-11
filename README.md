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
---

## 1. Descripción del Laboratorio
- El Laboratorio 1 se centra en la simulación interactiva de un robot móvil diferencial (modelo e-puck) utilizando el entorno Webots. El objetivo principal es comprender y validar el comportamiento cinemático del robot mediante la programación de un controlador en Python que manipula de forma independiente la velocidad de sus dos ruedas motrices. Al alterar las velocidades de los actuadores (vl​ y vr​), el sistema ejecuta diversas trayectorias secuenciales —tales como líneas rectas, curvas, círculos y rotaciones estáticas para dibujar un cuadrado— evidenciando la relación directa entre la formulación matemática y el desplazamiento físico. Para documentar los resultados, se habilitó el dispositivo virtual 'Pen', permitiendo trazar visualmente la ruta exacta del robot sobre la arena de simulación.
---
## 2. ¿Cómo ejecutar la simulación en Webots?
- Para ejecutar nuestra simulacion


---
## 3. Resultados Obtenidos
-


---
## 4. Preguntas de análisis

- ¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?
  - Cuando ambas ruedas operan a la misma velocidad, el robot se desplaza en línea recta porque ambos lados recorren la misma distancia simultáneamente, anulando cualquier desvío. Si las velocidades son distintas, la trayectoria se vuelve curva hacia el lado de la rueda más lenta, ya que la rueda con mayor velocidad obliga al eje a pivotar sobre la otra al recorrer un arco más largo. En el caso de que las ruedas giren en sentidos opuestos con la misma magnitud, el robot realiza una rotación sobre su propio eje, debido a que el desplazamiento lineal se anula y solo queda el cambio de orientación en el mismo punto. Finalmente, para dibujar un círculo, es necesario mantener estas velocidades asimétricas de forma constante, lo que asegura un radio de giro estable hasta completar la circunferencia.
  
- ¿Cómo cambia la trayectoria cuando las velocidades son diferentes?
  - Cuando existe una disparidad entre las velocidades de ambas ruedas, la trayectoria del robot deja de ser rectilínea y se vuelve curva, inclinándose siempre hacia el lado de la rueda que se desplaza más lento. Esto sucede porque la rueda con mayor velocidad recorre una distancia superior en el mismo intervalo de tiempo, lo que genera un momento de giro que obliga al chasis del robot a pivotar sobre el lado de menor tracción, modificando gradualmente su orientación de manera constante.

- ¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?
  - Cuando una rueda gira en una dirección y la otra en el sentido contrario con la misma intensidad, el robot pierde su capacidad de avanzar o retroceder de forma lineal, realizando en su lugar una rotación estática sobre su propio eje central. Esto ocurre porque los desplazamientos de ambas ruedas se anulan mutuamente respecto al avance del chasis, pero al tirar de los extremos del robot en direcciones opuestas, generan un par de giro continuo que obliga al sistema a pivotar en el mismo punto, permitiendo cambiar la orientación sin modificar la posición en el espacio.

- ¿Qué tipo de movimiento permite dibujar un círculo?
  - Para que el robot logre dibujar un círculo perfecto, es estrictamente necesario ejecutar un movimiento curvo manteniendo velocidades asimétricas pero constantes a lo largo de todo el trayecto. Al configurar una rueda para que gire más rápido que la otra (o incluso deteniendo una por completo), el robot tiende a inclinarse hacia el lado de menor velocidad; si esta diferencia de tracción no sufre ninguna alteración con el tiempo, el radio de giro se mantendrá completamente estable e invariable, obligando al chasis a trazar una curva continua que eventualmente se cerrará sobre sí misma completando la circunferencia.
