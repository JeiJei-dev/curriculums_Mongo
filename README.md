# curriculums_Mongo

## Enunciado

Los grupos deberán instalar la base de datos MongoDB y cargarla con datos diferentes curriculums, para posteriormente realizar consultas sobre todos estos documentos, en la búsqueda de generar información del conjunto, como pueden ser los intereses más comunes, la cantidad de herramientas manejada por cada individuo, trabajos realizados, entre otros.

Se espera que durante esta experiencia el grupo:

Asimile los conceptos de Colección y Documento.
- Defina un base de datos y una colección donde almacenar los documentos.
- Importe los Curriculums Vitae que se recopilarán con este propósito.
- Realizar operaciones de creación, eliminación y actualización de documentos.
- Realizar operaciones de búsqueda de documentos.

Cada grupo deberá elaborar al menos10 curriculums de diferentes personas. Estos 10 curriculums deben ser en formato JSON, formarán el total de documentos a importar en la base de datos.

Cada curriculum deberá contar con los siguientes campos, sin estar limitado a agregar otros:
- Resumen: texto que englobe todo lo contenido en el curriculum. Un párrafo de presentación.
- Datos Personales: Nombre, Dirección, Teléfonos, Email, Redes Sociales.
- Educación: Enseñanza Básica, Enseñanza media, Educación Universitaria, Otros.
- Laboral: Pasantía, Trabajos (freelancer, empleado, emprendedor, etc).
- Conocimientos Técnicos: OS, Lenguaje de Desarrollo, Bases de Datos, Mobiles (app), Otros Softwares.
- Intereses Personales: Deporte, Música, Animales, Entretenimiento. 

 Los equipos tienen la libertad de agregar los campos que estimen pertinentes y estructurarlos de la manera que deseen, pero cumpliendo con los siguientes requerimientos mínimos:
1. Un resumen que corresponda a un campo de texto.
2. Una clave con múltiples valores (key1:[val1, val2…])
3. Una clave de documentos (key:[(key1:val1, key2:val2…),(key3:val3…)…])

El Proyecto incluye la elaboración de Informe en el que el equipo demuestre el aprendizaje de los criterios anteriormente señalados, el que incluirá las diferentes consultas ejecutadas, Este Informe corresponderá al README de Github.
