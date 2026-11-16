"""Imágenes de «Cómo instalar Gemma 4 en tu teléfono» (es / en / pt)."""
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[1] / ".claude" / "skills" / "blog-imagenes" / "plantilla"))
from marca import cifra, columna, dos, escribir, flujo, marco, metricas, nota, pasos, portada, tarjetas  # noqa: E402

POST = json.loads((AQUI / "post.json").read_text(encoding="utf-8"))
IDIOMAS = POST["idiomas"]

T = {
    "es": {
        "pie": "gndx.dev · Gemma 4 en tu teléfono",
        "alt": {"portada": "Gemma 4 funcionando sin conexión en iPhone y Android", "requisitos": "Requisitos para ejecutar Gemma 4 en un teléfono", "iphone": "Pasos para instalar Gemma 4 en iPhone", "android": "Pasos para instalar Gemma 4 en Android", "rendimiento": "Consejos para mejorar el rendimiento de Gemma 4 en el teléfono"},
        "k0": "IA local · iPhone + Android", "t0": "Gemma 4 en **tu teléfono**", "s0": "Instálala con Google AI Edge Gallery y conversa sin conexión.", "c0": "libres para la descarga",
        "k1": "Requisitos rápidos", "t1": "Lo que necesita **tu teléfono**", "m1": [("iOS 17+", "iPhone · A16 recomendado"), ("Android 14", "Tensor o Snapdragon 8 Gen 2"), ("6 GB", "espacio libre + Wi-Fi")], "n1": "Puede funcionar en equipos inferiores, con menos memoria y respuestas más lentas.",
        "k2": "iPhone", "t2": "De la App Store al **chat local**", "p2": [("Instala", "Google AI Edge Gallery"), ("Abre AI Chat", "acepta los permisos locales"), ("Busca Gemma 4", "elige Edge Optimized"), ("Descarga y prueba", "inicia una conversación")],
        "k3": "Android", "t3": "Gemma 4 lista en **cuatro pasos**", "p3": [("Instala", "desde Google Play"), ("Permite guardar", "el modelo queda en el teléfono"), ("Abre AI Chat", "elige Gemma 4 Edge Optimized"), ("Descarga y prueba", "conversa sin conexión")],
        "k4": "Mejor experiencia", "t4": "Más autonomía, **menos freno**", "c4": [("Actualiza la app", "recibe nuevas optimizaciones"), ("Batería +40%", "prepárala para sesiones largas"), ("Desactiva el ahorro", "evita caídas de rendimiento")],
    },
    "en": {
        "pie": "gndx.dev · Gemma 4 on your phone",
        "alt": {"portada": "Gemma 4 running offline on iPhone and Android", "requisitos": "Phone requirements for running Gemma 4", "iphone": "Steps to install Gemma 4 on iPhone", "android": "Steps to install Gemma 4 on Android", "rendimiento": "Tips to improve Gemma 4 performance on a phone"},
        "k0": "Local AI · iPhone + Android", "t0": "Gemma 4 on **your phone**", "s0": "Install it with Google AI Edge Gallery and chat offline.", "c0": "free for the download",
        "k1": "Quick requirements", "t1": "What **your phone** needs", "m1": [("iOS 17+", "iPhone · A16 recommended"), ("Android 14", "Tensor or Snapdragon 8 Gen 2"), ("6 GB", "free storage + Wi-Fi")], "n1": "Modern hardware gives the best local performance.",
        "k2": "iPhone", "t2": "From the App Store to **local chat**", "p2": [("Install", "Google AI Edge Gallery"), ("Open AI Chat", "grant local permissions"), ("Find Gemma 4", "choose Edge Optimized"), ("Download and run", "start an offline chat")],
        "k3": "Android", "t3": "Gemma 4 ready in **four steps**", "p3": [("Install", "from Google Play"), ("Allow storage", "keep the model on-device"), ("Open Model Hub", "download Gemma 4"), ("Set as default", "start your first prompt")],
        "k4": "Best experience", "t4": "More runtime, **less throttling**", "c4": [("Update the app", "get the latest optimizations"), ("Battery above 40%", "prepare for longer sessions"), ("Disable power saving", "avoid performance drops")],
    },
    "pt": {
        "pie": "gndx.dev · Gemma 4 no seu telefone",
        "alt": {"portada": "Gemma 4 funcionando offline no iPhone e Android", "requisitos": "Requisitos do telefone para executar o Gemma 4", "iphone": "Passos para instalar o Gemma 4 no iPhone", "android": "Passos para instalar o Gemma 4 no Android", "rendimiento": "Dicas para melhorar o desempenho do Gemma 4 no telefone"},
        "k0": "IA local · iPhone + Android", "t0": "Gemma 4 no **seu telefone**", "s0": "Instale com o Google AI Edge Gallery e converse offline.", "c0": "livres para o download",
        "k1": "Requisitos rápidos", "t1": "O que **seu telefone** precisa", "m1": [("iOS 17+", "iPhone · A16 recomendado"), ("Android 14", "Tensor ou Snapdragon 8 Gen 2"), ("6 GB", "espaço livre + Wi-Fi")], "n1": "Hardware moderno oferece o melhor desempenho local.",
        "k2": "iPhone", "t2": "Da App Store ao **chat local**", "p2": [("Instale", "Google AI Edge Gallery"), ("Abra AI Chat", "aceite as permissões locais"), ("Busque Gemma 4", "escolha Edge Optimized"), ("Baixe e execute", "inicie uma conversa offline")],
        "k3": "Android", "t3": "Gemma 4 pronto em **quatro passos**", "p3": [("Instale", "pela Google Play"), ("Permita armazenar", "mantenha o modelo no aparelho"), ("Abra Model Hub", "baixe o Gemma 4"), ("Defina como padrão", "envie seu primeiro prompt")],
        "k4": "Melhor experiência", "t4": "Mais autonomia, **menos limitação**", "c4": [("Atualize o app", "receba as novas otimizações"), ("Bateria acima de 40%", "prepare sessões prolongadas"), ("Desative a economia", "evite queda de desempenho")],
    },
}

IMAGENES = [
    ("portada", lambda t: portada(t, t["k0"], t["t0"], t["s0"], abajo=flujo([("iOS", "iPhone"), ("AI", "Gemma 4"), ("AND", "Android")]), lado=cifra("6 GB", t["c0"]))),
    ("requisitos", lambda t: marco(t, t["k1"], t["t1"], columna(metricas(t["m1"]), nota(t["n1"]), gap=38))),
    ("iphone", lambda t: marco(t, t["k2"], t["t2"], dos(pasos(t["p2"]), cifra("17+", "iOS · iPhone"), izq_ancho=920))),
    ("android", lambda t: marco(t, t["k3"], t["t3"], dos(pasos(t["p3"]), cifra("14", "Android"), izq_ancho=920))),
    ("rendimiento", lambda t: marco(t, t["k4"], t["t4"], tarjetas(t["c4"], cols=3))),
]

if __name__ == "__main__":
    escribir(AQUI, IMAGENES, T, IDIOMAS)
