# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

**Nhóm:** `TLiet` · **Lớp:** VinUni L3B

> **Gate 2a chỉ xem xét kế hoạch pilot**, không phê duyệt triển khai diện rộng. Dữ liệu LogiX-VN, chi phí và thời gian nhân viên trong bài là **simulated**. Không có nhóm đối chứng đồng thời trong đợt chạy thử.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| **1 · Chi phí mỗi việc thành công** | CPS **4.472 đ/việc**; **978/1.200** thành công; tổng **4.373.585 đ**, gồm review/rework **simulated** | Giả lập | FinOps Engineer |
| **2 · Ba yếu tố nhạy nhất** | Làm lại ×2: **+51,77%**; xem lại ×2: **+40,70%**; lương +25%: **+23,12%** (simulated) | Giả lập | Product Owner |
| **3 · So với nhân viên tự làm** | Baseline **12.000 đ/yêu cầu**; cả hệ thống **5.865 đ/yc = 0,49×**; phạm vi pilot cộng cố định **4.599 đ = 0,38×** (`noi_dia` **2.696 đ**, `hang_nang` **8.221 đ**); loại `quoc_te` **22.515 đ = 1,88×** và `doi_tac` **10.215 đ = 0,85×** (`simulated`) | Giả lập | Product Owner |
| **4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn** | Chính **994/1.200 = 82,83%**; bỏ gợi ý **48/177 = 27,12%**; mở lại **51/1.200 = 4,25%**. Đợt chạy thử **không chứng minh cải thiện so với đối chứng** | Xong, có bằng chứng | Data Analyst |
| **5 · Bảng lỗi và cách khắc phục** | Gắn nhãn độc lập **20 ca/5 loại**, đồng thuận **20/20 = 100%**; đặc tả khắc phục **5 ca** đủ event, ngưỡng, tần suất và vai trò phụ trách | Xong, có bằng chứng | QA Lead |
| **6 · Pilot plan** | Phạm vi `noi_dia` + `hang_nang`; chia ngẫu nhiên theo `staff` (**20 + 20 cụm**, phân tầng theo depot); **MDE 6 điểm** (`n = 859` hiệu dụng/nhóm, `m ≥ 299` yc/người, `DE = 6,96`; power **0,64** ở mức +5 điểm); rollout `10/25/50%`, **3 luật dừng** | Xong, có bằng chứng | Giám đốc vận hành |
| **7 · Rủi ro kinh tế** | Đã đề xuất ≥2 rủi ro có số: làm lại ×2 **+51,77%**; xem lại ×2 **+40,70%**; xem lại 100% lên **11.743–12.415 đ** (`0,98–1,03×` baseline, `simulated`) | Giả lập | FinOps Engineer |

**Đề xuất: GO CÓ ĐIỀU KIỆN – chỉ trình Gate 2a xem xét kế hoạch pilot.**

1. **Kỹ sư trưởng agent**, trước ngày bắt đầu pilot: bổ sung khoá chống trùng (`idempotency_key`) và đối soát sổ cái tự động cho ca lỗi 7 & 20 (ngưỡng 0 ca báo hoàn thành công khi sổ cái lỗi). **Ngày kiểm tra đề xuất: 2026-12-01.**
2. **Giám đốc vận hành**, trước khi mở bước rollout `0.10`: ký xác nhận chấp nhận đánh đổi **MDE = 6 điểm** (lực kiểm định **0,64** nếu tác động thật chỉ là +5 điểm), phê duyệt 3 luật dừng và diễn tập tắt cờ rollback **≤ 15 phút**. **Ngày kiểm tra đề xuất: 2026-12-04.**
3. **Data Analyst**, trước ngày chạy pilot: bật đủ 9 event có `trace_id`, khoá seed chia ngẫu nhiên phân tầng 20 + 20 nhân viên và thay số phút `simulated` bằng thời gian xem lại/làm lại đo thật ngay sau tuần 1. **Ngày kiểm tra đề xuất: 2026-12-04.**
4. **Trưởng nhóm CSKH & Product Owner**, cuối bước rollout `0.25`: áp dụng lộ trình giảm tỉ lệ xem lại theo bậc khi tỉ lệ `sua + bo < 15%` (vì xem lại 100% làm CPS lên **11.743–12.415 đ**, `simulated`), giữ loại `quoc_te` và `doi_tac` ngoài pilot. **Ngày kiểm tra đề xuất: 2026-12-14.**

**Lý do:** Phạm vi pilot hẹp có CPS thấp hơn baseline trong dữ liệu giả lập, nhưng xét toàn bộ mẫu thì review/rework là chi phí chính; kịch bản review 100% có thể làm mất lợi thế. Tỉ lệ mở lại và sai tiền cần được giám sát, cùng nhóm đối chứng đồng thời. **Ngày kiểm tra trên là đề xuất**, không phải mốc đã được chấp thuận.

**Bằng chứng:** `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`.
