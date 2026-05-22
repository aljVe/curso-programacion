# Teoría Completa: Programación en IA desde Cero

Bienvenido al material teórico del curso. Aquí desarrollaremos en detalle cada uno de los puntos del temario para que sirva como guía de referencia permanente.

---

## 1. Fundamentos y Entorno

### 1.1 Conceptos de IA y herramientas principales
Antes de hablar de lenguajes, IDEs, arquitectura o aplicaciones, necesitamos entender qué papel juega realmente la inteligencia artificial en este curso.

El objetivo no es que el médico se convierta en programador profesional ni que memorice la sintaxis de Python, TypeScript o JavaScript. El objetivo es que aprenda a utilizar la IA como un **copiloto técnico** capaz de ayudarle a transformar una necesidad clínica en una solución digital bien planteada.

En otras palabras: no vamos a aprender solo a “escribir código”. Vamos a aprender a **pensar, especificar, pedir, revisar y dirigir** soluciones digitales asistidas por IA.

---

#### A. Qué es la IA generativa

La **IA generativa** es un tipo de inteligencia artificial capaz de crear contenido nuevo a partir de instrucciones del usuario. Puede generar texto, código, imágenes, esquemas, tablas, explicaciones, documentación, planes de trabajo o propuestas técnicas.

En el contexto de este curso, nos interesa especialmente su capacidad para ayudar a:

- Explicar conceptos técnicos en lenguaje comprensible.
- Convertir una idea clínica en una especificación funcional.
- Proponer arquitecturas de aplicaciones.
- Comparar tecnologías.
- Generar prototipos.
- Escribir código cuando sea necesario.
- Revisar errores.
- Crear documentación.
- Diseñar casos de prueba.
- Detectar riesgos de privacidad, seguridad o mantenimiento.

La IA generativa no sustituye al conocimiento médico ni convierte automáticamente una idea en una herramienta segura. Es una ayuda potente, pero necesita dirección, contexto y revisión crítica.

---

#### B. Qué es un LLM

Un **LLM** (*Large Language Model* o modelo grande de lenguaje) es un sistema de IA entrenado para comprender y generar lenguaje natural y código.

Ejemplos conocidos de LLMs son modelos como ChatGPT, Claude, Gemini u otros sistemas similares.

Un LLM puede actuar como:

- Profesor que explica conceptos.
- Traductor entre lenguaje clínico y lenguaje técnico.
- Asistente para diseñar una aplicación.
- Generador de prompts.
- Revisor de documentación.
- Ayudante para escribir código.
- Consultor para comparar tecnologías.
- Simulador de casos de prueba.

Pero un LLM también puede equivocarse. Puede inventar información, proponer soluciones demasiado complejas, generar código inseguro, olvidar requisitos importantes o no comprender del todo el contexto clínico.

Por eso, en este curso no trataremos la IA como una “máquina que lo hace todo”, sino como un copiloto al que hay que saber dirigir.

---

#### C. El cambio importante: del médico que pide “hazme una app” al médico que especifica bien

Una petición poco útil sería:

> “Hazme una aplicación para gestionar pacientes.”

Esa frase es demasiado amplia. No define el usuario, el problema, los datos, los riesgos ni el resultado esperado.

Una petición mucho mejor sería:

> “Quiero diseñar un prototipo educativo de una aplicación para registrar pacientes ficticios en una consulta. Debe tener un formulario con edad, diagnóstico y tratamiento, una tabla de resultados y un botón para exportar los datos. No debe usar datos reales. Propón una arquitectura sencilla, indica si conviene usar Python o TypeScript, y explícame qué partes tendría que revisar un desarrollador antes de usarlo en un entorno real.”

La diferencia no está en saber programar más, sino en saber **pensar y pedir mejor**.

---

#### D. Qué puede hacer bien la IA en un proyecto digital sanitario

La IA puede ser especialmente útil para tareas como:

- Ordenar ideas iniciales.
- Convertir un protocolo clínico en pasos lógicos.
- Proponer el flujo de una aplicación.
- Crear una primera versión de una especificación funcional.
- Sugerir qué tecnología usar según el problema.
- Explicar diferencias entre Python, TypeScript, SQL, APIs o bases de datos.
- Generar ejemplos con datos ficticios.
- Crear prototipos rápidos.
- Revisar si una solución parece demasiado compleja.
- Generar documentación para usuarios médicos.
- Proponer listas de comprobación de seguridad y privacidad.

Por ejemplo, ante la idea “quiero automatizar informes”, la IA puede ayudar a descomponer el problema:

- Qué datos entran.
- De dónde vienen esos datos.
- Qué plantilla de informe se usa.
- Qué partes son fijas.
- Qué partes cambian.
- Qué validaciones hacen falta.
- Qué riesgos existen.
- Qué tecnología podría ser suficiente.

---

#### E. Qué NO debemos delegar ciegamente en la IA

En medicina, una herramienta digital puede tener consecuencias clínicas. Por eso no debemos aceptar sin revisión:

- Reglas clínicas generadas por IA sin validar.
- Cálculos médicos no comprobados.
- Recomendaciones terapéuticas automatizadas.
- Procesamiento de datos reales de pacientes sin garantías.
- Arquitecturas que almacenen información sensible sin control.
- Código generado sin revisión técnica.
- Aplicaciones que se usen en pacientes reales sin validación clínica, legal y de seguridad.

La IA puede ayudar a construir, pero la responsabilidad de validar el uso clínico no desaparece.

---

#### F. Herramientas principales de IA que aparecerán en el curso

A lo largo del curso podemos usar o mencionar varias familias de herramientas:

##### 1. Chats de IA generalistas

Son herramientas conversacionales que permiten preguntar, razonar, resumir, explicar, generar documentación o ayudar con código.

Ejemplos:

- ChatGPT.
- Claude.
- Gemini.

Uso típico en este curso:

- Pedir explicaciones.
- Diseñar prompts.
- Comparar tecnologías.
- Revisar propuestas.
- Crear especificaciones.
- Generar ejemplos docentes.

##### 2. IDEs con IA

Un **IDE** es un entorno de trabajo para crear software. Algunos IDEs modernos integran IA para ayudar a escribir, revisar y modificar proyectos.

Ejemplos:

- Cursor.
- Windsurf.
- Visual Studio Code con extensiones de IA.
- Antigravity u otros entornos con agentes.

Uso típico en este curso:

- Abrir un proyecto.
- Pedir a la IA que lea varios archivos.
- Solicitar cambios concretos.
- Revisar errores.
- Generar documentación.
- Comprender la arquitectura de una aplicación.

##### 3. Agentes de programación

Un agente de programación es una IA capaz de trabajar con varios archivos, planificar cambios, ejecutar pasos y ayudar en tareas más largas.

Puede servir para:

- Analizar un repositorio.
- Proponer una estructura de proyecto.
- Modificar varios archivos relacionados.
- Revisar documentación.
- Buscar errores.
- Crear pruebas.
- Explicar cómo funciona una aplicación existente.

El médico no necesita conocer todos los detalles internos, pero sí debe saber darle instrucciones claras y revisar críticamente su resultado.

##### 4. Herramientas no-code y low-code

Son plataformas que permiten crear automatizaciones o aplicaciones sencillas con poco o ningún código.

Ejemplos:

- Google Forms.
- Google Sheets.
- Make.
- n8n.
- Airtable.
- Retool u otras plataformas similares.

Uso típico:

- Formularios.
- Automatización de correos.
- Recogida de datos.
- Flujos administrativos.
- Prototipos rápidos.

##### 5. Herramientas de prototipado

Permiten crear versiones iniciales de una idea antes de desarrollar un producto completo.

Ejemplos:

- Streamlit.
- Google Colab.
- Replit.
- GitHub Codespaces.
- Aplicaciones sencillas generadas con IA.

Uso típico:

- Calculadoras clínicas.
- Dashboards simples.
- Análisis de Excel.
- Interfaces básicas.
- Pruebas con datos ficticios.

---

#### G. El papel del médico en un proyecto con IA

El médico aporta algo que la IA no tiene por sí sola: el conocimiento real del problema clínico.

Su papel es definir:

- Qué problema merece la pena resolver.
- Qué usuario utilizará la herramienta.
- Qué flujo asistencial hay que respetar.
- Qué datos son necesarios y cuáles no.
- Qué errores serían clínicamente relevantes.
- Qué salida debe generar la herramienta.
- Qué límites debe tener.
- Qué debe validarse antes de usarlo en la práctica real.

La IA puede ayudar con el “cómo”, pero el médico debe dirigir el “para qué”, el “en qué contexto” y el “con qué límites”.

---

#### H. Ejemplo práctico: una calculadora clínica

Idea inicial:

> “Quiero una calculadora médica.”

Esto no es suficiente.

Una versión mejor especificada sería:

> “Quiero diseñar un calculador clínico educativo. El usuario introducirá variables ficticias de un paciente. La herramienta calculará una puntuación, mostrará una categoría de riesgo y explicará qué variables han influido en el resultado. No debe almacenar datos reales. Quiero que me propongas si conviene hacerla como hoja de cálculo, script en Python, app en Streamlit o aplicación web con TypeScript. Prioriza la opción más sencilla y segura para un prototipo.”

Esta forma de pedir obliga a la IA a razonar sobre:

- Usuario.
- Datos.
- Salida.
- Privacidad.
- Tecnología.
- Nivel de complejidad.
- Seguridad.
- Uso educativo frente a uso clínico real.

---

#### I. Principios de uso seguro de IA en este curso

Durante el curso seguiremos estos principios:

1. Usar datos ficticios o anonimizados.
2. No introducir información identificable de pacientes en herramientas externas sin garantías.
3. Separar claramente prototipos educativos de herramientas asistenciales reales.
4. Validar cualquier regla clínica con fuentes fiables.
5. Revisar los cálculos y casos límite.
6. Pedir siempre a la IA que explique sus decisiones.
7. Preferir soluciones simples antes que arquitecturas complejas.
8. Documentar qué hace la herramienta y qué no hace.
9. Pedir revisión técnica cuando una herramienta vaya a crecer.
10. Pedir revisión clínica, legal y de seguridad antes de usarla con pacientes reales.

---

#### J. Idea clave

La IA no elimina la necesidad de pensar bien. La aumenta.

Cuanto mejor definido esté el problema, mejor será la respuesta de la IA.

En este curso aprenderemos a formular problemas clínicos como soluciones digitales: con objetivos claros, datos definidos, reglas explícitas, riesgos identificados y una arquitectura razonable.

### 1.2 Lenguajes de programación e IDEs

Para programar, necesitamos dos cosas fundamentales: un **idioma** para hablar con el ordenador y un **lugar** donde escribirlo.

#### A. Los Lenguajes de Programación: El "Idioma"
Un lenguaje de programación es simplemente un conjunto de reglas y palabras que nos permiten dar instrucciones precisas a una computadora. En este curso nos centramos en los dos más populares y útiles:

*   **Python:** Es el lenguaje más recomendado para empezar. Su sintaxis es clara y directa, muy parecida al inglés, y es extremadamente versátil. Se usa para automatizar tareas, analizar datos y es el estándar de referencia en el mundo de la Inteligencia Artificial.
*   **JavaScript:** Es el lenguaje de la web. Si quieres crear una página interactiva o una aplicación que funcione en el navegador, necesitas JavaScript.
*   **TypeScript:** Es una versión "mejorada" y más segura de JavaScript. Es el estándar actual en el desarrollo profesional porque ayuda a detectar y evitar errores durante la escritura del código. Si JavaScript es el lenguaje base, TypeScript añade una capa de validación y control de tipos que garantiza la robustez del software.

**¿Por qué usamos estos y no otros?** Porque tienen las comunidades más grandes, lo que significa que la IA (como ChatGPT o Claude) los conoce a la perfección y puede ayudarte mejor a escribir código en ellos.

#### B. Los IDEs: El "Taller" de Trabajo
Un **IDE** (*Integrated Development Environment*) es simplemente un programa diseñado para escribir código. La mejor analogía es pensar en él como un "Microsoft Word" diseñado específicamente para programar: así como Word te ayuda a redactar documentos con correctores y formatos, un IDE te ayuda a escribir instrucciones para el ordenador, detectando errores y organizando tu proyecto de forma eficiente.

*   **VS Code (Visual Studio Code):** Es el estándar de la industria. Es gratuito, ligero y altamente personalizable mediante extensiones.
*   **Cursor:** El pionero de los IDEs nativos de IA. Basado en VS Code, permite una interacción profunda donde el usuario guía a la IA de forma **explícita** (usando el símbolo `@` para indicar archivos o carpetas). Es una herramienta muy madura y robusta.
*   **Windsurf:** Creado por Codeium, es también un entorno basado en VS Code. Su principal diferencia es el uso de **contexto implícito** (su motor "Cascade" intenta entender qué archivos son relevantes sin que tengas que indicárselo manualmente) y un enfoque basado en flujos de trabajo autónomos.
*   **Antigravity:** Familia de herramientas agente de Google para trabajar con proyectos de software desde varias superficies: una aplicación central, una CLI, un SDK y un IDE. Es útil para explicar a los alumnos que "usar IA para programar" ya no significa solo chatear, sino coordinar agentes que pueden leer repositorios, planificar cambios, ejecutar comandos y devolver artefactos revisables.

#### C. Entornos Interactivos y Notebooks (Ciencia de Datos)
Existen otros entornos muy populares, especialmente en el mundo científico y de investigación, que funcionan de forma distinta a los IDEs tradicionales. Se basan en el concepto de "Notebook" o cuaderno interactivo.

*   **Jupyter Notebook:** Es como un cuaderno digital donde puedes mezclar bloques de código, texto explicativo, gráficas y resultados en un mismo documento. Es ideal para experimentar y analizar datos paso a paso.
*   **Anaconda:** No es un editor en sí, sino una "caja de herramientas" que instala automáticamente Python y las librerías más importantes para ciencia de datos, incluyendo Jupyter.
*   **Google Colab:** Es una versión de Jupyter que funciona totalmente en la nube. No requiere instalar nada en tu ordenador y utiliza la potencia de los servidores de Google. Es la forma más rápida de empezar a programar con IA y datos sin configurar nada.

> **Idea clave:** No necesitas memorizar el lenguaje. Tu trabajo ahora es saber **qué** quieres hacer y dejar que el **IDE** y la **IA** te ayuden con el **cómo** se escribe.

### 1.3 Configuración del entorno local

Configurar el entorno local significa preparar el ordenador para poder crear, abrir, modificar, probar y guardar proyectos de software.

Para un médico que empieza desde cero, esta parte puede parecer la más técnica. Sin embargo, no hay que entenderlo como "instalar cosas raras", sino como preparar una mesa de trabajo:

- El **navegador** sirve para probar aplicaciones web.
- El **editor o IDE** sirve para leer y modificar el código.
- La **terminal** sirve para dar instrucciones al ordenador.
- **Git** sirve para guardar el historial de cambios.
- **GitHub** sirve para guardar una copia online, colaborar y compartir.
- **Node.js** sirve para ejecutar muchas aplicaciones web modernas.
- **Python** sirve para automatizar tareas, analizar datos y crear prototipos científicos.

No hace falta dominar todo el entorno desde el primer día. Basta con saber para qué sirve cada pieza y aprender el flujo básico.

---

#### A. Médico Dev Starter Pack

No todas las herramientas mencionadas en el curso son necesarias al principio. De hecho, uno de los errores habituales es intentar instalar demasiadas cosas antes de entender para qué sirven.

Para un médico que empieza, el objetivo no es tener un arsenal técnico, sino un entorno pequeño, comprensible y suficiente para completar los primeros proyectos.

El starter pack debe organizarse por niveles.

---

##### Nivel 0: imprescindible para empezar

Con esto ya se puede dar una clase completa:

1. **Navegador: Google Chrome o Microsoft Edge**
   - Para abrir aplicaciones web locales.
   - Para probar prototipos.
   - Para usar herramientas de IA en navegador.

2. **Editor: Visual Studio Code o Windsurf**
   - Para abrir carpetas de proyecto.
   - Para ver archivos.
   - Para pedir ayuda a la IA sobre el código.

3. **Git**
   - Para guardar versiones.
   - Para volver atrás si rompemos algo.
   - Para trabajar con repositorios.

4. **Node.js y npm**
   - Para ejecutar proyectos web sencillos.
   - Para usar herramientas como Slidev.

5. **Python**
   - Para automatización.
   - Para análisis de datos.
   - Para scripts clínicos sencillos con datos ficticios.

6. **Una herramienta de IA**
   - Puede ser ChatGPT, Claude, Gemini, Windsurf, Codex u otra similar.
   - Lo importante es aprender a darle contexto, límites y criterios de aceptación.

Mensaje para el alumno:

> "Con navegador, editor, Git, Node.js, Python y una IA ya puedes empezar. Todo lo demás llegará cuando el problema lo justifique."

---

##### Nivel 1: recomendable tras los primeros proyectos

Cuando el alumno ya ha abierto un repositorio, ejecutado un proyecto y hecho pequeños cambios, tiene sentido añadir:

1. **Cuenta de GitHub**
   - Para alojar repositorios.
   - Para compartir proyectos.
   - Para desplegar documentación o prototipos.

2. **pip o uv**
   - Para instalar librerías Python de forma controlada.

3. **Jupyter o Google Colab**
   - Para análisis de datos y notebooks.

4. **Streamlit**
   - Para crear aplicaciones docentes sencillas con Python.

5. **Un agente de programación integrado**
   - Por ejemplo Windsurf, Cursor, Codex, Claude Code o similar.

Este nivel permite empezar a construir prototipos más útiles sin saturar la primera sesión.

---

##### Nivel 2: avanzado o docente

Estas herramientas son potentes, pero no deberían presentarse como requisito inicial:

- **Docker**: útil para aislar entornos complejos.
- **GitHub CLI**: útil para usuarios avanzados; GitHub web basta al inicio.
- **nvm**: permite cambiar versiones de Node, pero puede confundir al principiante.
- **pnpm o yarn**: alternativas a npm; npm es suficiente para empezar.
- **Netlify, Railway u otras CLIs de despliegue**: útiles cuando ya hay prototipos publicables.
- **Mermaid CLI**: útil para diagramas, no esencial.
- **Codex CLI, Claude Code, Gemini CLI**: potentes, pero mejor después de entender carpetas, commits y dependencias.
- **MCP y skills avanzadas**: interesantes para ampliar capacidades, no para el primer contacto.
- **n8n, Make u otras plataformas no-code**: útiles en automatización, pero no necesarias para aprender la base.

Idea clave:

> La herramienta correcta es la que resuelve el siguiente problema del alumno, no la que parece más avanzada.

En una clase corta, no conviene convertir la instalación en el centro de la sesión. Si el tiempo es limitado, lo más práctico es ofrecer una guía previa de instalación, usar proyectos ya preparados y presentar las herramientas avanzadas como una segunda fase.

---

#### B. Mapa mental del entorno

Un proyecto de programación suele tener estas piezas:

- **Carpeta del proyecto**: el espacio donde vive todo.
- **Archivos de código**: contienen la lógica.
- **Archivos de configuración**: indican cómo se ejecuta el proyecto.
- **Dependencias**: paquetes externos que el proyecto necesita.
- **Repositorio Git**: historial de cambios del proyecto.
- **README**: instrucciones para entender y ejecutar el proyecto.

Ejemplo en este repositorio:

- `slides.md`: presentación principal en Slidev.
- `teoria.md`: material teórico largo.
- `index.md`: resumen del temario.
- `package.json`: lista de comandos y dependencias.
- `node_modules`: paquetes instalados por Node.js.
- `dist`: salida generada al construir la presentación.

La idea importante para los alumnos es esta: **un proyecto no es un único archivo**. Es una carpeta organizada con varias piezas que se relacionan entre sí.

---

#### C. Entornos de trabajo aislados

Cuando empezamos a crear varios proyectos, aparece un problema muy habitual: cada proyecto puede necesitar librerías, versiones o configuraciones distintas.

Ejemplo:

- Un proyecto de slides puede necesitar Slidev.
- Un prototipo de análisis de datos puede necesitar Python, pandas y matplotlib.
- Una app web puede necesitar React, TypeScript y una base de datos.
- Una automatización puede necesitar credenciales y variables de entorno propias.

Si mezclamos todo en una única carpeta o instalamos dependencias sin orden, es fácil que un proyecto rompa otro.

La idea de un **entorno aislado** es sencilla:

> Cada proyecto debe vivir en su propia carpeta, con sus propias dependencias, su propio historial Git y sus propias instrucciones.

---

##### 1. Aislamiento por repositorio

La forma más básica y útil de aislar trabajo es crear un repositorio diferente para cada proyecto.

Ejemplo de organización:

```text
proyectos/
  curso-IA-programacion/
  calculadora-riesgo-docente/
  analisis-actividad-quirofano/
  automatizacion-inscripciones/
```

Ventajas:

- Cada proyecto tiene su propio contexto.
- Git guarda el historial de cada proyecto por separado.
- La IA puede analizar una carpeta sin confundirse con otras.
- Es más fácil compartir solo lo necesario.
- Se reduce el riesgo de mezclar datos o credenciales.

Regla práctica:

> Si el objetivo, las dependencias o los datos son distintos, probablemente merece un repositorio separado.

---

##### 2. Dependencias aisladas en JavaScript/TypeScript

En proyectos web con Node.js, las dependencias se declaran en `package.json` y se instalan dentro de `node_modules`.

```text
mi-app-web/
  package.json
  package-lock.json
  node_modules/
  src/
```

Esto significa que las librerías de esa app viven dentro de esa carpeta. Otro proyecto puede tener otro `package.json` y otras versiones.

Comandos habituales:

```bash
npm install
npm run build
```

Mensaje importante para clase:

- No se copian manualmente carpetas `node_modules`.
- No se mezclan varios proyectos en una misma carpeta.
- El archivo importante para reproducir el entorno es `package.json` junto con el lockfile.

---

##### 3. Entornos virtuales en Python

En Python, el equivalente habitual es crear un entorno virtual.

Un entorno virtual es una carpeta que contiene una instalación aislada de Python y sus librerías para ese proyecto.

Estructura típica:

```text
analisis-datos/
  .venv/
  requirements.txt
  notebooks/
  src/
```

Comandos conceptuales:

```bash
python -m venv .venv
```

Crear el entorno.

```bash
.venv\Scripts\activate
```

Activarlo en Windows.

```bash
pip install pandas matplotlib
pip freeze > requirements.txt
```

Instalar librerías y guardar la lista.

La idea no es memorizar comandos, sino entender el principio: **las librerías de un proyecto no deben contaminar todos los demás proyectos**.

---

##### 4. Variables de entorno y secretos

Algunos proyectos necesitan claves, tokens o configuraciones privadas.

Ejemplos:

- Clave de una API.
- Contraseña de una base de datos.
- URL de un servicio.
- Token de GitHub.

Esos datos no deberían escribirse directamente en el código ni subirse a GitHub.

Se suelen guardar en archivos como `.env`, que deben quedar fuera del repositorio público mediante `.gitignore`.

Ejemplo:

```text
OPENAI_API_KEY=...
DATABASE_URL=...
```

Para docencia, lo más seguro es evitar claves reales y trabajar con ejemplos simulados.

---

##### 5. Contenedores: aislamiento avanzado

Cuando un proyecto necesita un entorno muy concreto, se pueden usar contenedores, como Docker.

Un contenedor empaqueta:

- Sistema base.
- Lenguaje.
- Librerías.
- Configuración.
- Comandos de ejecución.

Ventaja:

> "Si funciona dentro del contenedor, debería funcionar igual en otro ordenador."

Para una clase inicial no hace falta empezar por Docker. Es suficiente con entender que existe para proyectos más complejos o cuando varias personas necesitan reproducir exactamente el mismo entorno.

###### Nota práctica: Docker Desktop, WSL 2 y virtualización en Windows

En Windows, instalar o ejecutar Docker Desktop puede requerir pasos previos relacionados con virtualización. No es un tema para la primera práctica, pero conviene saberlo porque es una fuente frecuente de errores.

Docker Desktop en Windows suele usar **WSL 2** como backend para contenedores Linux. Según la documentación de Docker, para usar Docker Desktop con WSL 2 hacen falta, entre otros requisitos:

- WSL 2 activado en Windows.
- Un procesador de 64 bits con soporte de virtualización adecuado.
- Memoria suficiente.
- **Virtualización de hardware activada en BIOS/UEFI**.

Microsoft también indica que WSL 2 requiere la característica opcional **Virtual Machine Platform** y capacidades de virtualización. Si aparece un error del tipo "enable Virtual Machine Platform" o "ensure virtualization is enabled in the BIOS", normalmente hay que revisar dos capas distintas:

1. **Firmware del equipo: BIOS/UEFI**
   - Activar virtualización de CPU.
   - En Intel puede aparecer como Intel VT-x, Intel Virtualization Technology o VMX.
   - En AMD puede aparecer como AMD-V o SVM Mode.
   - El nombre exacto depende del fabricante del ordenador.

2. **Características de Windows**
   - Activar WSL.
   - Activar Virtual Machine Platform.
   - En algunos escenarios, activar Hyper-V o Windows Hypervisor Platform, sobre todo si se usa backend Hyper-V o determinadas ediciones/configuraciones de Windows.

Comandos habituales en Windows para instalar o actualizar WSL:

```powershell
wsl --install
wsl --update
```

Para comprobar la versión:

```powershell
wsl --version
```

Idea docente:

> Docker no es simplemente "instalar un programa". En Windows puede depender de que el ordenador tenga virtualización activada en BIOS/UEFI y de que Windows tenga habilitadas las características correctas.

En macOS y Linux también existen requisitos propios, pero la fricción más habitual para alumnos con Windows suele estar en WSL 2, Virtual Machine Platform, Hyper-V y virtualización de hardware.

Referencias:

- [Docker Desktop para Windows: requisitos](https://docs.docker.com/desktop/setup/install/windows-install/)
- [Docker Desktop con WSL 2](https://docs.docker.com/desktop/features/wsl/)
- [Instalar WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- [Instalación manual de WSL y Virtual Machine Platform](https://learn.microsoft.com/en-us/windows/wsl/install-manual)
- [Habilitar virtualización en Windows](https://support.microsoft.com/es-es/windows/habilitar-la-virtualizaci%C3%B3n-en-windows-c5578302-6e43-4b4b-a449-8ced115f58e1)

---

##### 6. Cómo pedir a la IA que trabaje de forma aislada

Prompt útil:

> "Quiero crear un proyecto nuevo y aislado para un prototipo docente. Crea una estructura de repositorio separada, define sus dependencias, añade instrucciones en README y no mezcles este proyecto con otros. Usa datos ficticios y no incluyas claves reales."

Otro prompt:

> "Antes de instalar librerías, dime si pertenecen a este proyecto, dónde se declararán, cómo se reproducirá el entorno en otro ordenador y qué archivos no deben subirse a GitHub."

Este tipo de instrucciones enseña a la IA a trabajar con orden, no solo a generar código.

---

##### 7. Actividad de clase

Plantear tres ideas:

1. Presentación del curso.
2. Calculadora docente con datos ficticios.
3. Análisis de un CSV simulado.

Preguntar al grupo:

- ¿Deben vivir en el mismo repositorio o en repositorios separados?
- ¿Qué dependencias tendría cada uno?
- ¿Qué archivos deberían ignorarse?
- ¿Qué datos no deberían entrar nunca?
- ¿Qué tendría que explicar el README?

Objetivo:

Que el alumno entienda que aislar proyectos no es una manía técnica, sino una forma de reducir errores, mejorar reproducibilidad y proteger información.

---

#### D. Terminal sin miedo

La terminal es una forma de hablar con el ordenador escribiendo instrucciones.

No hay que memorizar cientos de comandos. En este curso basta con reconocer algunos:

```bash
cd nombre-de-carpeta
```

Entrar en una carpeta.

```bash
npm install
```

Instalar las dependencias de un proyecto web.

```bash
npm run build
```

Construir el proyecto para comprobar que no hay errores graves.

```bash
git status
```

Ver qué archivos han cambiado.

```bash
git add .
git commit -m "Describe el cambio"
```

Guardar una versión del trabajo.

Para un médico, la terminal puede compararse con pedir una prueba complementaria concreta: hay que saber qué se solicita y qué resultado se espera, no entender toda la maquinaria interna del laboratorio.

---

#### E. Flujo básico de trabajo con IA

El flujo recomendable para principiantes es:

1. Abrir la carpeta del proyecto en el IDE.
2. Pedir a la IA que analice la estructura.
3. Explicar el objetivo con contexto clínico.
4. Pedir un plan antes de modificar.
5. Aplicar cambios pequeños.
6. Probar que funciona.
7. Pedir a la IA que resuma qué cambió y qué riesgos quedan.

Prompt útil:

> "Analiza este repositorio como si fueras mi profesor de programación. Soy médico y estoy empezando. Explícame qué archivos son importantes, cómo se ejecuta el proyecto y qué debo tocar si quiero cambiar el contenido de la clase. No modifiques nada todavía."

Cuando el alumno ya entienda el proyecto:

> "Ahora modifica solo el archivo `teoria.md`. Quiero ampliar el apartado de APIs con ejemplos sanitarios, sin datos reales de pacientes, y manteniendo un lenguaje para médicos sin experiencia técnica."

---

#### F. Errores frecuentes al empezar

Los errores más habituales no son "fallos de inteligencia", sino problemas normales de entorno:

- Instalar Node.js pero no reiniciar la terminal.
- Abrir un archivo suelto en vez de abrir la carpeta completa del proyecto.
- Ejecutar un comando desde una carpeta incorrecta.
- No instalar dependencias antes de ejecutar.
- Instalar librerías globalmente cuando deberían estar dentro del proyecto.
- Mezclar varios prototipos en la misma carpeta.
- Subir archivos `.env`, credenciales o datos sensibles a un repositorio.
- Mezclar datos reales en pruebas.
- Pedir a la IA cambios demasiado amplios.
- No revisar el resultado antes de usarlo.

Mensaje docente importante: **romper un prototipo forma parte del aprendizaje**. Por eso usamos Git, proyectos de prueba y datos ficticios.

---

#### G. Actividad de clase

Actividad breve para que los alumnos entiendan el entorno:

1. Abrir el repositorio del curso.
2. Localizar `README.md`, `slides.md`, `teoria.md` y `package.json`.
3. Preguntar a la IA: "Explícame para qué sirve cada archivo".
4. Ejecutar el proyecto o revisar cómo se ejecutaría.
5. Cambiar una frase pequeña en una slide.
6. Comprobar que el cambio aparece.

Objetivo real de la actividad: que pierdan el miedo a abrir un proyecto y entiendan que la IA puede leerlo con ellos.

### 1.4 Glosario técnico de supervivencia

Este glosario no pretende convertir al alumno en desarrollador. Su objetivo es que pueda entender conversaciones técnicas, pedir mejor a la IA y detectar cuándo una propuesta es demasiado compleja.

#### A. Conceptos de interfaz y aplicación

- **Frontend**: la parte que ve y usa el usuario. Botones, formularios, tablas, menús, pantallas.
- **Backend**: la parte que no se ve. Lógica, validaciones, permisos, conexión con bases de datos.
- **UI** (*User Interface*): la interfaz visual.
- **UX** (*User Experience*): la experiencia de uso. Que sea claro, rápido, seguro y no confuso.
- **Formulario**: zona donde el usuario introduce datos.
- **Dashboard**: pantalla resumen con indicadores, tablas o gráficos.
- **Prototipo**: primera versión para aprender, enseñar o validar una idea.
- **MVP** (*Minimum Viable Product*): versión mínima útil para probar si la idea tiene sentido.

Ejemplo clínico:

Una calculadora preoperatoria tendría como frontend el formulario donde se introducen variables, y como backend la lógica que calcula la categoría de riesgo.

---

#### B. Conceptos de datos

- **Dato**: unidad de información. Edad, fecha, diagnóstico, valor analítico.
- **Variable**: dato que puede cambiar entre pacientes o episodios.
- **Base de datos**: sistema organizado para guardar y consultar información.
- **Tabla**: estructura similar a una hoja de cálculo, con filas y columnas.
- **Registro**: una fila de una tabla.
- **Campo**: una columna de una tabla.
- **CSV**: archivo de texto con datos separados por comas. Muy usado para exportar desde Excel.
- **JSON**: formato muy habitual para intercambiar datos entre aplicaciones.
- **Dato identificable**: dato que permite reconocer a una persona directa o indirectamente.
- **Anonimización**: proceso para evitar que una persona pueda ser identificada.
- **Pseudonimización**: sustitución de identificadores directos por códigos, manteniendo alguna posibilidad de reidentificación bajo control.

Ejemplo:

```json
{
  "edad": 72,
  "asa": 3,
  "hemoglobina": 10.8,
  "cirugia": "protesis de rodilla"
}
```

Este JSON representa datos clínicos ficticios estructurados. Una aplicación puede leerlo mejor que un párrafo libre.

---

#### C. Conceptos de conexión

- **API**: mecanismo para que dos sistemas se comuniquen.
- **Endpoint**: dirección concreta de una API.
- **Request**: petición que enviamos.
- **Response**: respuesta que recibimos.
- **Autenticación**: demostrar quién eres.
- **Autorización**: definir qué puedes hacer.
- **Token**: credencial digital que permite acceder a un servicio.
- **Integración**: conexión entre herramientas distintas.

Ejemplo:

Una app podría enviar una petición a una API para obtener la lista de citas de un día. La API respondería con datos estructurados. En un entorno real esto exige permisos, trazabilidad y protección de datos.

---

#### D. Conceptos de código

- **Lenguaje de programación**: idioma formal para dar instrucciones al ordenador.
- **Script**: programa pequeño que automatiza una tarea.
- **Función**: bloque de código que hace una tarea concreta.
- **Librería o paquete**: código ya creado que podemos reutilizar.
- **Dependencia**: librería que nuestro proyecto necesita para funcionar.
- **Bug**: error de funcionamiento.
- **Debugging**: proceso de buscar y corregir errores.
- **Test**: prueba que comprueba si algo funciona como esperamos.
- **Refactorizar**: mejorar la estructura del código sin cambiar lo que hace.
- **Build**: proceso de preparar el proyecto para ejecutarlo o publicarlo.
- **Deploy**: publicar una aplicación para que otros puedan usarla.

Ejemplo:

Si una calculadora de dosis devuelve mal el resultado para pesos extremos, eso es un bug. Un test debería detectar ese caso antes de usar la herramienta.

---

#### E. Conceptos de arquitectura

- **Arquitectura**: forma en que se organizan las piezas de un sistema.
- **Cliente**: parte que pide información. Normalmente el navegador.
- **Servidor**: parte que recibe peticiones, procesa y responde.
- **Local**: en tu propio ordenador.
- **Nube**: en servidores externos.
- **Repositorio**: carpeta de proyecto con historial Git.
- **Rama**: línea de trabajo separada dentro de Git.
- **Commit**: punto guardado en el historial.
- **Pull request**: propuesta de cambios para revisar antes de integrar.

Nota breve sobre IA y pull requests:

Las PR también pueden ser revisadas por IA como apoyo al equipo. Por ejemplo, Codex puede revisar una PR desde GitHub si se configura la integración y se comenta `@codex review`; también puede activarse revisión automática para nuevas PRs. Claude Code GitHub Actions permite flujos similares con menciones `@claude` o workflows que revisan una PR y publican comentarios.

Esto es útil para detectar errores, regresiones, problemas de seguridad o cambios mal enfocados antes de mezclar el código. Pero debe explicarse como **un segundo par de ojos**, no como sustituto de una revisión humana. En proyectos sanitarios, una revisión de IA nunca reemplaza la validación clínica, legal ni de seguridad.

Referencias:

- [Codex en GitHub](https://developers.openai.com/codex/integrations/github)
- [Codex GitHub Action](https://developers.openai.com/codex/github-action)
- [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions)

Idea clave:

No necesitamos empezar por una arquitectura compleja. En proyectos docentes o prototipos clínicos, muchas veces basta con:

- Una hoja de cálculo bien diseñada.
- Un notebook.
- Una app local sencilla.
- Una aplicación web sin base de datos real.

La complejidad debe aparecer cuando el problema la justifica, no antes.

---

#### F. Markdown: escritura estructurada para humanos y agentes

Markdown es una forma sencilla de escribir texto estructurado. No es un lenguaje de programación. Es una manera de escribir documentos usando símbolos muy simples para indicar títulos, listas, tablas, enlaces o fragmentos literales.

Ejemplos de archivos Markdown en este repositorio:

- `README.md`: presentación del curso y guía técnica del repositorio.
- `slides.md`: diapositivas de Slidev.
- `teoria.md`: documento teórico maestro.
- `index.md`: temario resumido.
- `guia-markdown-medicos.md`: guía rápida y chuleta para alumnos.

Para médicos no técnicos, Markdown es especialmente útil porque se parece a escribir un informe ordenado: tiene títulos, apartados, listas, tablas y notas. La diferencia es que, al ser texto plano, también es fácil de leer por herramientas de IA, sistemas de control de versiones y plataformas como GitHub.

##### Por qué Markdown ayuda a los agentes de IA

Los agentes funcionan mejor cuando reciben contexto claro. Un documento Markdown bien escrito separa:

- Objetivo.
- Contexto.
- Datos de entrada.
- Restricciones.
- Riesgos.
- Criterios de aceptación.
- Pasos de verificación.

Esto reduce ambigüedad. No es lo mismo pedir:

> "Hazme una app para pacientes."

que entregar a la IA un archivo con esta estructura:

```markdown
# Prototipo educativo de consulta preoperatoria

## Objetivo

Registrar pacientes ficticios y mostrar una tabla resumen.

## Restricciones

- No usar datos reales.
- No guardar información identificable.
- Mantener una arquitectura simple.

## Criterios de aceptación

- El formulario se entiende por médicos no técnicos.
- La tabla muestra solo datos ficticios.
- El prototipo puede explicarse en clase.
```

##### Chuleta mínima

| Necesidad | Markdown |
|-----------|----------|
| Título principal | `# Título` |
| Sección | `## Sección` |
| Lista | `- Elemento` |
| Pasos | `1. Paso` |
| Negrita | `**importante**` |
| Texto literal | `` `edad` `` |
| Enlace | `[texto](https://...)` |
| Tarea pendiente | `- [ ] Revisar` |
| Cita | `> Texto destacado` |

##### Ejemplo sanitario seguro

```markdown
# Dataset ficticio para clase

## Variables

- Edad.
- ASA.
- Tipo de cirugía.
- Hemoglobina preoperatoria.

## Reglas

- No incluir nombres.
- No incluir números de historia.
- No copiar datos reales.
```

Mensaje clave:

> Markdown es una historia clínica del proyecto: ordena información, deja trazabilidad y ayuda a que otra persona o una IA entiendan el caso.

Para practicar, el alumno puede leer la guía específica del repositorio: `guia-markdown-medicos.md`.

---

## 2. Agentes IA y Conectividad

### 2.1 Uso de agentes avanzados

Un agente de programación es una IA que no se limita a responder en un chat. Puede trabajar sobre un proyecto, leer archivos, proponer cambios, editar código, ejecutar comandos y verificar resultados.

Para los alumnos, la diferencia práctica es:

- **Chat de IA**: útil para preguntar, aprender y redactar.
- **IDE con IA**: útil para modificar archivos concretos.
- **Agente de programación**: útil para tareas con varios pasos y varios archivos.

El punto importante no es el nombre de la herramienta. El punto importante es aprender a **dirigir el trabajo**.

---

#### A. Qué tareas se pueden delegar a un agente

Un agente puede ayudar a:

- Analizar la estructura de un repositorio.
- Explicar qué hace cada archivo.
- Crear una aplicación inicial.
- Añadir una pantalla nueva.
- Corregir un error.
- Escribir documentación.
- Crear tests.
- Revisar seguridad básica.
- Convertir una idea clínica en requisitos.
- Preparar material docente.

Ejemplos para este curso:

- "Analiza este repositorio de slides y dime cómo está organizado."
- "Amplía el apartado de teoría sobre APIs con ejemplos sanitarios."
- "Crea una actividad práctica de 20 minutos para médicos sin experiencia en programación."
- "Revisa si este prototipo usa datos reales o si todo son datos ficticios."

---

#### B. Cómo escribir una buena instrucción para un agente

Una buena instrucción tiene cinco partes:

1. **Contexto**
   - Quién eres.
   - Para quién es el material.
   - Qué nivel tiene el público.

2. **Objetivo**
   - Qué quieres conseguir.
   - Qué resultado esperas.

3. **Restricciones**
   - Qué no debe tocar.
   - Qué estilo debe mantener.
   - Qué riesgos debe evitar.

4. **Criterios de aceptación**
   - Cómo sabremos que está bien.
   - Qué pruebas debe pasar.

5. **Forma de entrega**
   - Resumen, archivo modificado, tabla, slides, checklist, etc.

Plantilla:

> "Soy médico y estoy preparando una clase de programación con IA para residentes. Analiza este repositorio y modifica solo `teoria.md`. Amplía el apartado `2.2 APIs y bases de datos` con lenguaje claro, ejemplos clínicos ficticios y advertencias de privacidad. No uses datos reales de pacientes. Al final, resume los cambios y dime qué queda pendiente."

---

#### C. Patrón de trabajo recomendado

Para evitar que el agente haga cambios demasiado grandes o incorrectos, se puede trabajar en fases:

1. **Explora**
   - "Lee el repositorio y dime qué has entendido."

2. **Propón**
   - "Antes de modificar, propón un plan."

3. **Edita**
   - "Aplica solo el punto 1 del plan."

4. **Verifica**
   - "Comprueba que el proyecto sigue funcionando."

5. **Resume**
   - "Resume cambios, riesgos y próximos pasos."

Este patrón es muy parecido al razonamiento clínico: historia, hipótesis, plan, intervención, reevaluación.

---

#### D. Qué revisar siempre

Aunque el agente parezca convincente, hay que revisar:

- Si ha respetado el objetivo.
- Si ha tocado archivos que no debía.
- Si ha introducido datos reales.
- Si ha inventado herramientas, normas o citas.
- Si el código se puede ejecutar.
- Si la explicación es comprensible para el público.
- Si las recomendaciones clínicas están validadas.

En proyectos sanitarios, la revisión humana no es opcional.

---

#### E. Antigravity: modalidades actuales e instalación

**Última verificación de esta sección:** 21 de mayo de 2026.

Google Antigravity es una familia de herramientas de programación asistida por agentes. Según la información pública revisada en la web oficial de Antigravity, el 19 de mayo de 2026 se publicaron novedades relevantes: Antigravity 2.0, Antigravity CLI, Antigravity SDK, integración en Gemini Enterprise y modelos actualizados como Gemini 3.5 Flash en Antigravity. En los endpoints oficiales de releases consultados el 21 de mayo de 2026 aparecían como versiones recientes Antigravity 2.0 `2.0.1` y Antigravity IDE `2.0.2`.

Estas herramientas cambian rápido, por lo que en clase conviene presentar la idea general y pedir a los alumnos que verifiquen siempre la documentación oficial antes de instalar.

##### 1. Antigravity 2.0

Antigravity 2.0 es la aplicación central. Su función principal es actuar como un centro de mando para gestionar varios agentes locales, conversaciones, proyectos y espacios de trabajo.

Para un médico no técnico, la analogía sería:

> No es solo "un chat". Es una mesa de trabajo donde varios asistentes pueden encargarse de tareas diferentes dentro de un proyecto.

Puede servir para:

- Explorar un repositorio docente.
- Dividir una tarea grande en pasos.
- Gestionar varios hilos de trabajo.
- Automatizar tareas repetitivas mediante mensajes programados.
- Revisar artefactos generados por los agentes.

Instalación:

1. Entrar en `https://antigravity.google/download`.
2. Descargar Antigravity 2.0 para el sistema operativo correspondiente.
3. Elegir arquitectura si procede:
   - macOS: Apple Silicon o Intel, archivo `.dmg`.
   - Windows: x64 o ARM64, archivo `.exe`.
   - Linux: x64 o ARM64, archivo `.tar.gz`.
4. Instalar, abrir la aplicación e iniciar sesión.

Requisitos destacados publicados en la página de descarga:

- macOS 12 Monterey o superior.
- Windows 10 de 64 bits.
- Linux con `glibc >= 2.28` y `glibcxx >= 3.4.25`.

##### 2. Antigravity CLI

Antigravity CLI es la modalidad de terminal. Permite trabajar con agentes desde una carpeta de proyecto usando comandos.

Conviene presentarla solo cuando el alumno ya entiende:

- Qué es una carpeta de proyecto.
- Qué es una terminal.
- Qué significa ejecutar comandos.
- Por qué hay que revisar cambios antes de aceptarlos.

Instalación oficial indicada en la web de Antigravity:

```bash
# macOS y Linux
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

```powershell
# Windows PowerShell
irm https://antigravity.google/cli/install.ps1 | iex
```

```cmd
:: Windows CMD
curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Nota importante: la web oficial indica que hay que autenticarse con Antigravity o Antigravity IDE antes de usar la CLI.

Uso docente recomendado:

- Pedir al agente que explore primero el repositorio.
- Limitar el alcance: "modifica solo `teoria.md`".
- Exigir verificación: "ejecuta la build y resume errores".
- Evitar datos reales de pacientes.

##### 3. Antigravity SDK

Antigravity SDK está pensado para crear agentes propios con Python sobre el entorno de Antigravity.

No es la primera herramienta para un alumno sin base técnica. Tiene más sentido para:

- Docentes que quieran preparar demos.
- Alumnos avanzados.
- Automatizaciones repetibles.
- Evaluaciones de agentes.
- Prototipos de investigación con datos ficticios.

Instalación inicial:

```bash
git clone https://github.com/google-antigravity/antigravity-sdk-python
cd antigravity-sdk-python
```

Después hay que seguir el `README` del repositorio oficial para crear el entorno Python e instalar sus dependencias. No conviene copiar instrucciones concretas de instalación sin revisarlas, porque el SDK puede cambiar rápido.

Uso docente recomendado:

- Mostrar que un agente también puede programarse.
- Crear ejemplos con archivos de prueba.
- Evaluar respuestas sobre tareas controladas.
- Evitar cualquier conexión a sistemas clínicos reales.

##### 4. Antigravity IDE

Antigravity IDE es el editor completo con agente integrado. Incluye funciones de editor, comprensión del repositorio, agente y artefactos revisables.

Es la modalidad más parecida a un "entorno de programación con IA" para el alumno, porque permite abrir una carpeta, leer archivos y pedir cambios en lenguaje natural.

Instalación:

1. Entrar en `https://antigravity.google/download`.
2. Descargar Antigravity IDE para el sistema operativo correspondiente:
   - macOS: `.dmg`.
   - Windows: `.exe`.
   - Linux: `.tar.gz`.
3. Instalar y abrir una carpeta de proyecto.
4. Antes de pedir cambios, solicitar una exploración:

> "Explora este repositorio y explícame qué archivos hay, cuál es el objetivo del proyecto y qué riesgos ves antes de modificar nada."

Esta regla es especialmente importante para médicos: antes de intervenir, primero se entiende el caso.

##### 5. Comparación rápida

| Modalidad | Nivel recomendado | Uso principal | Riesgo si se usa mal |
|-----------|------------------|---------------|----------------------|
| Antigravity 2.0 | Intermedio | Coordinar agentes y proyectos | Delegar demasiado sin revisar |
| Antigravity CLI | Intermedio-avanzado | Trabajar desde terminal | Ejecutar cambios sin entenderlos |
| Antigravity SDK | Avanzado/docente | Crear agentes propios | Automatizar comportamientos no validados |
| Antigravity IDE | Inicial-intermedio | Editar proyectos con IA | Aceptar código o cambios sin verificar |

##### 6. Regla sanitaria

En este curso, Antigravity debe usarse como herramienta docente y de prototipado, no como herramienta asistencial conectada a datos reales.

Reglas mínimas:

- No introducir datos identificables de pacientes.
- Usar datos ficticios o anonimizados.
- No conectar con sistemas hospitalarios reales sin autorización.
- Revisar cada cambio antes de aceptarlo.
- Separar prototipo educativo de producto clínico.
- Validar cualquier lógica clínica con expertos, casos de prueba y revisión técnica.

Prompt útil:

> "Trabaja solo con datos ficticios. Antes de modificar archivos, explica qué vas a leer, qué vas a cambiar, qué permisos necesitas y qué riesgos existen. No hagas cambios destructivos. Al final, resume qué has cambiado y cómo puedo verificarlo."

---

#### F. Actividad de clase

Ejercicio de 10 minutos:

1. Dar a los alumnos una mala instrucción:

> "Hazme una app para pacientes."

2. Pedirles que la transformen usando la plantilla:

- Contexto.
- Objetivo.
- Datos.
- Restricciones.
- Resultado esperado.
- Riesgos.

3. Comparar en grupo dos respuestas de la IA: una con la instrucción mala y otra con la instrucción buena.

Mensaje clave: **la calidad de la respuesta depende mucho de la calidad del encargo**.

### 2.2 Conexión con el mundo real (APIs y bases de datos)

Una aplicación aislada puede ser útil para aprender, pero muchas herramientas reales necesitan conectarse con otros sistemas: hojas de cálculo, bases de datos, calendarios, formularios, servicios de correo, historias clínicas, laboratorios o sistemas administrativos.

Esa conexión suele hacerse mediante APIs y bases de datos.

---

#### A. Qué es una API

Una **API** es una forma estandarizada de pedir o enviar información entre sistemas.

Analogía sanitaria:

- Un médico solicita una analítica.
- El laboratorio recibe una petición con datos concretos.
- El laboratorio devuelve resultados estructurados.
- Cada parte tiene un formato esperado y unas reglas.

Una API funciona de forma parecida:

- Una aplicación hace una petición.
- El servicio procesa la petición.
- El servicio devuelve una respuesta.

Ejemplo conceptual:

```text
Aplicación -> "Dame las citas de hoy"
API        -> "Aquí tienes la lista en formato estructurado"
```

En programación, esa respuesta suele venir en JSON.

---

#### B. Qué es una base de datos

Una **base de datos** es un sistema diseñado para guardar, buscar, ordenar y proteger información.

Una hoja de cálculo puede servir para empezar, pero una base de datos es más adecuada cuando:

- Hay muchos registros.
- Varias personas usan la herramienta.
- Se necesitan permisos.
- Hay que evitar duplicados.
- Hay que registrar cambios.
- La información se consulta desde una aplicación.

Ejemplo de tabla ficticia:

| id | edad | asa | tipo_cirugia | hb_preoperatoria |
|---:|-----:|----:|---------------|-----------------:|
| 1 | 68 | 3 | rodilla | 11.2 |
| 2 | 74 | 2 | cadera | 12.9 |
| 3 | 59 | 3 | columna | 10.5 |

Esta tabla no identifica pacientes y sirve para practicar. En un entorno real, cualquier estructura con información clínica debe diseñarse con criterios de privacidad, seguridad y trazabilidad.

---

#### C. Cuándo NO hace falta una base de datos

Un error frecuente es pedir una base de datos demasiado pronto.

No siempre hace falta. Para una primera versión puede bastar con:

- Un formulario que no guarda datos.
- Un archivo CSV ficticio.
- Un JSON de ejemplo.
- Una hoja de cálculo.
- Datos generados automáticamente para la demo.

Pregunta útil:

> "¿Necesitamos guardar información real o solo demostrar el flujo?"

Si solo queremos enseñar o validar una idea, lo más seguro suele ser no guardar datos reales.

---

#### D. Riesgos sanitarios al conectar sistemas

Conectar sistemas aumenta la potencia, pero también el riesgo:

- Exposición de datos identificables.
- Accesos no autorizados.
- Pérdida de trazabilidad.
- Errores al transformar datos.
- Uso de información desactualizada.
- Dependencia de servicios externos.
- Automatización de decisiones no validadas.

Regla práctica:

Cuanto más cerca esté una aplicación de datos reales o decisiones clínicas, más revisión necesita.

---

#### E. Prompt para diseñar una integración segura

> "Quiero diseñar un prototipo educativo que simule la conexión entre un formulario y una base de datos. No debe usar datos reales. Propón una arquitectura mínima, define qué datos ficticios usar, explica qué riesgos aparecerían si esto se conectara a sistemas reales y qué validaciones serían necesarias antes de usarlo en un hospital."

Este tipo de prompt obliga a la IA a separar prototipo, privacidad, arquitectura y validación.

---

#### F. Actividad de clase

Caso:

> "Queremos registrar pacientes ficticios valorados en una consulta preoperatoria y generar un resumen de riesgo."

Preguntas para el grupo:

- ¿Qué datos son imprescindibles?
- ¿Qué datos no deberíamos pedir?
- ¿Hace falta guardar información?
- ¿Basta con una hoja de cálculo?
- ¿Qué sería frontend?
- ¿Qué sería backend?
- ¿Dónde estarían los riesgos?

Resultado esperado:

Una tabla de requisitos antes de escribir código.

### 2.3 Ampliación de funciones: Skills y MCP

Los modelos de IA por sí solos generan texto. Para trabajar mejor necesitan contexto y herramientas.

Dos conceptos útiles son:

- **Skills**: instrucciones especializadas que enseñan a la IA cómo realizar una tarea concreta.
- **MCP** (*Model Context Protocol*): forma de conectar la IA con herramientas externas, archivos, bases de datos o servicios.

No es necesario que los alumnos memoricen la parte técnica. Basta con entender la idea:

> Un chat básico solo responde. Un agente con herramientas puede mirar archivos, ejecutar comandos, leer documentos, consultar una base de datos autorizada o modificar un proyecto.

---

#### A. Qué es una skill

Una skill es como un protocolo de actuación para la IA.

Ejemplos:

- Skill para crear presentaciones.
- Skill para revisar documentos.
- Skill para analizar PDFs.
- Skill para desplegar una web.
- Skill para revisar seguridad básica.
- Skill para trabajar con bases de datos.

Analogía clínica:

Un residente puede saber medicina general, pero actúa mejor si tiene un protocolo claro para sepsis, vía aérea difícil o transfusión masiva. La skill cumple una función parecida: orienta el trabajo de la IA en una tarea específica.

---

#### B. Qué es MCP

MCP permite que un modelo se conecte a herramientas externas de forma estructurada.

Ejemplos conceptuales:

- Leer archivos de un repositorio.
- Consultar una base de datos local.
- Buscar issues en GitHub.
- Abrir un navegador de prueba.
- Leer documentos.
- Usar una herramienta de despliegue.

Mensaje importante:

Más conexión no siempre significa más seguridad. Cada conexión amplía lo que la IA puede ver o hacer, por lo que hay que limitar permisos y revisar acciones.

---

#### C. Qué debe saber un médico sobre herramientas conectadas

Antes de dar acceso a una IA, hay que preguntarse:

- ¿Qué datos podrá leer?
- ¿Puede modificar archivos?
- ¿Puede ejecutar comandos?
- ¿Puede conectarse a internet?
- ¿Puede acceder a información sensible?
- ¿Queda registro de lo que hace?
- ¿Quién valida el resultado?

En un entorno sanitario real, no se debe conectar una IA a sistemas con datos de pacientes sin aprobación, garantías técnicas y marco legal claro.

---

#### D. Uso docente seguro

Para la clase, lo recomendable es trabajar con:

- Repositorios de ejemplo.
- Datos ficticios.
- Documentos de prueba.
- APIs públicas sin información sensible.
- Bases de datos locales simuladas.
- Proyectos que no afecten a sistemas reales.

Así los alumnos aprenden el concepto sin asumir riesgos innecesarios.

---

#### E. Prompt para usar herramientas con prudencia

> "Antes de usar cualquier herramienta conectada, dime qué permisos necesitas, qué archivos vas a leer o modificar, qué riesgos existen y cómo puedo revisar el resultado. No ejecutes cambios destructivos y no uses datos reales de pacientes."

Esta frase enseña un principio fundamental: no solo importa lo que la IA sabe, sino lo que puede hacer.

---

## 3. Proyectos Prácticos

### 3.1 Creación paso a paso

La parte práctica del curso debe enseñar una metodología, no solo una herramienta concreta.

El objetivo es que el alumno aprenda a pasar de una idea clínica imprecisa a un prototipo funcional, aunque sea sencillo.

---

#### A. Del problema clínico al producto digital

Toda idea debería formularse primero en lenguaje clínico:

- ¿Qué problema tengo?
- ¿A quién afecta?
- ¿Cuándo ocurre?
- ¿Qué se hace ahora?
- ¿Qué parte es repetitiva?
- ¿Qué error aparece con frecuencia?
- ¿Qué salida sería útil?

Después se traduce a lenguaje de producto:

- Usuario.
- Datos de entrada.
- Proceso.
- Datos de salida.
- Pantallas.
- Validaciones.
- Riesgos.
- Criterios de éxito.

Ejemplo:

> "En consulta preoperatoria revisamos anemia antes de cirugía programada. Queremos un prototipo educativo que, con datos ficticios, ayude a clasificar casos y generar una recomendación de siguiente paso basada en un protocolo previamente definido."

Esto ya es mucho mejor que "hazme una app de anemia".

---

#### B. Plantilla de especificación inicial

Antes de programar, completar esta tabla:

| Pregunta | Respuesta |
|----------|-----------|
| Usuario principal | Médico, residente, enfermería, administrativo |
| Contexto de uso | Consulta, planta, quirófano, investigación, docencia |
| Problema | Qué tarea queremos mejorar |
| Datos de entrada | Qué introduce el usuario |
| Datos de salida | Qué devuelve la herramienta |
| Datos reales | Sí/no. Para clase: no |
| Regla clínica | Fuente o protocolo validado |
| Riesgo si falla | Bajo, medio, alto |
| Primera versión | Lo mínimo que debe funcionar |
| Qué no hará | Límites explícitos |

Esta tabla es una de las habilidades más importantes del curso.

---

#### C. Elegir la tecnología más simple

La IA puede proponer tecnologías complejas. El docente debe enseñar a elegir la opción más sencilla que resuelva el problema.

Guía orientativa:

| Necesidad | Tecnología razonable |
|----------|----------------------|
| Explicar un cálculo sencillo | Hoja de cálculo |
| Analizar un CSV | Python o Google Colab |
| Crear una demo con formulario | Streamlit o app web simple |
| Crear una presentación interactiva | Slidev |
| Automatizar correos o formularios | Make o n8n |
| Aplicación multiusuario con permisos | Web app con backend y base de datos |

Principio:

> La mejor tecnología para empezar es la que permite aprender rápido, fallar barato y no comprometer datos reales.

---

#### D. Construcción por iteraciones

No se debe pedir a la IA "haz todo el proyecto completo" de una vez.

Mejor:

1. Crear estructura mínima.
2. Añadir formulario.
3. Añadir datos ficticios.
4. Añadir lógica.
5. Añadir validaciones.
6. Añadir explicación para el usuario.
7. Revisar casos límite.
8. Mejorar diseño.
9. Documentar limitaciones.

Cada paso debe poder probarse.

---

#### E. Criterios de aceptación

Un criterio de aceptación define cuándo una tarea está terminada.

Ejemplos:

- "La aplicación no almacena datos."
- "Todos los ejemplos son ficticios."
- "Si falta un campo obligatorio, muestra un aviso."
- "El resultado explica qué variables se han usado."
- "El cálculo coincide con tres casos manuales."
- "El README explica cómo ejecutar el proyecto."

Sin criterios de aceptación, la IA puede entregar algo vistoso pero incompleto.

---

#### F. Proyecto recomendado para la clase

Proyecto base:

> **Calculadora educativa de riesgo o priorización con datos ficticios.**

Debe incluir:

- Formulario simple.
- Variables clínicas no identificables.
- Resultado calculado.
- Explicación del resultado.
- Aviso de uso docente.
- Casos de prueba ficticios.

Por qué funciona bien:

- Es clínicamente reconocible.
- Permite hablar de frontend, backend, datos y validación.
- No exige conexión con sistemas reales.
- Permite introducir privacidad y seguridad.
- Se puede construir por pasos.

Variantes:

- Priorización de consulta preoperatoria.
- Checklist de preparación para procedimiento.
- Clasificador educativo de complejidad de ingreso.
- Generador de resumen clínico ficticio.
- Dashboard de actividad simulada.

### 3.2 Hackathon de ideas

El hackathon no debe medirse por quién crea la app más impresionante, sino por quién formula mejor un problema real y propone una solución segura, simple y evaluable.

---

#### A. Objetivo del hackathon

Que cada grupo sea capaz de:

- Identificar un problema clínico o administrativo concreto.
- Convertirlo en una especificación breve.
- Crear un prototipo o maqueta.
- Explicar riesgos y límites.
- Presentarlo en 3-5 minutos.

---

#### B. Reglas del ejercicio

1. No usar datos reales de pacientes.
2. No crear herramientas de decisión clínica sin fuente validada.
3. Priorizar problemas pequeños y frecuentes.
4. Definir qué hace y qué no hace el prototipo.
5. Preparar una demo reproducible.
6. Documentar el siguiente paso necesario antes de usarlo en la realidad.

---

#### C. Ejemplos de retos

- Automatizar un informe docente con datos ficticios.
- Crear una checklist interactiva para una técnica.
- Convertir un protocolo en un árbol de decisión educativo.
- Analizar una hoja de actividad simulada.
- Generar una presentación clínica desde un esquema.
- Crear un formulario para recoger incidencias no sensibles.
- Diseñar un panel de seguimiento con datos inventados.

---

#### D. Plantilla de presentación final

Cada grupo presenta:

1. Problema.
2. Usuario.
3. Situación actual.
4. Solución propuesta.
5. Demo o maqueta.
6. Datos usados.
7. Riesgos.
8. Qué haría falta para llevarlo a entorno real.

---

#### E. Rúbrica sencilla

| Criterio | Pregunta |
|----------|----------|
| Claridad | ¿Se entiende el problema? |
| Utilidad | ¿Resuelve una tarea real? |
| Simplicidad | ¿Evita complejidad innecesaria? |
| Seguridad | ¿Evita datos reales y decisiones no validadas? |
| Prototipo | ¿Hay algo visible o demostrable? |
| Validación | ¿Explica cómo se comprobaría? |

Esta rúbrica permite valorar pensamiento digital, no solo habilidad técnica.

---

## 4. Otros usos y Automatización

### 4.1 Google AI Studio y Generación de Contenido

La IA no solo sirve para programar. También puede acelerar tareas docentes, administrativas y de comunicación.

En una clase para médicos, esto es importante porque muchos alumnos empezarán usando IA para tareas de contenido antes que para escribir código.

---

#### A. Usos prácticos

- Crear esquemas de sesiones clínicas.
- Convertir notas en diapositivas.
- Resumir documentos largos.
- Generar preguntas tipo test.
- Crear casos clínicos ficticios.
- Reformular textos para pacientes o profesionales.
- Crear imágenes docentes no clínicas.
- Preparar guiones de talleres.
- Crear tablas comparativas.

---

#### B. Riesgos

- Alucinaciones.
- Citas inventadas.
- Exceso de confianza.
- Pérdida de matices clínicos.
- Uso accidental de datos sensibles.
- Material visual que parece real pero no lo es.

Regla práctica:

> La IA puede acelerar la primera versión, pero no debe ser la fuente final de verdad clínica.

---

#### C. Prompt para generar material docente

> "Actúa como docente clínico. Crea una explicación de 10 minutos sobre APIs para médicos sin experiencia técnica. Usa analogías sanitarias, evita jerga innecesaria, incluye un ejemplo con datos ficticios y termina con tres preguntas para comprobar comprensión. No inventes referencias bibliográficas."

---

#### D. Prompt para transformar teoría en slides

> "Convierte este apartado teórico en 5 diapositivas. Cada diapositiva debe tener un título claro, máximo 4 bullets y una nota para el presentador. El público son médicos sin experiencia en programación. Mantén el tono práctico y evita tecnicismos innecesarios."

Este prompt puede ayudar a convertir `teoria.md` en `slides.md` de forma controlada.

### 4.2 Automatización sin código (MAKE, n8n)

Las herramientas no-code y low-code permiten crear flujos automáticos conectando aplicaciones mediante bloques visuales.

Ejemplos:

- Cuando llega un formulario, añadir una fila a una hoja.
- Cuando se actualiza una tabla, enviar un correo.
- Cada lunes, generar un resumen de actividad.
- Convertir respuestas de un formulario en un documento.
- Mover archivos entre carpetas.

---

#### A. Cuándo tienen sentido

Son útiles cuando:

- La tarea es repetitiva.
- Las reglas son claras.
- Los datos no son sensibles o están bien controlados.
- No hace falta una aplicación completa.
- El objetivo es automatizar un flujo administrativo.

No son ideales cuando:

- Hay decisiones clínicas complejas.
- Se manejan datos identificables sin garantías.
- Se necesita trazabilidad estricta.
- La lógica cambia mucho.
- Hay muchos usuarios y permisos.

---

#### B. Anatomía de una automatización

Una automatización suele tener:

- **Disparador**: qué inicia el flujo.
- **Acciones**: qué pasos se ejecutan.
- **Condiciones**: qué pasa según cada caso.
- **Datos**: qué información viaja entre pasos.
- **Registro**: cómo sabemos qué ocurrió.

Ejemplo:

```text
Nuevo formulario ficticio
-> Validar campos
-> Añadir fila a tabla
-> Generar resumen
-> Enviar correo docente
```

---

#### C. Riesgos en contexto sanitario

Antes de automatizar, preguntar:

- ¿Qué ocurre si se envía a la persona equivocada?
- ¿Qué ocurre si el flujo se ejecuta dos veces?
- ¿Qué ocurre si falta un dato?
- ¿Qué ocurre si una regla cambia?
- ¿Hay información identificable?
- ¿Quién supervisa los errores?

La automatización reduce trabajo manual, pero también puede escalar errores.

---

#### D. Actividad de clase

Diseñar en papel una automatización:

> "Formulario de inscripción a un taller clínico con datos ficticios."

Flujo:

1. Alumno rellena formulario.
2. Se añade una fila a una hoja.
3. Se envía confirmación.
4. Se genera lista de asistentes.
5. Se avisa si se supera el aforo.

Después, pedir a la IA:

> "Convierte este flujo en una automatización no-code. Indica disparador, pasos, datos necesarios, errores posibles y cómo probarlo sin datos reales."

---

## Cierre de la teoría

El objetivo de este curso no es que todos los médicos terminen programando a nivel profesional.

El objetivo es que puedan:

- Entender qué es posible.
- Formular mejor problemas clínicos.
- Usar IA para prototipar.
- Dialogar con perfiles técnicos.
- Detectar riesgos.
- Diferenciar una demo educativa de una herramienta asistencial.
- Avanzar con seguridad desde una idea hacia una solución.

La competencia clave no es memorizar comandos. Es aprender a dirigir sistemas de IA con criterio clínico, pensamiento estructurado y límites claros.
