---
title: 'A história do projeto conhecido hoje como OpenClaw'
description: 'De Clawdbot para Moltbot e depois OpenClaw: a trajetória de um dos projetos de agentes de IA open source com crescimento mais rápido.'
pubDate: '2026-02-19T18:00:00.000Z'
heroImage: '/blog-placeholder.jpg'
categories: ['inteligencia-artificial', 'open-source', 'agentes']
authors: ['gndx']
tags: ['openclaw', 'clawdbot', 'moltbot', 'ia', 'openai']
slug: '190226-la-historia-del-proyecto-openclaw'
---

Em novembro de 2025, Peter Steinberger, desenvolvedor austríaco e fundador da PSPDFKit, iniciou um experimento de fim de semana que rapidamente se tornou um dos projetos de IA open source mais comentados.

A ideia central era simples de explicar, mas ambiciosa de implementar: criar um assistente autônomo e auto-hospedado que não apenas respondesse mensagens, mas realmente executasse tarefas por você.

## O começo: além de um chatbot

Desde o início, o objetivo não era criar apenas mais uma interface de chat. O projeto foi pensado para funcionar em canais como WhatsApp, Telegram, iMessage, Discord ou Slack, executando ações como:

- rodar comandos no sistema,
- gerenciar calendário e lembretes,
- ler e processar e-mails,
- coordenar fluxos com serviços externos.

Tudo isso poderia usar modelos como Claude, GPT, Gemini e outros, mantendo a lógica e o estado persistente em execução local.

## Linha do tempo e evolução do nome

### Novembro de 2025: Clawdbot

O primeiro lançamento público saiu como **Clawdbot**, com um assistente chamado **Clawd**, inicialmente ligado ao ecossistema Claude.

### Dezembro de 2025: crescimento viral

Em poucos dias, o repositório explodiu em popularidade: milhares de estrelas no GitHub em 24 horas, grande interesse da comunidade e ampla cobertura.

### 27 de janeiro de 2026: mudança para Moltbot

Após uma solicitação por possível confusão de marca entre Clawd/Clawdbot e Claude, o projeto foi renomeado para **Moltbot**, com o assistente passando a se chamar **Molty**.

O termo "molt" (muda de carapaça) manteve a temática de lagosta com uma nova identidade.

Durante essa transição, um antigo handle de rede social foi sequestrado por golpistas para promover um token falso relacionado ao Clawd, que teria alcançado cerca de US$ 16 milhões antes de despencar.

### Final de janeiro de 2026: OpenClaw

Pouco depois, o criador decidiu ajustar o branding mais uma vez. Assim surgiu **OpenClaw**, nome que permanece até hoje.

## Filosofia técnica

OpenClaw não é um modelo fundacional proprietário. É um framework de agente autônomo focado em execução real, memória e proatividade.

A arquitetura costuma ser explicada em três blocos:

- **Gateway**: recebe eventos e mensagens de canais externos.
- **Agent Loop**: núcleo de decisão, planejamento e execução.
- **Heartbeat**: preserva estado, continuidade e persistência.

Essa separação permitiu evoluir rápido sem perder foco: suporte a múltiplos modelos e operação local/auto-hospedada.

## Ecossistema e comunidade

A comunidade virou um motor importante do projeto. Surgiram skills e módulos extensíveis, com coleções comunitárias no estilo _awesome-openclaw-skills_ e ecossistemas relacionados como VoltAgent.

Também foi lançada a proposta do **Moltbook**, uma rede social para agentes de IA se comunicarem e se organizarem de forma autônoma.

## 2026 e os próximos passos

Com 100.000 a 200.000 estrelas no GitHub em tempo recorde, OpenClaw se consolidou como referência em software aberto para agentes autônomos.

Em meados de fevereiro de 2026, foi anunciado que Peter Steinberger se juntaria à OpenAI, enquanto OpenClaw seguiria sob uma fundação open source para desenvolvimento de longo prazo.

A grande pergunta agora não é se essa categoria vai crescer, e sim com que velocidade ela chegará ao usuário final.

Se 2026 é o ano da decolagem, 2027 pode ser o ano em que agentes pessoais autônomos se tornem uma camada cotidiana da computação.
