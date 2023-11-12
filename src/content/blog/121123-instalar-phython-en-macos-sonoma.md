---
title: "Instalar Phython en MacOS Sonoma"
description:
pubDate: "2023-11-12T22:43:17.223Z"
heroImage: "https://s3.amazonaws.com/gndx.dev/instalar-python-macos-sonoma.png"
heroImage: "/blog-placeholder.jpg"
categories: ["python"]
authors: ["gndx"]
tags: ["python", "pyenv", "homebrew"]
---

## ¿Listo para Potenciar tu Ambiente de Desarrollo en macOS Sonoma?

Si eres un apasionado del desarrollo en Python, optimizar tu entorno es clave. Aprender a instalar Python con Pyenv usando Brew en macOS Sonoma. Sigue estos pasos para potenciar tu flujo de trabajo de desarrollo.

### ¿Por qué Pyenv y Brew?

Pyenv te permite gestionar versiones de Python de manera eficiente, mientras que Brew simplifica la instalación de herramientas en macOS. Juntos, ofrecen un combo poderoso para tener un control total sobre tu entorno de desarrollo.

### ¿Qué es Brew y por qué Deberías Usarlo?
Homebrew, es un gestor de paquetes para macOS que simplifica la instalación y gestión de herramientas y software. Descubre por qué esta herramienta es esencial para optimizar tu experiencia de desarrollo en macOS.

Antes de comenzar, asegúrate de tener Brew instalado. Si aún no lo tienes, ejecuta el siguiente comando en tu terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### ## Paso 2: Instalando Pyenv

Con Brew instalado, instala Pyenv con un simple comando:

```bash
brew install pyenv
```

Luego, agrega estas líneas a tu archivo de perfil (como `.zshrc` o `.bashrc`):

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

### ## Paso 3: Instalando Python con Pyenv

Ahora que Pyenv está configurado, instala la versión de Python que necesitas. Por ejemplo, para Python 3.9.7:

```bash
pyenv install 3.12
```

Establece esta versión como la predeterminada:

```bash
pyenv global 3.12
```

### ## Paso 4: Verificación

Asegúrate de que la instalación fue exitosa:

```bash
python --version
```

Deberías ver la versión que acabas de instalar. ¡Listo! Ahora tienes un entorno Python gestionado con Pyenv y Brew en tu macOS Sonoma.