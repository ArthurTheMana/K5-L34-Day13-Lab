# Báo cáo nhóm · Day 13 — Launch Economics

Báo cáo tóm tắt kết quả mô phỏng cho trợ lý hoàn phí LogiX-VN. Số liệu chi tiết và phương pháp tính nằm trong các file hồ sơ liên kết bên dưới. **Tất cả dữ liệu LogiX-VN là dữ liệu giả lập (simulated)**; đây là đề xuất cho Gate 2a, không phải quyết định triển khai chính thức.

## 1. Thông tin nhóm

- Tên nhóm: *Chưa cập nhật.*
- Lớp: *Chưa xác nhận trong báo cáo này.*
- Thành viên: *Tạm để trống; sẽ cập nhật trong `TEAM.md` khi cần.*

## 2. Mục tiêu và cách tiếp cận

Mục tiêu là đánh giá liệu trợ lý hoàn phí có đáng được thử nghiệm tiếp, loại yêu cầu nào phù hợp, rủi ro khi trợ lý thất bại và cách thiết kế pilot có đối chứng. Nhóm sử dụng 1.200 yêu cầu và 1.624 lần chạy trong hai CSV do bài lab cung cấp; dùng `src/lab13.py` tính CPS (chi phí trên mỗi việc thành công), phân tích độ nhạy và cỡ mẫu. Các chi phí nhân viên dựa trên cột `_simulated` luôn được ghi nhãn **simulated**.

## 3. Giải pháp

- **A — Mô hình chi phí:** Kiểm tra ba phép thử đáp án biết trước, tổng hợp token/tool trên mọi lần chạy (kể cả lỗi), cộng chi phí xem lại/làm lại **simulated**, so sánh bốn loại yêu cầu và chi phí cố định. Xem [`bang_chi_phi.md`](bang_chi_phi.md).
- **B — Độ nhạy:** Thay từng biến giá token, chi phí nhân sự, giới hạn retry; so tổng chi phí cả hệ thống thay vì chỉ CPS của Agent. B4 sử dụng giả định riêng: review 5 phút cho yêu cầu có run `ok` và rework 9 phút cho ca `lam_lai`. Xem [`bang_chi_phi.md`](bang_chi_phi.md).
- **C — Phân loại lỗi:** Đề xuất nhãn cho 20 tình huống thuộc năm loại; xác định cách phát hiện có thể đo, hành động khắc phục và vai trò chịu trách nhiệm. **Chưa có bộ nhãn độc lập thứ hai hoặc tỷ lệ đồng thuận được xác nhận.** Xem [`bang_loi.md`](bang_loi.md).
- **D — Pilot:** Tính cỡ mẫu, chọn chia ngẫu nhiên theo từng yêu cầu và lập kế hoạch có đối chứng đồng thời, luật dừng, rollback và nguy cơ ảnh hưởng chéo. Xem [`pilot_plan.yaml`](pilot_plan.yaml).
- **E — Quyết định launch:** Đặc tả chỉ số, event có `trace_id`, rủi ro kinh tế và hồ sơ Gate 2a. Xem [`chi_so.md`](chi_so.md) và [`ho_so_launch_v0.md`](ho_so_launch_v0.md).

## 4. Kết quả

- **Chi phí:** Tổng **4.373.585 đ**, **978/1.200** yêu cầu thành công, CPS **4.472 đ**; chi phí xem lại **1.780.000 đ simulated** và làm lại **2.264.000 đ simulated** chiếm phần lớn tổng chi phí.
- **Phạm vi:** `noi_dia` có CPS **2.696 đ**, tỷ lệ thành công **95,0%**; `hang_nang` **8.221 đ**, **74,1%**. `quoc_te` có CPS **22.515 đ** và tỷ lệ thành công **27,3%**, không phù hợp mở rộng pilot hiện tại.
- **Độ nhạy:** Nhân đôi chi phí làm lại làm CPS tăng **51,77%**; nhân đôi chi phí xem lại tăng **40,70%**. Trong mô phỏng B3, giới hạn **2 lần chạy** cho tổng chi phí hệ thống thấp nhất: **6.901.220 đ**. B4 có CPS **11.743 đ simulated**, sát baseline nhân viên **12.000 đ**.
- **Chỉ số thử:** Đóng trong 24 giờ và không mở lại **994/1.200 = 82,83%**; sửa/bỏ gợi ý **48/177 = 27,12%**; mở lại trong 7 ngày **51/1.200 = 4,25%**. Các tỷ lệ này **không chứng minh Agent cải thiện** vì thiếu nhóm đối chứng đồng thời.
- **Cỡ mẫu pilot:** Khoảng **1.250 yêu cầu/nhóm** khi chia theo yêu cầu; cách chia theo nhân viên cần khoảng **42 người/nhóm**, vượt quá 40 nhân viên hiện có. Phương án request-level cần giám sát nguy cơ spillover.
- **Đề xuất Gate 2a:** **Go có điều kiện** cho *kế hoạch pilot* phạm vi `noi_dia` và `hang_nang`, chỉ sau khi xác nhận luật dừng, đối soát số tiền hoàn, rollback và đo đầy đủ chi phí review/rework. **Chưa có kết quả hội đồng duyệt chéo**, không ghi nhận đã được thông qua.

## 5. Khó khăn và cách xử lý

Môi trường PowerShell ban đầu chặn kích hoạt `.venv`; đã điều chỉnh chính sách cho phiên làm việc và cài đúng dependency. Ba hàm A1 ban đầu thiếu triển khai; đã sửa, chạy đủ ba phép thử và xác nhận kết quả. Lúc xử lý B4, kết quả đầu dùng thời gian xem lại trung bình từ CSV; đã thay bằng giả định 5/9 phút theo đề. Git phát hiện lỗi whitespace; đã sửa và chạy lại `git diff --check` cùng `python lab13.py`.

## 6. Tổng hợp đóng góp

Bài hiện được thực hiện cá nhân với hỗ trợ AI cho giải thích, gợi ý code và soạn thảo. Các kết quả số đã được chạy và kiểm tra trên môi trường Python của người thực hiện; việc xác nhận nhãn độc lập và đánh giá chéo **chưa thực hiện**. Thông tin thành viên và phân công chính thức sẽ được bổ sung riêng vào `TEAM.md` nếu cần.

## 7. Hạn chế và hướng cải thiện

Dữ liệu là **simulated**; chưa có thử nghiệm đối chứng hoặc đo thời gian thật của nhân viên. Cần xác minh độc lập 20 nhãn lỗi, kiểm tra số tiền hoàn bằng đối soát, thử rollback, theo dõi event/trace_id, đánh giá ảnh hưởng chéo giữa treatment/control và chốt ngưỡng dừng trước pilot. Không dùng CPS nhỏ hơn baseline làm bằng chứng duy nhất để mở rộng.

## 8. Tài liệu tham khảo

- [`src/lab13.py`](../../src/lab13.py), [`src/logix_runs.csv`](../../src/logix_runs.csv), [`src/logix_requests.csv`](../../src/logix_requests.csv).
- [`bang_chi_phi.md`](bang_chi_phi.md), [`bang_loi.md`](bang_loi.md), [`pilot_plan.yaml`](pilot_plan.yaml), [`chi_so.md`](chi_so.md), [`ho_so_launch_v0.md`](ho_so_launch_v0.md).
- `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` — hướng dẫn và yêu cầu chính thức của Lab 13.
