---
title: 'Customize your terminal from 0 to PRO 😎 Warp + Oh My Zsh'
description: 'Terminal customization can completely transform your developer experience, going from a basic and unappealing interface to a powerful and visually stunning tool. With Warp, a smart terminal that incorporates AI, along with some specific configurations, you will be able to create a more efficient and pleasant development environment.'
pubDate: '2024-12-09T02:28:42.232Z'
heroImage: 'https://s3.us-east-1.amazonaws.com/gndx.dev/personaliza-tu-terminal-warpdotdev.png'
categories:
  - 'youtube'
authors:
  - 'gndx'
tags:
  - 'warp'
  - 'terminal'
  - 'ohmyzsh'
---


Customizing your terminal can completely transform your experience as a developer, making it more functional, attractive and efficient. In this article, you'll learn how to set up a modern, powerful terminal using tools like Warp, Zsh, and Oh My Zsh, as well as taking advantage of built-in artificial intelligence.

  

## What terminal should you use to customize it?


Although you can use any terminal, [Warp.dev](https://warp.dev) is highly recommended. It is a terminal that incorporates artificial intelligence, which makes it ideal for developers. If you don't have it yet, install it before continuing.

Warp is available for macOS and Linux, and coming soon to Windows.

[Install Warp](https://app.warp.dev/referral/2YXKGD)

## How to install Zsh + Oh My Zsh?

The first step to customize your terminal is to install **Zsh**, an advanced and flexible command interpreter. Then, complement Zsh with **Oh My Zsh**, a tool that makes it easy to customize through themes, plugins, and settings. Follow these steps:

 
1. **Install Zsh**:

- On macOS, use Homebrew:

```bash

brew install zsh

```

- On Linux, use your distribution's package manager.

- On Windows, make sure you have WSL configured and use the Ubuntu package manager.

```bash
sudo apt install zsh -y
```

  

2. **Install Oh My Zsh**:

All you have to do is copy and paste the following code into your terminal to install Oh My Zsh.

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

 

## How to choose and configure a theme for Zsh?

  A well-designed theme improves the appearance and functionality of your terminal. To install a theme on Oh My Zsh:

1. Download the P10k theme from the official **[powerlevel10k](https://github.com/romkatv/powerlevel10k)** repository
2. Configure the theme by editing the `.zshrc` file:

- Open the file with your favorite code editor.
- Find the line `ZSH_THEME` and replace it with the name of the theme you downloaded, which in this chaos is `"powerlevel10k/powerlevel10k"`.
- Save the changes and restart Zsh with the `exec zsh` command to apply the configuration.
- Run the command `p10k configure` to start the configuration process.
 
 
## How to adjust the appearance and functionality of your terminal?

Warp and Oh My Zsh allow you to customize details such as colors, separators, and visual structures. During initial setup, follow these steps:

- Select the style of the icons and separators.
- Set the number of lines in the prompt.
- Sets the display of information such as time and connection status.

  

## How to take advantage of artificial intelligence at Warp?

Warp includes an artificial intelligence feature that you can activate with the `#` symbol. This allows you to make queries directly from the terminal, such as:


- **Delete folders from node_modules**:

```bash
find . -name "node_modules" -type d -prune -exec rm -rf '{}' +
```

- Get command explanations or tips to optimize your workflow.


## What advantages does this setup offer for developers?

With a custom terminal, you will not only have a more attractive interface, but also advanced tools that optimize your productivity. From managing projects to executing complex commands, this setup will allow you to work more efficiently and professionally.

I leave you a Step by Step video to achieve this configuration and customization of your terminal.


<iframe width="100%" height="315" src="https://www.youtube.com/embed/tuLkWShN8V4?si=UEyBsnY10e662ZdG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

