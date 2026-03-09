from flask import Flask, render_template, send_from_directory
from pathlib import Path

app = Flask(
    __name__,
    template_folder="src/apresentacao",
    static_folder="src/apresentacao"
)

APRESENTACAO_DIR = Path(__file__).parent / "src" / "apresentacao"


def get_paginas():
    """Retorna lista de HTMLs disponíveis na pasta apresentacao."""
    return [
        p.name for p in APRESENTACAO_DIR.glob("*.html")
        if p.name != "index.html"
    ]


@app.route("/")
def index():
    paginas = get_paginas()
    return render_template("index.html", paginas=paginas)


@app.route("/<pagina>")
def servir_pagina(pagina):
    return send_from_directory(APRESENTACAO_DIR, pagina)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
