---
title: "Personaliza tu terminal de 0 a PRO 😎 Warp + Oh My Zsh"
description: "La personalización de la terminal puede transformar por completo tu experiencia como desarrollador, pasando de una interfaz básica y poco atractiva a una herramienta potente y visualmente impresionante. Con Warp, una terminal inteligente que incorpora IA, junto con algunas configuraciones específicas, podrás crear un entorno de desarrollo más eficiente y agradable."
pubDate: "2024-12-09T02:28:42.232Z"
heroImage: "[https://s3.amazonaws.com/gndx.dev/subtitulos-de-videos-de-youtube.png](https://s3.us-east-1.amazonaws.com/gndx.dev/personaliza-tu-terminal-warpdotdev.png)"
categories: ["youtube"]
authors: ["gndx"]
tags: ["warp", "terminal", "ohmyzsh"]
---

Personalizar tu terminal puede transformar por completo tu experiencia como desarrollador, haciéndola más funcional, atractiva y eficiente. En este artículo, aprenderás cómo configurar una terminal moderna y poderosa utilizando herramientas como Warp, Zsh y Oh My Zsh, además de aprovechar la inteligencia artificial integrada.

  

## ¿Qué terminal deberías usar para personalizarla?


Aunque puedes usar cualquier terminal, [Warp.dev](https://warp.dev) es altamente recomendada. Es una terminal que incorpora inteligencia artificial, lo que la hace ideal para desarrolladores. Si aún no la tienes, instálala antes de continuar. 

Warp está disponible para macOS y Linux, y próximamente en Windows.

[Instalar Warp](https://app.warp.dev/referral/2YXKGD) 

## ¿Cómo instalar Zsh + Oh My Zsh?

El primer paso para personalizar tu terminal es instalar **Zsh**, un intérprete de comandos avanzado y flexible. Luego, complementa Zsh con **Oh My Zsh**, una herramienta que facilita la personalización mediante temas, plugins y configuraciones. Sigue estos pasos:

 
1. **Instalar Zsh**:

- En macOS, usa Homebrew:

```bash

brew install zsh

```

- En Linux, utiliza el gestor de paquetes de tu distribución.

- En Windows, asegúrate de tener WSL configurado y utilizar el gestor de paquetes de Ubuntu.

```bash
sudo apt install zsh -y
```

  

2. **Instalar Oh My Zsh**:

Lo único que tienes que hacer es copiar y pegar el siguiente código en tu terminal para instalar Oh My Zsh.

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

 

## ¿Cómo elegir y configurar un tema para Zsh?

  Un tema bien diseñado mejora la apariencia y funcionalidad de tu terminal. Para instalar un tema en Oh My Zsh:

1. Descarga el tema de P10k el repositorio oficial de **[powerlevel10k](https://github.com/romkatv/powerlevel10k)**
2. Configura el tema editando el archivo `.zshrc`:

- Abre el archivo con tu editor de código favorito.
- Busca la línea `ZSH_THEME` y reemplázala con el nombre del tema que descargaste que en este caos es `"powerlevel10k/powerlevel10k"`.
- Guarda los cambios y reinicia Zsh con el comando `exec zsh` para aplicar la configuración.
- Ejecuta el comando `p10k configure` Para iniciar el proceso de configuración.
 
 
## ¿Cómo ajustar la apariencia y funcionalidad de tu terminal?

Warp y Oh My Zsh permiten personalizar detalles como colores, separadores y estructuras visuales. Durante la configuración inicial, sigue estos pasos:

- Selecciona el estilo de los iconos y separadores.
- Configura el número de líneas en el prompt.
- Ajusta la visualización de información como el tiempo y el estado de conexión.

  

## ¿Cómo aprovechar la inteligencia artificial en Warp?

Warp incluye una función de inteligencia artificial que puedes activar con el símbolo `#`. Esto te permite realizar consultas directamente desde la terminal, como:


- **Eliminar  carpetas de node_modules**:

```bash
find . -name "node_modules" -type d -prune -exec rm -rf '{}' +
```

- Obtener explicaciones de comandos o sugerencias para optimizar tu flujo de trabajo.


## ¿Qué ventajas ofrece esta configuración para desarrolladores?

Con una terminal personalizada, no solo tendrás una interfaz más atractiva, sino también herramientas avanzadas que optimizan tu productividad. Desde la gestión de proyectos hasta la ejecución de comandos complejos, esta configuración te permitirá trabajar de manera más eficiente y profesional.

Te dejo un video Paso a Paso para lograr esta configuración y personalización de tu terminal. 


<iframe width="100%" height="315" src="https://www.youtube.com/embed/tuLkWShN8V4?si=UEyBsnY10e662ZdG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
