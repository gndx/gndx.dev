---
title: 'Install Python on MacOS Sonoma'
description: 'Learn how to install Python with Pyenv using Brew on macOS Sonoma. Follow these steps to supercharge your development workflow.'
pubDate: '2023-11-12T22:43:17.223Z'
heroImage: 'https://s3.amazonaws.com/gndx.dev/instalar-python-macos-sonoma.png'
categories:
  - 'python'
authors:
  - 'gndx'
tags:
  - 'python'
  - 'pyenv'
  - 'homebrew'
---

## Ready to Boost your Development Environment in macOS Sonoma?

If you are passionate about Python development, optimizing your environment is key. Learn how to install Python with Pyenv using Brew on macOS Sonoma. Follow these steps to supercharge your development workflow.

### Why Pyenv and Brew?

Pyenv lets you manage Python versions efficiently, while Brew simplifies installing tools on macOS. Together, they offer a powerful combo to have complete control over your development environment.

### What is Brew and Why Should You Use It?
Homebrew is a package manager for macOS that simplifies the installation and management of tools and software. Discover why this tool is essential to optimize your development experience on macOS.

Before you begin, make sure you have Brew installed. If you don't have it yet, run the following command in your terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### ## Step 2: Installing Pyenv

With Brew installed, install Pyenv with a simple command:

```bash
brew install pyenv
```

Then, add these lines to your profile file (such as `.zshrc` or `.bashrc`):

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

### ## Step 3: Installing Python with Pyenv

Now that Pyenv is configured, install the version of Python you need. For example, for Python 3.9.7:

```bash
pyenv install 3.12
```

Set this version as the default:

```bash
pyenv global 3.12
```

### ## Step 4: Verification

Make sure the installation was successful:

```bash
python --version
```

You should see the version you just installed. Ready! You now have a managed Python environment with Pyenv and Brew on your macOS Sonoma.
