# Tarea 2 - Un poco de matemática

Esta tarea tiene 2 objetivos principales:
1. Que tengas todas las herramientas de software que usaremos en el curso instaladas en tu computador
2. Que muevas un robot nuestra *Pequeña Fábrica:tm:* :fire:

### 1. Reconocer el roboc

Dibuja el robot y su representación de links y joints, describiendo tods los DOF que lo componen. Usa una regla para conocer sus dimensiones físicas y anótalas en el dibujo, usando milímetros.

### 2. Fork de este repositorio a tu cuenta

En la parte de arriba de este repositorio encuentras el boton <kbd> Fork </kbd> con él puedes copiar el repositorio en tu cuenta.

Luego, baja el respositorio desde tu cuenta. Al final de la clase te enseñaremos a subir tus propios cambios para que separ como conservar tus tareas y puedas revisarla en un futuro :)

### 3. Explorar los límites del roboc

Usa el script `set_joints.py` para mover el robot.

:warning: Algunos ángulos pueden dañar los motores del robot, por lo que tiene que haber una persona pendiente de resetear el controlasdor (Arduino) en caso que se trabe.

El robot tiene límites físicos, por lo que no todos los ángulos que se te ocurran van a ser factibles!

**Entregable**
Debes subir a U-Cursos el script modificado, con cuatro funciones de la siguiente forma

```python
def look_up():
    robot.set_joints(...)
```