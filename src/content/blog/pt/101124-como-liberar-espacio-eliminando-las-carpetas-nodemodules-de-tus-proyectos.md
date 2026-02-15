---
title: 'Como liberar espaço excluindo as pastas node_modules dos seus projetos?'
description: 'As dependências do seu projeto podem ocupar MUITO espaço considerável no seu disco rígido. As pastas `node_modules` em projetos JavaScript geralmente consomem centenas de MB e até excedem um GB.'
pubDate: '2024-11-11T00:41:23.150Z'
heroImage: 'https://s3.us-east-1.amazonaws.com/gndx.dev/eliminar-carpeta-node-modules-gndx.png'
categories:
  - 'GitHub'
  - 'JavaScript'
  - 'nó'
authors:
  - 'gndx'
tags:
  - 'GitHub'
  - 'javascript'
  - 'nó'
---


As dependências do seu projeto podem ocupar MUITO espaço considerável no seu disco rígido. Pastas `node_modules` em projetos JavaScript geralmente consomem centenas de MB e até excedem GB. Se você tiver muitos projetos pendentes, excluir apenas as pastas `node_modules` pode ajudá-lo a liberar uma quantidade significativa de espaço.

## Por que as pastas node_modules ocupam tanto espaço?

Cada vez que você instala dependências em um projeto JavaScript, a pasta `node_modules` é preenchida com arquivos e subpastas necessárias para executar o projeto. Isso inclui pacotes que o próprio projeto exige e, por sua vez, todas as dependências desses pacotes, resultando em uma árvore de dependências que pode se tornar muito extensa e pesada.

## Como verificar quanto espaço as pastas node_modules ocupam no macOS e Linux?

Se você tem seus projetos organizados em uma pasta específica, você pode verificar quanto espaço as pastas `node_modules` ocupam em seu sistema. Para usuários de macOS ou Linux, os comandos abaixo ajudarão a localizar essas pastas e a somar o espaço que estão ocupando.

1. Vá até a pasta principal onde seus projetos estão armazenados, no meu caso utilizo `~/Dev` para todos os meus projetos:

2. Liste o tamanho de cada pasta node_modules:

   ```bash
   find . -name "node_modules" -type d -prune | xargs du -chs
   ```

## Como verificar o espaço ocupado no Windows?

Para usuários do Windows, o processo é semelhante, embora o comando seja diferente:

1. Execute este comando no CMD para encontrar as pastas node_modules:
   ```cmd
   FOR /d /r . %d in (node_modules) DO @IF EXIST "%d" echo %d
   ```

## Como excluir permanentemente as pastas node_modules?

Se você decidiu liberar espaço, lembre-se de que a exclusão das pastas `node_modules` exigirá a reinstalação das dependências de quaisquer projetos nos quais deseja trabalhar no futuro usando `npm install`. Também é importante garantir que seus projetos estejam armazenados e atualizados no GitHub.

### No Linux ou macOS

1. Certifique-se de estar na pasta que contém seus projetos no meu caso `~/Dev`

2. Exclua todas as pastas `node_modules` do seu computador:
   ```bash
   find . -name 'node_modules' -type d -prune -print -exec rm -rf '{}' \;
   ```

### No Windows (CMD)

1. Vá para a pasta principal dos seus projetos:

2. Use este comando para excluir as pastas node_modules:
   ```cmd
   FOR /d /r . %d in (node_modules) DO @IF EXIST "%d" rd /s /q "%d"
   ```

Com essas etapas, você pode liberar espaço significativamente no disco rígido. Em alguns casos, os usuários conseguiram recuperar vários GB de armazenamento, como você pode ver no meu caso, o que é especialmente útil se você tiver vários projetos acumulados e não os estiver usando regularmente. Lembre-se que é importante ter seus projetos conectados a um repositório em nuvem como o GitHub e usar o arquivo .gitignore para evitar o envio de todas aquelas centenas de megabytes para um repositório.

