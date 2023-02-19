# Información de la aplicación

Aquí se muestra todo lo necesario para poder usar la aplicación. Desde como instalar, los archivos necesarios hasta comprobaciones.

Todo esta basado en un sistema de x64 bits, en caso de ser x86 bits se deberá compilar el programa en un Windows de 32 bits. 

> Los paquetes necesarios están en el archivo de **pyproject.toml** y para crear el instalador usando **main.spec** de pyintaller.

### Distribución de la aplicación  
Copiar y pegar la carpeta de **dist** en el equipo que instalamos la aplicación.  
  
Iniciar la aplicación un una terminal y usando el parámetro **-p** o **--path**.

> Ejemplo: $ main.exe -p C:/ruta/a/archivo.mdb

Si todo va bien se muestra un mensaje de éxito, en caso de fallo lanzara una excepción indicando que es lo que falla.

## Requisitos   
  
 1. Tener instalado **[VC_redist.x64](https://learn.microsoft.com/es-es/cpp/windows/latest-supported-vc-redist?view=msvc-170)** (necesario para instalar el driver odbc) Microsoft Access Driver. **"Microsoft Visual C++ _Redistributable_ Package (_64-bit_)"**.  
  
 2. Tener instalado el driver **[accessdatabaseengine_X64](https://www.microsoft.com/es-es/download/details.aspx?id=54920)** para poder acceder a Access desde el programa. **"Microsoft Access 2016 Runtime"**.  
      
### Comprobar que se ha instalado correctamente  
En Windows 10 ir a inicio -> Administrador de origen de datos ODBC (64 Bits) -> Controladores.   
  
Deberá aparecer **Microsoft Access Driver (\*.mdb, \*.accdb)**.

> Este programa nos indicara si todo esta correctamente instalado.

# Como crear archivo exe (pyinstaller)
Abrir una terminal y ejecutar **$ pyinstaller main.spec** teniendo el entorno virtual activo y los paquetes instalados **[Poetry](https://python-poetry.org/)**.

Automáticamente creara una carpeta llamada **dist** en el que se almacenara el ejecutable para usar. 