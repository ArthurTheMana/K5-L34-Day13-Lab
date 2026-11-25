# Báo cáo cá nhân - Nguyễn Tài Minh Huy - 2A202603828

## 1. Thông tin thành viên

- **Họ tên:** Nguyễn Tài Minh Huy
- **MSSV:** 2A202603828
- **Email:** nguyentaiminhhuy831975@gmail.com
- **Vai trong nhóm:** Người viết code, phụ trách Nhiệm vụ A (CP1) và Nhiệm vụ B (CP2)
- **Bài lab:** Day 13 - Launch Economics, trợ lý hoàn phí LogiX-VN

## 2. Phần việc phụ trách

Mình phụ trách phần lập trình và kiểm tra số liệu cho **Nhiệm vụ A - Mô hình chi phí (CP1)** và **Nhiệm vụ B - Phân tích độ nhạy (CP2)**. Công việc gồm thiết lập môi trường Python, hoàn thiện các hàm tính chi phí trong `src/lab13.py`, chạy thử với hai tập dữ liệu CSV của lab và tổng hợp kết quả vào `report/team/bang_chi_phi.md`.

## 3. Đóng góp cụ thể

### Nhiệm vụ A - Mô hình chi phí

- **A1:** Hoàn thiện ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong` và `he_so_chi_phi_moi_viec_thanh_cong`. Cả ba phép thử đáp án biết trước đều **ĐẠT**, cho kết quả **1,20; 1,25; 1,25**.
- **A2:** Xây dựng hàm `mo_hinh` để cộng chi phí token, tool, các lần chạy lại, thời gian nhân viên xem lại và làm lại. Với **1.200 yêu cầu**, kết quả gồm **978 yêu cầu thành công**, tổng chi phí **4.373.585 đ (simulated)** và **CPS 4.472 đ/việc thành công**. Chi phí chạy lại **93.804 đ** đã nằm trong token và tool, không cộng thêm lần thứ hai vào tổng.
- **A3:** Phân tích bốn loại yêu cầu: `noi_dia` có CPS **2.696 đ**; `hang_nang` **8.221 đ**; `quoc_te` **22.515 đ**; `doi_tac` **10.215 đ**. Kết quả cho thấy yêu cầu quốc tế chưa phù hợp để tự động hóa rộng rãi trong mô hình giả lập vì CPS vượt mức nhân viên tự xử lý **12.000 đ/yêu cầu**.
- **A4:** Phân bổ **40 triệu đ/tháng** chi phí cố định (giả định) cho phạm vi `noi_dia` và `hang_nang`. CPS sau phân bổ là **4.599 đ** với 45.000 yêu cầu/tháng và **5.784 đ** với 22.500 yêu cầu/tháng.

### Nhiệm vụ B - Phân tích độ nhạy

- **B1:** Tính chín kịch bản thay đổi giá token, chi phí xem lại, làm lại, lương nhân viên và giới hạn số lần chạy. Trong các kịch bản tăng chi phí đã khảo sát, làm lại gấp đôi khiến CPS tăng **51,77%**, xem lại gấp đôi tăng **40,70%**, còn giá token gấp đôi chỉ tăng **5,62%**.
- **B2:** Tính kịch bản giá token gấp đôi đồng thời chi phí xem lại gấp đôi: CPS **6.543 đ**, tăng **46,31%** so với mô hình cơ sở.
- **B3:** So sánh giới hạn chạy lại 1, 2 và 3 lần. Giới hạn **2 lần** có tổng chi phí toàn hệ thống thấp nhất trong ba kịch bản: **6.901.220 đ (simulated)**, dù giới hạn 1 lần có CPS Agent thấp hơn.
- **B4:** Kiểm tra giả định nhân viên xem lại 100% các yêu cầu chạy `ok` thuộc `noi_dia` và `hang_nang`, với **5 phút xem lại** và **9 phút làm lại** cho ca sai. Mô hình cho kết quả CPS **11.743 đ (simulated)**, gần mức baseline **12.000 đ**, cho thấy chi phí review/rework có thể làm giảm phần lớn lợi ích kinh tế.

## 4. Bằng chứng

- **Code:** `src/lab13.py`, gồm ba hàm kiểm tra A1, hàm `mo_hinh` và các kịch bản A2-B4.
- **Bảng tính và phân tích:** `report/team/bang_chi_phi.md`.
- **Kiểm tra thực thi:** `python lab13.py` in thông báo `Ba phép thử đáp án biết trước: ĐẠT` và các kết quả A, B đã nêu.
- **Git:** Commit nhóm `faad1b1` trên nhánh `main` với thông điệp `feat: complete Day 13 cost analysis and launch pilot reports`. Commit này là bằng chứng phiên bản repository, không dùng để khẳng định toàn bộ nội dung trong commit đều do một mình mình thực hiện.

## 5. Công cụ AI đã dùng

Mình sử dụng **ChatGPT** để hỗ trợ giải thích công thức số lần chạy kỳ vọng, gợi ý cấu trúc hàm Python, xử lý lỗi khi chạy code, đề xuất cách tính các kịch bản độ nhạy và rà soát nội dung báo cáo Markdown.

Mình tự chạy code trên môi trường Python cục bộ trong VS Code và PowerShell, đối chiếu ba phép thử A1 với đáp án biết trước (**1,20; 1,25; 1,25**), kiểm tra số liệu CPS và các kịch bản A-B bằng output chương trình, đồng thời dùng `git diff --check` để phát hiện và sửa lỗi định dạng trước khi commit. Các số liệu nhân sự và chi phí giả định được ghi nhãn **simulated**.

## 6. Tự đánh giá

Mình đã hoàn thành phần code và phân tích số liệu được phân công cho **CP1 (A1-A4)** và **CP2 (B1-B4)**. Qua bài lab, mình hiểu rõ hơn vì sao không thể chỉ dựa vào hóa đơn token để đánh giá hiệu quả Agent: chi phí nhân viên xem lại, làm lại và xử lý yêu cầu không thành công cũng ảnh hưởng đáng kể đến chi phí toàn hệ thống.

Điểm cần cải thiện là kiểm tra các giả định mô phỏng một cách chặt chẽ hơn, đặc biệt khi giới hạn retry hoặc thay đổi tỷ lệ review/rework. Kết quả trên dữ liệu giả lập chỉ hỗ trợ đề xuất cho pilot; chưa chứng minh hiệu quả khi vận hành thực tế.
