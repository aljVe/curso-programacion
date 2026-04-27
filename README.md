# Programación en Inteligencia Artificial para Profesionales Clínicos

> Un curso práctico sobre cómo usar IA para programar y automatizar tareas en tu entorno laboral, sin necesidad de conocimientos técnicos previos.

**Instructores:** Alejandro & David

---

## 📋 Descripción del Curso

Este curso está diseñado para profesionales clínicos que desean aprender a usar herramientas de Inteligencia Artificial para mejorar su productividad y automatizar procesos en su día a día.

### Contenido del Curso

**1. Fundamentos y Entorno**
*   Conceptos de IA y herramientas principales.
*   Lenguajes de programación e IDEs.
*   Configuración del entorno local (Git, GitHub, Artifacts).
*   Glosario técnico básico (Frontend, Backend, Arquitectura, etc).

**2. Agentes IA y Conectividad**
*   Uso de agentes avanzados (Antigravity, Codex, Claude Code).
*   Conocer el lenguaje de programación de tu hospital para poder integrar proyectos.
*   Ampliación de funciones con Skills y MCP.

**3. Proyectos Prácticos**
*   **Proyecto desde Cero:** Desarrolla una aplicación paso a paso.
*   **Hackathon Clínico:** Crea y presenta un prototipo para resolver un problema de tu día a día.

**4. Otros usos**
*   Google AI Studio y generación de contenido (PPTs, Imágenes).
*   Automatización sin código (MAKE, n8n).

---

## 🚀 Comenzar Rápidamente

### Requisitos Previos

- [Node.js](https://nodejs.org/) (versión LTS recomendada)
- [Git](https://git-scm.com/)

### Instalación

```bash
# Clonar el repositorio
git clone <repository-url>
cd curso-IA-programacion

# Instalar dependencias
npm install
```

### Ejecutar Localmente

```bash
# Iniciar el servidor de desarrollo (slides interactivas)
npx slidev
```

El servidor abrirá automáticamente en `http://localhost:3030` donde podrás ver y editar las slides en tiempo real.

---

## 📤 Desplegar las Slides

### Opción 1: GitHub Pages (Recomendado)

Si usas GitHub, puedes desplegar automáticamente con GitHub Actions:

1. **Crear archivo de workflow:**
   - Crea la carpeta `.github/workflows/` en la raíz del proyecto
   - Crea el archivo `.github/workflows/deploy.yml` con el siguiente contenido:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 'lts/*'
      - run: npm install
      - run: npm run build -- --base /${{ github.event.repository.name }}/
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/deploy-pages@v4
        id: deployment
```

2. **Push a main branch:**
   ```bash
   git add .
   git commit -m "Add GitHub Pages deployment"
   git push origin main
   ```

3. **Las slides se desplegarán automáticamente** en: `https://<your-username>.github.io/<repository-name>/`

### Opción 2: Construir Localmente

Si prefieres construir y servir manualmente:

```bash
# Construir las slides
npx slidev build

# El resultado estará en la carpeta 'dist/'
# Puedes servir con cualquier servidor web estático
```

---

## 📁 Exportar las Slides

### Exportar a PDF

```bash
# Primero, instala playwright (necesario una sola vez)
npm install -D playwright-chromium

# Exportar a PDF
npx slidev export
```

El PDF se guardará como `slides-export.pdf`

### Exportar a PPTX (PowerPoint)

```bash
# Exportar a PowerPoint
npx slidev export --format pptx
```

### Exportar a PNG (Imágenes)

```bash
# Exportar cada slide como imagen
npx slidev export --format png
```

**Opciones adicionales:**
- `--output <carpeta>` - Especificar carpeta de salida
- `--dark` - Exportar en modo oscuro
- `--range 1,4-8` - Exportar solo slides específicas

---

## 📝 Editar las Slides

Las slides están en el archivo `slides.md`. Puedes editar:

- **Títulos y contenido:** Texto normal en Markdown
- **Interactividad:** Añadir componentes Vue
- **Temas:** Cambiar el tema en el frontmatter

Lee la [documentación oficial de Slidev](https://sli.dev) para más opciones.

---

## 📚 Recursos Útiles

- [Documentación Slidev](https://sli.dev)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)

---

## 💬 Contacto y Soporte

Para preguntas sobre el contenido del curso o dudas técnicas:

- **Alejandro:** [contacto]
- **David:** [contacto]

---

## 📄 Licencia

Este curso es material educativo creado para profesionales clínicos.

---

<!-- TEMP: style branches for review — delete this section once a style is chosen -->
## 🎨 Variantes de Estilo (revisión pendiente)

| Rama | Estilo | Vista previa |
|------|--------|--------------|
| `main` | Neural Clinic — oscuro, cyan, Cormorant Garamond | `npx slidev slides.md` |
| `feature/alternative-styles` | Retro-Futurista — neón, scanlines, IBM Plex | `git checkout feature/alternative-styles && npx slidev slides.md` |
| `feature/data-scientific` | Científico — cuadrícula, verde/naranja, IBM Plex | `git checkout feature/data-scientific && npx slidev slides.md` |
| `feature/minimalist-editorial` | Minimalista — crema/salvia, Merriweather serif | `git checkout feature/minimalist-editorial && npx slidev slides.md` |
<!-- END TEMP -->

---

**¡Gracias por ser parte de este viaje hacia la programación con IA! 🚀**
