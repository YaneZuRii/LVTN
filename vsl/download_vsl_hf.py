"""Download VSL videos + label.csv from Hugging Face (SignConnect)."""
from pathlib import Path

from huggingface_hub import snapshot_download

ROOT = Path(__file__).resolve().parent
DEST = ROOT / "vsl-signconnect"
REPO = "Lakeserl/SignConnect"


def main() -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {REPO} -> {DEST}")
    print("Chi tai: Videos/*.mp4 va Text/label.csv")
    path = snapshot_download(
        repo_id=REPO,
        repo_type="dataset",
        local_dir=str(DEST),
        local_dir_use_symlinks=False,
        allow_patterns=["Videos/*.mp4", "Text/label.csv"],
    )
    videos = list((DEST / "Videos").glob("*.mp4")) if (DEST / "Videos").exists() else []
    label = DEST / "Text" / "label.csv"
    print("Done.")
    print(f"  local_dir: {path}")
    print(f"  videos: {len(videos)}")
    print(f"  label.csv exists: {label.is_file()}")


if __name__ == "__main__":
    main()