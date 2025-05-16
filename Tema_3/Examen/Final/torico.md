# Resultados

**Alumno:** Rafael Ponce Vivancos  
**Estadísticas de evaluación:** 4 puntos posibles  
**Tiempo de este intento:** 25 minutos

---

## Pregunta 1 (0,4 puntos)

Dado el siguiente código:

```python
class c1:
        def __init__(self, a):
                self.a = a
class c2:
        def __init__(self, b):
                self.b = b
class c3(c1, c2):
        def __init__(self, a, b):
                super().__init__(a)
                super().__init__(b)
        def met1(self):
                print(self.a + 5 + self.b)

c3 = c3(2, 2)
c3.met1()
```

**Indica la consideración correcta:**

- [x] Al ejecutarlo provocará un error. 
- [ ] La clase c3 sobreescribe el método met1 de la clase padre.  
- [ ] Mostrará por pantalla 9.  
- [ ] Las clases c1 y c2 son clases padre o derivadas.

---

## Pregunta 2 (0,4 puntos)

```python
x = list(range(100))
for i in x[:-1]:
        if i == x[-1]:
                print("finished")
        else:   
                continue
```

**¿Qué ocurrirá al ejecutarlo?**

- [ ] Mostrará "finished".  
- [x] Nada. 
- [ ] Mostrará None.  
- [ ] Provocará un error.

---

## Pregunta 3 (0,4 puntos)

```python
class Carcaj:
        def __init__(self, f):
                self.flechas = f

class Arquero:
        def __init__(self, carcaj):
                self.carcaj = carcaj

c = Carcaj(dict(tipo = "mediano", capacidad = 10, color = "rojo"))
a = Arquero(c)
```

**¿Cómo imprimimos la capacidad del carcaj del arquero `a`?**

- [x] `print(a.carcaj.flechas["capacidad"])` 
- [ ] `print(a.carcaj.flechas.capacidad)`  
- [ ] `print(len(a.carcaj.flechas.get(capacidad)))`  
- [ ] `print(c.arquero.flecha["capacidad"])`

---

## Pregunta 4 (0,2 puntos)

```python
class Clase1:
        def __init__(self, a, b = 10):
                self.a = a
                self.b = b
        def metodo1(self, c):
                self.a = c
        def metodo2(sell, d):
                return self.a + self.b
        def __str__(self):
                return f"m1 = {self.metodo1(4)}, m2 = {self.metodo2(5)}"
  
c = Clase1(5, 20)
print(c)
```

**¿Qué ocurrirá al ejecutarlo?**

- [x] Provocará un error. 
- [ ] Mostrará "m1 = None, m2 = 24".  
- [ ] No mostrará nada por pantalla.  
- [ ] Mostrará "m1 = 4, m2 = 24".

---

## Pregunta 5 (0,2 puntos)

**Indica la consideración correcta si hablamos de POO:**

- [ ] Una instancia es el proceso de creación de una clase de un objeto determinado; al crearla se llama al constructor.  
- [x] Una clase es la representación de una entidad o concepto; describe las características de un objeto. 
- [ ] Un objeto es donde se definen métodos y datos que resumen sus características.  
- [ ] Un objeto sólo se compone de métodos que permiten interactuar con él.

---

## Pregunta 6 (0,2 puntos)

**Indica la consideración correcta en herencia:**

- [ ] En herencia, una clase padre o base es aquella que hereda atributos y métodos de otra clase.  
- [x] En herencia, una clase hija puede heredar de una o varias clases base. 
- [ ] En herencia, es lo mismo una clase base que una clase derivada.  
- [ ] En herencia, una clase hija o derivada hereda métodos de otra clase, pero nunca atributos.

---

## Pregunta 7 (0,4 puntos)

```python

class Clase1:
        def __init__(self, a, b = 10):
                self.a = a
                self.b = b
        def metodo1(self):
                return self.a + self.b
   
class Clase2(Clase1):
        def __init__(self, a, b, c = 20):
                super.__init__(a, b)
                self.c = c
        def metodo1(self):
                return self.a + self.b + self.c
   
c2 = Clase2(1, 2, 3)

```

**¿Qué ocurrirá al ejecutarlo?**

- [x] Provocará un error de sintaxis. 
- [ ] Funcionará correctamente y creará el objeto `c2`.  
- [ ] Provocará un error porque la herencia está al revés.  
- [ ] Provocará un error porque falta un `self`.

---

## Pregunta 8 (0,2 puntos)

```python
def Func1(*n, m):

        for i in n:
                if m in i:
                        return True
        return False
```

**¿Cómo se debe llamar a la función para que devuelva True?**

- [ ] `Func1("12345", "6789", m=3)`  
- [x] No hay forma de que devuelva True. 
- [ ] `Func1([1, 2], [4, 5], [7, 8], m=5)`  
- [ ] `Func1(1, 2, 3, 4, 5, m=3)`

---

## Pregunta 9 (0,2 puntos)

**Indica la consideración correcta:**

- [ ] Sólo es posible modificar un atributo de un objeto a través de un método.  
- [x] Para llamar a un método de un objeto es necesario usar `self`. 
- [ ] No es posible borrar un objeto hasta que no finaliza la ejecución del programa.  
- [ ] Es posible borrar un atributo de un objeto con la sentencia `del`.

---

## Pregunta 10 (0,2 puntos)

**¿Cuáles son características de POO?**

- [ ] Sobreescritura, Sobrecarga y Ocultación.  
- [x] Abstracción, Encapsulación y Polimorfismo. 
- [ ] Herencia, Polimorfismo y Multiparadigma.  
- [ ] Herencia, Instanciación y Abstracción.

---

## Pregunta 11 (0,2 puntos)

**Indica la consideración correcta:**

- [x] `self` sirve de referencia a la instancia actual de la clase. 
- [ ] Se puede usar otro nombre distinto de `self` en los métodos.  
- [ ] `self` sirve para referenciar al método de cada clase.  
- [ ] `self` no es obligatorio en todos los métodos y atributos.

---

## Pregunta 12 (0,2 puntos)

```python

def Func1(a, b, c = 0):
        try:
                if a - c == 0:
                        a *= 2
                else:
                        print("Resultado: " + str(a/b-c))
        except:
                print("Error")
       
        Func1(10, 6, 5)

```

**¿Qué ocurrirá al ejecutarlo?**

- [ ] Mostrará "Error".  
- [ ] No mostrará nada por pantalla.  
- [x] Provocará un error antes de la ejecución. 
- [ ] Mostrará "Resultado: 10".

---

## Pregunta 13 (0,4 puntos)

```python

class C1:
        def __init__(self, a, b = 33):
                self.a = a
                self.__b = b
        def met1(self):
                print(self.a + self.__b)
o = C1(11)
o.met1()

```

**Indica la consideración correcta:**

- [ ] El método `met1` no es accesible desde fuera de la clase en ningún caso.  
- [x] El atributo `a` de `o` es accesible desde fuera, pero `__b` no. 
- [ ] La clase es incorrecta; fallará al invocar `met1()`.  
- [ ] A través de `o` se puede acceder a todos los atributos y métodos.

---

## Pregunta 14 (0,4 puntos)

**Indica la consideración correcta:**

- [ ] La sobreescritura solo se puede realizar en Python con parámetros opcionales.  
- [ ] En Python, es posible realizar sobrecarga de métodos de forma sencilla en las clases.  
- [x] La sobrecarga significa dos métodos con el mismo nombre, pero distinta firma y funcionalidad. 
- [ ] La sobreescritura solo se da si no existe relación de herencia.

