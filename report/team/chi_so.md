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
| `agent_invoked` | Agent Backend | `trace_id`, `run_id`, `attempt`, `model_version`, `tool_calls` | Khi bắt đầu một lần chạy Agent |
| `agent_response_ready` | Agent Backend | `trace_id`, `run_id`, `status`, `tokens_in`, `tokens_out`, `suggestion_id` | Khi Agent trả gợi ý hoặc gặp lỗi |
| `suggestion_reviewed` | Staff UI | `trace_id`, `suggestion_id`, `decision` (`giu`/`sua`/`bo`), `review_duration_seconds` | Khi nhân viên duyệt gợi ý |
| `refund_reconciled` | Refund/Ledger Service | `trace_id`, `expected_amount`, `actual_amount`, `amount_error_confirmed`, `refund_id` | Sau khi đối soát khoản hoàn |
| `request_closed` | Workflow Service | `trace_id`, `closed_at`, `opened_at`, `dong_trong_24h`, `final_status` | Khi yêu cầu đóng |
| `request_reopened` | Customer Support Backend | `trace_id`, `reopened_at`, `days_after_close`, `reason_code` | Khi khách mở lại trong vòng theo dõi |
| `agent_usage_recorded` | Experiment Service | `trace_id`, `assignment_arm`, `eligible`, `agent_used`, `nonuse_reason` | Khi yêu cầu kết thúc xử lý |
| `cost_recorded` | Billing/FinOps Service | `trace_id`, `token_cost`, `tool_cost`, `review_minutes_simulated_or_actual`, `rework_minutes_simulated_or_actual` | Sau mỗi yêu cầu được quyết toán chi phí |

**Kiểm tra chéo chỉ số → event:**

- **Chỉ số chính:** `request_assigned` + `request_closed` + `request_reopened`, join theo `request_id` và `trace_id`; chỉ kết luận khi đủ cửa sổ 7 ngày.
- **Tỉ lệ bỏ qua gợi ý:** `agent_response_ready` + `suggestion_reviewed`; mẫu số là những gợi ý thực sự được xem lại.
- **Tỉ lệ mở lại:** `request_closed` + `request_reopened`; cần theo dõi đủ 7 ngày.
- **Tỉ lệ sử dụng Agent:** `request_assigned` + `agent_usage_recorded` + `agent_invoked`; tách rõ được gán treatment và thực tế sử dụng.
- **Tỉ lệ hoàn sai:** `refund_reconciled` + `request_assigned`; chỉ tính khi đã đối soát với dữ liệu chuẩn.

## E2 · Rủi ro kinh tế

Dưới đây là *kịch bản giả lập (simulated)* từ bảng CP2, không phải dự báo đã kiểm chứng trong vận hành thật.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Chi phí nhân viên làm lại tăng | Nếu làm lại ×2, CPS từ **4.472 đ** lên **6.787 đ**, **+51,77%** (simulated) | `cost_recorded.rework_minutes...`; CPS theo ngày và % request cần làm lại | Giữ rollout, phân tích top failure codes, sửa luồng/guardrail, kiểm tra lại trước mở rộng | AI Engineer |
| Chi phí xem lại tăng mạnh | Nếu xem lại ×2, CPS tăng lên **6.292 đ**, **+40,70%** (simulated) | `suggestion_reviewed.review_duration_seconds`, tỉ lệ review và `cost_recorded` | Tối ưu UX duyệt, phân tầng rủi ro, chỉ giảm review khi an toàn được chứng minh | Product Owner |
| Giá token tăng | Nếu giá token ×2, CPS tăng lên **4.723 đ**, **+5,62%** (simulated) | `cost_recorded.token_cost`, token/request, giá nhà cung cấp | Cảnh báo ngân sách, tối ưu prompt và cache có kiểm soát; không cắt bước xác minh an toàn | AI/FinOps Engineer |

**Ưu tiên theo số B1:** làm lại ×2 (**+51,77%**), xem lại ×2 (**+40,70%**), lương nhân viên +25% (**+23,12%**). Đây là xếp hạng theo *kịch bản tăng chi phí được cho*, không phải so độ nhạy chuẩn hóa của các yếu tố.
