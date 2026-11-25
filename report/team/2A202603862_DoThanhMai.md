# Báo cáo cá nhân — Đỗ Thanh Mai — 2A202603862

## 1. Thông tin thành viên

- Họ tên: Đỗ Thanh Mai
- MSSV: `2A202603862`
- Email: `thanhmaido24@gmail.com`
- GitHub: `Laurent2526`
- Vai trò: Thành viên 2, kiểm số ở Nhiệm vụ A và B, phụ trách viết code tính cỡ mẫu ở CP4.

## 2. Phần việc phụ trách

Mình đối chiếu mô hình chi phí và các kịch bản giới hạn số lần chạy. Ở CP4, mình phụ trách phần tính cỡ mẫu D1a–D1e và kiểm tra các số liệu đầu vào cho kế hoạch pilot của trợ lý hoàn phí LogiX-VN.

## 3. Đóng góp cụ thể

- **A2 — Kiểm chi phí.** Chia tổng chi phí 4.373.585 đ cho 978 việc thành công được khoảng **4.472 đ/việc thành công** (`simulated`). Khi tính cả 222 yêu cầu chuyển sang cho nhân viên tự xử lý với giá 12.000 đ/yêu cầu, phép tính `(4.373.585 + 222 × 12.000) ÷ 1.200` cho khoảng **5.865 đ/yêu cầu** (`simulated`), bằng **0,49 lần** mức xử lý thủ công (`simulated`).
- **B3 — Kiểm giới hạn số lần chạy.** Cộng chi phí nhân viên xử lý các yêu cầu thất bại vào chi phí trợ lý ở từng kịch bản. Giới hạn 2 lần chạy cho chi phí cả hệ thống thấp nhất, **6.901.220 đ** (`simulated`). Giới hạn 1 lần chạy cho CPS thấp nhất, **4.111 đ/việc thành công** (`simulated`). Hai thước đo dẫn đến hai lựa chọn khác nhau vì chúng tính chi phí của các yêu cầu thất bại theo hai cách khác nhau.
- **D1 — Kiểm cỡ mẫu pilot.** Với 20 nhân viên mỗi nhóm và `ICC = 0,02`, cỡ mẫu hiệu dụng có giới hạn trên là `20 ÷ 0,02 = 1.000` mỗi nhóm. Mức cải thiện 5 điểm phần trăm cần khoảng 1.250 mẫu hiệu dụng mỗi nhóm. Kế hoạch chọn MDE 6 điểm phần trăm và đặt mục tiêu 859 mẫu hiệu dụng mỗi nhóm. Ở 299 yêu cầu mỗi nhân viên, hệ số thiết kế là `1 + (299 − 1) × 0,02 = 6,96` và cỡ mẫu hiệu dụng là `20 × 299 ÷ 6,96 ≈ 859,20`. Với thiết kế này, lực kiểm định ở mức cải thiện 5 điểm phần trăm vào khoảng 64%.
- **CP4 — Đối chiếu ngưỡng mở lại.** Tỉ lệ mở lại trong 7 ngày là **51/1.200 = 4,25%** toàn mẫu và **39/982 = 3,97%** trong phạm vi `noi_dia` và `hang_nang`. Ngưỡng dừng tuyệt đối 3% thấp hơn cả hai mức quan sát. Kế hoạch pilot dùng mức chênh từ 2 điểm phần trăm so với nhóm đối chứng đồng thời, kèm trần tuyệt đối 6%.

## 4. Bằng chứng

- Kết quả A2 và B3, gồm mẫu số tính CPS và chi phí của các yêu cầu do nhân viên xử lý. [Bảng chi phí](bang_chi_phi.md)
- Phép tính D1a–D1e, thông số chia cụm và luật dừng theo tỉ lệ mở lại. [Mã tính Lab 13](../../src/lab13.py) · [Kế hoạch pilot](pilot_plan.yaml)
- Phân công và tổng hợp đóng góp của Thành viên 2. [TEAM.md](../../TEAM.md)

## 5. Công cụ AI đã dùng

ChatGPT (Codex) hỗ trợ soạn báo cáo và đối chiếu các phép tính với mã nguồn, dữ liệu CSV và hồ sơ nhóm. Các phép tính ở mục 3 ghi rõ tử số, mẫu số hoặc hệ số thiết kế để có thể kiểm tra lại trực tiếp.

## 6. Tự đánh giá

Phép đối chiếu B3 giúp mình thấy rằng CPS có thể giảm khi giới hạn số lần chạy, trong khi tổng chi phí tăng vì nhân viên phải xử lý thêm yêu cầu thất bại. Khi giải thích phương án pilot, mình cần nêu rõ giả định `ICC = 0,02` và mức cải thiện nhỏ nhất thiết kế có đủ khả năng phát hiện, vì cả hai ảnh hưởng trực tiếp đến cách diễn giải kết quả.
