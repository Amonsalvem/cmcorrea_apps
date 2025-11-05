import streamlit as st
from PIL import Image

# =========================
# Config básica & estilo
# =========================
st.set_page_config(page_title="Aplicaciones de IA — Amonsalvem", page_icon="🤖", layout="wide")

DARK_CSS = """
<style>
:root { --bg:#000; --fg:#fff; --muted:#bdbdbd; --card:#0b0b0b; --accent:#ffffff; }
html, body, .stApp { background: var(--bg) !important; color: var(--fg) !important; }
section[data-testid="stSidebar"] { background: #000000; border-right: 1px solid #111; }
h1, h2, h3, h4, h5, h6, p, span, li, label, div { color: var(--fg) !important; }
a, a:visited { color: var(--fg) !important; text-decoration: underline; }
.block-container { padding-top: 1.5rem; }
.card {
  background: var(--card);
  border: 1px solid #1a1a1a;
  border-radius: 18px;
  padding: 16px 16px 14px 16px;
}
.card h3 { margin: 0 0 .25rem 0; font-size: 1.05rem; letter-spacing: .2px; }
.card p { margin: .25rem 0 .75rem 0; color: var(--muted) !important; font-size: .925rem; }
.btnrow { display:flex; gap:.5rem; flex-wrap:wrap; }
button[kind="secondary"] { border-radius: 10px !important; }
.small { color: var(--muted) !important; font-size: .85rem; }
hr { border: none; border-top: 1px solid #151515; margin: 24px 0; }
.badge { font-size:.72rem; padding:.2rem .45rem; border:1px solid #222; border-radius:8px; color:#bbb; }
</style>
"""
st.markdown(DARK_CSS, unsafe_allow_html=True)

st.title("Aplicaciones de Inteligencia Artificial")
st.caption("Hub negro/-blanco • minimal • enlaces a tus repos y demos")

with st.sidebar:
    st.subheader("Acerca de este hub")
    st.write(
        "Colección de utilidades y experimentos de IA: visión, voz, análisis de texto, "
        "RAG y control IoT. Todo en una estética minimalista (fondo negro, contraste blanco)."
    )
    st.markdown("---")
    st.subheader("Páginas y ejercicios")
    st.write("Sitio de ejercicios: "
             "[Enlace](https://sites.google.com/view/aplicacionesdeia/inicio)")

# ========== Utilidades ==========
def safe_image(path: str, width: int = 220):
    """
    Intenta cargar una imagen local; si no existe, no rompe el layout.
    """
    try:
        img = Image.open(path)
        st.image(img, width=width)
    except Exception:
        # placeholder ligero
        st.markdown(
            f"<div class='badge'>img</div>",
            unsafe_allow_html=True
        )

def card(title: str, desc: str, github_url: str, app_url: str | None = None, image: str | None = None):
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        if image:
            safe_image(image, width=220)
        st.markdown(f"<h3>{title}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p>{desc}</p>", unsafe_allow_html=True)
        colb1, colb2 = st.columns([1,1])
        with colb1:
            st.link_button("GitHub", github_url, use_container_width=True, type="secondary")
        with colb2:
            if app_url:
                st.link_button("Abrir app", app_url, use_container_width=True)
            else:
                st.markdown("<div class='small'>Añade la URL de Streamlit para mostrar este botón.</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ========== Inventario de proyectos ==========
# Puedes rellenar/actualizar las URLs de Streamlit cuando publiques cada app.
GH_BASE = "https://github.com/Amonsalvem"

projects = [
    # Columna 1
    dict(title="OCR", repo="OCR",
         desc="Reconocimiento óptico de caracteres. Extrae texto desde imágenes/fotos.",
        app=None, img="ocr.png"),
    dict(title="ctrl_voice", repo="ctrl_voice",
         desc="Control por voz vía navegador → comandos MQTT (‘voice_alejandro’).",
         app=None, img="voice.png"),
    dict(title="sistemas_iot", repo="sistemas_iot",
         desc="Panel IoT: telemetría y control con MQTT/Streamlit.",
         app=None, img="iot.png"),

    # Columna 2
    dict(title="vision_app", repo="vision_app",
         desc="Análisis de imagen con modelos multimodales (gpt-4o).",
         app=None, img="vision.png"),
    dict(title="Yolov5", repo="Yolov5",
         desc="Detección de objetos en tiempo real con YOLOv5.",
         app=None, img="yolo.png"),
    dict(title="antexttt", repo="antexttt",
         desc="Análisis básico de texto: TF-IDF, similitud y visualizaciones.",
         app=None, img="nlp.png"),

    # Columna 3
    dict(title="Textblobadvance", repo="Textblobadvance",
         desc="Sentiment + traducción (TextBlob) con front minimal.",
         app=None, img="sentiment.png"),
    dict(title="tablero", repo="tablero",
         desc="‘Tablero de energías’: lienzo, color y estados emocionales.",
         app=None, img="tablero.png"),
    dict(title="oct_16", repo="oct_16",
         desc="Colección de utilidades y ejemplos (experimentos).",
         app=None, img="utils.png"),

    # Extras (segunda fila si quieres mostrarlos también)
    dict(title="historias", repo="historias",
         desc="Narrativas y prototipos de storytelling asistido por IA.",
         app=None, img="stories.png"),
    dict(title="Traductor", repo="Traductor",
         desc="Traducción rápida (enfoque práctico).",
         app=None, img="translate.png"),
    dict(title="textblob", repo="textblob",
         desc="Playground minimal con TextBlob (básico).",
         app=None, img="tb.png"),
    dict(title="ITV", repo="ITV",
         desc="Prototipos varios; base para iteraciones.",
         app=None, img="itv.png"),
    dict(title="Intro", repo="Intro",
         desc="Intro / boilerplate para apps.",
         app=None, img="intro.png"),
]

# ========== Render ==========
st.markdown("---")
st.subheader("Colección")

# distribuye en 3 columnas, en el mismo orden que en tus capturas
cols = st.columns(3)
for i, p in enumerate(projects):
    with cols[i % 3]:
        card(
            title=p["title"],
            desc=p["desc"],
            github_url=f"{GH_BASE}/{p['repo']}",
            app_url=p["app"],     # pon aquí la URL de Streamlit cuando la tengas
            image=p.get("img")    # nombre de imagen local opcional (no es obligatorio)
        )

st.markdown("---")
st.caption("Tip: para que el botón “Abrir app” aparezca, edita este archivo y agrega la URL de tu despliegue en Streamlit Cloud a la clave `app` de cada proyecto.")
