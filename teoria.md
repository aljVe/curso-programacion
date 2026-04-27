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
*   **Antigravity:** Representa el siguiente nivel: un asistente agente capaz de razonar, planificar y ejecutar tareas complejas de forma autónoma sobre tu código, ahorrando horas de trabajo manual.

#### C. Entornos Interactivos y Notebooks (Ciencia de Datos)
Existen otros entornos muy populares, especialmente en el mundo científico y de investigación, que funcionan de forma distinta a los IDEs tradicionales. Se basan en el concepto de "Notebook" o cuaderno interactivo.

*   **Jupyter Notebook:** Es como un cuaderno digital donde puedes mezclar bloques de código, texto explicativo, gráficas y resultados en un mismo documento. Es ideal para experimentar y analizar datos paso a paso.
*   **Anaconda:** No es un editor en sí, sino una "caja de herramientas" que instala automáticamente Python y las librerías más importantes para ciencia de datos, incluyendo Jupyter.
*   **Google Colab:** Es una versión de Jupyter que funciona totalmente en la nube. No requiere instalar nada en tu ordenador y utiliza la potencia de los servidores de Google. Es la forma más rápida de empezar a programar con IA y datos sin configurar nada.

> **Idea clave:** No necesitas memorizar el lenguaje. Tu trabajo ahora es saber **qué** quieres hacer y dejar que el **IDE** y la **IA** te ayuden con el **cómo** se escribe.

### 1.3 Configuración del entorno local
*Guía paso a paso: Instalación de Git, configuración de GitHub y uso de herramientas de asistencia.*

### 1.4 Glosario técnico de supervivencia
*   **Frontend**: Lo que el usuario ve (la interfaz).
*   **Backend**: La lógica y los datos detrás de la interfaz.
*   **API**: El puente de comunicación entre sistemas.
*   **Arquitectura**: Cómo se estructuran todas las piezas de un proyecto.

---

## 2. Agentes IA y Conectividad

### 2.1 Uso de agentes avanzados
*Cómo interactuar con agentes como Antigravity, Codex y Claude Code para delegar tareas complejas.*

### 2.2 Conexión con el mundo real (APIs y bases de datos)
*Cómo lograr que nuestras aplicaciones se conecten con otros servicios web, envíen y reciban datos externos.*

### 2.3 Ampliación de funciones: Skills y MCP
*Uso del Model Context Protocol para dotar a la IA de capacidades de interacción directa con archivos y bases de datos locales.*

---

## 3. Proyectos Prácticos

### 3.1 Creación paso a paso
*Metodología para plantear un problema desde cero y construir una aplicación web funcional asistida por IA.*

### 3.2 Hackathon de ideas
*Guía para la creación de prototipos rápidos y presentación de soluciones a problemas del día a día.*

---

## 4. Otros usos y Automatización

### 4.1 Google AI Studio y Generación de Contenido
*Técnicas avanzadas de prompting para la creación de presentaciones, imágenes y textos.*

### 4.2 Automatización sin código (MAKE, n8n)
*Cómo conectar aplicaciones (Email, Calendarios, Bases de datos) sin escribir una sola línea de código.*
