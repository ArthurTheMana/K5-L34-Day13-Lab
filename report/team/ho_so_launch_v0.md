# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

**Nhóm:** Bài làm cá nhân (chưa có nhóm duyệt chéo) · **Lớp:** VinUni L3B

> **Gate 2a chỉ xem xét kế hoạch pilot**, không phê duyệt triển khai diện rộng. Dữ liệu LogiX-VN, chi phí và thời gian nhân viên trong bài là **simulated**. Không có nhóm đối chứng đồng thời trong đợt chạy thử.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| **1 · Chi phí mỗi việc thành công** | CPS **4.472 đ/việc**; **978/1.200** thành công; tổng **4.373.585 đ**, gồm review/rework **simulated** | Giả lập | FinOps Engineer |
| **2 · Ba yếu tố nhạy nhất** | Làm lại ×2: **+51,77%**; xem lại ×2: **+40,70%**; lương +25%: **+23,12%** (simulated) | Giả lập | Product Owner |
| **3 · So với nhân viên tự làm** | Baseline **12.000 đ/yêu cầu**; `noi_dia` **2.696 đ/CPS**, `hang_nang` **8.221 đ/CPS**; `quoc_te` **22.515 đ/CPS**, cao hơn baseline (simulated) | Giả lập | Product Owner |
| **4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn** | Chính **994/1.200 = 82,83%**; bỏ gợi ý **48/177 = 27,12%**; mở lại **51/1.200 = 4,25%**. Đợt chạy thử **không chứng minh cải thiện so với đối chứng** | Giả lập | Data Analyst |
| **5 · Bảng lỗi và cách khắc phục** | **20 ca/5 loại**, 5 biện pháp đề xuất; **chưa có nhãn độc lập của người thứ hai** nên chưa được xác nhận đồng thuận ≥80% | Chưa | QA Lead |
| **6 · Pilot plan** | Chọn `noi_dia` + `hang_nang`; ngẫu nhiên theo request, đối chứng 50%; **1.250 request/nhóm** (theo `statsmodels`), 3 luật dừng, rollout 10/25/50% | Giả lập | Product Owner |
| **7 · Rủi ro kinh tế** | Đã đề xuất ≥2 rủi ro có số: làm lại ×2 **+51,77%**; xem lại ×2 **+40,70%**; cần theo dõi CPS và thời gian nhân viên (simulated) | Giả lập | FinOps Engineer |

**Đề xuất: GO CÓ ĐIỀU KIỆN – chỉ trình Gate 2a xem xét kế hoạch pilot.**

1. **QA Lead**, trước buổi duyệt Gate 2a: xác nhận bộ 20 nhãn bởi người đánh giá độc lập hoặc xin chấp thuận hình thức cá nhân; hoàn thiện kiểm tra 5 biện pháp khắc phục. **Ngày kiểm tra đề xuất: 2026-12-01.**
2. **Operations Lead**, trước khi bật pilot: kiểm tra các ngưỡng an toàn, đối soát hoàn tiền, quyền dừng và rollback (mục tiêu **≤15 phút**, phải diễn tập); giữ duyệt của nhân viên tại giai đoạn đầu. **Ngày kiểm tra đề xuất: 2026-12-04.**
3. **Data Analyst**, trước khi khóa kế hoạch pilot: xác nhận randomization 50/50, tránh spillover, đủ cỡ mẫu tối thiểu **1.250 mỗi nhóm**, cách theo dõi kết quả sau **7 ngày**, định nghĩa metric và event/`trace_id`. **Ngày kiểm tra đề xuất: 2026-12-04.**
4. **Product Owner**, tại Gate 2a: phê duyệt hoặc bác bỏ các stop rules dự thảo trong `pilot_plan.yaml`; không mở rộng sang `quoc_te` khi CPS còn **22.515 đ** và tỉ lệ thành công **27,3%**. **Ngày kiểm tra đề xuất: 2026-12-04.**

**Lý do:** Phạm vi pilot hẹp có CPS thấp hơn baseline trong dữ liệu giả lập, nhưng xét toàn bộ mẫu thì review/rework là chi phí chính; kịch bản review 100% có thể làm mất lợi thế. Tỉ lệ mở lại và sai tiền cần được giám sát, cùng nhóm đối chứng đồng thời. **Ngày kiểm tra trên là đề xuất**, không phải mốc đã được chấp thuận.

**Bằng chứng:** `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`.
