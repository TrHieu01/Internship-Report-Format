# FCJ Workshop Template (Hugo)

Repo này là một website **Hugo** (theme `hugo-theme-learn`) dùng để viết báo cáo thực tập / internship report (song ngữ EN/VI).

## Yêu cầu

- **Hugo Extended** (Windows/amd64): kiểm tra bằng `hugo version` (phải có `+extended`).
- Có thể tải nhanh  **Hugo Extended** bằng lệnh sau: winget install Hugo.Hugo.Extended

## Chạy local

Mở PowerShell và `cd` vào thư mục repo (nơi có `config.toml`), ví dụ:

```powershell
.\fcj-workshop-template-main
```

Chạy:

```powershell
hugo server -D
```

Mở: `http://localhost:1313/`

## Chỉnh nội dung

Nội dung nằm trong `content/` (Markdown). Mỗi mục thường có 2 bản:
- `_index.md` (English)
- `_index.vi.md` (Tiếng Việt)

Các file hay chỉnh:

- Trang thông tin chính:
  - `content/_index.md`
  - `content/_index.vi.md`
- Worklog theo tuần:
  - `content/1-Worklog/**/_index.md`
  - `content/1-Worklog/**/_index.vi.md`
- Ảnh đại diện:
  - `static/images/avatar.png` (đúng đường dẫn trong `content/_index*.md`)


## Build (xuất bản)

Chạy:

```powershell
hugo
```

Output nằm trong thư mục `public/`.


### Đã bỏ hẳn mục BlogsTranslated khỏi site

### Khung “Warning” trong template

Repo đã có override shortcode `notice` để **không render** loại `warning`:

- `layouts/shortcodes/notice.html`

Nếu muốn hiện lại warning, bạn có thể chỉnh file này theo nhu cầu.
