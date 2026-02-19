---
title: 'La historia del proyecto conocido hoy como OpenClaw'
description: 'De Clawdbot a Moltbot y finalmente OpenClaw: el recorrido de uno de los proyectos de agentes de IA open source con mayor crecimiento reciente.'
pubDate: '2026-02-19T18:00:00.000Z'
heroImage: '/blog-placeholder.jpg'
categories: ['inteligencia-artificial', 'open-source', 'agentes']
authors: ['gndx']
tags: ['openclaw', 'clawdbot', 'moltbot', 'ia', 'openai']
---

En noviembre de 2025, Peter Steinberger, desarrollador austriaco y fundador de PSPDFKit, inició un experimento de fin de semana que terminaría convirtiéndose en uno de los proyectos de IA open source más comentados del momento.

Su idea era simple de explicar, pero compleja de ejecutar: crear un asistente autónomo y autoalojado que no solo contestara mensajes, sino que pudiera actuar por ti en tareas reales.

## El inicio: más que un chatbot

Desde el principio, el objetivo no era construir otro bot de texto. El proyecto buscaba operar en canales reales como WhatsApp, Telegram, iMessage, Discord o Slack, y ejecutar acciones como:

- correr comandos en tu sistema,
- gestionar calendario y recordatorios,
- leer y procesar correo,
- coordinar tareas con servicios externos.

Todo esto apoyado por modelos como Claude, GPT, Gemini u otros, mientras la lógica y el estado persistente vivían de forma local.

## Línea de tiempo del proyecto

### Noviembre 2025: Clawdbot

El primer lanzamiento público llegó bajo el nombre **Clawdbot**, con un asistente llamado **Clawd**, inicialmente vinculado al ecosistema de Claude.

### Diciembre 2025: viralización

En muy pocos días el repositorio explotó en popularidad: miles de estrellas en 24 horas, fuerte tracción entre desarrolladores y gran cobertura en redes y medios tecnológicos.

### 27 de enero de 2026: cambio a Moltbot

Tras una solicitud por posible confusión de marca entre Clawd/Clawdbot y Claude, el proyecto se renombró como **Moltbot** y el asistente pasó a llamarse **Molty**.

El concepto de "molt" (muda del caparazón) mantenía la temática de langosta, pero con identidad renovada.

Durante esta transición ocurrió un incidente delicado: el antiguo handle en redes fue secuestrado por estafadores para promocionar un token falso relacionado con Clawd, que alcanzó un pico aproximado de 16 millones de dólares antes de desplomarse.

### Finales de enero de 2026: nace OpenClaw

Poco después, el creador decidió volver a iterar el naming. Así apareció **OpenClaw**, nombre que se mantiene hasta ahora.

## Filosofía técnica

OpenClaw no es un modelo fundacional propio. Es un framework de agente autónomo que prioriza ejecución real, memoria y proactividad.

Su arquitectura se entiende por tres bloques principales:

- **Gateway**: recibe eventos desde apps de mensajería y otros canales.
- **Agent Loop**: toma decisiones, planea y ejecuta acciones.
- **Heartbeat**: mantiene estado, continuidad y persistencia del agente.

Esa separación ha permitido crecer en capacidades sin perder foco: integrar varios proveedores de IA y operar en entornos locales o auto-hospedados.

## Comunidad y ecosistema

Otra pieza clave ha sido la comunidad. Alrededor del proyecto surgieron "skills" y módulos extensibles, incluyendo colecciones comunitarias tipo *awesome-openclaw-skills* y ecosistemas relacionados como VoltAgent.

También apareció **Moltbook**, una red social orientada a agentes de IA, donde estas instancias pueden comunicarse y coordinarse de forma autónoma.

## 2026 y lo que viene

Con más de 100,000 a 200,000 estrellas en GitHub en tiempo récord, OpenClaw se convirtió en referencia de crecimiento dentro del software abierto para agentes.

A mediados de febrero de 2026, se anunció que Peter Steinberger se uniría a OpenAI, mientras OpenClaw evolucionaría bajo una fundación open source para sostener su desarrollo de largo plazo.

La pregunta ahora no es si este tipo de herramientas seguirán creciendo, sino a qué velocidad llegarán al usuario final.

Si 2026 marca el despegue, 2027 podría consolidar una nueva categoría de asistentes: agentes personales capaces de operar de verdad en nuestros sistemas, no solo de conversar sobre ellos.
