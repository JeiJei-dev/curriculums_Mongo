curriculums_Mongo
Enunciado
Los grupos deberán instalar la base de datos MongoDB y cargarla con datos diferentes curriculums, para posteriormente realizar consultas sobre todos estos documentos, en la búsqueda de generar información del conjunto, como pueden ser los intereses más comunes, la cantidad de herramientas manejada por cada individuo, trabajos realizados, entre otros.

Se espera que durante esta experiencia el grupo:

Asimile los conceptos de Colección y Documento.

Defina un base de datos y una colección donde almacenar los documentos.
Importe los Curriculums Vitae que se recopilarán con este propósito.
Realizar operaciones de creación, eliminación y actualización de documentos.
Realizar operaciones de búsqueda de documentos.
Cada grupo deberá elaborar al menos10 curriculums de diferentes personas. Estos 10 curriculums deben ser en formato JSON, formarán el total de documentos a importar en la base de datos.

Cada curriculum deberá contar con los siguientes campos, sin estar limitado a agregar otros:

Resumen: texto que englobe todo lo contenido en el curriculum. Un párrafo de presentación.
Datos Personales: Nombre, Dirección, Teléfonos, Email, Redes Sociales.
Educación: Enseñanza Básica, Enseñanza media, Educación Universitaria, Otros.
Laboral: Pasantía, Trabajos (freelancer, empleado, emprendedor, etc).
Conocimientos Técnicos: OS, Lenguaje de Desarrollo, Bases de Datos, Mobiles (app), Otros Softwares.
Intereses Personales: Deporte, Música, Animales, Entretenimiento.
Los equipos tienen la libertad de agregar los campos que estimen pertinentes y estructurarlos de la manera que deseen, pero cumpliendo con los siguientes requerimientos mínimos:

Un resumen que corresponda a un campo de texto.
Una clave con múltiples valores (key1:[val1, val2…])
Una clave de documentos (key:[(key1:val1, key2:val2…),(key3:val3…)…])
El Proyecto incluye la elaboración de Informe en el que el equipo demuestre el aprendizaje de los criterios anteriormente señalados, el que incluirá las diferentes consultas ejecutadas, Este Informe corresponderá al README de Github.

Herramientas Utilizadas
GitHub: Como administrador del proyecto
MongoDB: Como Bases de datos
Mongosh: La shell de la base de datos
Python: Lenguaje de programación para funcionalidad
PyMongo: Libreria de Mongo para python, sirve para conectar mongodb con python
Conceptos utilizados en el proyecto
Uso de Colecciones y Documentos
Una clave con múltiples valores (key1:[val1, val2…])
Una clave de documentos (key:[(key1:val1, key2:val2…),(key3:val3…)…])
Operaciones de un CRUD
Estructura de la base de datos
//Una coleccion con multiples valores, algunos valores como laboral contienen otros documento

{ resumen: "Soy un desarrollador apasionado por la tecnología y la innovación, con experiencia en proyectos diversos y habilidades técnicas sólidas.", datosPersonales: { nombre: "Juan Pérez", cedula: "28456928", direccion: "Calle Principal 123", telefonos: ["123-456-789", "987-654-321"], email: "juanperez@example.com", edesSociales: ["Facebook: Juanito Pérez", "Twitter: @juanito"] }, educacion: { ensenanzaBasica: "Colegio San José", ensenanzaMedia: "Liceo Nacional", educacionUniversitaria: "Ingeniería en Informática", otros: ["Curso de programación", "Curso de ingles"] }, laboral: { pasantia: [ { empresa: "ABC Tech", descripción: "Desarrollador Junior" }, { empresa: "XYZ Software", descripción: "Analista de Datos" } ], trabajos: [ { tipo: "Freelancer", descripción: "Desarrollo de sitio web para cliente X" }, { tipo: "Empleado", descripción: "Desarrollador Full Stack" } ] }, conocimientosTecnicos: ["JavaScript", "Html", "Css"], interesesPersonales: ["Música", "Deporte"] }
