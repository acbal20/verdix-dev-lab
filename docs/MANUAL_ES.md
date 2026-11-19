# Manual — VERDIX DEV LAB

## Qué es
Catálogo inteligente de herramientas para devs: fichas con fuente y fecha, búsqueda,
comparador lado a lado y recomendador. Prioridad: código abierto y planes gratuitos.

## Cómo usarlo
1. Abre `web/index.html` (o el sitio VERDIX/⟶ Dev Lab) — funciona sin conexión.
2. Busca por texto (`agente`, `APK`, `open source`) o filtra por categoría / gratis / OSS / IA.
3. Pulsa una tarjeta para ver la ficha completa (ventajas, desventajas, fuente).
4. Marca dos o más con "+ comparar" y pulsa Comparar.
5. Usa el Recomendador (¿qué construyes? / presupuesto / máquina) — siempre prefiere gratis.

## Interpretar las fichas
- ✓ Verificada AAAA-MM-DD: datos confirmados con fuente oficial o comparación independiente en esa fecha.
- ⚠ Sin verificar: candidata razonable, NO confirmada — verifica tú antes de depender de ella.
- "Plan gratis" describe el tier gratuito tal como se publica en la fuente citada.

## Añadir o actualizar una herramienta
1. Edita `catalog/tools.json`: añade el objeto (id sin espacios, español, fuente https, fecha ISO).
2. Ejecuta `python3 -m pytest tests/ -q` — valida 9 invariantes (ids únicos, URLs https, fechas, alternativas existentes).
3. Si verificas manualmente, pon `verified: true` y `last_verified` con HOY; si no, `false`.
