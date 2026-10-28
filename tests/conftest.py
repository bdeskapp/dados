import shutil
import subprocess
import sys
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent

if str(RAIZ) not in sys.path:
    sys.path.insert(0, str(RAIZ))


@pytest.fixture
def site_construido(tmp_path) -> Path:
    # Site mínimo com a configuração real: o docs/ do repositório só é
    # construível depois da primeira sincronização (as próprias linkam espelhadas).
    raiz = tmp_path / "projeto"
    (raiz / "docs").mkdir(parents=True)
    modelo = (RAIZ / "sincronizacao" / "mkdocs.modelo.yml").read_text(encoding="utf-8")
    (raiz / "mkdocs.yml").write_text(
        "".join(l for l in modelo.splitlines(keepends=True) if "{{NAV_GERADO}}" not in l),
        encoding="utf-8",
    )
    shutil.copytree(RAIZ / "overrides", raiz / "overrides")
    (raiz / "docs" / "index.md").write_text("# Bdesk: Dados\n", encoding="utf-8")
    destino = tmp_path / "site"
    r = subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict", "-d", str(destino)],
        cwd=raiz,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        pytest.fail(f"mkdocs build --strict falhou:\n{r.stdout}\n{r.stderr}")
    return destino


@pytest.fixture
def fonte_sintetica(tmp_path) -> Path:
    destino = tmp_path / "repo-sintetico"
    shutil.copytree(RAIZ / "tests" / "fixtures" / "fonte", destino)
    return destino
