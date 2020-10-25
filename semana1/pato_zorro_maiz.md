# El cruce del pato, el zorro y el maíz

**Descripción del problema**
> Un granjero tiene que cruzar un río con un zorro, una gallina y un saco de maíz.
> Tiene un bote de remos, y sólo puede llevar con él una cosa en la barca.
> Si el zorro y el pato quedan solos, el zorro se come al pato.
> Si el pato y el maíz quedan solos, el pato se come el maíz.
> ¿Cómo lo conseguirá el hombre hacer cruzar el zorro, la gallina y el maíz?
> 
> Restricciones clave:
> 1. El granjero solo puede llevar a uno en el bote.
> 2. El zorro y el pato no pueden quedarse solos.
> 3. El pato y el maíz no pueden quedarse solos.

**Soluci[on del problema**
Antes de explicar la solución, se explicara el breve planteamiento. Entiendase que el río tiene un lado A y un lado B, el lado A es dónde encotramos inicialmente al granjero, al zorro, al pato y el maíz. El lado B es el otro lado, a donde se pretenden mover. Entonces, los movimientos son los siguientes:

1. El granjero debe llevar al ganso al punto B. Dejando al Zorro y el maíz solos.
2. El granjero debe regresar al lado A. Terminamos con el ganso en el lado B y el zorro, el maíz y el granjero en el lado A.
3. El granjero debe llevar al zorro al lado B. Ahora tenemos en el lado B al granjero, al zorro y al ganso y dejamos en lado A al maíz.
4. El granjero debe volver al lado A y llevar consigo al ganso. Ahora tenemos al zorro en el lado B y al granjero, al ganso y al maíz en el lado A.
5. Movemos al granjero devuelta al lado B junto con el máiz. Terminamos con el granjero, el zorro y el maíz en lado B y el ganso en el lado A.
6. El granjero regresa solo al lado B. El zorro y el maíz se quedan en el lado B mientras el granjero y el ganso en el lado A.
7. Finalmente, llevamos al granjero junto con e ganso al lado B. Con esto todos estan del lado B y nadie ni nada queda del lado A.

Todos cruzaron el río.