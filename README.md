# LVTN

Luận văn / đồ án: dữ liệu ký hiệu ngôn ngữ ký hiệu Việt Nam (VSL) + script xử lý + CSDL mẫu LTDD.

## Cấu trúc

| Thư mục | Nội dung |
|---------|----------|
| `vsl/` | Script tải dataset SignConnect, demo video → vector, `Text/label.csv` (4362 nhãn) |
| `database/` | File SQL + API PHP mẫu (thư viện sách, điện thoại) |
| `docs/` | Ghi chú nguồn dữ liệu và cách tải video |

## Video (không nằm trên Git)

File `.mp4` (~2,7 GB) **không** đẩy lên GitHub. Tải về máy:

```bash
pip install huggingface_hub opencv-python mediapipe numpy
python vsl/download_vsl_hf.py
```

Video lưu tại `vsl-signconnect/Videos/` (cấu hình trong script).

Nguồn gốc: [Lakeserl/SignConnect](https://huggingface.co/datasets/Lakeserl/SignConnect) (mirror QIPEDC / Kaggle VSL).

## Nhãn (label)

`vsl/Text/label.csv` — cột `VIDEO` + `LABEL` (tiếng Việt), 4362 dòng.