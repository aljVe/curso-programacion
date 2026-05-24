# Conceptos

## Alex
***LLM*** - Modelo de Lenguaje Grande. Modelo entrenado con una cantidad masiva de datos. Trabajan prediciendo el siguiente token en base a sus datos de entrenamiento. Básicamente, ChatGPT, Claude, Gemini, etc.

> ⚠️ **NOTA PARA PPT:** Las diferencias prácticas entre modelos (Claude, ChatGPT, Gemini, Copilot) se desarrollarán en voz alta. Si se genera presentación, incluir una diapositiva de apoyo con tabla comparativa básica, no como contenido exhaustivo.

***Prompt*** - Instrucciones que le damos al LLM para que genere código o texto.
***Token*** - Unidad mínima de texto que el LLM puede procesar. Como los morfemas que se estudiaban en lengua.
***ventana de Contexto*** - Es la cantidad de tokens que el LLM puede procesar en un momento dado. Para entendernos, es la "memoria activa de trabajo por sesión" del LLM.

***Lenguaje de programación:*** - Es un lenguaje formal que permite al programador especificar un conjunto de instrucciones que serán ejecutadas por un computador. Para entendernos, es como un idioma que el computador entiende. Existen múltiples lenguajes de programación, cada uno con sus ventajas e inconvenientes.

***IDE:*** - Entorno de Desarrollo Integrado. Es un programa informático utilizado para la creación y modificación de software. Es el word que se utiliza para programar. ¿Se podría escribir lenguaje de programación en el bloc de notas? Sí, y funcionaría, pero es lo mismo que usar el bloc de notas como procesador de texto. Suele incluir herramientas que permite predecir palabras, expresiones, señala fallos en la escritura del código, y ahora los hay con IA.

***Git y GitHub:*** Git es un programa gratuito diseñado para el control de versiones de software; actúa en local. GitHub es un repositorio online donde frecuentemente los programadores suben su contenido, pudiendo hacerlos públicos o mantenerlos como repositorios privados.

***Vibe Coding:*** Es una metodología de desarrollo de software que consiste en generar código usando la IA a través de prompts.



---
## David


(***Niveles de vibe coding:***
Se pueden desarrollar programas con mayor o menor intervención por nuestra parte. La manera más sencilla son los artifacts. Empezaron en Claude pero se han extendido al resto de LLMs. Consisten en pequeños programas que se crean y ejecutan en la propia interfaz del LLM. Cada proveedor les ha dado un nombre distinto y en ocasiones requieren que se active alguna funcionalidad tipo canva para que se creen.

Posteriormente podríamos pedirle a un LLM que nos cree un programa sencillo de archivo único, lo copiamos en el bloc de notas, lo guardamos con la extensión (.py; .html; .java, etc) que nos indique la IA y listo, a ejecutarlo.

Luego vendrían IDEs tipo la nueva versión de antigravity, en la cual prácticamente no se ve el código y por último, los IDE con IA tipo Cursor o Antigravity IDE.

Hay sistemas algo más complejos y menos "amigables" que consisten en programar a través de la terminal del ordenador. Esto se denomina "CLI" (Command Line Interface) y el ejemplo paradigmático sería Claude Code, aunque su entorno actual permite también trabajar con un entorno gráfico.)

---

### Agentes IA y su integración

***Agentes IA vs Chatbots***
NOTA PARA LA IA: NO INCLUIR ESTO EN LA PRESENTACIÓN, LO DIREMOS DE PALABRA.
Los chatbots son esos sistemas de IA (LLM) en los que pensamos habitualmente, ChatGPT, Claude, Gemini; tienen una interfaz con un cuadro de texto, se les lanza un prompt y nos dan una respuesta.
Si a esos chatbots les damos la capacidad para utilizar herramientas y cierta autonomía para llevar a cabo tareas, estaríamos empezando a hablar de agentes. Los hay más simples y más complejos. La forma inicial fueron los "deep research", en los que al chatbot se le proveyó de herramientas para realizar búsquedas online y recopilar información para luego estructurarla. 
Los IDEs que usan IA actualmente se comportan más como agentes, ya que suelen tener la capacidad de realizar búsquedas online, ejecutar ellos mismos el código y si les damos permiso, usar la terminal o el propio ordenador.

Estos IDEs agénticos, para gente lega, principalmente serían Antigravity, que estaría disponible únicamente para las cuentas de pago de Google, Codex (que creo que también pero de OpenAI), Claude Code pero límites de uso muy marcado incluso en cuentas de pago. De manera gratuita, tiene mejores límites Cursor.

***Arquitectura muy muy básica:***
Los programas tienen un frontend o interfaz, es lo que se ve de los programas.
Posteriormente tienen un servidor o backend. Sería el centro del programa, lo que alberga su función propiamente dicha.
***Bases de datos:*** Finalmente los programas pueden tener bases de datos (o no), que son archivos en los que se almacena información. Esto será clave para aquellos programas que requieran recordar información de una sesión a otra. También puede ser información clave para ejecutar los programas, si hacemos un programa que muestre dosis de perfusiones, podríamos hacer un archivo específico del que se recupere la información por si en un futuro queremos añadir nuevos fármacos sin tener que tocar todos los archivos que forman el programa.

***MCP:***
Los MCP o Model Context Protocol son protocolos que definen cómo un LLM puede exponer y usar herramientas externas. Ejemplo: flow con Mermaid o Google Calendar, etc.

***Lenguajes:***
NOTA PARA LA IA: NO INCLUIR ESTO EN LA PRESENTACIÓN, LO DIREMOS DE PALABRA.
Cada lenguaje tiene sus características. Python por ejemplo es uno de los lenguajes "más sencillos" pero altamente funcional y es uno de los que mejor manejan los sistemas de IA. Otros son HTML, en los que se basa la mayoría de los frontend de los programas. Java por ejemplo suele estar compartimentalizado en paquetes, muy usado a nivel profesional. JavaScript es un lenguaje que se usa para frontend pero que también puede usarse en backend (Node.js) y que tiene como característica que se ejecuta en el navegador web (y no tanto en el ordenador como tal).
Por lo general, para programar y ejecutar algo de código, tienes que tener instalado los paquetes que contengan dicho lenguaje.
Si en algún momento queréis crear un programa para que se suba en vuestra intranet, es muy importante conocer qué lenguaje y sistema utilizan de frontend, backend y el servidor, así como la versión del lenguaje.

Para pequeños ejecutables, recomiendo crear archivos tipo python, y posteriormente pedirle a la IA que te explique cómo convertirlo en un archivo ejecutable (que en Windows sería un .exe).

***Skills (Claude):*** instrucciones/prompts preconfigurados que le dicen a Claude cómo comportarse en una tarea concreta. Pueden ser simples instrucciones o comandos de programación concretos. Ejemplo: AI template.

***Extensiones (IDE):*** Las extensiones son el equivalente a las skills en Antigravity. Permiten conectar Antigravity con otras herramientas. 


# Ideas para programas
***Hipomagnesemia e hipofosfatemia*** Te descargas las páginas directamente de UpToDate y las pones en una carpeta y haces un primer programa.

***Descargar cualquier protocolo de alguien del público y hacer un programa***

***Cálculo de dosis de perfusiones***

***Programa con base de datos con fármacos supabase*** 


# Hackaton

# Automatizaciones

Sólo si sobra tiempo.

***Apps script***
Ejemplo formulario satisfacción de consulta.


***Make***
Buzón de sugerencias.



