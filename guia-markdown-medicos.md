# Guia rapida de Markdown para medicos

Markdown es una forma sencilla de escribir texto estructurado usando simbolos faciles de recordar.

No es un lenguaje de programacion. Es una forma de escribir documentos que leen bien las personas, GitHub, muchas herramientas tecnicas y los agentes de IA.

## Por que importa en este curso

Markdown es util porque permite guardar informacion de forma:

- Clara para humanos.
- Facil de copiar y pegar.
- Facil de versionar con Git.
- Facil de leer para agentes de IA.
- Independiente de Word, PDF o formatos cerrados.
- Ligera: un archivo `.md` es texto plano.

Para un agente de IA, un documento Markdown bien organizado es mucho mejor que una conversacion larga y desordenada.

## Idea clave

Un buen archivo Markdown convierte conocimiento disperso en contexto reutilizable.

Ejemplos:

- `README.md`: explica que es un proyecto y como usarlo.
- `teoria.md`: contiene el material docente completo.
- `slides.md`: contiene las diapositivas de Slidev.
- `guia-markdown-medicos.md`: contiene esta guia.

El agente puede leer estos archivos, entender la estructura y proponer cambios con mas precision.

## Reglas basicas

1. Usa titulos para separar ideas.
2. Usa listas para pasos, criterios o riesgos.
3. Usa tablas para comparar opciones.
4. Usa bloques de codigo para ejemplos literales.
5. Usa enlaces para fuentes.
6. Escribe una idea por seccion.
7. No mezcles datos reales de pacientes en documentos docentes.

## Chuleta rapida

| Necesidad | Markdown | Resultado |
|-----------|----------|-----------|
| Titulo principal | `# Titulo` | Encabezado grande |
| Seccion | `## Seccion` | Encabezado de segundo nivel |
| Subseccion | `### Subseccion` | Encabezado de tercer nivel |
| Negrita | `**importante**` | Texto destacado |
| Cursiva | `*matiz*` | Texto enfatizado |
| Lista | `- Elemento` | Lista con puntos |
| Pasos | `1. Paso` | Lista numerada |
| Cita | `> Texto citado` | Bloque destacado |
| Codigo corto | `` `edad` `` | Texto literal |
| Bloque literal | Tres acentos graves | Ejemplo en bloque |
| Enlace | `[texto](https://...)` | Link clicable |
| Tarea | `- [ ] Pendiente` | Checklist |
| Tabla | Ver ejemplo abajo | Comparacion ordenada |

## Titulos

Usa titulos para que el documento tenga mapa.

```markdown
# Proyecto de calculadora clinica

## Objetivo

## Datos de entrada

## Riesgos

## Criterios de aceptacion
```

Para una IA, estos titulos son senales. Le dicen donde esta cada tipo de informacion.

## Listas

Usa listas cuando tengas elementos separados:

```markdown
Datos de entrada:

- Edad.
- ASA.
- Tipo de cirugia.
- Hemoglobina preoperatoria.
```

Usa listas numeradas cuando el orden importe:

```markdown
1. Abrir el repositorio.
2. Leer el README.
3. Ejecutar la aplicacion.
4. Revisar errores.
```

## Tablas

Las tablas son utiles para comparar tecnologias, riesgos o requisitos.

```markdown
| Campo | Tipo | Obligatorio | Comentario |
|-------|------|-------------|------------|
| edad | numero | si | Usar datos ficticios |
| diagnostico | texto | no | No introducir datos reales |
| riesgo | categoria | si | Bajo, medio o alto |
```

## Bloques de codigo o texto literal

Aunque no estemos programando, los bloques literales sirven para prompts, JSON, comandos o plantillas.

````markdown
```text
Quiero crear un prototipo educativo con datos ficticios.
No uses datos reales de pacientes.
Explica riesgos y criterios de aceptacion.
```
````

## Checklists

Las checklists ayudan a revisar tareas.

```markdown
- [ ] El prototipo usa datos ficticios.
- [ ] No contiene nombres ni numeros de historia.
- [ ] Hay criterios de aceptacion.
- [ ] Se ha probado al menos un caso limite.
```

## Plantilla util para pedir ayuda a una IA

```markdown
# Encargo

Quiero crear un prototipo educativo para medicos.

## Contexto

El publico no tiene experiencia tecnica.

## Objetivo

Explicar como registrar datos ficticios y mostrar una tabla.

## Restricciones

- No usar datos reales.
- Mantener lenguaje claro.
- No proponer una arquitectura compleja.

## Resultado esperado

- Una propuesta sencilla.
- Riesgos principales.
- Pasos para probarlo.

## Criterios de aceptacion

- Se entiende por un medico no programador.
- Los datos son ficticios.
- La solucion puede explicarse en clase.
```

## Buenas practicas para agentes de IA

Cuando prepares informacion para un agente:

- Pon el objetivo al principio.
- Separa contexto, restricciones y resultado esperado.
- Usa nombres de archivo claros.
- Incluye ejemplos pequenos.
- Di explicitamente que no use datos reales.
- Pide que primero explore y luego proponga.
- Pide resumen de cambios y riesgos.

Ejemplo:

```markdown
# Tarea para el agente

Explora este repositorio y explica que contiene.

No modifiques archivos todavia.

Despues propone tres mejoras concretas para que el curso sea mas claro para medicos no tecnicos.
```

## Errores frecuentes

- Escribir todo en un parrafo largo.
- No usar titulos.
- Mezclar teoria, tareas y riesgos sin separar.
- Pegar datos reales de pacientes.
- No indicar que archivos puede modificar la IA.
- No definir que significa "terminado".

## Frase para recordar

Markdown es una historia clinica del proyecto: ordena informacion, deja trazabilidad y ayuda a que otra persona o una IA entiendan el caso.
