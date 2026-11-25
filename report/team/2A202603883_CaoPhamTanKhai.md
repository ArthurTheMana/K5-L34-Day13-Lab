# Báo cáo cá nhân — `Cao Phạm Tân Khải - 2A202603883`

> **Lưu ý trước khi nộp:** Đổi tên file này theo đúng định dạng `MSSV_HoTenKhongDau.md` (ví dụ `20241234_NguyenVanKhai.md`) và điền Họ tên, MSSV ở mục 1. File mẫu `MSSV_HoTen.md` được giữ nguyên.

## 1. Thông tin thành viên

- Họ tên: `Cao Phạm Tân Khải`
- MSSV: `2A2020603883`
- Email: `cptkhai@gmail.com`
- GitHub: `capkhai`
- Vai trong nhóm: **Người gắn nhãn 1** *(đọc đề, theo dõi điều kiện "Xong khi", gắn nhãn độc lập 20 ca lỗi ở Nhiệm vụ C và kiểm tra chéo chỉ số – event)*

## 2. Phần việc phụ trách

- Nghiên cứu đề bài gốc, ý nghĩa các cột dữ liệu và 6 công thức chuẩn trong `docs/du_lieu_va_cong_thuc.md`; kiểm soát 5 quy tắc bắt buộc và điều kiện **"Xong khi"** của cả 5 nhiệm vụ A–E.
- Đảm nhận vai **Người gắn nhãn 1** trong Nhiệm vụ C: đọc và phân loại độc lập toàn bộ 20 ca lỗi của trợ lý hoàn phí LogiX-VN theo khung 5 loại lỗi của Google PAIR.
- Phối hợp cùng Người gắn nhãn 2 đối chiếu độ đồng thuận, xây dựng bộ quy tắc phân biệt các ca dễ nhầm lẫn và đặc tả cơ chế phát hiện – khắc phục có thể đo lường được.
- Phối hợp kiểm tra chéo đặc tả chỉ số và danh sách event có `trace_id` ở Nhiệm vụ E1 (`report/team/chi_so.md`) để bảo đảm mọi chỉ số và cảnh báo lỗi đều đo được từ log hệ thống.

## 3. Đóng góp cụ thể

- **Phân loại độc lập 20 ca lỗi và xây dựng quy tắc phân biệt (`report/team/bang_loi.md`):**
  - Thực hiện gắn nhãn độc lập 20 tình huống lỗi dựa trên **nguyên nhân gốc** thay vì vị trí sửa lỗi, cho kết quả: **4 ca Do người dùng** (`1, 6, 9, 14`), **5 ca Hệ thống** (`2, 7, 8, 15, 20`), **4 ca Ngữ cảnh** (`3, 10, 16, 18`), **4 ca Giới hạn hệ thống** (`4, 11, 13, 19`) và **3 ca Ngầm** (`5, 12, 17`).
  - Đối chiếu với bộ nhãn độc lập của Người gắn nhãn 2 (đồng thuận `20/20 = 100%`, vượt ngưỡng yêu cầu `≥ 80%`) và viết 4 quy tắc phân biệt rõ ràng cho các ca ranh giới: phân biệt *Do người dùng* với *Hệ thống* ở ca 6, 9; *Giới hạn hệ thống* ở ca 13 dù câu trả lời còn chung chung; *Hệ thống* (lỗi đã lộ ra ở ca 8, 15) với *Ngầm* (lỗi hoàn thừa hoặc đội token âm thầm ở ca 5, 12, 17); và *Ngữ cảnh* ở ca 3, 10, 16, 18 khi số tiền đúng chính sách nhưng lệch kỳ vọng khách hàng.
  - Cùng nhóm hoàn thiện bảng khắc phục cho 5 ca đại diện (`9, 7, 18, 4, 17`), bảo đảm mỗi dòng đều có đủ: tên event kèm `trace_id`, ngưỡng kích hoạt bằng số, tần suất kiểm tra và duy nhất một vai trò chịu trách nhiệm.
- **Kiểm tra chéo hệ thống chỉ số – event (`report/team/chi_so.md`):**
  - Đối chiếu kết quả tính thử 3 chỉ số trên 1.200 yêu cầu (`82,83%` đóng trong 24 giờ và không mở lại sau 7 ngày; `27,12%` sửa/bỏ gợi ý `48/177`; `4,25%` mở lại trong 7 ngày) và bảo đảm diễn giải đúng nguyên tắc không suy diễn nhân quả khi chưa có nhóm đối chứng.
  - Đồng bộ danh sách 12 event có `trace_id` (`input_validation_failed`, `handoff_to_staff`, `refund_ledger_write`, `ticket_reopened`, `audit_sample_checked`, …) khớp trực tiếp với các cơ chế phát hiện lỗi ở Nhiệm vụ C.
- **Rà soát chất lượng hồ sơ theo điều kiện "Xong khi" (Nhiệm vụ A → E):**
  - Kiểm tra đầy đủ nhãn `simulated` trên mọi con số tính từ `phut_xem_lai_simulated` và `phut_lam_lai_simulated` trong `bang_chi_phi.md`, `chi_so.md`, `pilot_plan.yaml` và `ho_so_launch_v0.md`.
  - Soát giới hạn độ dài câu trả lời (≤ 3 dòng, có số liệu), kiểm tra không còn ký tự `?` trong `pilot_plan.yaml`, đủ 3 luật dừng theo cấu trúc 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` và không xuất hiện từ cấm trong toàn bộ hồ sơ Gate 2a.

## 4. Bằng chứng

- **Bảng lỗi và khắc phục:** [`report/team/bang_loi.md`](bang_loi.md) (mục 1 — cột `Nhãn người 1`, mục 2 — *Quy tắc phân biệt cho các ca dễ lẫn*, mục 3 — *Bảng khắc phục cho 5 ca*).
- **Đặc tả chỉ số & event:** [`report/team/chi_so.md`](chi_so.md) (bảng E1 và bảng 12 event có `trace_id`).
- **Kiểm soát điều kiện hoàn thành trên toàn bộ hồ sơ:** [`report/team/bang_chi_phi.md`](bang_chi_phi.md), [`report/team/pilot_plan.yaml`](pilot_plan.yaml), [`report/team/ho_so_launch_v0.md`](ho_so_launch_v0.md) và lịch sử commit trên repo nhóm `K5-L3B-DAY13-TLiet-LaunchEconomics` (`faad1b1`, `a200bdc`, `29d797f`).

## 5. Công cụ AI đã dùng

- **Công cụ sử dụng:** Trợ lý AI tích hợp trong IDE (Antigravity / Gemini) và ChatGPT.
- **Mục đích sử dụng:**
  - Tra cứu và làm rõ ranh giới khái niệm giữa 5 nhóm lỗi của Google PAIR (*People + AI Guidebook*, chương *Errors + Graceful Failure*).
  - Hỗ trợ biên tập câu chữ ngắn gọn (≤ 3 dòng/ý), đồng bộ tên trường event có `trace_id` giữa `bang_loi.md` và `chi_so.md`, và rà soát checklist định dạng YAML/Markdown.
- **Cách tự kiểm tra kết quả:**
  - Tự đọc trực tiếp từng tình huống trong 20 ca lỗi của đề bài và đặt câu hỏi truy tìm nguyên nhân gốc (ai tạo ra sai lệch đầu tiên, hệ thống làm đúng hay sai thiết kế, lỗi đã lộ diện hay hoàn toàn âm thầm) để xác nhận từng nhãn thay vì phụ thuộc vào gợi ý tự động.
  - Chạy trực tiếp `python lab13.py` trong thư mục `src/` để kiểm chứng độc lập toàn bộ các con số kinh tế và cỡ mẫu (`CPS = 4.472 đ`, `5.865 đ/yc`, `B4 = 11.743 đ / 12.415 đ`, `D1e: m = 299, DE = 6,96, power = 64,17%`, tỉ lệ mở lại `4,25%` toàn mẫu và `3,97%` trong phạm vi pilot).
  - Chạy lệnh `yaml.safe_load` để xác minh `pilot_plan.yaml` hợp lệ, kiểm tra không còn dấu `?` và quét toàn bộ thư mục `report/team/` để bảo đảm tuân thủ tuyệt đối các quy tắc của bài lab.

## 6. Tự đánh giá

- **Mức độ hoàn thành:** Hoàn thành tốt và đầy đủ vai trò Người gắn nhãn 1 cũng như nhiệm vụ rà soát chất lượng, tính nhất quán của toàn bộ bộ hồ sơ launch v0.
- **Nhận thức rút ra qua bài lab:**
  - Hiểu rõ sự khác biệt giữa hoá đơn token/tool (`274,7 đ/yêu cầu`) và chi phí thật mỗi việc thành công (`4.472 đ` `simulated`, gấp `16,28 lần`) do chi phí thời gian xem lại và làm lại của nhân viên chiếm tới `92,46%`; đồng thời thấy rõ vì sao tối ưu cục bộ CPS (1 lần chạy) lại làm tăng tổng chi phí cả hệ thống so với giới hạn 2 lần chạy (`7.449.781 đ` so với `6.901.220 đ` `simulated`).
  - Nắm vững nguyên tắc phân loại lỗi theo nguyên nhân gốc, đặc biệt là nhóm lỗi **Ngầm** (ca 5, 12, 17) — loại lỗi nguy hiểm về tài chính nhưng không thể phát hiện qua khiếu nại khách hàng mà bắt buộc phải thiết kế kiểm toán mẫu định kỳ (`audit_sample_checked`) và giám sát chi phí theo depot.
  - Hiểu bản chất giới hạn cỡ mẫu hiệu dụng khi phân cụm theo nhân viên (`c / ICC = 1.000` mẫu/nhóm với 40 nhân viên) và tầm quan trọng của việc trình bày minh bạch điểm bất lợi (`power = 0,64` ở mức `+5 điểm` khi chọn `MDE = 6 điểm`) trước hội đồng Gate 2a.
