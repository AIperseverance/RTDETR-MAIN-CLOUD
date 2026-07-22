"""Train the SOEP-MFM-FreqP4 experiment without changing the existing train.py."""

from pathlib import Path
import warnings

from ultralytics import RTDETR
from ultralytics.utils.torch_utils import init_seeds


warnings.filterwarnings("ignore")

PROJECT_ROOT = Path(__file__).resolve().parent
MODEL_CFG = PROJECT_ROOT / "ultralytics/cfg/models/rt-detr/rtdetr-SOEP-MFM-FreqP4.yaml"
PRETRAINED_WEIGHTS = "/home/waas/weights/rtdetr-r18.pt"
DATA_CFG = "/home/waas/datasets/data.yaml"


if __name__ == "__main__":
    init_seeds(0, deterministic=True)

    model = RTDETR(str(MODEL_CFG))
    model.load(PRETRAINED_WEIGHTS)
    model.train(
        data=DATA_CFG,
        cache=False,
        imgsz=640,
        epochs=300,
        batch=4,
        workers=4,
        optimizer="AdamW",
        seed=0,
        deterministic=True,
        amp=False,
        patience=30,
        project="/home/waas/results/train",
        name="exp_2026_07_23_rtdetr-SOEP-MFM-FreqP4_300epoch",
    )
