# Scarlett
PROCESO DE TRABAJO
  1. Crear una rama apartir de la main
  2. Hacemos un PULL de la rama que hemos creado a nuestro local (Aplicar todos los cambios solo a esa rama)
  3. Anter de hacer la PR hacemos un Pull de la main para asegurarnos que no hay nuevos cambios mientras estabamos trabajando.
  4. Al terminar hacer un PUSH de nuestra rama a la rama main.
  5. Comprobar los cambios y mergear la rama desde el Git

COMO ACTUALIZAR UNA RAMA
  1. git fetch
  2. git checkout main
  3. git pull
  4. git checkout "tu rama"
  5. git merge main "tu rama"

NUNCA TRABAJAR DIRECTAMENTE SOBRE Main

Se deberia crear una rama por cada punto conseguido.

**Nomenclatura**

- style/ : si es algo de diseño
- bugfix/ : resolucion de errores
- feature/ : nuevo desarrollo

Ejemplo: feature/SCAR-X(Numero de ticket del Kanban)-nombre(funcionalidad del ticket)

Los espacios se separan por -
