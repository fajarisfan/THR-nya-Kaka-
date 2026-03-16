import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Kirim THR 🎁",
    page_icon="🎁",
    layout="centered"
)

# Detect hash #zizah → convert ke query param
components.html("""
<script>
    const hash = window.location.hash;
    if (hash === '#zizah') {
        const url = new URL(window.parent.location.href);
        if (!url.searchParams.get('mode')) {
            url.searchParams.set('mode', 'zizah');
            window.parent.location.href = url.toString();
        }
    }
</script>
""", height=0)

params = st.query_params
is_zizah = (params.get("mode", "") == "zizah")

# ── GANTI NOMOR DANA LO DI SINI ──
DANA_NUMBER = "08xxxxxxxxxx"

DANA_DEEPLINK = f"dana://transfer?target={DANA_NUMBER}"
DANA_FALLBACK = f"https://link.dana.id/transfer?target={DANA_NUMBER}"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
.stApp { background: #0f0f0f; color: #f0ede6; }

.thr-receh-card {
    background: #111; border: 1px solid #2a2a2a; border-radius: 14px;
    padding: 1.4rem; margin: 1rem 0; font-size: 0.95rem; color: #ccc; line-height: 1.8;
}
.thr-receh-card strong { color: #f5c842; }

.thr-doa {
    background: linear-gradient(135deg, #0f0a00, #1a1200);
    border: 1px solid #8a6a00; border-radius: 12px;
    padding: 1.2rem 1.5rem; margin-top: 1.5rem;
    font-size: 0.92rem; color: #e0cc88; line-height: 1.7; text-align: center;
}

.dana-btn-wrap { text-align: center; margin: 1.8rem 0; }
.dana-btn {
    display: inline-block;
    background: linear-gradient(135deg, #118EEA, #0D6EBF);
    color: white !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    padding: 1rem 2.5rem;
    border-radius: 50px;
    text-decoration: none !important;
    box-shadow: 0 4px 24px rgba(17,142,234,0.4);
    transition: all 0.2s ease;
    letter-spacing: 0.3px;
}
.dana-btn:hover {
    background: linear-gradient(135deg, #0D6EBF, #0A5A9E);
    box-shadow: 0 6px 32px rgba(17,142,234,0.6);
    transform: translateY(-2px);
    color: white !important;
    text-decoration: none !important;
}
.dana-btn-sub {
    color: #555;
    font-size: 0.78rem;
    margin-top: 0.6rem;
    text-align: center;
}

/* ZIZAH */
.zizah-card {
    background: linear-gradient(135deg, #1a0a14, #140a18);
    border: 1px solid #c084fc; border-left: 4px solid #f472b6;
    border-radius: 14px; padding: 1.5rem; margin: 1.2rem 0;
    font-size: 0.95rem; color: #e9d5f5; line-height: 1.9;
}
.zizah-card strong { color: #f9a8d4; }
.zizah-dana-btn {
    display: inline-block;
    background: linear-gradient(135deg, #9333ea, #7c3aed);
    color: white !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    padding: 1rem 2.5rem;
    border-radius: 50px;
    text-decoration: none !important;
    box-shadow: 0 4px 24px rgba(147,51,234,0.45);
    transition: all 0.2s ease;
    letter-spacing: 0.3px;
}
.zizah-dana-btn:hover {
    background: linear-gradient(135deg, #7c3aed, #6d28d9);
    box-shadow: 0 6px 32px rgba(147,51,234,0.65);
    transform: translateY(-2px);
    color: white !important;
    text-decoration: none !important;
}
.zizah-doa {
    background: linear-gradient(135deg, #0a001a, #10001f);
    border: 1px solid #7c3aed; border-radius: 12px;
    padding: 1.4rem 1.6rem; margin-top: 1.5rem;
    font-size: 0.92rem; color: #ddd6fe; line-height: 1.8; text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════
# HALAMAN ZIZAH 💜
# ══════════════════════════════════════════
if is_zizah:
    st.markdown("""
    <div style="text-align:center;padding:2.5rem 0 1.5rem;">
        <div style="font-size:3.5rem;">🌸✨</div>
        <div style="font-family:'Amiri',serif;font-size:2.4rem;font-weight:700;color:#f9a8d4;margin-bottom:0.3rem;">
            Khusus Buat Zizah
        </div>
        <div style="color:#777;font-size:0.88rem;">Halaman rahasia. Cuma kamu yang punya link ini 🤫</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="zizah-card">
        Hai Zizah 👋<br><br>
        Jadi gini... gua bikin app ini buat tagih utang orang, tapi pas sampe bagian <strong>"kirim THR"</strong>
        gua kepikiran kamu. Entah kenapa. Mungkin emang rejekinya kamu yang lagi gatel 🗿<br><br>
        Nggak maksa ya. Tapi kalau kamu lagi ngerasa rejeki bulan ini lebih dari cukup,
        dan tangan kamu tiba-tiba pengen berbagi kebaikan...
        <strong>tinggal klik tombol di bawah.</strong> Langsung terhubung ke DANA gua. 😇
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="dana-btn-wrap">
        <a href="{DANA_DEEPLINK}" 
           onclick="setTimeout(()=>{{window.location.href='{DANA_FALLBACK}'}},1500)"
           class="zizah-dana-btn">
            💜 Buka DANA & Kirim THR
        </a>
        <div class="dana-btn-sub">Klik → app DANA langsung kebuka, tinggal masukin nominal 🙏</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="zizah-card">
        <strong>Kenapa kamu yang dapet link ini?</strong><br>
        Karena dari sekian banyak orang di kontak gua, kamu yang paling... mungkin mau kirim. Kayaknya. Semoga. 🥺<br><br>
        <strong>Kalau nggak mau kirim?</strong><br>
        Ya nggak papa juga. Tapi setidaknya kamu udah baca sampe sini, itu udah bikin hari gua lebih baik. 😄<br><br>
        <strong>Ini serius apa becanda?</strong><br>
        <em>...dua-duanya.</em> 🗿
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="zizah-doa">
        🤲 Kalau kamu udah transfer, ini doa khusus buat kamu:<br><br>
        <span style="font-family:'Amiri',serif;font-size:1.3rem;color:#e879f9;">
        بَارَكَ اللَّهُ لَكِ فِي أَهْلِكِ وَمَالِكِ
        </span><br>
        <em style="font-size:0.85rem;color:#bbb;">"Bārakallāhu laki fī ahliki wa mālik."</em><br>
        <span style="color:#aaa;font-size:0.82rem;">Semoga Allah memberkahi keluarga dan hartamu. — HR. Abu Dawud</span><br><br>
        Makasih ya Zizah. Serius. 🥹💜
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="text-align:center;margin-top:1.5rem;color:#333;font-size:0.75rem;font-style:italic;">🔒 halaman ini cuma bisa dibuka dari link khusus yang gua kirim ke kamu</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════
# HALAMAN NORMAL 🎁
# ══════════════════════════════════════════
else:
    st.markdown("""
    <div style="text-align:center;padding:2rem 0 1rem;">
        <div style="font-size:4rem;">🎁</div>
        <div style="font-family:'Amiri',serif;font-size:2.4rem;font-weight:700;color:#f5c842;margin-bottom:0.3rem;">
            Kirim THR Dong
        </div>
        <div style="color:#888;font-size:0.9rem;">Nggak minta, nggak maksa. Tapi kalau mau... ya Alhamdulillah 🗿</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="thr-receh-card">
        Assalamu'alaikum, wahai para <strong>dokter, sultan, crazy rich, side hustle warrior</strong>,
        dan siapapun yang rejekinya lagi deras 🌊<br><br>
        Gua cuma manusia biasa yang lagi nunggu <strong>transfer masuk</strong> sambil pura-pura sibuk.<br>
        Kalau hari ini lo ngerasa rejeki lo lagi berlebih dan tangan lo tiba-tiba gatel pengen transfer...
        itu bukan kebetulan. Itu <strong>panggilan hati nurani.</strong> 🫀<br><br>
        Tinggal klik tombol di bawah. <strong>Langsung kebuka DANA.</strong> Nominal bebas. Doa gratis. 🤝
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="dana-btn-wrap">
        <a href="{DANA_DEEPLINK}"
           onclick="setTimeout(()=>{{window.location.href='{DANA_FALLBACK}'}},1500)"
           class="dana-btn">
            💙 Buka DANA & Kirim THR
        </a>
        <div class="dana-btn-sub">Klik → app DANA langsung kebuka, tinggal masukin nominal 🙏</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="thr-receh-card">
        <strong>FAQ Jujur:</strong><br><br>
        ❓ <em>Harus kirim berapa?</em><br>
        → Bebas. Rp 10.000 juga berkah. Rp 1.000.000 lebih berkah lagi. Rp 10.000.000 kayaknya lu dokter beneran.<br><br>
        ❓ <em>Dapat apa kalau kirim THR?</em><br>
        → Dapat doa tulus, rasa senang udah bikin orang bahagia, dan pahala sedekah insyaAllah 🌟<br><br>
        ❓ <em>Kalau nggak kirim?</em><br>
        → Nggak papa. Rejeki masing-masing. Semoga rejekinya makin lancar walau nggak kirim 🙏
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="thr-doa">
        🤲 <strong>Doa buat yang udah kirim:</strong><br><br>
        <span style="font-family:'Amiri',serif;font-size:1.2rem;color:#f5d87a;">
        بَارَكَ اللَّهُ لَكَ فِي أَهْلِكَ وَمَالِكَ
        </span><br>
        <em style="font-size:0.85rem;color:#bbb;">"Bārakallāhu laka fī ahlika wa mālik."</em><br>
        <span style="color:#aaa;font-size:0.82rem;">Semoga Allah memberkahi keluarga dan hartamu. — HR. Abu Dawud</span><br><br>
        Aamiin. Jazakallahu khairan. Lo baik banget sumpah 🥹
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="text-align:center;margin-top:2rem;color:#444;font-size:0.8rem;">THR diterima ikhlas · Doa dikirim real-time langsung ke langit ☁️</div>', unsafe_allow_html=True)
