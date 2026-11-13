import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASETS_DIR = PROJECT_ROOT / "Datasets"
SENTIMENT_DATASET_PATH = PROJECT_ROOT / "vader_sentiment_dataset.csv"


def get_chroma_db_path() -> Path:
    configured_path = os.environ.get("GACHA_CHROMA_PATH")
    if configured_path:
        return Path(configured_path).expanduser().resolve()

    project_path = PROJECT_ROOT / "chromadb"
    legacy_path = PROJECT_ROOT.parent / "chromadb"

    if project_path.exists():
        return project_path
    if legacy_path.exists():
        return legacy_path
    return project_path
