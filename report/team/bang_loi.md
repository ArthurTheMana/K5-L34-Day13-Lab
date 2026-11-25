# Bảng lỗi và cách khắc phục · Nhiệm vụ C

**Nguồn:** `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, nhiệm vụ C, 20 ca lỗi.

Năm loại lỗi theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**.
Quy tắc cốt lõi: **phân loại theo nguyên nhân gốc**, không phân loại theo chỗ cần sửa.

## 1. Hai bộ nhãn độc lập và tỉ lệ đồng thuận

- **Người gắn nhãn 1:** Thành viên 1 *(cập nhật họ tên & MSSV trong `TEAM.md`)*
- **Người gắn nhãn 2:** Thành viên 2 *(cập nhật họ tên & MSSV trong `TEAM.md`)*

| Ca | Tóm tắt tình huống | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | :---: | --- |
| 1 | Khách nhập số tài khoản thiếu 2 chữ số, ngân hàng trả lỗi | Do người dùng | Do người dùng | Có | **Do người dùng** |
| 2 | Kiện 28 kg nhưng gọi tool tham số hàng thường, hoàn thiếu 45.000 đ | Hệ thống | Hệ thống | Có | **Hệ thống** |
| 3 | Thiết kế hoàn về ví LogiX 5 phút, khách chờ tài khoản ngân hàng | Ngữ cảnh | Ngữ cảnh | Có | **Ngữ cảnh** |
| 4 | Không có dữ liệu chặng hãng nước ngoài giao, báo rõ và chuyển nhân viên | Giới hạn hệ thống | Giới hạn hệ thống | Có | **Giới hạn hệ thống** |
| 5 | 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, không ai phát hiện | Ngầm | Ngầm | Có | **Ngầm** |
| 6 | Khách chọn mục "giao trễ" nhưng mô tả hàng vỡ, bị từ chối vì đúng hạn | Do người dùng | Do người dùng | Có | **Do người dùng** |
| 7 | API sổ cái lỗi 503 sau 3 lần thử nhưng vẫn báo khách đã hoàn thành công | Hệ thống | Hệ thống | Có | **Hệ thống** |
| 8 | Trợ lý viện dẫn "Điều 7.2" không tồn tại trong chính sách hiện hành | Hệ thống | Hệ thống | Có | **Hệ thống** |
| 9 | Khách nhập mã đơn sàn TMĐT thay vì mã vận đơn, trợ lý dừng không gợi ý | Do người dùng | Do người dùng | Có | **Do người dùng** |
| 10 | Từ chối hoàn do bão đúng chính sách, khách bức xúc vì app hiện cam kết 24h | Ngữ cảnh | Ngữ cảnh | Có | **Ngữ cảnh** |
| 11 | Khách gửi tin nhắn thoại 40 giây, trợ lý không xử lý được âm thanh | Giới hạn hệ thống | Giới hạn hệ thống | Có | **Giới hạn hệ thống** |
| 12 | Tool depot D05 thiếu trường làm chi phí token gấp 3 suốt 3 tuần không ai thấy | Ngầm | Ngầm | Có | **Ngầm** |
| 13 | Hỏi hoàn phí bảo hiểm đối tác (ngoài phạm vi), trợ lý trả lời chung chung | Giới hạn hệ thống | Giới hạn hệ thống | Có | **Giới hạn hệ thống** |
| 14 | Khách bấm nhầm "Xác nhận đã nhận tiền" khi chưa nhận nên yêu cầu đóng | Do người dùng | Do người dùng | Có | **Do người dùng** |
| 15 | Đơn trễ 26h, chính sách hoàn 50% nhưng tính 100%, nhân viên bắt được | Hệ thống | Hệ thống | Có | **Hệ thống** |
| 16 | Thiết kế gửi ngay khi xong nên nhắn Zalo lúc 2:14 sáng, khách bị làm phiền | Ngữ cảnh | Ngữ cảnh | Có | **Ngữ cảnh** |
| 17 | Cache giữ bảng giá cũ cho đơn < 2 kg, lệch 212 đơn trong 9 ngày không ai biết | Ngầm | Ngầm | Có | **Ngầm** |
| 18 | Hoàn đúng 15.000 đ (50% của 30.000 đ) nhưng không ghi cách tính, khách mở lại | Ngữ cảnh | Ngữ cảnh | Có | **Ngữ cảnh** |
| 19 | Đơn 14 tháng trước vượt giới hạn dữ liệu 12 tháng, chuyển nhân viên kèm tóm tắt | Giới hạn hệ thống | Giới hạn hệ thống | Có | **Giới hạn hệ thống** |
| 20 | Khách gửi lại sau 10 phút, thiếu khoá chống trùng nên hoàn tiền hai lần | Hệ thống | Hệ thống | Có | **Hệ thống** |

- **Tỉ lệ đồng thuận:** **20 / 20 = 100%** (đạt yêu cầu ≥ 80%).
- **Tổng hợp theo loại:** Do người dùng: **4 ca** (1, 6, 9, 14) · Hệ thống: **5 ca** (2, 7, 8, 15, 20) · Ngữ cảnh: **4 ca** (3, 10, 16, 18) · Giới hạn hệ thống: **4 ca** (4, 11, 13, 19) · Ngầm: **3 ca** (5, 12, 17).

## 2. Quy tắc phân biệt cho các ca dễ lẫn

- **Do người dùng vs. Hệ thống (Ca 6, 9):** Nếu đầu vào hoặc lựa chọn ban đầu của khách đã sai (chọn nhầm mục giao trễ cho hàng vỡ, nhập mã sàn TMĐT thay mã vận đơn) thì nguyên nhân gốc là **Do người dùng**; việc trợ lý chưa biết gợi ý chuyển luồng nằm ở phần khắc phục.
- **Giới hạn hệ thống vs. Hệ thống (Ca 13):** Khi yêu cầu nằm ngoài phạm vi/dữ liệu/đầu vào hỗ trợ (bảo hiểm của đối tác ngoài phạm vi trợ lý) thì nguyên nhân gốc là **Giới hạn hệ thống**, kể cả khi câu trả lời từ chối hiện tại còn chung chung.
- **Hệ thống vs. Ngầm (Ca 8, 12, 15, 17):** Chọn **Hệ thống** khi lỗi sai thiết kế/chính sách đã lộ ra qua giao diện hoặc bước duyệt (trích dẫn điều khoản bịa đặt nhìn thấy được ở ca 8, nhân viên bắt được ở ca 15). Chỉ chọn **Ngầm** khi cả khách lẫn hệ thống giám sát đều không nhận ra cho tới khi kiểm tra mẫu hoặc rà chi phí (hoàn thừa âm thầm ca 5, đội token 3 tuần ca 12, lệch tiền do cache cũ ca 17).
- **Ngữ cảnh vs. Hệ thống (Ca 3, 10, 16, 18):** Chọn **Ngữ cảnh** khi trợ lý thực thi đúng thiết kế và đúng số tiền chính sách, nhưng giả định ngầm về kỳ vọng/thông tin của khách không khớp thực tế (thiếu diễn giải phép tính `30.000 đ × 50% = 15.000 đ` ở ca 18, gửi thông báo lúc 2:14 sáng ở ca 16).

## 3. Bảng khắc phục cho 5 ca (mỗi loại một ca)

| Ca | Loại lỗi | Phát hiện bằng gì (event, ngưỡng, tần suất) | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (có `trace_id`) theo dõi hằng ngày; cảnh báo khi vượt **> 2% tổng yêu cầu/ngày** | Nhận diện định dạng mã đơn sàn TMĐT để tra chéo sang mã vận đơn; nếu không tra được thì hiển thị ảnh minh hoạ vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ giữa event thông báo khách và `refund_ledger_write` (`status == ok`) cùng `trace_id`; cảnh báo ngay ở ngưỡng **> 0 ca lệch** | Chỉ gửi thông báo "đã hoàn" sau khi sổ cái trả `ok`; nếu API 503 sau 3 lần thử thì báo "đang xử lý" và chuyển nhân viên kèm khoá chống trùng | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Event `ticket_reopened` nối `trace_id` với các đơn có số tiền hoàn đúng chính sách, tổng hợp hằng tuần; cảnh báo khi **> 1% đơn hoàn/tuần** mở lại vì thắc mắc số tiền | Cập nhật mẫu tin nhắn hoàn tiền luôn hiển thị công thức chi tiết (ví dụ: `30.000 đ × 50% = 15.000 đ`) và điều khoản áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu` (có `trace_id`) thống kê hằng ngày theo `loai`; cảnh báo khi **> 0 ca thiếu dữ liệu không chuyển nhân viên** | Giữ cơ chế thông báo rõ giới hạn dữ liệu kèm tóm tắt cho nhân viên; loại nhóm `quoc_te` (`22.515 đ = 1,88×` baseline, `simulated`) khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` (có `trace_id`) kiểm tra mẫu 100 đơn/tuần đối chiếu bảng giá hiện hành; cảnh báo khi **> 1% mẫu lệch số tiền** | Tự động xoá cache ngay khi phát hành bảng giá mới, ghi `pricing_version` vào mọi `trace_id` và đối soát bù/thu hồi phần chênh | Kế toán trưởng |
