# Nguồn dữ liệu

## 1. Video VSL + label

| Mục | Chi tiết |
|-----|----------|
| Nguồn | Hugging Face `Lakeserl/SignConnect` |
| Bản quyền / license | MIT (theo README dataset) |
| Số video | 4362 |
| Nhãn | `vsl/Text/label.csv` (ID, VIDEO, LABEL) |
| Lưu trên Git | Chỉ `label.csv` + script; video tải local |

**Tải toàn bộ video + label.csv:**

```powershell
cd vsl
python download_vsl_hf.py
```

**Xem nhãn của một file:** mở CSV, tìm cột `VIDEO` (ví dụ `D0002.mp4`) → cột `LABEL`.

## 2. CSDL mẫu LTDD (web)

| File | Database | Mô tả |
|------|----------|-------|
| `database/thuvien_db.sql` | `thuvien_db` | Sách, đăng nhập thẻ |
| `database/dienthoai_db.sql` | `dienthoai_db` | Điện thoại, người dùng |
| `database/sach_get.php`, `sach_post.php` | API thư viện | GET JSON / thao tác sách |
| `database/dienthoai_get.php`, `dienthoai_post.php` | API điện thoại | GET JSON / thao tác |

Nguồn export: phpMyAdmin (host 127.0.0.1), bài ôn LTDD trên máy phát triển.

**Tải dữ liệu trên web (sau khi deploy PHP + MySQL):**

- `sach_get.php?action=getall` → JSON toàn bộ sách  
- `dienthoai_get.php?action=getall` → JSON điện thoại  

(Thay URL bằng đường dẫn server thực tế.)

## 3. Repo GitHub

- URL: https://github.com/YaneZuRii/LVTN.git  
- Clone: `git clone https://github.com/YaneZuRii/LVTN.git`