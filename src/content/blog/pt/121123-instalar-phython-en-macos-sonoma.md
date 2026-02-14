---
title: 'Instale Python no MacOS Sonoma'
description: 'Aprenda como instalar Python com Pyenv usando Brew no macOS Sonoma. Siga estas etapas para turbinar seu fluxo de trabalho de desenvolvimento.'
pubDate: '2023-11-12T22:43:17.223Z'
heroImage: 'https://s3.amazonaws.com/gndx.dev/instalar-python-macos-sonoma.png'
categories:
  - 'píton'
authors:
  - 'gndx'
tags:
  - 'píton'
  - 'pyenv'
  - 'cerveja caseira'
---

## Pronto para impulsionar seu ambiente de desenvolvimento no macOS Sonoma?

Se você é apaixonado pelo desenvolvimento em Python, otimizar seu ambiente é fundamental. Aprenda como instalar Python com Pyenv usando Brew no macOS Sonoma. Siga estas etapas para turbinar seu fluxo de trabalho de desenvolvimento.

### Por que Pyenv e Brew?

Pyenv permite gerenciar versões do Python com eficiência, enquanto o Brew simplifica a instalação de ferramentas no macOS. Juntos, eles oferecem uma combinação poderosa para ter controle total sobre seu ambiente de desenvolvimento.

### O que é Brew e por que você deve usá-lo?
Homebrew é um gerenciador de pacotes para macOS que simplifica a instalação e gerenciamento de ferramentas e software. Descubra por que esta ferramenta é essencial para otimizar sua experiência de desenvolvimento no macOS.

Antes de começar, certifique-se de ter o Brew instalado. Caso ainda não o tenha, execute o seguinte comando em seu terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### ## Etapa 2: Instalando o Pyenv

Com o Brew instalado, instale o Pyenv com um comando simples:

```bash
brew install pyenv
```

Em seguida, adicione estas linhas ao seu arquivo de perfil (como `.zshrc` ou `.bashrc`):

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

### ## Etapa 3: Instalando Python com Pyenv

Agora que o Pyenv está configurado, instale a versão do Python necessária. Por exemplo, para Python 3.9.7:

```bash
pyenv install 3.12
```

Defina esta versão como padrão:

```bash
pyenv global 3.12
```

### ## Etapa 4: verificação

Certifique-se de que a instalação foi bem-sucedida:

```bash
python --version
```

Você deverá ver a versão que acabou de instalar. Preparar! Agora você tem um ambiente Python gerenciado com Pyenv e Brew em seu macOS Sonoma.
