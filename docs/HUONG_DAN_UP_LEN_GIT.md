# Hướng dẫn up file lên GitHub (LVTN)

Repo GitHub: **https://github.com/YaneZuRii/LVTN.git**  
Thư mục chứa **toàn bộ file** trên máy: `E:\LVTN-temp-clone` (sau khi push xong có thể đổi tên thành `E:\LVTN`).

File đã nằm trong thư mục này và **đã commit** (lệnh `git push` chỉ là **gửi lên web**).

## Cấu trúc thư mục (1 folder chứa hết)

```text
LVTN-temp-clone/
├── README.md
├── database/          ← SQL + PHP
├── docs/              ← tài liệu (file này)
├── vsl/
│   ├── Text/label.csv ← nhãn 4362 video
│   ├── download_vsl_hf.py
│   └── demo_video_to_vector.py
└── .gitignore         ← không up video .mp4
```

Video `.mp4` **không** up lên Git — tải bằng `python vsl\download_vsl_hf.py`.

---

## Lỗi 403 “Permission denied to YaneZuRii”

Nguyên nhân: Windows đang lưu **mật khẩu/token GitHub cũ hoặc sai**.

### Bước 1 — Xóa credential cũ

1. Nhấn **Windows + R** → gõ: `control /name Microsoft.CredentialManager`
2. **Windows Credentials** (Thông tin xác thực Windows)
3. Tìm mục có chữ **git:https://github.com** hoặc **github.com**
4. **Remove** (Xóa)

### Bước 2 — Tạo token mới

1. Đăng nhập GitHub bằng tài khoản **YaneZuRii**
2. Vào: https://github.com/settings/tokens
3. **Generate new token (classic)**
4. Note: `LVTN-push`
5. Chọn quyền: **repo** (full control of private repositories)
6. **Generate token** → **copy** token (chỉ hiện 1 lần)

### Bước 3 — Push lại

Mở **PowerShell**:

```powershell
cd E:\LVTN-temp-clone
git push -u origin main
```

- **Username:** `YaneZuRii`
- **Password:** dán **token** (không dùng mật khẩu đăng nhập web)

Gõ đúng **`origin`** (không phải `orogin`).

---

## Cách 2 — Up bằng GitHub Desktop (dễ hơn)

1. Tải: https://desktop.github.com/
2. Đăng nhập account **YaneZuRii**
3. **File → Add local repository** → chọn `E:\LVTN-temp-clone`
4. Bấm **Publish repository** hoặc **Push origin**

---

## Cách 3 — Up từng file trên web (không dùng Git)

Nếu chỉ vài file nhỏ:

1. Vào https://github.com/YaneZuRii/LVTN
2. **Add file → Upload files**
3. Kéo thả file từ `E:\LVTN-temp-clone` (ví dụ `vsl\Text\label.csv`)

Không phù hợp upload hàng nghìn file — nên dùng **push** sau khi sửa token.

---

## Thêm file mới sau này

```powershell
cd E:\LVTN-temp-clone
copy D:\duong_dan\file_moi.txt database\
git add .
git commit -m "Them file moi"
git push
```