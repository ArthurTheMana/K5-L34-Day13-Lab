# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token (mọi lần chạy) | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool (5.600 lần gọi) | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | `attempt > 1` | đo từ trace |
| Xem lại (890 phút) | 1.780.000 | `phut_xem_lai_simulated` | `simulated` |
| Làm lại (1.132 phút) | 2.264.000 | `phut_lam_lai_simulated` | `simulated` |
| Tổng chi phí | 4.373.585 | token + tool + xem lại + làm lại | có phần `simulated` |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | `4.373.585 ÷ 978` | `simulated` |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | `(245.585 + 84.000) ÷ 1.200` | đo từ trace |

- Chi phí mỗi việc thành công **4.472 đ** (`simulated`) cao gấp **16,28 lần** hoá đơn token + tool bình quân **274,7 đ/yêu cầu** (đo từ trace). Khi cộng thêm 222 ca không thành công nhân viên phải làm thay (12.000 đ/ca), chi phí cả hệ thống là **5.865 đ/yêu cầu = 0,49×** baseline (`simulated`).
- Khoản lớn nhất là **làm lại** (**2.264.000 đ**, chiếm **51,77%** tổng chi phí, `simulated`), tiếp theo là **xem lại** (**1.780.000 đ**, chiếm **40,70%**, `simulated`); tổng giờ nhân viên chiếm **92,46%** chi phí (`simulated`).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: | ---: | ---: | ---: |
| `noi_dia` | 824 | 95,0% | 1,11 | 2.696 đ (`simulated`) | 0,22× (`simulated`) |
| `hang_nang` | 158 | 74,1% | 1,47 | 8.221 đ (`simulated`) | 0,69× (`simulated`) |
| `quoc_te` | 150 | 27,3% | 2,32 | 22.515 đ (`simulated`) | 1,88× (`simulated`) |
| `doi_tac` | 68 | 54,4% | 1,88 | 10.215 đ (`simulated`) | 0,85× (`simulated`) |

- **`quoc_te` không đáng để trợ lý xử lý**: CPS **22.515 đ = 1,88×** baseline (`simulated`), thành công chỉ **27,3%**. Chạy lại tới 3 lần không giúp vì tỉ lệ `ok` giảm mạnh qua từng lần thử (lần 1: **30,0%**, lần 2: **11,4%**, lần 3: **2,2%** — lỗi thiếu dữ liệu lặp lại trên cùng yêu cầu); `doi_tac` sát ngưỡng (**10.215 đ = 0,85×**, `simulated`) và có điều khoản riêng nên cũng loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (`simulated`) | 0,38× (`simulated`) |
| Một nửa khối lượng (22.500/tháng) | 16.875 | 2.370 đ | 5.784 đ (`simulated`) | 0,48× (`simulated`) |

- Cộng chi phí cố định 40 triệu đ/tháng vào CPS biến đổi phạm vi `noi_dia + hang_nang` (**3.414 đ**, `simulated`) cho **4.599 đ = 0,38×** ở 45.000 yêu cầu/tháng và **5.784 đ = 0,48×** (`simulated`) ở 22.500 yêu cầu/tháng (cố định tăng từ **1.185 đ** lên **2.370 đ/việc**), không đổi kết luận ở quy mô đầy đủ nhưng tăng mạnh khi sản lượng thấp.

## B1 · Đổi từng yếu tố

CPS gốc (A2) để đối chiếu: **4.472 đ** (`simulated`).

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (`simulated`) | Thay đổi (%) (`simulated`) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ (`simulated`) | +5,62% |
| Giá token giảm một nửa | 13 đ và 65 đ cho 1.000 token | 4.346 đ (`simulated`) | -2,81% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ (`simulated`) | +40,70% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ (`simulated`) | -20,35% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ (`simulated`) | +51,77% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ (`simulated`) | -25,88% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ (`simulated`) | +23,12% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có `attempt > 2`; yêu cầu có `so_lan_chay > 2` coi là `chuyen_nhan_vien` | 4.237 đ (`simulated`) | -5,25% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (`simulated`) | -8,07% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: CPS lên **6.543 đ** (`simulated`), tăng **+46,31%** so với **4.472 đ** (`simulated`), đúng bằng tổng hai tác động riêng (`+5,62% + 40,70%`) vì mô hình cộng tuyến tính trên cùng 978 việc thành công.
- Xếp hạng ba yếu tố tác động mạnh nhất: **1. Số ca làm lại** (`+51,77%` / `-25,88%`, `simulated`) · **2. Tỉ lệ xem lại** (`+40,70%` / `-20,35%`, `simulated`) · **3. Lương nhân viên** (`+23,12%`, `simulated`).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (`simulated`) | Số yêu cầu không thành công | Chi phí cả hệ thống (`simulated`) | Chi phí mỗi việc thành công (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (`simulated`) | 319 | 7.449.781 đ (`simulated`) | 4.111 đ (`simulated`) |
| 2 lần | 4.093.220 đ (`simulated`) | 234 | **6.901.220 đ** (`simulated`) | 4.237 đ (`simulated`) |
| 3 lần | 4.373.585 đ (`simulated`) | 222 | 7.037.585 đ (`simulated`) | 4.472 đ (`simulated`) |

- **Giới hạn 2 lần chạy** có chi phí cả hệ thống rẻ nhất (**6.901.220 đ**, `simulated`), không trùng với giới hạn cho CPS thấp nhất là **1 lần chạy** (**4.111 đ**, `simulated`). Tối ưu riêng CPS ở mức 1 lần sẽ đẩy thêm **85 yêu cầu** sang nhân viên tự làm (12.000 đ/ca), làm tổng chi phí toàn hệ thống tăng lên **7.449.781 đ** (`simulated`).

## B4 · Nếu phải xem lại tất cả

- Phạm vi `noi_dia + hang_nang` (982 yêu cầu, 900 thành công, token + tool **224.513 đ**): xem lại 100% các yêu cầu có run `ok` (948 ca × 5 phút = **9.480.000 đ**) và làm lại 48 ca `lam_lai` × 9 phút (**864.000 đ**) làm CPS vọt lên **11.743 đ = 0,98×** baseline 12.000 đ (`simulated`); nếu tính theo trung bình dữ liệu **15,3 phút/ca** làm lại thì CPS lên tới **12.415 đ = 1,03×** (`simulated`), đắt hơn nhân viên tự làm (hoà vốn xem lại chỉ còn **≤ 5,1 phút** hoặc **≤ 4,8 phút**/yêu cầu), nên pilot bắt buộc phải kiểm chứng lộ trình giảm tỉ lệ xem lại.
