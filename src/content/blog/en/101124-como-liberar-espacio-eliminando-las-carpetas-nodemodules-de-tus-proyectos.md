---
title: 'How to free up space by deleting the node_modules folders from your projects?'
description: 'Your project dependencies can take up a LOT of considerable space on your hard drive. The `node_modules` folders in JavaScript projects usually consume hundreds of MB and even exceed one GB.'
pubDate: '2024-11-11T00:41:23.150Z'
heroImage: 'https://s3.us-east-1.amazonaws.com/gndx.dev/eliminar-carpeta-node-modules-gndx.png'
categories:
  - 'github'
  - 'JavaScript'
  - 'node'
authors:
  - 'gndx'
tags:
  - 'github'
  - 'javascript'
  - 'node'
---


Your project dependencies can take up a LOT of considerable space on your hard drive. `node_modules` folders in JavaScript projects usually consume hundreds of MB and even exceed GB. If you have a lot of backlogged projects, deleting just the `node_modules` folders can help you free up a significant amount of space.

## Why do node_modules folders take up so much space?

Every time you install dependencies on a JavaScript project, the `node_modules` folder is filled with files and subfolders necessary to run the project. This includes packages that the project itself requires and, in turn, all the dependencies of those packages, resulting in a dependency tree that can become very extensive and heavy.

## How to check how much space node_modules folders take up on macOS and Linux?

If you have your projects organized in a specific folder, you can check how much space the `node_modules` folders take up on your system. For macOS or Linux users, the commands below will help locate these folders and add up the space they are taking up.

1. Go to the main folder where your projects are stored, in my case I use `~/Dev` for all my projects:

2. List the size of each node_modules folder:

   ```bash
   find . -name "node_modules" -type d -prune | xargs du -chs
   ```

## How to check the occupied space in Windows?

For Windows users, the process is similar, although the command differs:

1. Run this command in CMD to find the node_modules folders:
   ```cmd
   FOR /d /r . %d in (node_modules) DO @IF EXIST "%d" echo %d
   ```

## How to permanently delete the node_modules folders?

If you've decided to free up space, keep in mind that deleting the `node_modules` folders will require you to reinstall the dependencies of any projects you want to work on in the future using `npm install`. It is also important to ensure that your projects are stored and up to date on GitHub.

### On Linux or macOS

1. Make sure you are in the folder that contains your projects in my case `~/Dev`

2. Delete all `node_modules` folders from your computer:
   ```bash
   find . -name 'node_modules' -type d -prune -print -exec rm -rf '{}' \;
   ```

### On Windows (CMD)

1. Go to your main projects folder:

2. Use this command to delete the node_modules folders:
   ```cmd
   FOR /d /r . %d in (node_modules) DO @IF EXIST "%d" rd /s /q "%d"
   ```

With these steps, you can significantly free up space on your hard drive. In some cases, users have managed to recover several GB of storage as you can see in my case, which is especially useful if you have multiple projects accumulated and you are not using them regularly. Remember that it is important to have your projects connected to a cloud repository like GitHub and use the .gitignore file to avoid sending all those hundreds of megabytes to a repository.

