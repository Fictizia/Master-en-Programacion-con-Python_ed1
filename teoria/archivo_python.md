# Manejo de archivos y entrada y salida

Ya aprendiste mucho sobre **salida por consola** cuando estudiaste
[cadenas de texto](https://github.com/Fictizia/Master-en-Programacion-con-Python_ed1/blob/master/teoria/b03t01.md#cadenas-de-texto)
y `print` al comienzo del bloque 3.

## Entrada por consola

1. La entrada por consola es también muy sencilla. Se utiliza la función
[`input`](https://docs.python.org/3/library/functions.html#input):

    ```python
    string = input() # will wait for input until pressing enter
    print(f'Entered string is: {string}')
    ```

2. La función `input` puede imprimir un _prompt_, invitando al usuario a
introducir un texto:

    ```python
    string = input('Enter some text and press enter ')
    print(f'Entered string is: {string}')
    ```

3. El resultado de utilizar `input` es un objeto `str`, **siempre**:

    ```python
    string = input('Enter some text and press enter ')
    type(string)
    ```

4. Es nuestra responsabilidad interpretar la entrada de forma que creamos
oportuna. Por ejemplo:

    ```python
    def parse_coordinates(string):
        x, y = string.split()
        return int(x), int(y)

    user_input = input('Enter a 2D coordinate in the form x y: ')
    coordinates = parse_coordinates(user_input)
    print(coordinates)
    ```

5. También es nuestra reponsabilidad reintentar en caso de error:

    ```python
    def parse_coordinates(string):
        x, y = string.split()
        return int(x), int(y)

    while True:
        user_input = input('Enter a 2D coordinate in the form x y: ')
        try:
            coordinates = parse_coordinates(user_input)
        except:
            print('Invalid syntax!')
        else:
            break

    print(coordinates)
    ```

## Ficheros

El manejo de ficheros en Python está en el corazón del lenguaje a través
de la función `open`.

**Importante**: en esta sección vas a crear y manipular ficheros, cuando crees
ficheros o los leas utilizando rutas relativas, estás serán **relativas al
directorio de trabajo** que es el lugar desde el que lanzas el intérprete. Si
lo haces con PyCharm, el directorio de trabajo será aquel donde está el script
que estés ejecutando.

1. Crea un nuevo fichero de texto con `open`:

    ```python
    with open('./test.txt', 'w') as f:
        f.write('Greetings, humans!')
    ```

    Comprueba que el fichero existe en el sistema de archivos y que contiene
    exactamente lo que hemos escrito. Recuerda que se habrá creado en el
    mismo directorio desde el que lanzaste el intérprete.

2. Lee ahora el fichero también con `open`:

    ```python
    with open('./test.txt', 'r') as f:
        print(f.read())
    ```

    La forma más segura y "pitónica" de acceder a un fichero es mediante
    un bloque `with`. El contexto (estudiado durante la lección anterior)
    asegura que, ocurra lo que ocurra durante la ejecución del cuerpo, el
    fichero se cierra correctamente.

3. El primer parámetro de la función `open` es la ruta hasta el fichero. El
segundo es el modo de acceso: `'w'` para escribir y `'r'` para leer. Tratar de
leer en un fichero abierto en modo escritura es un error:

    ```python
    with open('./test.txt', 'w') as f:
        f.read()
    ```

    Prueba a escribir en un archivo abierto en modo lectura y comprueba que
    también es inválido.

4. Abrir un fichero en modo escritura **borra** el contenido anterior. Si
ejecutaste el código del paso anterior, comprueba en el sistema de ficheros
qué le ha pasado al fichero `test.txt`.

5. Restaura los contenidos del fichero.

6. Si quieres abrir un fichero para **añadir información**, utiliza el modo
`'a'`:

    ```python
    with open('./test.txt', 'a') as f:
        f.write('🛸 I am Ziltoid, the omniscient')
    ```

    Comprueba qué has añadido la nueva cadena de caracteres al fichero. Si todo
    ha ido bien, la cadena se habrá añadido **justo a continuación** del
    contenido anterior.

7. Puedes abrir un fichero en modo "lectura y escritura":

    ```python
    with open('./test.txt', 'r+') as f:
        text = f.read()
        f.write('\n' + text.upper())
    ```

    En el modo `'r+'`, el fichero no se vacía primero.

8. Otra forma de abrir un fichero en modo "lectura y escritura" es:

    ```python
    with open('./test.txt', 'w+') as f:
        text = f.read()
        assert len(text) == 0
    ```

    En el modo `'w+'`, el fichero se trunca al abrirse.

### Modos de apertura

Existen otros modos de abrir un archivo que puedes explorar, combinables
hasta cierto punto:

| Carácter/Combinación   | Significado                                        |
|------------------------|----------------------------------------------------|
| `'r'`  | Abiero para lectura (por defecto).                                 |
| `'w'`  | Abierto para escritura, vacía el fichero si ya existe.             |
| `'x'`  | Abierto para creación exclusiva; si ya existe, falla.              |
| `'a'`  | Abierto para escritura, añade al final si ya existe.               |
| `'b'`  | Abierto en modo binario, `read` y `write` trabajan con `bytes`.    |
| `'t'`  | Abierto en modo texto (por defecto).                               |
| `'+'`  | Abierto para lectura y escritura.                                  |
| `'r+'` | Abierto para lectura y escritura, añade al final si ya existe.     |
| `'w+'` | Abierto para lectura y escritura, vacía el fichero si ya existe.   |

### Codificación

Como puedes comprobar, por defecto `open` trabaja con ficheros de texto. Pero
como ya estudiaste, un fichero de texto sólo guarda bytes que representan texto
en alguna codificación. Podemos indicar la codificación a utilizar pasando
el parámetro `encoding` a `open`:

```python
with open('./test.txt', 'w+', encoding='utf8') as f:
    text = """Greetings humans!
🛸 I am Ziltoid, the omniscient."""
    f.write(text)
```

Con esto nos aseguramos que el fichero tiene codificación UTF-8. Si no se
especifica ninguna, la codificación por defecto se obtiene del sistema,
mediante:

```python
import locale
locale.getpreferredencoding(False)
```

El acceso a ficheros en modo texto es, con diferencia, más lento que el acceso
binario del que hablaremos un poco más adelante pero ofrece muchas
conveniencias para manejar texto.

### Leyendo línea a línea

En modo texto, podemos leer línea a línea o iterar por las líneas de un fichero:

1. Para leer las líneas explícitamente, utilizamos:

    ```python
    with open('./test.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line)
    ```

2. Para iterar sobre las líneas hacemos:

    ```python
    with open('./test.txt', 'r') as f:
        for line in f:
            print(line)
    ```

* Documentación de los objetos devueltos por `open` en
[modo texto](https://docs.python.org/3/library/io.html#io.TextIOWrapper)

### Trabajo con ficheros binarios

Los ficheros binarios están a la orden del días: imágenes, ficheros de audio,
ejecutables, archivos comprimidos...

Cuando se trabaja con ficheros binarios, pasando el modo `'b'`, los métodos
de lectura y escritura como `write`, `read` dejan de aceptar cadenas (`str`)
y sólo aceptan cadenas de bytes (`bytes`).

Sin embargo, la gestión de tales cadenas de bytes y su significado, queda
totalmente bajo nuestra responsabilidad. Como ejemplo, vamos a crear un formato
que permita crear listas de puntos 2D con coordenadas comprendidas entre
0 y 255.

1. Crea la función que convierte puntos (tuplas de dos elementos) a bytes
&mdash;el **serializador**&mdash;:

    ```python
    def serialize_point(p):
        if not isinstance(p, tuple) or len(p) != 2:
            raise ValueError('can only serialize tuples of two integers')

        x, y = p
        return serialize_byte(x) + serialize_byte(y)

    def serialize_byte(n):
        if not isinstance(n, int) and (n < 0 or n > 255):
            raise ValueError('can only serialize integers in the range [0, 255]')

        return bytes([n])
    ```

2. Crea la función que convierte listas de puntos a bytes:

    ```python
    def serialize_point_list(point_list):
        if len(point_list) > 255:
            raise ValueError('cannot serialize lists bigger than 255 elemnts')

        bytes_ = bytearray([len(point_list)])
        for point in point_list:
            bytes_ += serialize_point(point)
        return bytes(bytes_)
    ```

    La representación es el número de elemntos (de 0 a 255), seguido de los
    elementos.

3. Ahora podemos escribir estos bytes en un fichero binario:

    ```python
    with open('./points.data', 'wb') as f:
        list_of_points = [(0, 0), (10, 20), (254, 30)]
        f.write(serialize_point_list(list_of_points))
    ```

    Comprueba que el fichero se ha creado correctamente e intenta abrirlo
    con un editor de texto. Sólo verás unos símbolos extraños, muestra de que
    estamos ante un fichero binario.

Vamos a leerlo.

1. Crea la función que convierte bytes a puntos (tuplas) &mdash;el
**deserializador**&mdash;:

    ```python
    def deserialize_point(bytes_):
        if len(bytes_) > 2:
            raise ValueError('point is bad formed')

        x, y = bytes_
        return x, y
    ```

2. Ahora crea el deserializador de listas de puntos:

    ```python
    def deserialize_point_list(list_bytes):
        if len(bytlist_byteses_) < 1:
            raise ValueError('the list of points is bad formed')

        list_length = list_bytes[0]
        items_bytes = list_bytes[1:]
        if len(items_bytes) != list_length * 2:
            raise ValueError('the list of points is bad formed')

        list_of_points = []
        for i in range(0, list_length, 2):
            point_bytes = items_bytes[i:i+2] # each point is two-bytes long
            list_of_points.append(deserialize_point(point_bytes))

        return list_of_points
    ```

3. Ahora leemos el archivo en modo binario:

    ```python
    with open('./points.data', 'rb') as f:
        data = f.read()
        list_of_points = deserialize_point_list(data)
        assert list_of_points == [(0, 0), (10, 20), (254, 30)]
    ```

* Documentación de los objetos devueltos por `open` en
[modo binario](https://docs.python.org/3/library/io.html#io.BufferedIOBase)

#### Relación entre el modo de texto y el modo binario

Cuando Python abre un fichero en modo texto, realmente lo abre en modo binario
pero le añade una capa de codificación/decodificación por encima.

Para acceder al objeto binario subyacente, podemos hacer:

```python
with open('./test.txt', 'r') as f:
    character_count = len(f.read())
    underlying_binary_buffer = f.buffer
    underlying_binary_buffer.seek(0) # set the read cursor at the beginning
    byte_count = len(underlying_binary_buffer.read())
    print(f'Char count: {character_count}, Byte count: {byte_count}')
```
¿Por qué hay más bytes que caracteres?

## Persistencia de datos

Por fortuna, serializar y deserializar tipos básicos de Python es algo que ya
hace Python sin necesidad de nuestra intervención, por medio de utilidades en
la biblioteca estándar.

### Pickle

El módulo `pickle` permite la serialización y deserialización de objetos de
Python. Es una forma rápida de almacenar y recuperar el estado de un programa.

Comparemos el esfuerzo necesario para serializar una lista de puntos, como
hacíamos hace un par de secciones.

1. Para almacenar la lista de puntos haremos:

    ```python
    import pickle
    with open('./points.pickle', 'wb') as f:
        list_of_points = [(0, 0), (10, 20), (254, 30)]
        list_bytes = pickle.dumps(list_of_points)
        f.write(list_bytes)
    ```

2. Para leer la lista de puntos haremos:

    ```python
    import pickle
    with open('./points.pickle', 'rb') as f:
        list_bytes = f.read()
        list_of_points = pickle.loads(list_bytes)
        assert list_of_points == [(0, 0), (10, 20), (254, 30)]
    ```

    Puedes comprobar como se trata de un procedimiento muy parecido con
    la salvedad de que no tenemos que proporcionar las funciones de
    serialización y deserialización (que en la jerga de _pickle_ se llaman
    "_pickling_" y "_unplicking_".)

    Hay todavía una
    [API más sencilla](https://docs.python.org/3/library/pickle.html#examples)
    que gestiona la forma en la que se escribe y lee el fichero
    automáticamente.

3. Los algoritmos de serialización y deserialización tienen una versión del
protocolo. Para guardar los datos, de forma que sean compatibles con versiones antiguas de Python, podamos usar los protocolos `0` o `1`:

    ```python
    import pickle
    with open('./points.old-pickle', 'wb') as f:
        list_of_points = [(0, 0), (10, 20), (254, 30)]
        list_bytes = pickle.dumps(list_of_points, protocol=0)
        f.write(list_bytes)
    ```

    El protocolo `0` es un formato de texto así que puedes echarle un vistazo
    al contenido (otra cosa es que seas capaz de entenderlo).

4. No necesitas indicar el protocolo para leerlo, este se selecciona
automáticamente. Si los datos no se pueden deserializar, se lanza una excepción.

    ```python
    import pickle
    with open('./points.old-pickle', 'rb') as f:
        list_bytes = f.read()
        list_of_points = pickle.loads(list_bytes)
        assert list_of_points == [(0, 0), (10, 20), (254, 30)]
    ```

5. Las versiones del protocolo pickle avanzan conforme nuevas versiones de
Python aparecen. El protocolo por defecto actual es `3`.

    |Version |Purpose                                                          |
    |--------|-----------------------------------------------------------------|
    | 0      | Formato de texto usado en las versiones de Python más antiguas. |
    | 1      | Formato binario usado en las versiones de Python más antiguas.  |
    | 2      | Formato binario de Python 2.3 en adelante.  Mejor serialización de clases. |
    | 3      | Formato binario de Python 3.0. Python 2 no puede deserializarlo.|
    | 4      | Añade soporte para objetos muy grandes.                         |

    Tienes
    [más información acerca de los protocolos](https://docs.python.org/3/library/pickle.html#data-stream-format)
    de pickle en la documentación de Python.

Una nota de cautela usando `pickle`. El protocolo no es capaz de almacenar
cualquier objeto de Python. De los tipos y módulos, en particular, sólo se
almacena el nombre (el nombre completo, con la ruta de paquetes y módulos) y
se requiere que sean importables.

En la práctica significa que los ficheros "pickle" creados con un programa
no se pueden cargar en otro programa a menos que todo sean tipos incorporados
en Python (y todos estén presentes en el intérprete desde el que se intenta
cargar el fichero).

El protocolo Pickle posee mecanismos de expansión para ayudar a guardar y
cargar objetos no directamente serializables por Pickle.

* [Documentación del módulo `pickle`](https://docs.python.org/3/library/pickle.html)

### JSON

[JSON](https://www.json.org/) es un formato de texto que sigue la notación de
objetos de JavaScript para almacenar algunos tipos sencillos de datos,
incluyendo listas y mapas. Los tipos básicos de Python como cadenas, números,
tuplas, listas y diccionarios son fácilmente traducibles a JSON.

1. Comparamos con el ejemplo que viene siendo habitual. Para almacenar
la lista de puntos:

    ```python
    import json
    with open('./points.json', 'w') as f:
        list_of_points = [(0, 0), (10, 20), (254, 30)]
        list_representation = json.dumps(list_of_points)
        f.write(list_representation)
    ```

    Fíjate en el modo del fichero porque ya no es binario, sino texto.

    Echa un vistazo a `points.json` y comprueba que tu lista está ahí,
    en un formato muy parecido al de los literales que usaste para
    crear la lista.

    En particular, la siguiente tabla de equivalencia se aplica a la hora
    de codificar [tipos Python en JSON](https://docs.python.org/3/library/json.html#json.JSONEncoder):

    |Python             | JSON   |
    |-------------------|--------|
    |dict               |object  |
    |list, tuple        |array   |
    |str                |string  |
    |int, float & enums | number |
    |True               |true    |
    |False              |false   |
    |None               |null    |

2. Cargar la lista es también sencillo:

    ```python
    import json
    with open('./points.json', 'r') as f:
        list_representation = f.read()
        list_of_points = json.loads(list_representation)
        assert list_of_points == [(0, 0), (10, 20), (254, 30)]
    ```

    El aserto falla porque JSON **no puede representar tuplas**, en su lugar
    utiliza listas (puede guardar tuplas convirtiéndolas en listas primero).
    Esto ilustra una de las limitaciones de JSON:

    ```python
    import json
    with open('./points.json', 'r') as f:
        list_representation = f.read()
        list_of_points = json.loads(list_representation)
        assert list_of_points == [[0, 0], [10, 20], [254, 30]]
    ```

    La siguiente tabla de equivalencia se aplica cuando se
    [decodifica JSON en Python](https://docs.python.org/3/library/json.html#json.JSONDecoder):

    |JSON           | Python |
    |---------------|--------|
    |object         |dict    |
    |array          |list    |
    |string         |str     |
    |number (int)   |int     |
    |number (float) |float   |
    |true           |True    |
    |false          |False   |
    |null           |None    |

3. El módulo `json` también tiene funciones
[`dump`](https://docs.python.org/3/library/json.html#json.dump) y
[`load`](https://docs.python.org/3/library/json.html#json.load)
(fíjate que no terminan en "s") que toman el fichero como parámetro y se
encargan, automáticamente, de escribir y leer el fichero.

Como ocurre con Pickle, el módulo `json` tiene mecanismos de expansión para
permitir que un número mayor de objetos puedan convertirse a y desde JSON.

Las principales diferencias entre JSON y Pickle son:

1. JSON es un estándar intercompatible; Pickle es específico de Python.
2. JSON soporta un número limitado de tipos básicos de Python; Pickle puede
hacerse cargo de casi cualquier objeto de Python.
3. JSON es un formato de texto; Pickle utiliza, por lo general, un formato
binario.

* [Documentación del módulo `json`](https://docs.python.org/3/library/json.html).

### sqlite3

Python incorpora un módulo para gestionar **bases de datos relacionales
[SQLite 3](https://www.sqlite.org/index.html)**.
Esta base de datos proporciona una versión no estándar del lenguaje SQL y
funciona sobre un fichero, **sin necesitar de un servidor** corriendo al mismo
tiempo.

Usa SQLite para prototipar tus aplicaciones y luego podrás migrar tus datos
a bases de datos SQL más avanzadas como PostgreSQL.

El módulo `sqlite3` proporciona una API sencilla pero eficaz para introducir
comandos SQL y depende fuertemente de este lenguaje. No nos detendremos más
en ella. Si quieres conocer cómo conectar y utilizar una base de datos SQLite 3,
echa un vistazo a la
[documentación del módulo](https://docs.python.org/3/library/sqlite3.html).

## Objetos que parecen ficheros

En Python hablamos de "_file-like objects_" u objetos que parecen ficheros
cuando el objeto implementa la interfaz
[`io.IOBase`](https://docs.python.org/3/library/io.html#io.IOBase).

Por ello podemos tener objetos que no estén vinculados a ningún fichero pero
se comporten como tales. Los más utilizados son los "ficheros de texto en
memoria" y los "ficheros binarios en memoria".

1. Podemos usar "una cadena" como si fuera un fichero:

    ```python
    import io
    in_memory_text_file = io.StringIO()

    print('Greetings humans.', file=in_memory_text_file)
    in_memory_text_file.write('I am Ziltoid, the omniscient.')
    contents = in_memory_text_file.getvalue() # obtain the text
    in_memory_text_file.seek(0) # position at the beginning of the text
    first_line = in_memory_text_file.readline()

    print(f'All the contents:\n{contents}')
    print(f'First line is: {first_line}')

    in_memory_text_file.close() # free the underlying buffers
    in_memory_text_file.getvalue() # will fail after close()
    ```

2. Un objeto `io.StringIO` no es un contexto, pero podemos convertirlo en
uno que se comporte como `open()` gracias a la función
[`contextlib.closing`](https://docs.python.org/3/library/contextlib.html#contextlib.closing):

    ```python
    import io
    from contextlib import closing

    with closing(io.StringIO()) as in_memory_f:
        print('Greetings humans.', file=in_memory_f)
        in_memory_f.write('I am Ziltoid, the omniscient.')
        contents = in_memory_f.getvalue()
        print(contents)
    ```

3. El equivalente al "fichero binario en memoria" es
[`io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO):

    ```python
    import io
    from contextlib import closing

    with closing(io.BytesIO()) as in_memory_f:
        list_of_points = [(0, 0), (10, 20), (254, 30)]
        in_memory_f.write(serialize_point_list(list_of_points))
        contents = in_memory_f.getvalue()
        print(contents)
    ```

* [Documentación de `io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO)
* [Documentación de `io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO)

### Entrada, salida y error estándar

Hace un par de ejemplos viste un uso de `print` que no habías visto antes
en el curso: pasáste el parámetro `file` que permite escribir en un fichero
en lugar de en la terminal.

Propio de los sistemas UNIX, la entrada y salida estándares suelen estar
representadas por ficheros. En Python, estos ficheros son
[sys.stdout, sys.stdin, sys.stderr](https://docs.python.org/3/library/sys.html#sys.stdin)
y es, precisamente, `sys.stdout`, el valor por defecto que adquiere
[`print`](https://docs.python.org/3/library/functions.html#print)
en caso de no indicar nada.

Es una **muy buena práctica** que las funciones que tengan que escribir en
un fichero reciban este objeto como parámetro. Así, da igual si estamos
escribiendo en la salida estándar, en un fichero o en memoria y las
posibilidades de reutilización del objeto aumentan:

```python
import io
import sys
import json
from contextlib import closing

def save_json(data, file_=sys.stdout):
    data_representation = json.dumps(data)
    file_.write(data_representation)

data = {'name': 'Ziltoid', 'title':'The Omniscient'}

# Write to standard output (due to the default value of the parameter)
save_json(data)

# Write to a file
with open('./data.json', 'w') as f:
    save_json(data, f)

# Write to a in-memory string
with closing(io.StringIO()) as in_memory:
    save_json(data, in_memory)
    print(in_memory.getvalue())
```
