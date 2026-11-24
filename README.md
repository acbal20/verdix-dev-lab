# VERDIX DEV LAB

Catálogo inteligente de herramientas para desarrollo del ecosistema VERDIX.
Funciona sin conexión: abre `web/index.html` o visita `/devlab/` en el sitio VERDIX.

## Qué incluye

- 60 fichas en `catalog/tools.json` (web, backend, datos, seguridad, móvil, diseño e IA).
- Búsqueda por texto y filtros por categoría, plan gratuito, open source e IA.
- Comparador lado a lado y recomendador que prioriza opciones gratuitas y de código abierto.
- Fichas con fuente y fecha; las no verificadas se marcan explícitamente como ⚠.

## Uso

```bash
python3 -m pytest tests/ -q   # 9 invariantes: ids únicos, URLs https, fechas, alternativas
```

Para añadir o actualizar una herramienta, edita `catalog/tools.json` con id sin
espacios, descripción en español, fuente `https://` y fecha ISO. Solo marca
`verified: true` cuando hayas comprobado la fuente oficial ese mismo día.

La guía completa está en `docs/MANUAL_ES.md`; la política de seguridad en
`SECURITY.md`.
