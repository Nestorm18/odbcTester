# Información de la aplicación

Aquí se muestra todo lo necesario para poder usar la aplicación. Desde como instalar, los archivos necesarios hasta comprobaciones.

Todo esta basado en un sistema de x64 bits, en caso de ser x86 bits se deberá compilar el programa en un Windows de 32 bits. 

> Los paquetes necesarios están en el archivo de **pyproject.toml** y para crear el instalador usando **main.spec** de pyintaller.

### Distribución de la aplicación  
Copiar y pegar la carpeta de **dist** en el equipo que instalamos la aplicación.  
  
Iniciar la aplicación un una terminal y usando el parámetro **-p** o **--path**.

> Ejemplo: $ main.exe -p C:/ruta/a/archivo.mdb

Si todo va bien se muestra un mensaje de éxito, en caso de fallo lanzara una excepción indicando que es lo que falla.

# Como crear archivo exe (pyinstaller)
Abrir una terminal y ejecutar **$ pyinstaller main.spec** teniendo el entorno virtual activo y los paquetes instalados **[Poetry](https://python-poetry.org/)**.

Automáticamente creara una carpeta llamada **dist** en el que se almacenara el ejecutable para usar. 