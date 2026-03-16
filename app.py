import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Tagih Utang & THR",
    page_icon="💸",
    layout="centered"
)

# ─── Inject JS untuk detect hash & kirim ke Streamlit via query param ───
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

# ─── Detect mode ───
params = st.query_params
mode = params.get("mode", "")
is_zizah = (mode == "zizah")

# ══════════════════════════════════════════
# SHARED STYLES
# ══════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
.stApp { background: #0f0f0f; color: #f0ede6; }

.header-title {
    font-family: 'Amiri', serif;
    font-size: 2.4rem; font-weight: 700;
    color: #d4a843; text-align: center;
    margin-bottom: 0.2rem; letter-spacing: 1px;
}
.header-sub { text-align: center; color: #888; font-size: 0.9rem; margin-bottom: 2rem; }

.hadits-card {
    background: linear-gradient(135deg, #1a1400, #1e1a00);
    border: 1px solid #d4a843; border-left: 4px solid #d4a843;
    border-radius: 12px; padding: 1.5rem; margin: 1.2rem 0;
}
.hadits-arabic {
    font-family: 'Amiri', serif; font-size: 1.4rem; color: #f5d87a;
    line-height: 2.2; text-align: right; direction: rtl;
}
.hadits-latin { font-size: 0.85rem; color: #aaa; font-style: italic; margin-top: 0.6rem; }
.hadits-arti { font-size: 0.95rem; color: #e8dfc8; margin-top: 0.8rem; line-height: 1.6; }
.hadits-source { font-size: 0.75rem; color: #d4a843; margin-top: 0.8rem; font-weight: 600; }
.divider { border: none; border-top: 1px solid #2a2a2a; margin: 2rem 0; }
.warning-box {
    background: #1a0a00; border: 1px solid #ff6b35; border-radius: 10px;
    padding: 1rem 1.2rem; margin-top: 1.5rem;
    font-size: 0.9rem; color: #ffb59e; line-height: 1.6;
}

/* THR NORMAL */
.thr-receh-card {
    background: #111; border: 1px solid #2a2a2a; border-radius: 14px;
    padding: 1.4rem; margin: 1rem 0; font-size: 0.95rem; color: #ccc; line-height: 1.8;
}
.thr-receh-card strong { color: #f5c842; }
.thr-dana-big {
    background: linear-gradient(135deg, #0d1f0d, #0a1a0a);
    border: 2px solid #4caf50; border-radius: 16px;
    padding: 2rem; text-align: center; margin: 1.5rem 0;
}
.thr-dana-num {
    font-size: 2.2rem; font-weight: 700; color: #69f0ae; letter-spacing: 3px;
    background: #001500; padding: 0.7rem 1.5rem; border-radius: 10px;
    display: inline-block; border: 1px dashed #4caf50; margin: 0.5rem 0;
}
.thr-doa {
    background: linear-gradient(135deg, #0f0a00, #1a1200);
    border: 1px solid #8a6a00; border-radius: 12px;
    padding: 1.2rem 1.5rem; margin-top: 1.5rem;
    font-size: 0.92rem; color: #e0cc88; line-height: 1.7; text-align: center;
}

/* ZIZAH PAGE */
.zizah-hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}
.zizah-emoji { font-size: 3.5rem; display: block; margin-bottom: 0.8rem; }
.zizah-title {
    font-family: 'Amiri', serif;
    font-size: 2.4rem; font-weight: 700;
    color: #f9a8d4;
    margin-bottom: 0.4rem;
}
.zizah-sub { color: #999; font-size: 0.9rem; }

.zizah-card {
    background: linear-gradient(135deg, #1a0a14, #140a18);
    border: 1px solid #c084fc;
    border-left: 4px solid #f472b6;
    border-radius: 14px;
    padding: 1.5rem;
    margin: 1.2rem 0;
    font-size: 0.95rem;
    color: #e9d5f5;
    line-height: 1.9;
}
.zizah-card strong { color: #f9a8d4; }

.zizah-dana-box {
    background: linear-gradient(135deg, #0f001a, #1a0025);
    border: 2px solid #a855f7;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin: 1.5rem 0;
}
.zizah-dana-num {
    font-size: 2.2rem; font-weight: 700; color: #e879f9; letter-spacing: 3px;
    background: #1a0025; padding: 0.7rem 1.5rem; border-radius: 10px;
    display: inline-block; border: 1px dashed #a855f7; margin: 0.5rem 0;
}
.zizah-doa {
    background: linear-gradient(135deg, #0a001a, #10001f);
    border: 1px solid #7c3aed;
    border-radius: 12px;
    padding: 1.4rem 1.6rem; margin-top: 1.5rem;
    font-size: 0.92rem; color: #ddd6fe; line-height: 1.8; text-align: center;
}
.zizah-secret {
    text-align: center; margin-top: 1rem;
    font-size: 0.75rem; color: #4a4a4a;
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════
# ZIZAH SECRET PAGE 💜
# ══════════════════════════════════════════
if is_zizah:
    st.markdown("""
    <div class="zizah-hero">
        <span class="zizah-emoji">🌸✨</span>
        <div class="zizah-title">Khusus Buat Zizah</div>
        <div class="zizah-sub">Halaman rahasia. Cuma kamu yang punya link ini 🤫</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="zizah-card">
        Hai Zizah 👋<br><br>
        Jadi gini... gua bikin app ini buat tagih utang, tapi pas sampe bagian <strong>"kirim THR"</strong>
        gua kepikiran kamu. Entah kenapa. Mungkin emang rejekinya kamu yang gatel 🗿<br><br>
        Nggak maksa ya. Tapi kalau kamu lagi ngerasa rejeki bulan ini lebih dari cukup,
        dan tangan kamu tiba-tiba pengen berbagi kebaikan ke seseorang yang sudah baik ke kamu...
        <strong>nomor DANA gua ada di bawah.</strong><br><br>
        Nominal bebas. Doa unlimited. Transfer sekarang juga boleh. 😇
    </div>
    """, unsafe_allow_html=True)

    zizah_dana = "082298180077"  # ← GANTI NOMOR DANA LO DI SINI

    st.markdown(f"""
    <div class="zizah-dana-box">
        <div style="color:#c084fc;font-size:0.85rem;margin-bottom:0.4rem;">💜 Transfer via DANA ke:</div>
        <div class="zizah-dana-num">{zizah_dana}</div>
        <div style="color:#aaa;font-size:0.82rem;margin-top:0.7rem;">
            Konfirmasi via WA ya — biar langsung gua doain 🙏
        </div>
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

    st.markdown('<div class="zizah-secret">🔒 halaman ini cuma bisa dibuka dari link khusus yang gua kirim ke kamu</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════
# HALAMAN NORMAL
# ══════════════════════════════════════════
else:
    tab1, tab2 = st.tabs(["📜 Tagih Utang", "🎁 Kirim THR"])

    # ── TAB 1 ──
    with tab1:
        st.markdown('<div class="header-title">📜 Tagih Utang Halal</div>', unsafe_allow_html=True)
        st.markdown('<div class="header-sub">Karena utang itu dicatat, dan yang diam bukan berarti lupa.</div>', unsafe_allow_html=True)

        st.markdown("### 🗂️ Detail Utang")
        col1, col2 = st.columns(2)
        with col1:
            nama = st.text_input("Nama yang berutang", placeholder="Si Fulan...")
        with col2:
            nominal = st.number_input("Nominal utang (Rp)", min_value=0, step=1000, value=0)
        keterangan = st.text_area("Keterangan", placeholder="Gosend laptop ketinggalan, tanggal...", height=80)

        if nominal > 0 and nama:
            st.markdown(f"""
            <div style="background:#111;border:1px solid #333;border-radius:10px;padding:1rem;margin-top:0.5rem;">
                <span style="color:#888;font-size:0.85rem;">Ringkasan</span><br>
                <span style="color:#f0ede6;font-size:1rem;font-weight:600;">{nama}</span>
                <span style="color:#aaa;"> berutang </span>
                <span style="color:#d4a843;font-size:1.1rem;font-weight:700;">Rp {nominal:,.0f}</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<hr class="divider">', unsafe_allow_html=True)
        st.markdown("### 📖 Hadits tentang Utang")

        hadits_list = [
            {
                "arabic": "مَطْلُ الْغَنِيِّ ظُلْمٌ",
                "latin": "Matlul ghaniyyi zhulm.",
                "arti": "\"Menunda-nunda pembayaran utang bagi orang yang mampu adalah kezaliman.\"",
                "source": "HR. Bukhari no. 2400, Muslim no. 1564"
            },
            {
                "arabic": "نَفْسُ الْمُؤْمِنِ مُعَلَّقَةٌ بِدَيْنِهِ حَتَّى يُقْضَى عَنْهُ",
                "latin": "Nafsu al-mu'mini mu'allaqatun bi-daynihi hattā yuqḍā 'anhu.",
                "arti": "\"Jiwa seorang mukmin tergantung (terhalang) karena utangnya hingga utang itu dilunasi.\"",
                "source": "HR. Tirmidzi no. 1078, Ibnu Majah no. 2413 — Hasan"
            },
            {
                "arabic": "مَنْ أَخَذَ أَمْوَالَ النَّاسِ يُرِيدُ أَدَاءَهَا أَدَّى اللَّهُ عَنْهُ، وَمَنْ أَخَذَهَا يُرِيدُ إِتْلَافَهَا أَتْلَفَهُ اللَّهُ",
                "latin": "Man akhadha amwālan-nāsi yurīdu adā'ahā addallāhu 'anhu...",
                "arti": "\"Barangsiapa mengambil harta manusia dengan niat untuk melunasinya, Allah akan melunasinya. Dan barangsiapa mengambilnya dengan niat merusaknya (tidak membayar), Allah akan membinasakannya.\"",
                "source": "HR. Bukhari no. 2387"
            },
            {
                "arabic": "إِنَّ أَعْظَمَ الذُّنُوبِ عِنْدَ اللَّهِ أَنْ يَلْقَاهُ بِهَا عَبْدٌ بَعْدَ الْكَبَائِرِ الَّتِي نَهَى اللَّهُ عَنْهَا أَنْ يَمُوتَ الرَّجُلُ وَعَلَيْهِ دَيْنٌ",
                "latin": "Inna a'zhamadhdhunūbi 'indallāhi an yalqāhu bihā 'abdun ba'dal kabā'ir...",
                "arti": "\"Sesungguhnya dosa terbesar di sisi Allah setelah dosa-dosa besar yang dilarang adalah seseorang meninggal dalam keadaan masih memiliki utang.\"",
                "source": "HR. Abu Dawud no. 3341 — Shahih"
            },
        ]

        for h in hadits_list:
            st.markdown(f"""
            <div class="hadits-card">
                <div class="hadits-arabic">{h['arabic']}</div>
                <div class="hadits-latin">{h['latin']}</div>
                <div class="hadits-arti">{h['arti']}</div>
                <div class="hadits-source">📚 {h['source']}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class="warning-box">
            ⚠️ <strong>Ingat:</strong> Utang bukan perkara kecil dalam Islam. Shalat jenazah pun bisa tertahan karena utang yang belum lunas.
            Bayar sebelum terlambat — di dunia maupun akhirat.<br><br>
            🤲 <em>"Dan janganlah kamu makan harta di antara kamu dengan jalan yang batil..."</em> — QS. Al-Baqarah: 188
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div style="text-align:center;margin-top:2rem;color:#444;font-size:0.8rem;">Made with niat baik 🤍</div>', unsafe_allow_html=True)

    # ── TAB 2 ──
    with tab2:
        st.markdown("""
        <div style="text-align:center;padding:2rem 0 1rem;">
            <div style="font-size:4rem;">🎁</div>
            <div style="font-family:'Amiri',serif;font-size:2.2rem;font-weight:700;color:#f5c842;">Kirim THR Dong</div>
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
            Nomor DANA ada di bawah. <strong>Nominal bebas.</strong> Doa gratis. Deal? 🤝
        </div>
        """, unsafe_allow_html=True)

        dana_input = st.text_input("Nomor DANA kamu", placeholder="08xxxxxxxxxx", key="dana_thr")

        if dana_input:
            st.markdown(f"""
            <div class="thr-dana-big">
                <div style="color:#888;font-size:0.85rem;margin-bottom:0.4rem;">📱 Transfer via DANA ke:</div>
                <div class="thr-dana-num">{dana_input}</div>
                <div style="color:#aaa;font-size:0.82rem;margin-top:0.7rem;">
                    Nominal bebas · Konfirmasi via WA biar langsung didoain 🤲
                </div>
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
            → Nggak papa. Tapi scroll ke tab sebelah — siapa tau ada reminder buat kamu juga 👀
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
