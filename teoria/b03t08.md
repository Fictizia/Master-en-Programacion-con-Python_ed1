# Excepciones y gestión de errores

El código puede fallar por muchas razones. Existen diversas técnicas de
señalización de fallo y una de las más populares son las excepciones.

Tradicionalmente, una excepción es una situación que desencadena la
interrupción del flujo del programa y **propaga el control por la pila de
funciones llamantes hasta alcanzar el programa principal** dónde hace que este
se detenga por completo y termine en estado de error.

1. En Python, podemos desencadenar una excepción con la
[sentencia `raise`](https://docs.python.org/3/tutorial/errors.html#raising-exceptions):

    ```python
    def a():
        b()

    def b():
        c()

    def c():
        d()

    def d():
        raise Exception()

    a()
    ```

1. La sentencia `raise` toma un parámetro también llamado excepción, que es
un objeto de tipo `Exception` o derivado y que suele contener información
para el desarrollador sobre la naturaleza de la excepción:

    ```python
    def a():
        b()

    def b():
        c()

    def c():
        d()

    def d():
        raise Exception('Intended error')

    a()
    ```

    Si, como en el ejemplo anterior, no estamos pasando argumentos a la
    excepción, podemos devolver la clase del error y Python creará un objeto
    excepción llamando a la clase sin parámetros:

    ```python
    raise Exception # equivalent to raise Exception()
    ```

## Excepciones incorporadas en Python

Python incluye una
[colección de tipos de errores](https://docs.python.org/3/library/exceptions.html)
definida por el lenguaje en sí y por la biblioteca estándar:

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```

Python usa las excepciones para señalizar situaciones extraordinarias, muchas
de ellas, errores, aunque no siempre. Los errores están bajo el tipo
`Exception` y estos son algunos de los más comunes:

* `KeyboardInterrupt`: se produce cuando el programa recibe la señal de
interrupción, normalmente `ctrl+C` o `ctr+supr`.

    ```python
    while True:
        pass
    ```

    Ahora presiona `ctrl+C` para forzar la interrupción.

* `AssertionError`: no se cumple la condición del `assert`. El mensaje es el
segundo parámetro.

    ```python
    assert 3 == 5, '3 is not equal to 5'
    ```

* `AttributeError`: no se encuentra un atributo en un objeto. El mensaje
incluye el atributo y la clase del objeto.

    ```python
    o = object()
    o.answer
    ```

* `ImportError`: no se puede importar el nombre indicado. El mensaje
incluye el nombre de lo que se quería importar y de dónde se quería importar.

    ```python
    from datetime import Date
    ```

* `ModuleNotFoundError`: no se encuentra el módulo especificado. El mensaje
incluye el nombre del módulo que se trataba de importar.

    ```python
    import no_existe
    ```

* `IndexError`: el índice se encuentra fuera del rango. No se da información
más específica.

    ```python
    l = [1,2,3]
    l[5]
    ```

* `KeyError`: no se encuentra la clave en el diccionario. El mensaje es la
clave que no se encuentra:

    ```python
    d = {'a':1, 'b':2}
    d['c']
    ```

* `FileNotFoundError`: no existen en fichero o el directorio. El mensaje
incluye la ruta a la que se intenta acceder.

    ```python
    f = open('no/existe', 'r')
    ```

* `TimeoutError`: se produce cuando una operación bloqueante excede un
tiempo de espera. El mensaje no lleva más información.

    ```python
    import http
    c = http.client.HTTPConnection('example.com', timeout=0.1)
    c.request('GET', '/noexiste')
    ```

* `RecursionError`: se alcanza el máximo de recursión. No se da ninguna
información extra.

    ```python
    def f():
        f()

    f()
    ```

* `SyntaxError`: se produce un error sintáctico. Los detalles se encuentran en
el mensaje.

    ```python
    for i in range(10) print(i)
    ```

* `TypeError`: se produce al tratar de realizar una operación en un tipo no
compatible. El mensaje suele incluir los detalles.

    ```python
    1 + '2'
    ```

* `ValueError`: se produce cuando el valor de un tipo es inválido. El mensaje
suele incluir información acerca de por qué el valor es inválido.

    ```python
    import datetime
    new_year = datetime.date(2020, 0, 1)
    ```

* `DeprecationWarning`: se produce al tratar de usar una característica
obsoleta de un programa. Es normal en bibliotecas de terceros. Los detalles,
como por ejemplo, la alternativa preferida se suele encontrar en el mensaje.

    ```python
    import warnings

    def f():
        warnings.warn(
            'It is preferred if you use `g` instead', DeprecationWarning)
        g()

    def g():
        ...

    f()
    ```

## Excepciones personalizadas

Es [posible definir tipos de error nuevos](https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions).

Sabrás cómo cuando hablemos de clases y objetos. Por el momento, cuando
tengas que señalizar el error, **trata de reutilizar alguna de las
existentes**. Reutilizar excepciones es importante porque el usuario puede
reutilizar el conocimiento que tiene resolviendo excepciones de ese tipo.

Si necesitas una semántica especial, añade un mensaje descriptivo a una
exepción genérica `Exception`.

## Capturar una excepción

Cuando se produce una excepción, el flujo del programa se interrumpe y el
control trata de abandonar la función actual, transmitiendo el objeto
`Exception`, hacia la función llamante.

1. Podemos impedir que una excepción se propage mediante un bloque
`try ... except ...`.

    ```python
    def safediv(n, divisor):
        try:
            return n/divisor
        except:
            return float('inf')

    safediv(10, 0)
    ```

    Se dice que las operaciones que **no lanzan excepciones son seguras**.
    De ahí el nombre.

2. Podemos refinar la captura de la excepción para distinguir entre un tipo
de excepción y otro:

    ```python
    def safediv(n, divisor):
        try:
            return n/divisor
        except ZeroDivisionError:
            return float('inf')
        except TypeError:
            return float('nan')

    safediv(10, 0)
    ```

    Una cláusula `except` **es compatible si no indica la clase (el caso más
    general) o si contiene la clase de la excepción o una clase padre**. La
    primera cláusula compatible, se ejecuta:

    ```python
    try:
        import no_existe
    except ModuleNotFoundError:
        print('ModuleNotFoundError')
    except ImportError:
        print('ImportError')
    ```

    Prueba a invertir las cláusulas. ¿Qué ocurre?

4. También podemos recoger varias excepciones con una misma cláusula:

    ```python
    try:
        import no_existe
    except (ModuleNotFoundError, ImportError) as ex:
        print('ModuleNotFoundError or ImportError?', type(ex))
    ```

    En realidad, la lista de errores puede ser cualquier **tupla**:

    ```python
    some_errors = (ModuleNotFoundError, ImportError)
    try:
        import no_existe
    except some_errors as ex:
        print('ModuleNotFoundError or ImportError?', type(ex))
    ```

5. Si queremos recoger la excepción en sí, usaremos las siguiente fórmula:

    ```python
    def log_module_absence(name):
        ...

    try:
        import no_existe
    except ModuleNotFoundError as ex:
        log_module_absence(ex.name)
        raise ex
    ```

    Equivalentemente, cuando queramos elevar la misma excepción que hemos
    capturado, podemos hacer:

    ```python
    def log_module_absence(name):
        ...

    try:
        import no_existe
    except ModuleNotFoundError as ex:
        log_module_absence(ex.name)
        raise # equivalent to raise ex
    ```

6. Hay situaciones en las que queremos ejecutar código tanto si se produce
una excepción como si no. Por ejemplo:

    ```python
    def do_computations(*args):
        raise Exception

    def store_computations(file, *args):
        f = open(file, 'w')
        for arg in args:
            result = do_computation(arg)
            f.write(result)
        f.close() # very important: close before returning
        return result
    ```

    Es importante y parte del contrato de uso de los ficheros, cerrar el
    fichero cuando hayamos terminado de utilizarlo. Dejarlo abierto lleva
    a comportamientos indefinidos, a menudo no deseados.

5. Si se produce una excepción, queremos **también** cerrar el fichero:

    ```python
    def do_computations(*args):
        raise Exception

    def store_computations(file, *args):
        try:
            f = open(file, 'w')
            for arg in args:
                result = do_computation(arg)
                f.write(result)
            f.close()
            return result
        except:
            f.close() # very important: close before returning
            raise
    ```

6. En lugar de utilizar este patrón, es mejor usar la cláusula `finally`:

    ```python
    def do_computations(*args):
        raise Exception

    def store_computations(file, *args):
        try:
            f = open(file, 'w')
            for arg in args:
                result = do_computation(arg)
                f.write(result)
        finally:
            f.close()

        return result
    ```

### Contextos y gestión de excepciones

A veces te encontrarás escribiendo código con esta pinta:

```python
# set-up code
...
...
# main code
...
...
# clean-up code
...
...
```

Por ejemplo, en el caso anterior:

```python
def store_computations(file, *args):
    # set-up
    try:
        f = open(file, 'w')
        # main code
        for arg in args:
            result = do_computation(arg)
            f.write(result)

    # clean-up
    finally:
        f.close()

    return result
```

Para abstraer y sintetizar este patrón utilizamos **contextos**. Los contextos
son una de las características más prominentes de Python 3 y le dedicaremos
más tiempo cuando estudiemos protocolos.

Por el momento, baste decir que los **contextos son objetos que incluyen código
de inicialización (_set-up_) y limpieza (_clean-up_) predefinidos**. Los
contextos pueden, también, capturar y manejar las excepciones que ocurran
durante la ejecución del código principal (_main code_).

1. Un contexto se usa con la sintáxis `with`. El caso de los ficheros es el
ejemplo paradigmático: aún mejor que usar una cláusula `finally` es
[usar un bloque `with`](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions):

    ```python
    def store_computations(file, *args):
        with open(file) as f:
            result = do_computation(*args)
            f.write(result)

        return result
    ```

2. Otro contexto de utilidad es la supresión de una excepción. En lugar de
hacer:

    ```python
    try:
        raise ValueError:
    except:
        pass
    ```

    Hacemos, de forma más clara y semántica:

    ```python
    from contextlib import suppress
    with suppress(Exception):
        raise ValueError
    ```

    Observa las diferencias entre este contexto y el contexto del ejemplo
    anterior. El contexto devuelto por `open` no suprime la excepción, sólo
    la captura, cierra el fichero, y la relanza. El contexto devuelto por
    [`suppress(Exception)`](https://docs.python.org/3/library/contextlib.html#contextlib.suppress),
    captura y suprime cualquier excepción.

* Si estás interesado en otros contextos, échale un vistazo al
módulo [contextlib](https://docs.python.org/3/library/contextlib.html).

* Los bloques `try ... except ...` pueden tener una
[cláusula `else`](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
con código del que no esperes ningún error (código seguro).

## Excepciones y causas

La información que acompaña a una excepción es vital para depurar el problema.
El mensaje, dónde se produjo y la pila de llamadas son importantes. Python,
además, permite indicar que una excepción fue la causa de otra.

1. Considera el siguiente código:

    ```python
    class LibraryError(Exception): ...

    def do_computations(*args):
        raise Exception('Invalid computation')

    def do_something(*args):
        try:
            do_computations(*args)
        except Exception:
            print('Something bad happened')
            raise LibraryError('Library cannot do as instructed.')

    do_something()
    ```

    Fíjate en que la excepción indica exactamente lo que ha pasado: _`During
    handling of the above exception, another exception occurred`_.

2. Sin embargo, no es que haya pasado "algo"; lo que queríamos decir es que
la excepción de `do_computations` **causa** la excepción de `do_something`.
Esto se puede indicar de manera más explícita con una sentencia `raise ... from
...`:

    ```python
    class LibraryError(Exception): ...

    def do_computations(*args):
        raise Exception('Invalid computation')

    def do_something(*args):
        try:
            do_computations(*args)
        except Exception as ex:
            print('Something bad happened')
            raise LibraryError('Library cannot do as instructed.') from ex

    do_something()
    ```

    Fíjate cómo ahora indica: _`The above exception was the direct cause of the following exception`_, significando que la excepción de `do_computations`
    **es la causa** de la excepción de `do_something`.

3. Sin embargo, a veces es posible que se quiera ocultar la causa de la
excepción. Si este es el caso, se deberá usar:

    ```python
    class LibraryError(Exception): ...

    def do_computations(*args):
        raise Exception('Invalid computation')

    def do_something(*args):
        try:
            do_computations(*args)
        except Exception as ex:
            print('Something bad happened')
            raise LibraryError('Library cannot do as instructed.') from None

    do_something()
    ```

4. A estos tres estilos anteriores falta sumarle la mera propagación de una
excepción (es decir, no tiene otra causa) que ya has aprendido:

    ```python
    class LibraryError(Exception): ...

    def do_computations(*args):
        raise Exception('Invalid computation')

    def do_something(*args):
        try:
            do_computations(*args)
        except Exception:
            print('Something bad happened')
            raise

    do_something()
    ```

## Cuándo usar excepciones

Se ha hablado mucho del coste de las excepciones. Es importante atender al
nombre de esta herramienta. Una excepción debería ocurrir **excepcionalmente**.
Si una situación puede ocurrir con cierta frecuencia, deja de ser algo
excepcional.

Alguna literatura al respecto:

* [Good Exception Management Rules of Thumb](https://www.hanselman.com/blog/GoodExceptionManagementRulesOfThumb.aspx)*
* [Performance Penalty of Python Exception](http://gerg.ca/blog/post/2015/try-except-speed/)*
* [How fast are exceptions?](https://docs.python.org/3/faq/design.html#how-fast-are-exceptions)
