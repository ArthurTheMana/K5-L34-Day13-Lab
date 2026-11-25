# Team

## Thông tin nhóm

- Tên nhóm: `TLiet` *(cập nhật tên nhóm không dấu)*
- Lớp: `L3B` *(đổi thành `L3A` nếu học lớp sáng/L3A)*
- Repo nhóm: `K5-L3B-DAY13-TLiet-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/ArthurTheMana/K5-L3B-DAY13-TLiet-LaunchEconomics` · nhánh `main`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
| 1 | `<Thành viên 1>` | `<MSSV_1>` | '<Email_1>' | `ArthurTheMana` | Người viết code (CP1, CP2) |
| 2 | `<Thành viên 2>` | `<MSSV_2>` | `<Email_2>` | `<GitHub_2>` | Người kiểm số & viết code (CP4) |
| 3 | `Cao Phạm Tân Khải` | `2A202603883` | `cptkhai@gmail.com` | `capkhai` | Người gắn nhãn 1 (CP3) |
| 4 | `<Thành viên 4>` | `<MSSV_4>` | `<Email_4>` | `<GitHub_4>` | Người gắn nhãn 2, kiêm giữ hồ sơ (CP3, CP5) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở nhiệm vụ C.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở nhiệm vụ C.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng `report/team/MSSV_HoTen.md` (giữ nguyên file mẫu).

---

## `<HoVaTen_1>-<MSSV_1>`

### Phần việc phụ trách

- Người viết code chính giai đoạn đầu (Nhiệm vụ A và Nhiệm vụ B).
- Thiết lập môi trường Python, kiểm thử dữ liệu đầu vào và đối chiếu kết quả chạy `src/lab13.py`.

### Đóng góp cụ thể

- Cài đặt 3 hàm kinh tế chạy lại ở A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) đạt 3 phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`).
- Xây dựng hàm `mo_hinh` ở A2, tách chi phí theo 4 loại yêu cầu kèm tỉ lệ `ok` qua từng `attempt` ở A3, phân bổ chi phí cố định 40 triệu đ/tháng ở A4 và chạy 9 kịch bản độ nhạy B1, kịch bản kết hợp B2, chi phí cả hệ thống B3, kịch bản xem lại 100% B4.

### Bằng chứng

- Code và output thực thi trong `src/lab13.py`; số liệu trong `report/team/bang_chi_phi.md`.

---

## `<HoVaTen_2>-<MSSV_2>`

### Phần việc phụ trách

- Người kiểm số (Nhiệm vụ A, B) và nhận vai viết code sau giờ giải lao (Nhiệm vụ D).
- Kiểm tra chéo nhãn `simulated`, công thức cỡ mẫu cụm và điều kiện dừng an toàn.

### Đóng góp cụ thể

- Tính tay kiểm chứng CPS gốc (`4.373.585 ÷ 978 = 4.472 đ`, `simulated`), chi phí cả hệ thống (`5.865 đ/yêu cầu = 0,49×`) và điền hoàn chỉnh `report/team/bang_chi_phi.md`.
- Viết phần tính cỡ mẫu D1a–D1e bằng `statsmodels` (`NormalIndPower`), tính `design_effect = 6,96` ở `m = 299`, lực kiểm định thực tế `64,17%` ở mức `+5 điểm` và tỉ lệ mở lại `4,25%` (`3,97%` phạm vi pilot); hoàn thiện `report/team/pilot_plan.yaml`.

### Bằng chứng

- Phần tính cỡ mẫu trong `src/lab13.py`, bảng đối chiếu trong `report/team/bang_chi_phi.md` và kế hoạch `report/team/pilot_plan.yaml`.

---

## `2A202603883-CaoPhamTanKhai`

### Phần việc phụ trách

- Người gắn nhãn 1 (Nhiệm vụ C) và đặc tả chỉ số, danh sách event (Nhiệm vụ E1).
- Theo dõi checklist điều kiện hoàn thành của từng nhiệm vụ.

### Đóng góp cụ thể

- Đọc độc lập 20 tình huống lỗi, gắn bộ nhãn Người 1 theo 5 nhóm Google PAIR dựa trên nguyên nhân gốc, đối chiếu đồng thuận và đúc kết 4 quy tắc phân biệt các ca dễ nhầm.
- Tính thử 3 chỉ số trên 1.200 yêu cầu (`82,83% · 27,12% · 4,25%`), đề xuất 2 chỉ số bổ sung và thiết kế schema event có `trace_id` trong `report/team/chi_so.md`.

### Bằng chứng

- Cột Nhãn người 1 và mục quy tắc phân biệt trong `report/team/bang_loi.md`; mục E1 và bảng event trong `report/team/chi_so.md`.

---

## `<HoVaTen_4>-<MSSV_4>`

### Phần việc phụ trách

- Người gắn nhãn 2 (Nhiệm vụ C) kiêm giữ hồ sơ xuyên suốt buổi (`ho_so_launch_v0.md`, `group_report.md`, `phieu_cham.md`).

### Đóng góp cụ thể

- Gắn độc lập bộ nhãn Người 2 cho 20 ca lỗi, cùng nhóm đặc tả bảng khắc phục 5 ca đại diện (Ca `9, 7, 18, 4, 17`) với đầy đủ event, ngưỡng, tần suất và vai trò phụ trách.
- Tổng hợp bảng rủi ro kinh tế E2, biên tập trang tổng hợp 7 mục `report/team/ho_so_launch_v0.md` với đề xuất `GO CÓ ĐIỀU KIỆN` kèm 4 điều kiện có mốc kiểm tra, và hoàn thiện `report/team/group_report.md`.

### Bằng chứng

- Cột Nhãn người 2 và bảng khắc phục 5 ca trong `report/team/bang_loi.md`; mục E2 trong `report/team/chi_so.md`; `report/team/ho_so_launch_v0.md` và `report/team/group_report.md`.
