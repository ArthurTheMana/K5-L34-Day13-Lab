# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): TLiet
- Nhóm được chấm: BuaDi

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Agent có CPS 4.472 đ, thấp hơn baseline 12.000 đ. Nhóm nhận diện được rủi ro khi chi phí làm lại tăng 51,77% và đề xuất Go có điều kiện. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Phân tích 1.200 yêu cầu, 978 ca thành công. Dữ liệu chi phí được ghi nhãn simulated. Pilot tập trung vào noi_dia (CPS 2.696 đ) và hang_nang (8.221 đ), loại quoc_te (22.515 đ). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Thiết kế đối chứng 50/50, cần 1.250 yêu cầu/nhóm. Có luật dừng khi tỷ lệ mở lại vượt 6% trong 2 ngày và cơ chế rollback trong 15 phút. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go · Go có điều kiện · No-go (giữ một)

**Lý do:** Đội trình nhận diện đúng rủi ro thiếu ngẫu nhiên hóa và giới hạn cỡ mẫu (1.000 < 1.251 mẫu hiệu dụng/nhóm); đề xuất điều chỉnh MDE lên 6% và đạt 859 mẫu hiệu dụng/nhóm. Trước khi phê duyệt cần đối chiếu bằng chứng chi phí, nhãn simulated và luật dừng.

**Một câu hỏi cho đội trình:** Pilot đủ 1.250 yêu cầu/nhóm nhưng không đủ randomization có đạt chỉ tiêu không?

**Câu trả lời của đội trình (ghi lại tại buổi):** Không đạt chỉ tiêu. Dù đạt đủ cỡ mẫu thống kê (1.251 yêu cầu mỗi nhóm), việc thiếu ngẫu nhiên hóa (randomization) hoặc chia theo từng yêu cầu trên cùng một nhân viên sẽ gây thiên lệch chọn mẫu và tràn tác động (spillover), khiến pilot không thể tách riêng được tác động thật của trợ lý. Thực tế với 40 nhân viên và ICC = 0,02, giới hạn cỡ mẫu hiệu dụng tối đa chỉ là 20 / 0,02 = 1.000 (< 1.251) ở mức +5 điểm, nên nhóm bắt buộc phải giữ chia ngẫu nhiên theo cụm 20 + 20 nhân viên và chấp nhận nâng mức chênh kỳ vọng lên +6 điểm (859 yêu cầu/nhóm, tối thiểu 299 yêu cầu/nhân viên) để kết quả vừa đáng tin cậy vừa đủ cỡ mẫu

