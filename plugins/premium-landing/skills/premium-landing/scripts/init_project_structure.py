#!/usr/bin/env python3
"""Create the non-destructive Premium Landing input skeleton."""

from __future__ import annotations

import argparse
import os
from pathlib import Path


DIRECTORIES = (
    "_inputs/inbox",
    "_inputs/brand/logos",
    "_inputs/brand/fonts",
    "_inputs/brand/guidelines",
    "_inputs/brand-kit",
    "_inputs/integration-kit",
    "_inputs/media/images",
    "_inputs/media/video",
    "_inputs/media/3d",
    "_inputs/media/audio",
    "_inputs/content",
    "_inputs/references",
    "_inputs/legal",
    "deliverables/design-kit",
)

FILES = {
    "README.md": """# Proyecto web

- Brief: [`.premium-landing/brief.md`](.premium-landing/brief.md)
- Material original: [`_inputs/`](_inputs/)

## Operación

El agente documentará aquí los requisitos y comandos verificados para desarrollo, pruebas, build y despliegue cuando defina el stack.
""",
    "_inputs/README.md": """# Archivos de entrada

Dejá aquí los archivos recibidos del cliente. Cuando defina su uso, el agente los renombrará y moverá a su ubicación definitiva dentro del proyecto sin conservar una copia fuente duplicada.

- `inbox/`: opción más simple; podés dejar todo mezclado aquí y el agente lo clasificará.
- `brand/logos/`: logos e isotipos. Preferir SVG; agregar PNG en máxima resolución si existe.
- `brand/fonts/`: fuentes autorizadas y sus licencias.
- `brand/guidelines/`: manual de marca, colores, usos y restricciones.
- `brand-kit/`: paquete versionado generado por Logo Studio; no lo edites ni ordenes manualmente.
- `integration-kit/`: paquete funcional versionado generado por Backoffice Builder; no lo edites manualmente.
- `media/images/`: fotografías, renders, ilustraciones y capturas originales.
- `media/video/`: videos originales o masters, aunque todavía no estén comprimidos.
- `media/3d/`: modelos, escenas, texturas y materiales 3D.
- `media/audio/`: música, locuciones y efectos autorizados.
- `content/`: textos, propuestas, catálogos, PDFs y documentos del negocio.
- `references/`: URLs, capturas, Figma y notas sobre qué tomar de cada referencia.
- `legal/`: textos legales, políticas, condiciones y requisitos regulatorios.

No guardes contraseñas, tokens ni credenciales aquí. Si no tenés algún material, dejá su carpeta vacía: el agente seguirá adelante.
""",
    "_inputs/asset-notes.md": """# Activos y licencias

El agente mantendrá este registro durante el ordenamiento. Para cada activo debe indicar nombre recibido, ubicación actual, procedencia, derechos y uso efectivo.

| Nombre recibido | Ubicación actual | Uso | Procedencia | Licencia o propietario | Restricciones |
| --- | --- | --- | --- | --- | --- |
""",
    "_inputs/references/links.md": """# Referencias

Agregá una URL por línea y, si querés, indicá qué te interesa de ella.
""",
    "_inputs/content/notes.md": """# Información adicional

Podés dejar aquí cualquier texto o aclaración que deba conocer el agente.
""",
}


def safe_path(root: Path, relative: str) -> Path:
    path = root / relative
    resolved = path.resolve(strict=False)
    common = os.path.commonpath((str(root), str(resolved)))
    if os.path.normcase(common) != os.path.normcase(str(root)):
        raise ValueError(f"Path escapes project root: {relative}")
    return path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_root", help="Project directory to initialize")
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    if (root / ".logo-studio").exists():
        raise SystemExit(
            "Refusing shared root: Logo Studio already owns this directory. "
            "Use a dedicated landing module root."
        )
    root.mkdir(parents=True, exist_ok=True)

    created: list[str] = []
    preserved: list[str] = []
    for relative in DIRECTORIES:
        path = safe_path(root, relative)
        if path.exists():
            if not path.is_dir():
                raise NotADirectoryError(f"Expected directory: {path}")
            preserved.append(relative)
        else:
            path.mkdir(parents=True)
            created.append(relative + "/")

    for relative, content in FILES.items():
        path = safe_path(root, relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            if not path.is_file():
                raise IsADirectoryError(f"Expected file: {path}")
            preserved.append(relative)
        else:
            path.write_text(content, encoding="utf-8")
            created.append(relative)

    print(f"Project root: {root}")
    print("Created: " + (", ".join(created) if created else "nothing"))
    print("Preserved: " + (", ".join(preserved) if preserved else "nothing"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
