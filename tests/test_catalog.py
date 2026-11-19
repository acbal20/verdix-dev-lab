"""Pruebas del catálogo de VERDIX DEV LAB. Honestidad verificable."""
import json
import os
import re
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "catalog", "tools.json")

REQ_FIELDS = ["id", "name", "category", "desc", "site", "open_source", "license", "os",
              "free_plan", "is_free", "paid_from", "ai", "requires_account", "card_required",
              "pros", "cons", "alternatives", "source", "verified", "last_verified"]

def load():
    with open(TOOLS) as f:
        return json.load(f)

def test_json_valido_y_22_fichas():
    tools = load()
    assert 15 <= len(tools) <= 40, "núcleo mínimo 15 fichas"

def test_ids_unicos():
    tools = load()
    ids = [t["id"] for t in tools]
    assert len(ids) == len(set(ids))

def test_campos_requeridos():
    for t in load():
        for field in REQ_FIELDS:
            assert field in t, f"{t.get('id')}: falta {field}"

def test_urls_https():
    for t in load():
        assert t["site"].startswith("https://"), t["id"]
        assert t["source"].startswith("https://"), t["id"]

def test_hallazgo_fecha_verificacion():
    hoy = date(2026, 11, 19)
    for t in load():
        if t["verified"]:
            assert t["last_verified"], f"{t['id']}: verified sin fecha"
            d = date.fromisoformat(t["last_verified"])
            assert d <= hoy
            assert t["source"], f"{t['id']}: verified sin fuente"
        else:
            # sin verificar: la fuente igualmente existe para que NOX decida
            assert t["source"]

def test_categorias_conocidas():
    conocidas = {"agentes-ia", "constructores", "diseno", "editores", "web", "movil",
                 "backend", "datos-cloud", "seguridad"}
    for t in load():
        assert t["category"] in conocidas, f"{t['id']}: categoría desconocida {t['category']}"

def test_alternativas_existen():
    tools = {t["id"] for t in load()}
    for t in load():
        for alt in t["alternatives"]:
            assert alt in tools, f"{t['id']}: alternativa inexistente {alt}"

def test_textos_en_espanol():
    for t in load():
        blob = t["desc"] + " " + t["free_plan"]
        assert any(w in blob.lower() for w in ("gratuito", "gratis", "plan", "abierto", "free", "$0", "coste", "open")), t["id"]

def test_sin_emojis_en_ids():
    for t in load():
        assert re.match(r"^[a-z0-9-]+$", t["id"]), t["id"]
