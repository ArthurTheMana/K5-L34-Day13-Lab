"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1:
        raise ValueError("p must be between 0 and 1")

    # Unlimited attempts
    if k is None:
        return 1 / p

    # Limited attempts
    if k < 1:
        raise ValueError("k must be at least 1")

    expected_runs = 0.0

    for attempt in range(k):
        expected_runs += (1 - p) ** attempt

    return expected_runs


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 < p <= 1:
        raise ValueError("p must be between 0 and 1")

    if k is None:
        return 1.0

    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    expected_runs = so_lan_chay_ky_vong(p, k)
    success_rate = ti_le_thanh_cong(p, k)

    return expected_runs / success_rate


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()

    # Chỉ lấy những lần chạy thuộc các yêu cầu được chọn
    runs = runs[runs["request_id"].isin(reqs["request_id"])].copy()

    # Giới hạn số lần chạy tối đa, sử dụng trong CP2
    if max_lan_chay is not None:
        runs = runs[runs["attempt"] <= max_lan_chay]

        exceeded = reqs["so_lan_chay"] > max_lan_chay
        reqs.loc[exceeded, "ket_qua"] = "chuyen_nhan_vien"
        reqs.loc[
            exceeded,
            ["phut_xem_lai_simulated", "phut_lam_lai_simulated"]
        ] = 0

    # Tính chi phí token đầu vào và đầu ra của tất cả lần chạy
    token_cost = (
        runs["tokens_in"] / 1000 * gia_vao
        + runs["tokens_out"] / 1000 * gia_ra
    ).sum()

    # Tính tổng chi phí gọi công cụ
    tool_cost = (runs["tool_calls"] * gia_tool).sum()

    # Tính chi phí các lần chạy lại, từ lần thứ 2 trở đi
    retry_runs = runs[runs["attempt"] > 1]
    retry_cost = (
        retry_runs["tokens_in"] / 1000 * gia_vao
        + retry_runs["tokens_out"] / 1000 * gia_ra
        + retry_runs["tool_calls"] * gia_tool
    ).sum()

    # Tính chi phí nhân viên xem lại kết quả của Agent
    # Thời gian được lấy từ dữ liệu giả lập
    review_cost = (
        reqs["phut_xem_lai_simulated"].sum()
        * luong_phut * he_so_xem_lai
    )


    # Tính chi phí nhân viên phải làm lại công việc
    # Thời gian được lấy từ dữ liệu giả lập
    rework_cost = (
        reqs["phut_lam_lai_simulated"].sum()
        * luong_phut * he_so_lam_lai
    )

    # Tính tổng chi phí vận hành Agent
    total_cost = token_cost + tool_cost + review_cost + rework_cost

    # Đếm số yêu cầu được xử lý thành công
    successful = (reqs["ket_qua"] == "thanh_cong").sum()

    # Tính chi phí trung bình trên mỗi yêu cầu thành công (CPS)
    # Nếu không có yêu cầu thành công, trả về giá trị vô cực
    cps = total_cost / successful if successful else float("inf")

    # Tính chi phí hóa đơn token và công cụ trên mỗi yêu cầu
    invoice_per_request = (
        (token_cost + tool_cost) / len(reqs)
        if len(reqs) else float("inf")
    )

    # Trả về kết quả chi tiết của mô hình chi phí
    return {
        "token": token_cost,
        "tool": tool_cost,
        "chay_lai": retry_cost,
        "xem_lai": review_cost,
        "lam_lai": rework_cost,
        "tong": total_cost,
        "thanh_cong": successful,
        "cps": cps,
        "hoa_don_moi_yc": invoice_per_request
    }



if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:12s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:12s} {gia_tri:>14,.0f}')
    boi_so_hoa_don = ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]
    chi_phi_he_thong_moi_yc = (
        ket_qua["tong"] + (len(reqs) - ket_qua["thanh_cong"]) * BASELINE
    ) / len(reqs)
    print(f"CPS / hoa don moi yeu cau: {boi_so_hoa_don:.2f}x")
    print(
        f"Chi phi ca he thong / yeu cau (simulated): "
        f"{chi_phi_he_thong_moi_yc:,.0f} đ ({chi_phi_he_thong_moi_yc / BASELINE:.2f}x baseline)"
    )

    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    print("\n===== A3: CHI PHÍ THEO LOẠI YÊU CẦU =====")

    for loai in ["noi_dia", "hang_nang", "quoc_te", "doi_tac"]:
        # Lọc các yêu cầu thuộc loại đang xét
        reqs_loai = reqs[reqs["loai"] == loai]

        # Tính chi phí bằng mô hình A2
        kq = mo_hinh(runs, reqs_loai)

        # Tính số yêu cầu và tỷ lệ thành công
        so_yeu_cau = len(reqs_loai)
        ty_le_thanh_cong = kq["thanh_cong"] / so_yeu_cau

        # Tính số lần chạy trung bình trên mỗi yêu cầu
        so_lan_chay = reqs_loai["so_lan_chay"].mean()

        # So sánh chi phí với mức nhân viên tự xử lý
        ty_le_chi_phi = kq["cps"] / BASELINE

        print(
            f"{loai:12s} | "
            f"{so_yeu_cau:4d} yêu cầu | "
            f"Thành công: {ty_le_thanh_cong:.1%} | "
            f"Lần chạy: {so_lan_chay:.2f} | "
            f"CPS (sim): {kq['cps']:,.0f} đ | "
            f"So với baseline: {ty_le_chi_phi:.2f}x"
        )

    # Tỉ lệ lần chạy ok theo từng attempt và loại yêu cầu (kiểm tra chạy lại có giúp không)
    runs_loai = runs.merge(reqs[["request_id", "loai"]], on="request_id")
    runs_loai["is_ok"] = (runs_loai["status"] == "ok").astype(float)
    bang_ok_attempt = runs_loai.pivot_table(
        index="loai", columns="attempt", values="is_ok", aggfunc="mean"
    )
    print("\nTỉ lệ status == 'ok' theo từng lần thử (attempt):")
    for loai in ["noi_dia", "hang_nang", "quoc_te", "doi_tac"]:
        r1 = bang_ok_attempt.loc[loai, 1]
        r2 = bang_ok_attempt.loc[loai, 2]
        r3 = bang_ok_attempt.loc[loai, 3]
        print(f"  {loai:10s} | Lần 1: {r1:5.1%} | Lần 2: {r2:5.1%} | Lần 3: {r3:5.1%}")


    # ---------- Nhiệm vụ A4: Chi phí cố định ----------
    print("\n===== A4: CHI PHÍ CỐ ĐỊNH =====")

    # Chỉ chọn hai loại yêu cầu trong phạm vi pilot
    reqs_pilot = reqs[
        reqs["loai"].isin(["noi_dia", "hang_nang"])
    ]

    # Tính chi phí và số yêu cầu thành công trong phạm vi
    kq_pilot = mo_hinh(runs, reqs_pilot)

    # Tỷ lệ thành công tính trên toàn bộ mẫu 1.200 yêu cầu
    ty_le_thanh_cong = kq_pilot["thanh_cong"] / len(reqs)

    # Chi phí cố định hàng tháng
    chi_phi_co_dinh = 40_000_000

    # Tính cho hai mức khối lượng yêu cầu
    for khoi_luong in [45000, 22500]:
        # Ước tính số yêu cầu thành công hàng tháng
        thanh_cong_thang = khoi_luong * ty_le_thanh_cong

        # Phân bổ chi phí cố định cho mỗi việc thành công
        co_dinh_moi_viec = chi_phi_co_dinh / thanh_cong_thang

        # Tổng chi phí mỗi việc thành công sau khi cộng cố định
        cps_tong = kq_pilot["cps"] + co_dinh_moi_viec

        # So sánh với chi phí nhân viên tự xử lý
        so_voi_baseline = cps_tong / BASELINE

        print(
            f"{khoi_luong:,} yêu cầu/tháng | "
            f"Thành công: {thanh_cong_thang:,.0f} | "
            f"Cố định/việc: {co_dinh_moi_viec:,.0f} đ | "
            f"CPS tổng: {cps_tong:,.0f} đ | "
            f"Baseline: {so_voi_baseline:.2f}x"
        )


    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    print("\n===== B1: PHÂN TÍCH ĐỘ NHẠY =====")

    # Chi phí cơ sở dùng để so sánh các kịch bản
    cps_goc = mo_hinh(runs, reqs)["cps"]

    # Các kịch bản thay đổi từng yếu tố (đủ 9 kịch bản B1)
    kich_ban = [
        ("Gia token gap doi", {"gia_vao": 52, "gia_ra": 260}),
        ("Gia token giam nua", {"gia_vao": 13, "gia_ra": 65}),
        ("Xem lai gap doi", {"he_so_xem_lai": 2.0}),
        ("Xem lai giam nua", {"he_so_xem_lai": 0.5}),
        ("Lam lai gap doi", {"he_so_lam_lai": 2.0}),
        ("Lam lai giam nua", {"he_so_lam_lai": 0.5}),
        ("Luong tang 25%", {"luong_phut": 2500}),
        ("Toi da 2 lan chay", {"max_lan_chay": 2}),
        ("Chi 1 lan chay", {"max_lan_chay": 1}),
    ]

    # Chạy từng kịch bản và so sánh với chi phí gốc
    for ten, tham_so in kich_ban:
        ket_qua = mo_hinh(runs, reqs, **tham_so)

        cps_moi = ket_qua["cps"]

        thay_doi = (cps_moi / cps_goc - 1) * 100

        print(
            f"{ten:24s} | "
            f"CPS: {cps_moi:,.0f} đ | "
            f"Thay doi: {thay_doi:+.2f}%"
        )

    # ---------- CP2 - B2: Thay đổi đồng thời hai yếu tố ----------
    print("\n===== B2: KỊCH BẢN KẾT HỢP =====")

    ket_qua = mo_hinh(
        runs,
        reqs,
        gia_vao=52,
        gia_ra=260,
        he_so_xem_lai=2.0
    )

    thay_doi = (ket_qua["cps"] / cps_goc - 1) * 100

    print(f"CPS ket hop: {ket_qua['cps']:,.0f} đ")
    print(f"Thay doi: {thay_doi:+.2f}%")


    # ---------- CP2 - B3: Giới hạn số lần chạy ----------
    print("\n===== B3: GIOI HAN SO LAN CHAY =====")

    for gioi_han in [1, 2, 3]:
        # Tính lại chi phí Agent theo giới hạn
        kq = mo_hinh(runs, reqs, max_lan_chay=gioi_han)

        # Số yêu cầu không được Agent giải quyết thành công
        so_that_bai = len(reqs) - kq["thanh_cong"]

        # Cộng chi phí nhân viên xử lý các yêu cầu thất bại
        chi_phi_he_thong = kq["tong"] + so_that_bai * BASELINE

        print(
            f"{gioi_han} lan | "
            f"Agent: {kq['tong']:,.0f} d | "
            f"That bai: {so_that_bai} | "
            f"He thong: {chi_phi_he_thong:,.0f} d | "
            f"CPS: {kq['cps']:,.0f} d"
        )


    # ---------- CP2 - B4: Xem lại 100% ----------
    print("\n===== B4: XEM LAI 100% =====")

    # Chỉ chọn yêu cầu nội địa và hàng nặng
    reqs_pilot = reqs[
        reqs["loai"].isin(["noi_dia", "hang_nang"])
    ].copy()

    runs_pilot = runs[
        runs["request_id"].isin(reqs_pilot["request_id"])
    ].copy()

    # Tính chi phí token và tool từ dữ liệu trace
    kq = mo_hinh(runs, reqs_pilot)

    # Đếm số yêu cầu có ít nhất một lần chạy thành công
    so_yeu_cau_ok = runs_pilot.loc[
        runs_pilot["status"] == "ok", "request_id"
    ].nunique()

    # Đếm số ca sai cần nhân viên làm lại
    so_ca_sai = (
        reqs_pilot["ket_qua"] == "lam_lai"
    ).sum()

    # Chi phí xem lại và làm lại theo giả định B4
    chi_phi_xem_lai = so_yeu_cau_ok * 5 * LUONG_PHUT
    chi_phi_lam_lai = so_ca_sai * 9 * LUONG_PHUT

    # Không cộng lại chi phí nhân sự simulated ban đầu
    tong_moi = (
        kq["token"] + kq["tool"]
        + chi_phi_xem_lai + chi_phi_lam_lai
    )

    # Giữ số yêu cầu thành công theo mô hình gốc
    cps_moi = tong_moi / kq["thanh_cong"]

    print(f"Yeu cau co run ok: {so_yeu_cau_ok}")
    print(f"So ca lam lai: {so_ca_sai}")
    print(f"CPS B4 (9 phut lam lai, sim): {cps_moi:,.0f} d ({cps_moi / BASELINE:.2f}x baseline)")

    # Độ nhạy B4 theo số phút làm lại trung bình từ cột simulated
    phut_lam_lai_tb = reqs.loc[
        reqs["ket_qua"] == "lam_lai", "phut_lam_lai_simulated"
    ].mean()
    chi_phi_lam_lai_tb = so_ca_sai * round(phut_lam_lai_tb, 1) * LUONG_PHUT
    tong_moi_tb = kq["token"] + kq["tool"] + chi_phi_xem_lai + chi_phi_lam_lai_tb
    cps_moi_tb = tong_moi_tb / kq["thanh_cong"]
    phut_hoa_von_9 = (
        kq["thanh_cong"] * BASELINE - kq["token"] - kq["tool"] - chi_phi_lam_lai
    ) / (so_yeu_cau_ok * LUONG_PHUT)
    phut_hoa_von_tb = (
        kq["thanh_cong"] * BASELINE - kq["token"] - kq["tool"] - chi_phi_lam_lai_tb
    ) / (so_yeu_cau_ok * LUONG_PHUT)
    print(
        f"CPS B4 ({phut_lam_lai_tb:.1f} phut lam lai, sim): "
        f"{cps_moi_tb:,.0f} d ({cps_moi_tb / BASELINE:.2f}x baseline)"
    )
    print(
        f"Phut xem lai hoa von: <= {phut_hoa_von_9:.1f} phut (voi 9 phut lam lai) "
        f"hoac <= {phut_hoa_von_tb:.1f} phut (voi {phut_lam_lai_tb:.1f} phut lam lai)"
    )

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower

    # ---------- CP4 - D1: Tính cỡ mẫu Pilot ----------
    print("\n===== CP4 - D1: TÍNH CỠ MẪU =====")

    import math
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower

    # Các tham số theo đề bài
    baseline = 0.70
    muc_tieu = 0.75
    alpha = 0.05
    power = 0.80
    icc = 0.02

    # Hàm tính hệ số thiết kế khi chia theo cụm
    def he_so_thiet_ke(m, icc):
        return 1 + (m - 1) * icc

    # Hàm tính cỡ mẫu hiệu dụng
    def co_mau_hieu_dung(so_cum, m, icc):
        return so_cum * m / he_so_thiet_ke(m, icc)

    # D1a: Chia ngẫu nhiên theo từng yêu cầu
    effect_size = proportion_effectsize(muc_tieu, baseline)
    n = NormalIndPower().solve_power(
        effect_size=effect_size,
        alpha=alpha,
        power=power,
        ratio=1.0,
        alternative="two-sided"
    )

    n_moi_nhom = math.ceil(n)
    print(f"D1a - Theo yêu cầu: {n_moi_nhom} yêu cầu/nhóm")

    # D1b: Chia theo nhân viên, 75 yêu cầu mỗi người
    m = 75
    deff = he_so_thiet_ke(m, icc)
    n_can = math.ceil(n * deff)
    nhan_vien_can = math.ceil(n_can / m)

    print(f"D1b - Design effect: {deff:.2f}")
    print(f"      Cỡ mẫu: {n_can} yêu cầu/nhóm")
    print(f"      Nhân viên cần: {nhan_vien_can} người/nhóm")
    print(f"      Đủ 40 nhân viên: {nhan_vien_can * 2 <= 40}")

    # D1c: 20 nhân viên mỗi nhóm, số yêu cầu không giới hạn
    hieu_dung_staff = 20 / icc
    print(f"D1c - Tối đa: {hieu_dung_staff:.0f} mẫu hiệu dụng/nhóm")
    print(f"      Đạt D1a: {hieu_dung_staff >= n}")

    # D1d: 6 depot mỗi nhóm
    hieu_dung_depot = 6 / icc
    print(f"D1d - Tối đa: {hieu_dung_depot:.0f} mẫu hiệu dụng/nhóm")

    # D1e: MDE = 6 điểm, cần 859 mẫu hiệu dụng mỗi nhóm
    n_muc_tieu = 859
    so_nhan_vien = 20

    # Giải phương trình c*m/(1+(m-1)*ICC) >= 859
    mau_so = so_nhan_vien - n_muc_tieu * icc

    m_can = math.ceil(
        n_muc_tieu * (1 - icc) / mau_so
    )

    print(f"D1e - Số yêu cầu cần mỗi nhân viên: {m_can}")
    print(f"      Design effect ở m={m_can}: {he_so_thiet_ke(m_can, icc):.2f}")
    print(
        f"      Cỡ mẫu hiệu dụng: "
        f"{co_mau_hieu_dung(20, m_can, icc):.2f}"
    )
    power_5pp_tai_859 = NormalIndPower().power(
        effect_size=effect_size,
        nobs1=n_muc_tieu,
        alpha=alpha,
        ratio=1.0,
        alternative="two-sided",
    )
    print(f"      Power thực tế ở mức +5 điểm (với n={n_muc_tieu}): {power_5pp_tai_859:.2%}")

    # Kiểm tra tỷ lệ mở lại từ dữ liệu chạy thử
    ty_le_mo_lai = (reqs["mo_lai_trong_7_ngay"] == 1).mean()
    ty_le_mo_lai_pilot = (reqs_pilot["mo_lai_trong_7_ngay"] == 1).mean()

    print("\n===== CP4 - KIỂM TRA AN TOÀN =====")
    print(f"Tỷ lệ mở lại trong 7 ngày (toàn mẫu 1.200 yc): {ty_le_mo_lai:.2%}")
    print(f"Tỷ lệ mở lại trong 7 ngày (noi_dia + hang_nang): {ty_le_mo_lai_pilot:.2%}")
