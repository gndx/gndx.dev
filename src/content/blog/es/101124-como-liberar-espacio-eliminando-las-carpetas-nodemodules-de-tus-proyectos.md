---
title: '¿Cómo liberar espacio eliminando las carpetas node_modules de tus proyectos?'
description: 'Las dependencias de tus proyectos pueden ocupar MUCHO espacio considerable en tu disco duro. Las carpetas `node_modules` en proyectos con JavaScript suelen llegar a consumir cientos de MB e incluso superar el GB. '
pubDate: '2024-11-11T00:41:23.150Z'
heroImage: 'https://s3.us-east-1.amazonaws.com/gndx.dev/eliminar-carpeta-node-modules-gndx.png'
categories: ['github', 'JavaScript', 'node']
authors: ['gndx']
tags: ['github', 'javascript', 'node']
---

Las dependencias de tus proyectos pueden ocupar MUCHO espacio considerable en tu disco duro. Las carpetas `node_modules` en proyectos con JavaScript suelen llegar a consumir cientos de MB e incluso superar el GB. Si tienes muchos proyectos acumulados, borrar solo las carpetas de `node_modules` puede ayudarte a liberar una cantidad significativa de espacio.

## ¿Por qué ocupan tanto espacio las carpetas node_modules?

Cada vez que instalas dependencias en un proyecto JavaScript, la carpeta `node_modules` se llena de archivos y sub carpetas necesarios para ejecutar el proyecto. Esto incluye paquetes que el propio proyecto requiere y, a su vez, todas las dependencias de esos paquetes, resultando en un árbol de dependencias que puede llegar a ser muy extenso y pesado.

## ¿Cómo revisar cuánto espacio ocupan las carpetas node_modules en macOS y Linux?

Si tienes tus proyectos organizados en una carpeta específica, puedes revisar cuánto espacio ocupan las carpetas `node_modules` en tu sistema. Para usuarios de macOS o Linux, los comandos a continuación ayudarán a localizar estas carpetas y sumar el espacio que están ocupando.

1. Dirígete a la carpeta principal donde se almacenan tus proyectos, en mi caso utilizo `~/Dev` para todos mis proyectos:

2. Listar el tamaño de cada carpeta node_modules:

   ```bash
   find . -name "node_modules" -type d -prune | xargs du -chs
   ```

## ¿Cómo verificar el espacio ocupado en Windows?

Para usuarios de Windows, el proceso es similar, aunque el comando difiere:

1. Ejecuta este comando en CMD para encontrar las carpetas node_modules:
   ```cmd
   FOR /d /r . %d in (node_modules) DO @IF EXIST "%d" echo %d
   ```

## ¿Cómo eliminar definitivamente las carpetas node_modules?

Si has decidido liberar espacio, ten en cuenta que al eliminar las carpetas `node_modules` deberás reinstalar las dependencias de cualquier proyecto en el que desees trabajar en el futuro usando `npm install`. También importante asegurar que tus proyectos están almacenado y al dia en GitHub.

### En Linux o macOS

1. Asegúrate de estar en la carpeta que contiene tus proyectos en mi caso `~/Dev`

2. Eliminar todas las carpetas `node_modules` de tu computadora:
   ```bash
   find . -name 'node_modules' -type d -prune -print -exec rm -rf '{}' \;
   ```

### En Windows (CMD)

1. Dirígete a la carpeta principal de tus proyectos:

2. Usa este comando para eliminar las carpetas node_modules:
   ```cmd
   FOR /d /r . %d in (node_modules) DO @IF EXIST "%d" rd /s /q "%d"
   ```

Con estos pasos, puedes liberar espacio de manera significativa en tu disco duro. En algunos casos, usuarios han logrado recuperar varios GB de almacenamiento como lo puedes apreciar en mi caso, lo cual es especialmente útil si tienes múltiples proyectos acumulados y no los estás utilizando regularmente. Recuerda que es importante tener tus proyectos conectados a un repositorio en la nube como GitHub y utilizar el archivo .gitignore para no enviar todos esos cientos de megas a un repositorio.
