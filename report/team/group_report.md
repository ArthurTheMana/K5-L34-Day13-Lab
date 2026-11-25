# Báo cáo nhóm · Day 13 — Launch Economics

Báo cáo tóm tắt kết quả mô phỏng cho trợ lý hoàn phí LogiX-VN. Số liệu chi tiết và phương pháp tính nằm trong các file hồ sơ liên kết bên dưới. **Tất cả dữ liệu LogiX-VN là dữ liệu giả lập (simulated)**; đây là đề xuất cho Gate 2a, không phải quyết định triển khai chính thức.

## 1. Thông tin nhóm

- Tên nhóm: `<TenNhom>` *(cập nhật tên nhóm khớp với `TEAM.md`)*
- Lớp: `L3B` *(cập nhật nếu thuộc `L3A`)*
- Thành viên: Xem danh sách chi tiết, vai trò và đóng góp trong [`TEAM.md`](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Mục tiêu là đánh giá liệu trợ lý hoàn phí có đáng được thử nghiệm tiếp, loại yêu cầu nào phù hợp, rủi ro khi trợ lý thất bại và cách thiết kế pilot có đối chứng. Nhóm sử dụng 1.200 yêu cầu và 1.624 lần chạy trong hai CSV do bài lab cung cấp; dùng `src/lab13.py` tính CPS (chi phí trên mỗi việc thành công), phân tích độ nhạy và cỡ mẫu. Các chi phí nhân viên dựa trên cột `_simulated` luôn được ghi nhãn **simulated**.

## 3. Giải pháp

- **A — Mô hình chi phí:** Kiểm tra ba phép thử đáp án biết trước, tổng hợp token/tool trên mọi lần chạy (kể cả lỗi), cộng chi phí xem lại/làm lại **simulated**, so sánh bốn loại yêu cầu và chi phí cố định. Xem [`bang_chi_phi.md`](bang_chi_phi.md).
- **B — Độ nhạy:** Thay từng biến giá token, chi phí nhân sự, giới hạn retry; so tổng chi phí cả hệ thống thay vì chỉ CPS của Agent. B4 sử dụng giả định riêng: review 5 phút cho yêu cầu có run `ok` và rework 9 phút cho ca `lam_lai`. Xem [`bang_chi_phi.md`](bang_chi_phi.md).
- **C — Phân loại lỗi:** Hai thành viên gắn nhãn độc lập 20 tình huống theo năm loại của Google PAIR (đồng thuận **20/20 = 100%**), ghi quy tắc phân biệt các ca dễ lẫn và đặc tả khắc phục 5 ca đại diện có event, ngưỡng, tần suất và một vai trò chịu trách nhiệm. Xem [`bang_loi.md`](bang_loi.md).
- **D — Pilot:** Tính cỡ mẫu cho ba cách chia, chọn chia ngẫu nhiên phân tầng theo nhân viên (`staff`, 20 + 20 cụm) để tách sạch tác động, chấp nhận đánh đổi MDE = 6 điểm (`n = 859` hiệu dụng/nhóm, `m ≥ 299` yêu cầu/người, `DE = 6,96`), thiết lập 3 luật dừng 4 vế và cơ chế rollback ≤ 15 phút. Xem [`pilot_plan.yaml`](pilot_plan.yaml).
- **E — Quyết định launch:** Đặc tả chỉ số, event có `trace_id`, rủi ro kinh tế và hồ sơ Gate 2a. Xem [`chi_so.md`](chi_so.md) và [`ho_so_launch_v0.md`](ho_so_launch_v0.md).

## 4. Kết quả

- **Chi phí:** Tổng **4.373.585 đ** (có phần `simulated`), **978/1.200** yêu cầu thành công, CPS **4.472 đ** (`simulated`); chi phí cả hệ thống **5.865 đ/yêu cầu = 0,49×** baseline (`simulated`). Chi phí xem lại **1.780.000 đ** (`simulated`) và làm lại **2.264.000 đ** (`simulated`) chiếm **92,46%** tổng chi phí.
- **Phạm vi:** `noi_dia` có CPS **2.696 đ** (`0,22×`, `simulated`), thành công **95,0%**; `hang_nang` **8.221 đ** (`0,69×`, `simulated`), **74,1%**. Loại `quoc_te` (**22.515 đ = 1,88×**, thành công **27,3%**, `simulated`) và `doi_tac` (**10.215 đ = 0,85×**, điều khoản riêng, `simulated`) khỏi pilot.
- **Độ nhạy:** Nhân đôi chi phí làm lại làm CPS tăng **+51,77%**; nhân đôi chi phí xem lại tăng **+40,70%** (`simulated`). Ở B3, giới hạn **2 lần chạy** cho tổng chi phí hệ thống thấp nhất (**6.901.220 đ**, `simulated`). Ở B4, xem lại 100% làm CPS lên **11.743 đ = 0,98×** (với 9 phút làm lại) hoặc **12.415 đ = 1,03×** (với 15,3 phút trung bình dữ liệu, `simulated`).
- **Chỉ số thử:** Đóng trong 24 giờ và không mở lại **994/1.200 = 82,83%**; sửa/bỏ gợi ý **48/177 = 27,12%**; mở lại trong 7 ngày **51/1.200 = 4,25%** (**3,97%** trong phạm vi pilot). Các tỷ lệ này **không chứng minh Agent cải thiện** vì thiếu nhóm đối chứng đồng thời.
- **Cỡ mẫu pilot:** Chia theo yêu cầu cần **1.250 yêu cầu/nhóm** nhưng tràn tác động cao; chia theo nhân viên với 40 người có trần hiệu dụng **1.000 mẫu/nhóm** (`ICC = 0,02`), không đủ cho MDE 5 điểm. Nhóm chọn chia theo `staff` (**20 + 20 cụm**) với **MDE = 6 điểm** (`859` mẫu hiệu dụng/nhóm, tối thiểu **299 yêu cầu/nhân viên**, `DE = 6,96`; power ở mức +5 điểm là **0,64**).
- **Đề xuất Gate 2a:** **Go có điều kiện** cho *kế hoạch pilot* phạm vi `noi_dia` và `hang_nang`, chỉ sau khi khoá chống trùng sổ cái (ca 7, 20), ký chấp nhận đánh đổi MDE 6 điểm (power 0,64 ở mức +5 điểm), diễn tập rollback ≤ 15 phút và bật đủ event có `trace_id` để đo thời gian nhân viên thật.

## 5. Khó khăn và cách xử lý

Môi trường mới clone chưa có `.venv` và PowerShell mặc định chặn script kích hoạt; nhóm xử lý bằng `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` hoặc dùng trực tiếp Python 3.11 đã đủ thư viện. Ở A3 và B4, để tránh kết luận cảm tính về chạy lại hoặc bỏ sót rủi ro thời gian làm lại thực tế cao hơn giả định, nhóm bổ sung code tính tỉ lệ `ok` theo `attempt` và độ nhạy B4 ở mức `15,3 phút/ca` (`12.415 đ = 1,03×`, `simulated`). Ở nhiệm vụ D, do 40 nhân viên bị chặn trần hiệu dụng `1.000 mẫu/nhóm` (`ICC = 0,02`), nhóm chọn chia theo `staff` (20 + 20 cụm) với `MDE = 0,06` và ghi rõ điểm bất lợi power `0,64` ở mức `+5 điểm`.

## 6. Tổng hợp đóng góp

Nhóm phân công theo đúng bốn vai của buổi lab (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ) và luân phiên người viết code ở nửa sau buổi để nhiều thành viên trực tiếp chạy mô hình trên `src/lab13.py`. Mọi con số trong hồ sơ đều được kiểm chứng lại từ output của `src/lab13.py` và đối chiếu chéo giữa các file báo cáo; chi tiết đóng góp từng cá nhân được khai báo tại [`TEAM.md`](../../TEAM.md) và các file `MSSV_HoTen.md`.

## 7. Hạn chế và hướng cải thiện

Toàn bộ dữ liệu hiện tại là **simulated**, chưa có nhóm đối chứng đồng thời và chưa đo thời gian xem lại/làm lại thật của nhân viên CSKH. Việc chấp nhận `MDE = 6 điểm` để giữ thiết kế 20 + 20 cụm theo nhân viên làm giảm lực kiểm định xuống `0,64` nếu tác động thật chỉ đạt `+5 điểm`. Khi bước vào pilot, cần thay thế ngay số phút `simulated` sau tuần 1, kiểm toán mẫu 100 đơn/tuần để bắt lỗi ngầm (như ca 5, 17), giám sát nhiễm chéo trong cùng depot và tuân thủ nghiêm ngặt 3 luật dừng đã khoá trước.

## 8. Tài liệu tham khảo

- [`src/lab13.py`](../../src/lab13.py), [`src/logix_runs.csv`](../../src/logix_runs.csv), [`src/logix_requests.csv`](../../src/logix_requests.csv).
- [`bang_chi_phi.md`](bang_chi_phi.md), [`bang_loi.md`](bang_loi.md), [`pilot_plan.yaml`](pilot_plan.yaml), [`chi_so.md`](chi_so.md), [`ho_so_launch_v0.md`](ho_so_launch_v0.md).
- `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` — hướng dẫn và yêu cầu chính thức của Lab 13.
