import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Kirim THR 🎁",
    page_icon="🎁",
    layout="centered"
)

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

DANA_NUMBER = "082298180077"
WA_NUMBER = "6282298180077"
ROBLOX_SERVER = "https://www.roblox.com/share?code=f0f4bcb80ae4e84b8f1fda58ffd0123d&type=Server"
WA_TRAP = f"https://wa.me/{WA_NUMBER}?text=Haii%20gua%20mau%20ambil%20hadiah%20rod%20Fish%20It%20nih%20🎣"

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

.zizah-card {
    background: linear-gradient(135deg, #1a0a14, #140a18);
    border: 1px solid #c084fc; border-left: 4px solid #f472b6;
    border-radius: 14px; padding: 1.5rem; margin: 1.2rem 0;
    font-size: 0.95rem; color: #e9d5f5; line-height: 1.9;
}
.zizah-card strong { color: #f9a8d4; }
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
        Nggak maksa ya. Tapi kalau kamu lagi ngerasa rejeki bulan ini lebih dari cukup
        dan tangan kamu tiba-tiba pengen berbagi kebaikan...
        <strong>tap tombol di bawah, nomor DANA langsung ke-copy.</strong>
        Tinggal buka DANA, paste, kirim. Semudah itu. 😇
    </div>
    """, unsafe_allow_html=True)

    # Copy DANA button
    components.html(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700&display=swap');
        body {{ margin: 0; background: transparent; }}
        .wrap {{ text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #0f001a, #1a0025); border: 2px solid #a855f7; border-radius: 16px; }}
        .label {{ color: #c084fc; font-size: 0.85rem; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 0.4rem; }}
        .num {{ font-size: 2rem; font-weight: 700; color: #e879f9; letter-spacing: 3px; background: #1a0025; padding: 0.6rem 1.2rem; border-radius: 10px; display: inline-block; border: 1px dashed #a855f7; margin: 0.4rem 0; font-family: monospace; }}
        .btn {{ margin-top: 0.8rem; background: #a855f7; color: #fff; font-weight: 700; font-size: 1rem; padding: 0.7rem 2rem; border-radius: 50px; border: none; cursor: pointer; font-family: 'Plus Jakarta Sans', sans-serif; transition: all 0.2s; display: block; width: 100%; }}
        .btn:hover {{ background: #9333ea; }}
        .copied {{ background: #22c55e !important; }}
        .hint {{ color: #666; font-size: 0.78rem; margin-top: 0.6rem; font-family: 'Plus Jakarta Sans', sans-serif; }}
    </style>
    <div class="wrap">
        <div class="label">💜 Nomor DANA — tap untuk copy:</div>
        <div class="num">{DANA_NUMBER}</div><br>
        <button class="btn" id="btn" onclick="copyNum()">📋 Salin Nomor DANA</button>
        <div class="hint" id="hint">Setelah disalin, buka DANA → Kirim → Paste nomor → masukkan nominal</div>
    </div>
    <script>
        function copyNum() {{
            navigator.clipboard.writeText('{DANA_NUMBER}').then(function() {{
                document.getElementById('btn').textContent = '✅ Tersalin!';
                document.getElementById('btn').classList.add('copied');
                document.getElementById('hint').textContent = 'Nomor sudah tersalin! Buka DANA sekarang 🚀';
                document.getElementById('hint').style.color = '#22c55e';
                setTimeout(function() {{
                    document.getElementById('btn').textContent = '📋 Salin Nomor DANA';
                    document.getElementById('btn').classList.remove('copied');
                    document.getElementById('hint').textContent = 'Setelah disalin, buka DANA → Kirim → Paste nomor → masukkan nominal';
                    document.getElementById('hint').style.color = '#666';
                }}, 3000);
            }});
        }}
    </script>
    """, height=200)

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

    # ── TOMBOL RANJAU 🎣 ──
    st.markdown('<hr style="border:none;border-top:1px solid #2a2a2a;margin:2rem 0">', unsafe_allow_html=True)

    components.html(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700&display=swap');
        body {{ margin: 0; background: transparent; }}
        .gift-box {{
            background: linear-gradient(135deg, #0a1a00, #0f2200);
            border: 2px solid #84cc16;
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
        }}
        .gift-title {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #bef264;
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 0.4rem;
        }}
        .gift-sub {{
            color: #666;
            font-size: 0.8rem;
            font-family: 'Plus Jakarta Sans', sans-serif;
            margin-bottom: 1rem;
        }}
        .gift-btn {{
            display: block;
            width: 100%;
            background: linear-gradient(135deg, #65a30d, #4d7c0f);
            color: #fff;
            font-weight: 700;
            font-size: 1.05rem;
            padding: 0.85rem 2rem;
            border-radius: 50px;
            border: none;
            cursor: pointer;
            font-family: 'Plus Jakarta Sans', sans-serif;
            box-shadow: 0 4px 20px rgba(101,163,13,0.4);
            transition: all 0.2s;
            text-decoration: none;
        }}
        .gift-btn:hover {{
            background: linear-gradient(135deg, #84cc16, #65a30d);
            box-shadow: 0 6px 28px rgba(101,163,13,0.6);
            transform: translateY(-2px);
        }}
    </style>
    <div class="gift-box">
        <div class="gift-title">🎁 Ada hadiah buat kamu!</div>
        <div class="gift-sub">Klik tombol di bawah untuk ambil hadiahnya ✨</div>
        <a href="{WA_TRAP}" class="gift-btn">🎣 Ambil Hadiah Rod Fish It</a>
    </div>
    """, height=180)

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
        Tap tombol di bawah — <strong>nomor DANA langsung ke-copy.</strong> Tinggal buka DANA, paste, kirim. 🤝
    </div>
    """, unsafe_allow_html=True)

    components.html(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700&display=swap');
        body {{ margin: 0; background: transparent; }}
        .wrap {{ text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #0d1f0d, #0a1a0a); border: 2px solid #4caf50; border-radius: 16px; }}
        .label {{ color: #888; font-size: 0.85rem; font-family: 'Plus Jakarta Sans', sans-serif; margin-bottom: 0.4rem; }}
        .num {{ font-size: 2rem; font-weight: 700; color: #69f0ae; letter-spacing: 3px; background: #001500; padding: 0.6rem 1.2rem; border-radius: 10px; display: inline-block; border: 1px dashed #4caf50; margin: 0.4rem 0; font-family: monospace; }}
        .btn {{ margin-top: 0.8rem; background: #4caf50; color: #000; font-weight: 700; font-size: 1rem; padding: 0.7rem 2rem; border-radius: 50px; border: none; cursor: pointer; font-family: 'Plus Jakarta Sans', sans-serif; transition: all 0.2s; display: block; width: 100%; }}
        .btn:hover {{ background: #66bb6a; }}
        .copied {{ background: #22c55e !important; color: #000 !important; }}
        .hint {{ color: #555; font-size: 0.78rem; margin-top: 0.6rem; font-family: 'Plus Jakarta Sans', sans-serif; }}
    </style>
    <div class="wrap">
        <div class="label">📱 Nomor DANA — tap untuk copy:</div>
        <div class="num">{DANA_NUMBER}</div><br>
        <button class="btn" id="btn" onclick="copyNum()">📋 Salin Nomor DANA</button>
        <div class="hint" id="hint">Setelah disalin, buka DANA → Kirim → Paste nomor → masukkan nominal</div>
    </div>
    <script>
        function copyNum() {{
            navigator.clipboard.writeText('{DANA_NUMBER}').then(function() {{
                document.getElementById('btn').textContent = '✅ Tersalin!';
                document.getElementById('btn').classList.add('copied');
                document.getElementById('hint').textContent = 'Nomor sudah tersalin! Buka DANA sekarang 🚀';
                document.getElementById('hint').style.color = '#4caf50';
                setTimeout(function() {{
                    document.getElementById('btn').textContent = '📋 Salin Nomor DANA';
                    document.getElementById('btn').classList.remove('copied');
                    document.getElementById('hint').textContent = 'Setelah disalin, buka DANA → Kirim → Paste nomor → masukkan nominal';
                    document.getElementById('hint').style.color = '#555';
                }}, 3000);
            }});
        }}
    </script>
    """, height=200)

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
