# Tarea 3 - Cinemática Inversa

Esta tarea tiene 2 objetivos principales:
1. Que entiendas cómo se mueve el robot, sus grados de libertad, la diferencia entre posición & pose y que puedas comprender las transformaciones geométricas que describen su movimiento.
2. Que programes el robot de la *Pequeña Fábrica:tm:* para que dibuje :pencil: figuras sencillas (y no tan sencillas) en una hoja de papel. 

### 1. Tener la matemática clara

1. Dibuja un esquema simplificado del robot, donde se aprecien sus eslabones (links) y articulaciones (joints). Reconoce qué tipos de grados de libertad lo componen y las matrices de transformaciones asociadas.

2. Haz la matraca de la cinemática directa (multiplicación de matrices)

3. Haz la matraca de la cinemática inversa: ¿qué ángulos (*q<sub>0</sub>*, *q<sub>1</sub>*, *q<sub>2</sub>*) permiten posicionar al efector en la posición (*x*, *y*, *z*)?

### 2. Actualizar tu repositorio

1. En **tu repositorio**, ve a la sección *Pull Requests*.
2. Crea un nuevo *Pull Rquest* y elige la siguiente comparación 
![](img/pull_request.png)

3. Fíjate que no hayan conflictos y luego haz **Merge**. Con esto listo, tu repositorio en Github ya está actualizado
4. Baja las actualizaciones en tu respositorio local con el comando 
```sh
git pull
```

### 3. Hacer que el robot dibuje

En la tarea anterior usamos el script `set_joints.py` para mover el robot. En esta clase lo volveremos a usar, pero calcularemos los valores de los angulos usando la cinemática inversa.

1. Para esto, edita la función `position_to_dof` en el archivo `inverse_kinematics.py` de modo que retorne los valores correctos de `q_0`, `q_1` y `q_2`.
**Bonus**: 
¿Cómo comprobarías que están bien estos valores?

2. Usa el archivo `move_the_robot.py` y modifícalo para que puedas dibujar usando coordenadas cartesianas, en lugar de ángulos del robot.



## Entregables

**La matraca**
- Dibujo del esquema simplificado del robot, con sus grados de libertad identificados
- Las matrices de transformación, en función de sus grados de libertad, que describen el movimiento del robot
- La ecuación explícita para obtener la **posición** del efector (mano) del robot, en cartesianas, en función de sus grados de libertad.
- La ecuación de cinmática inversa del robot

**Código**

*No más U-Cursos para el código!*

1. Anda a la carpeta donde tienes este repositorio y abre una terminal de *Git Bash*
2. Agrega todos los cambios que tengas con el siguiente comando
    ```sh
    git add 01_basics 02_kinematics 03_inverse_kinematics
    ```
3. Confima los cambios con el commando `commit`
    ```sh
    git commit -m "agrega mis soluciones de la tarea 3 y otras anteriores"
    ```
 4. Sube los cambios a github con el comando `push`
    ```sh
    git push
    ```

Si todo sale bien, deberías ver que tu repositorio en github tiene todos los cambios que hiciste durante esta tarea :)!

Debes subir a tu github los cambios en los archivos:
- `inverse_kinematics.py`: modificar la función `position_to_dof` con las ecuaciones y sus unidades correctas
- `move_the_robot.py`: agregar las instrucciones para dibujar figuras simples
- *BONUS*: crea una función para cada figura

