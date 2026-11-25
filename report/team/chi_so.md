# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

> **Nguồn:** `src/logix_requests.csv` (1.200 yêu cầu giả lập), `src/logix_runs.csv`, kết quả CP1–CP2 trong `report/team/bang_chi_phi.md`. Các trường `_simulated` là dữ liệu **simulated**; dữ liệu chạy thử **không có nhóm đối chứng**, vì vậy không thể kết luận Agent đã cải thiện chỉ số.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `sum((dong_trong_24h == 1) & (mo_lai_trong_7_ngay == 0)) / len(reqs)` | **994 / 1.200 = 82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | `sum(quyet_dinh_xem_lai in {sua, bo}) / sum(duoc_xem_lai == 1)` | **48 / 177 = 27,12%** (41 sửa, 7 bỏ) |
| An toàn | Tỉ lệ lỗi lọt đến khách (proxy theo đề) | `sum(mo_lai_trong_7_ngay == 1) / len(reqs)` | **51 / 1.200 = 4,25%** |
| Dùng (đề xuất) | Tỉ lệ Agent được sử dụng khi đủ điều kiện | `count(eligible request được xử lý qua Agent) / count(eligible request được phân vào treatment)`; đo theo phân nhóm đã chỉ định, báo cáo riêng *assigned* và *used* | **Chưa có dữ liệu pilot; không tính từ mẫu hiện tại** |
| An toàn (đề xuất) | Tỉ lệ hoàn tiền sai được xác nhận | `count(request có lỗi số tiền xác nhận bởi đối soát) / count(request có kết quả hoàn đã đối soát)`; báo cáo theo `loai`, depot và nhóm thử nghiệm | **Chưa có event đối soát đầy đủ; chưa tính được** |

**Diễn giải:** Chỉ số trong đợt chạy thử là **82,83%**, không phải “trợ lý đã nâng chỉ số lên 82,83%”. Mốc baseline **70%** do đề bài cho là giả định phục vụ thiết kế pilot, không phải nhóm đối chứng đồng thời trong mẫu này. Tỉ lệ mở lại **4,25%** chỉ là *proxy* cho lỗi lọt đến khách; không phải mọi ca mở lại đều chứng minh Agent trả sai.

### Mã Python để đối chiếu (chạy trong `src/`)

```python
import pandas as pd
reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
primary = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).sum()
reviewed = (reqs['duoc_xem_lai'] == 1).sum()
overridden = reqs['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum()
reopened = (reqs['mo_lai_trong_7_ngay'] == 1).sum()
print(f'Chính: {primary}/{len(reqs)} = {primary/len(reqs):.2%}')
print(f'Dùng: {overridden}/{reviewed} = {overridden/reviewed:.2%}')
print(f'An toàn: {reopened}/{len(reqs)} = {reopened/len(reqs):.2%}')
```

## Danh sách event (thiết kế cho pilot)

Mỗi event cần có `event_id`, `event_time`, `request_id`, `trace_id`, `assignment_arm` (`control`/`treatment`), `depot`, `staff_id` khi áp dụng. Với nhóm đối chứng không gọi Agent, `trace_id` có thể là mã tương quan do hệ thống cấp lúc nhận yêu cầu; tuyệt đối không tự tạo trace Agent giả.

| Event | Ai tạo | Thuộc tính chính (ngoài trường chung) | Thời điểm |
| --- | --- | --- | --- |
| `request_assigned` | Experiment Service | `trace_id`, `eligible`, `assignment_arm`, `randomization_version` | Ngay lúc chia ngẫu nhiên, trước khi xử lý |
| `input_validation_failed` | Intake / Frontend Service | `trace_id`, `field_name`, `error_code`, `raw_format_type` | Khi đầu vào khách gửi sai định dạng/mã đơn (ca 1, 9) |
| `agent_invoked` | Agent Backend | `trace_id`, `run_id`, `attempt`, `model_version`, `pricing_version`, `tool_calls` | Khi bắt đầu một lần chạy Agent |
| `agent_response_ready` | Agent Backend | `trace_id`, `run_id`, `status`, `tokens_in`, `tokens_out`, `suggestion_id` | Khi Agent trả gợi ý hoặc gặp lỗi |
| `handoff_to_staff` | Agent Backend | `trace_id`, `reason` (`thieu_du_lieu`, `qua_so_lan_chay`), `summary_included` | Khi Agent chuyển yêu cầu sang nhân viên (ca 4, 19) |
| `suggestion_reviewed` | Staff UI | `trace_id`, `suggestion_id`, `decision` (`giu`/`sua`/`bo`), `review_duration_seconds` | Khi nhân viên duyệt gợi ý |
| `refund_ledger_write` | Refund/Ledger Service | `trace_id`, `idempotency_key`, `expected_amount`, `actual_amount`, `status`, `amount_error_confirmed` | Khi ghi sổ cái và đối soát khoản hoàn (ca 7, 20) |
| `request_closed` | Workflow Service | `trace_id`, `closed_at`, `opened_at`, `dong_trong_24h`, `final_status` | Khi yêu cầu đóng |
| `ticket_reopened` | Customer Support Backend | `trace_id`, `reopened_at`, `days_after_close`, `reason_code` | Khi khách mở lại trong vòng theo dõi (ca 18) |
| `agent_usage_recorded` | Experiment Service | `trace_id`, `assignment_arm`, `eligible`, `agent_used`, `nonuse_reason` | Khi yêu cầu kết thúc xử lý |
| `cost_recorded` | Billing/FinOps Service | `trace_id`, `token_cost`, `tool_cost`, `review_minutes_actual`, `rework_minutes_actual` | Sau mỗi yêu cầu được quyết toán chi phí |
| `audit_sample_checked` | Finance Audit Tool | `trace_id`, `refunded_amount`, `policy_amount`, `pricing_version`, `discrepancy_vnd` | Khi Kế toán kiểm tra mẫu 100 đơn/tuần (ca 5, 17) |

**Kiểm tra chéo chỉ số → event:**

- **Chỉ số chính:** `request_assigned` + `request_closed` + `ticket_reopened`, nối theo `request_id` và `trace_id`; chỉ kết luận khi đủ cửa sổ 7 ngày.
- **Tỉ lệ bỏ qua gợi ý:** `agent_response_ready` + `suggestion_reviewed`; mẫu số là những gợi ý thực sự được xem lại.
- **Tỉ lệ mở lại:** `request_closed` + `ticket_reopened`; cần theo dõi đủ 7 ngày.
- **Tỉ lệ sử dụng Agent:** `request_assigned` + `agent_usage_recorded` + `agent_invoked`; tách rõ được gán treatment và thực tế sử dụng.
- **Tỉ lệ hoàn sai / lỗi ngầm:** `refund_ledger_write` + `audit_sample_checked` + `request_assigned`; đối soát tự động hằng giờ kết hợp kiểm tra mẫu hằng tuần.

## E2 · Rủi ro kinh tế

Dưới đây là *kịch bản giả lập (`simulated`)* từ bảng độ nhạy và phân bổ cố định, không phải dự báo đã kiểm chứng trong vận hành thật.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca phải làm lại tăng gấp đôi | Làm lại ×2 kéo CPS từ **4.472 đ** lên **6.787 đ**, **+51,77%** (`simulated`) | `cost_recorded.rework_minutes_actual`; tỉ lệ làm lại tuần > **8,0%** (mẫu phạm vi pilot hiện tại: 4,9%) | Thu hẹp về `noi_dia`, giới hạn 2 lần chạy, rà 20 trace lỗi hàng đầu trước khi mở lại `hang_nang` | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% kéo dài | Xem lại ×2 làm CPS tăng **+40,70%** lên **6.292 đ**; xem lại 100% làm CPS vọt lên **11.743 đ = 0,98×** (9 phút làm lại) hoặc **12.415 đ = 1,03×** (15,3 phút trung bình dữ liệu) (`simulated`) | `suggestion_reviewed`: tỉ lệ yêu cầu phải xem lại còn > **50%** ở cuối bước rollout `0.25` hoặc thời gian xem lại > **4,8 phút/ca** | Giảm tỉ lệ xem lại theo bậc cho `noi_dia` khi tỉ lệ `sua + bo < 15%`; tối ưu giao diện hiển thị sẵn công thức tính | Trưởng nhóm CSKH |
| Sản lượng thực tế thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng cộng thêm **1.185 đ/việc** ở 45.000 yc/tháng (`4.599 đ = 0,38×`), nhưng tăng gấp đôi lên **2.370 đ/việc** (`5.784 đ = 0,48×`) nếu khối lượng giảm một nửa (`simulated`) | Số việc thành công hằng tuần qua `request_closed` đạt < **50%** kế hoạch phân bổ | Không mở rộng hạ tầng, đàm phán lại gói phí vận hành cố định trước khi đề xuất cổng tiếp theo | FinOps Engineer |
| Giá token nhà cung cấp tăng | Giá token ×2 làm CPS tăng lên **4.723 đ**, **+5,62%** (`simulated`) | `cost_recorded.token_cost`, số token/request trên từng depot (bắt bất thường kiểu depot D05 ở ca 12) | Đặt cảnh báo ngân sách theo depot, giới hạn tối đa 2 lần chạy (tiết kiệm nhất cho cả hệ thống: **6.901.220 đ**, `simulated`) | Kỹ sư trưởng agent |

**Ưu tiên theo số B1:** làm lại ×2 (**+51,77%**), xem lại ×2 (**+40,70%**), lương nhân viên +25% (**+23,12%**). Đây là xếp hạng theo *kịch bản tăng chi phí được cho*, không phải so độ nhạy chuẩn hóa của các yếu tố.
