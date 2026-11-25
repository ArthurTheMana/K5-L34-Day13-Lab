# Team

## Thông tin nhóm

- Tên nhóm: `TLiet` *(cập nhật tên nhóm không dấu)*
- Lớp: `L3B` *(đổi thành `L3A` nếu học lớp sáng/L3A)*
- Repo nhóm: `K5-L3B-DAY13-TLiet-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/ArthurTheMana/K5-L3B-DAY13-TLiet-LaunchEconomics` · nhánh `main`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
| 1 | `Nguyễn Tài Minh Huy` | `2A203603828` | `nguyentaiminhhuy831975@gmail.com` | `ArthurTheMana` | Người viết code (CP1, CP2) |
| 2 | `<Thành viên 2>` | `<MSSV_2>` | `<Email_2>` | `<GitHub_2>` | Người kiểm số & viết code (CP4) |
| 3 | `Cao Phạm Tân Khải` | `2A202603883` | `cptkhai@gmail.com` | `capkhai` | Người gắn nhãn 1 (CP3) |
| 4 | `Vũ Văn Bình` | `2A202603831` | `binhvuvan2004@gmail.com` | `hnib1908` | Người gắn nhãn 2, kiêm giữ hồ sơ (CP3, CP5) |

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

## `2A202603831-VuVanBinh`

### Phần việc phụ trách

- Phụ trách lượt gắn nhãn thứ hai ở CP3 và giữ hồ sơ ở CP5, gồm hồ sơ launch, báo cáo nhóm và phiếu duyệt chéo.

### Đóng góp cụ thể

- Rà soát 20 nhãn hiện có theo nhãn tham khảo và kiểm tra bảng khắc phục các ca 9, 7, 18, 4 và 17 về tín hiệu phát hiện, ngưỡng, tần suất và vai trò phụ trách.
- Đối chiếu số liệu rủi ro kinh tế ở E2 với kết quả B4 và đề xuất Go có điều kiện trong hồ sơ launch.

### Bằng chứng

- [Báo cáo cá nhân](report/team/2A202603831_VuVanBinh.md), [bảng lỗi](report/team/bang_loi.md), [bảng chi phí](report/team/bang_chi_phi.md) và [hồ sơ launch](report/team/ho_so_launch_v0.md).

## 2A202603828-NguyenTaiMinhHuy

### Phần việc phụ trách

- Người viết code chính giai đoạn đầu, phụ trách Nhiệm vụ A (CP1) và Nhiệm vụ B (CP2).
- Thiết lập môi trường Python, kiểm thử dữ liệu đầu vào và đối chiếu kết quả chạy `src/lab13.py`.

### Đóng góp cụ thể

- Cài đặt 3 hàm kinh tế chạy lại ở A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), đạt 3 phép thử đáp án biết trước (1,20 · 1,25 · 1,25).
- Xây dựng hàm `mo_hinh` ở A2, tính chi phí token, tool, chạy lại, xem lại và làm lại từ dữ liệu trace; xác định CPS là 4.472 đ cho 978 yêu cầu thành công.
- Phân tích A3 theo 4 loại yêu cầu (`noi_dia`, `hang_nang`, `quoc_te`, `doi_tac`), tính tỷ lệ thành công, số lần chạy trung bình và CPS của từng loại.
- Thực hiện A4, phân bổ chi phí cố định 40 triệu đ/tháng cho hai kịch bản 45.000 và 22.500 yêu cầu/tháng.
- Hoàn thành 9 kịch bản độ nhạy B1, kịch bản kết hợp B2 và phân tích chi phí toàn hệ thống theo giới hạn số lần chạy ở B3.
- Xây dựng kịch bản B4 xem lại 100%, sử dụng giả định simulated 5 phút xem lại và 9 phút làm lại; tính CPS là 11.743 đ.
- Tổng hợp và kiểm tra kết quả Nhiệm vụ A và B trong báo cáo chi phí, đồng thời sử dụng AI để hỗ trợ viết code, giải thích công thức và rà soát kết quả.

### Bằng chứng

- Code và kết quả thực thi trong `src/lab13.py`.
- Bảng số liệu và phân tích trong `report/team/bang_chi_phi.md`.
- Commit GitHub: `faad1b1` trên nhánh `main`.
