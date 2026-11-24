# Bảng lỗi và cách khắc phục · Nhiệm vụ C

**Nguồn:** `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, nhiệm vụ C, 20 ca (trang 4–5).

**Trạng thái:** Bản dự thảo có hỗ trợ AI để **một học viên** rà soát. Đây **không phải** hai bộ nhãn độc lập và **chưa đáp ứng** điều kiện đồng thuận của bài nhóm.

Năm loại theo Google PAIR trong đề: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Phân loại theo **nguyên nhân gốc**, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: **Học viên thực hiện một mình (cần tự kiểm tra và xác nhận bộ nhãn gợi ý)**.
Người gắn nhãn 2: **Chưa có; cần một thành viên/người đánh giá độc lập nếu muốn đáp ứng yêu cầu nhóm**.

| Ca | Nhãn người 1 (dự thảo AI, chờ xác nhận) | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Chưa có | Chưa xác định | Chờ đối chiếu |
| 2 | Hệ thống | Chưa có | Chưa xác định | Chờ đối chiếu |
| 3 | Ngữ cảnh | Chưa có | Chưa xác định | Chờ đối chiếu |
| 4 | Giới hạn hệ thống | Chưa có | Chưa xác định | Chờ đối chiếu |
| 5 | Ngầm | Chưa có | Chưa xác định | Chờ đối chiếu |
| 6 | Do người dùng | Chưa có | Chưa xác định | Chờ đối chiếu |
| 7 | Hệ thống | Chưa có | Chưa xác định | Chờ đối chiếu |
| 8 | Hệ thống | Chưa có | Chưa xác định | Chờ đối chiếu |
| 9 | Do người dùng | Chưa có | Chưa xác định | Chờ đối chiếu |
| 10 | Ngữ cảnh | Chưa có | Chưa xác định | Chờ đối chiếu |
| 11 | Giới hạn hệ thống | Chưa có | Chưa xác định | Chờ đối chiếu |
| 12 | Ngầm | Chưa có | Chưa xác định | Chờ đối chiếu |
| 13 | Giới hạn hệ thống | Chưa có | Chưa xác định | Chờ đối chiếu |
| 14 | Do người dùng | Chưa có | Chưa xác định | Chờ đối chiếu |
| 15 | Hệ thống | Chưa có | Chưa xác định | Chờ đối chiếu |
| 16 | Ngữ cảnh | Chưa có | Chưa xác định | Chờ đối chiếu |
| 17 | Ngầm | Chưa có | Chưa xác định | Chờ đối chiếu |
| 18 | Ngữ cảnh | Chưa có | Chưa xác định | Chờ đối chiếu |
| 19 | Giới hạn hệ thống | Chưa có | Chưa xác định | Chờ đối chiếu |
| 20 | Hệ thống | Chưa có | Chưa xác định | Chờ đối chiếu |

**Tỉ lệ đồng thuận:** Chưa tính được (chưa có bộ nhãn thứ hai). **Không được ghi 20/20 = 100%** dựa trên việc AI tự tạo cả hai cột.

## Giải thích ngắn gọn 20 nhãn đề xuất

| Ca | Vì sao chọn nhãn này? |
| --: | --- |
| 1 | Khách nhập sai số tài khoản (thiếu 2 chữ số). |
| 2 | Trợ lý gọi tool sai tham số hàng nặng, dẫn đến tính sai tiền. |
| 3 | Hệ thống hoàn về ví đúng thiết kế nhưng khách mong nhận qua ngân hàng. |
| 4 | Không có dữ liệu chặng do hãng nước ngoài vận chuyển; trợ lý báo không xử lý được. |
| 5 | Hoàn thừa tiền trong 14 đơn nhưng khách và hệ thống không phát hiện. |
| 6 | Khách chọn nhầm loại yêu cầu giao trễ dù sự cố là hàng vỡ. |
| 7 | API 503 nhưng trợ lý lại thông báo đã hoàn tiền thành công. |
| 8 | Trợ lý viện dẫn điều khoản không có trong chính sách hiện hành. |
| 9 | Khách nhập nhầm mã đơn thương mại điện tử thay cho mã vận đơn. |
| 10 | Chính sách bất khả kháng được áp dụng đúng, nhưng thông điệp cam kết 24 giờ khiến khách kỳ vọng khác. |
| 11 | Trợ lý không hỗ trợ đầu vào âm thanh. |
| 12 | Tool thiếu trường khiến token của depot D05 tăng gấp ba suốt 3 tuần nhưng không ai phát hiện. |
| 13 | Hoàn phí bảo hiểm của đối tác nằm ngoài phạm vi trợ lý; câu trả lời chung chung còn cần được khắc phục. |
| 14 | Khách bấm nhầm nút xác nhận đã nhận tiền. |
| 15 | Trợ lý tính 100% thay vì 50% theo chính sách; nhân viên bắt lỗi trước khi gửi. |
| 16 | Thông báo lúc 2:14 sáng đúng thiết kế nhưng trái kỳ vọng không bị làm phiền của khách. |
| 17 | Dữ liệu giá trong cache lỗi thời gây sai tiền ở 212 đơn mà không có phản hồi/cảnh báo. |
| 18 | Số tiền hoàn đúng nhưng thiếu lời giải thích cách tính khiến khách nghĩ bị hoàn thiếu. |
| 19 | Yêu cầu 14 tháng vượt khả năng truy cập dữ liệu 12 tháng. |
| 20 | Thiếu khóa chống trùng khiến một đơn bị hoàn tiền hai lần. |

## Quy tắc phân biệt và xử lý bất đồng

- **Do người dùng / Hệ thống:** Nếu dữ liệu hoặc thao tác khách nhập sai là nguyên nhân đầu tiên, chọn *Do người dùng*; nếu tool hoặc logic thực thi sai chính sách/thiết kế, chọn *Hệ thống*.
- **Hệ thống / Ngữ cảnh:** Nếu thực hiện sai quy tắc hiện hành, chọn *Hệ thống*; nếu thực hiện đúng thiết kế nhưng khách hiểu/kỳ vọng khác, chọn *Ngữ cảnh*.
- **Giới hạn hệ thống / Hệ thống:** Nếu ngoài dữ liệu, phạm vi hoặc kiểu đầu vào hỗ trợ, chọn *Giới hạn hệ thống*; việc không thông báo rõ giới hạn là vấn đề khắc phục thêm, không nhất thiết thay đổi nhãn nguyên nhân gốc.
- **Ngầm / Hệ thống:** Chọn *Ngầm* nếu tồn tại lỗi hoặc tác động bất lợi mà cả khách và cơ chế giám sát đều không phát hiện tại thời điểm xảy ra, như ca 5, 12, 17.
- **Các ca dễ bất đồng:** 8 (viện dẫn điều khoản không có), 12 (tốn chi phí âm thầm), 13 (vượt phạm vi nhưng thông báo chưa tốt), 17 (cache cũ nhưng không ai thấy). Thảo luận dựa vào *nguyên nhân gốc* và ghi lại nhãn cuối cùng sau khi có đánh giá thứ hai.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Các ngưỡng bên dưới là **đề xuất để pilot kiểm thử**, chưa phải ngưỡng chính thức hay sự kiện đã được đo trên dữ liệu thực tế.

| Ca | Loại lỗi | Phát hiện bằng gì (đo được) | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_account_validation_failed` khi tài khoản thiếu/sai độ dài; theo dõi tỉ lệ lỗi theo ngày | Kiểm tra định dạng trước khi tạo lệnh; yêu cầu khách sửa và xác nhận lại số tài khoản | Frontend Engineer |
| 2 | Hệ thống | Event `refund_amount_mismatch` khi số tiền Agent tính khác kết quả kiểm tra bằng rule theo loại hàng; chặn ngay khi chênh > 0 đ | Sửa mapping hàng nặng → tham số tool; thêm test hồi quy cho kiện 28 kg | Backend Engineer |
| 3 | Ngữ cảnh | Event `refund_channel_dispute` khi khách mở lại vì nhầm kênh nhận tiền; theo dõi số ca/tuần | Hiển thị rõ “hoàn về ví LogiX” và thời gian ước tính trước khi xác nhận | Product Owner |
| 4 | Giới hạn hệ thống | Event `external_carrier_data_missing`, đếm theo hãng/depot và cảnh báo nếu > 0 trường hợp chưa được chuyển nhân viên | Nói rõ dữ liệu không có; chuyển nhân viên kèm tóm tắt, không tự suy đoán trạng thái | Backend Engineer |
| 5 | Ngầm | Đối soát `refund_overpayment_detected` hằng ngày giữa tiền hoàn, giá sau mã giảm và sổ cái; cảnh báo nếu chênh > 0 đ | Thêm kiểm tra giá sau giảm trước chi tiền, đối soát và xử lý các khoản hoàn thừa | Finance Operations Lead |

## Việc còn cần xác nhận trước khi nộp

1. Học viên đọc lại 20 mô tả trong đề và tự xác nhận hoặc sửa bộ nhãn dự thảo.
2. Nếu lớp yêu cầu đúng quy trình nhóm: nhờ một người gắn nhãn **độc lập**, sau đó nhập nhãn của họ vào cột 2, tính `số ca trùng / 20 × 100%` và thống nhất nhãn cuối.
3. Nếu chỉ có một người, ghi rõ tình trạng **chưa đáp ứng yêu cầu hai người độc lập**, không báo cáo tỷ lệ đồng thuận không có thật.
4. Các ngưỡng/event trong bảng khắc phục là thiết kế đề xuất; cần đưa vào hệ thống giám sát nếu triển khai pilot.
