import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
from datetime import datetime, timedelta

# ==========================================
# 1. PAGE CONFIGURATION & CSS (إعدادات الصفحة والتصميم)
# ==========================================
st.set_page_config(
    page_title="Yapay Zeka Dedektifleri | Fraud Detection",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تصميم احترافي CSS
st.markdown("""
    <style>
    /* تحسين شكل الأزرار */
    .stButton>button {
        border-radius: 8px;
        transition: 0.3s;
        border: 1px solid #4CAF50;
    }
    .stButton>button:hover {
        background-color: #4CAF50;
        color: white;
        transform: scale(1.02);
    }
    /* تحسين شكل المقاييس (Metrics) */
    div[data-testid="metric-container"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 5% 10%;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. SESSION STATE MANAGEMENT (إدارة حالة التطبيق)
# ==========================================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Ana Menü"

def navigate(page_name):
    st.session_state.current_page = page_name

# ==========================================
# 3. LOGIN PAGE (شاشة تسجيل الدخول D-1)
# ==========================================
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<h1 style='text-align: center;'>🕵️‍♂️ Yapay Zeka Dedektifleri</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: gray;'>Finansal Güvenlik ve Dolandırıcılık Tespit Sistemi</p>", unsafe_allow_html=True)
        st.divider()
        
        email = st.text_input("📧 E-posta", placeholder="ornek@firat.edu.tr")
        password = st.text_input("🔒 Şifre", type="password", placeholder="••••••••")
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🚀 Giriş Yap", use_container_width=True):
                with st.spinner("Sisteme bağlanılıyor..."):
                    time.sleep(1)
                st.session_state.logged_in = True
                st.rerun()
        with col_btn2:
            st.button("📝 Kayıt Ol", use_container_width=True)
            
        st.markdown("<p style='text-align: center; font-size: 12px; margin-top: 10px;'><a href='#'>Şifremi Unuttum</a></p>", unsafe_allow_html=True)

# ==========================================
# 4. MAIN APPLICATION (التطبيق الرئيسي بعد الدخول)
# ==========================================
else:
    # --- SIDEBAR (القائمة الجانبية D-2) ---
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3260/3260867.png", width=80)
        st.markdown("### 👨‍💻 Mustafa Alkhattab")
        st.caption("Kıdemli Veri Analisti")
        st.divider()
        
        if st.button("🏠 Ana Menü", use_container_width=True): navigate("Ana Menü")
        if st.button("📂 Yeni Analiz", use_container_width=True): navigate("Yeni Analiz")
        if st.button("📊 Aktif Raporlar", use_container_width=True): navigate("Aktif Raporlar")
        if st.button("📜 Tahmin Detayları", use_container_width=True): navigate("Tahmin Detayları")
        if st.button("⚙️ Hesap Ayarları", use_container_width=True): navigate("Ayarlar")
        
        st.divider()
        if st.button("🚪 Çıkış Yap", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    # --- ANA MENÜ (الشاشة الرئيسية) ---
    if st.session_state.current_page == "Ana Menü":
        st.title("🏠 Dashboard: Sistem Özeti")
        st.markdown("Yapay Zeka algoritmaları kullanarak elde edilen son veriler.")
        
        # Metrics (مؤشرات الأداء)
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Toplam İşlem", "12,450", "Yükselişte")
        m2.metric("Şüpheli İşlem", "342", "-12% (İyileşme)", delta_color="inverse")
        m3.metric("Önlenen Zarar", "₺1.2M", "+₺50K")
        m4.metric("Model Doğruluğu", "%96.8", "+0.4%")

        st.divider()

        # Charts (رسوم بيانية تفاعلية)
        col_chart1, col_chart2 = st.columns([2, 1])
        
        with col_chart1:
            st.subheader("📈 Son 7 Günlük İşlem Hacmi")
            dates = [datetime.today() - timedelta(days=i) for i in range(7)][::-1]
            normal_tx = np.random.randint(1000, 2000, 7)
            fraud_tx = np.random.randint(10, 50, 7)
            
            df_trend = pd.DataFrame({'Tarih': dates, 'Normal İşlem': normal_tx, 'Şüpheli İşlem': fraud_tx})
            fig_line = px.line(df_trend, x='Tarih', y=['Normal İşlem', 'Şüpheli İşlem'], 
                               color_discrete_sequence=['#2ecc71', '#e74c3c'],
                               markers=True)
            st.plotly_chart(fig_line, use_container_width=True)
            
        with col_chart2:
            st.subheader("🛡️ Risk Dağılımı")
            fig_pie = px.pie(values=[95, 3, 2], names=['Güvenli', 'İncelemede', 'Dolandırıcılık'], 
                             hole=0.4, color_discrete_sequence=['#2ecc71', '#f1c40f', '#e74c3c'])
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie, use_container_width=True)

    # --- YENİ ANALİZ (رفع البيانات D-3 & D-4) ---
    elif st.session_state.current_page == "Yeni Analiz":
        st.title("📂 Yeni Analiz: Veri Yükleme ve Konfigürasyon")
        
        tab1, tab2 = st.tabs(["📁 Dosya Yükle", "🗄️ Veritabanı Bağlantısı"])
        
        with tab1:
            st.markdown("Lütfen analiz edilecek kredi kartı veri setini yükleyin (.csv veya .json)")
            uploaded_file = st.file_uploader("", type=["csv", "json"])
            
            if uploaded_file:
                st.success(f"✅ {uploaded_file.name} başarıyla yüklendi!")
                st.divider()
                
                st.subheader("⚙️ Analiz Konfigürasyonu (D-4)")
                col1, col2 = st.columns(2)
                with col1:
                    hedef = st.selectbox("1. Analiz Hedefi Seç", ["Tahmin (Prediction)", "Sınıflandırma (Classification)"])
                    model = st.selectbox("3. Kullanılacak Model", ["Lojistik Regresyon", "Karar Ağacı (Decision Tree)", "Random Forest"])
                with col2:
                    sutun = st.selectbox("2. Hedef Sütunu Seç", ["Is_Fraud", "Class", "Risk_Score"])
                    split = st.slider("4. Eğitim/Test Veri Ayrımı", 50, 90, 80)
                
                if st.button("🚀 Makine Öğrenmesi Analizini Başlat", type="primary", use_container_width=True):
                    progress_text = "Veriler ön işleniyor (Data Preprocessing)..."
                    my_bar = st.progress(0, text=progress_text)
                    for percent_complete in range(100):
                        time.sleep(0.02)
                        if percent_complete == 40:
                            my_bar.progress(percent_complete + 1, text="Modeller eğitiliyor (Model Training)...")
                        elif percent_complete == 80:
                            my_bar.progress(percent_complete + 1, text="Sonuçlar değerlendiriliyor...")
                        else:
                            my_bar.progress(percent_complete + 1)
                    
                    st.balloons()
                    st.success("🎉 Analiz başarıyla tamamlandı!")
                    time.sleep(1)
                    navigate("Aktif Raporlar")
                    st.rerun()

    # --- AKTİF RAPORLAR (النتائج D-5) ---
    elif st.session_state.current_page == "Aktif Raporlar":
        st.title("📊 Analiz Sonuçları ve Tahmin Paneli")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Tahmin Edilen Olay Sayısı", "8,432")
        c2.metric("Ortalama Güven Skoru", "%92.5")
        c3.metric("Tespit Edilen Şüpheli", "142")
        
        st.divider()
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("🔍 Önemli Öngörüler (Feature Importance)")
            features = pd.DataFrame({
                'Özellik': ['İşlem Tutarı (Amount)', 'Zaman (Time)', 'V14', 'V4', 'Konum (Location)'],
                'Etki Değeri': [93, 75, 62, 55, 27]
            })
            fig_bar = px.bar(features, x='Etki Değeri', y='Özellik', orientation='h', color='Etki Değeri', color_continuous_scale='Reds')
            fig_bar.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig_bar, use_container_width=True)
            
        with col2:
            st.subheader("🚨 Acil İncelenmesi Gereken İşlemler")
            # جدول بيانات تفاعلي
            suspicious_data = pd.DataFrame({
                'İşlem ID': ['#TRX-9982', '#TRX-9901', '#TRX-8732', '#TRX-1123'],
                'Tutar': ['₺15,000', '₺8,450', '₺12,000', '₺45,000'],
                'Risk Oranı': ['%98', '%94', '%89', '%85'],
                'Durum': ['Kritik', 'Yüksek', 'Yüksek', 'Orta']
            })
            st.dataframe(suspicious_data, use_container_width=True)
            if st.button("Tüm Detayları Gör"):
                navigate("Tahmin Detayları")
                st.rerun()

    # --- TAHMİN DETAYLARI (التفاصيل D-6) ---
    elif st.session_state.current_page == "Tahmin Detayları":
        st.title("🔍 Tahmin Detayları (İşlem İncelemesi)")
        
        st.info("Aşağıdaki işlem yapay zeka tarafından **Kritik Riskli** olarak işaretlenmiştir.")
        
        col_det1, col_det2 = st.columns([1, 1])
        with col_det1:
            st.markdown("### İşlem Kartı")
            st.write("---")
            st.markdown("**[Tahmin ID: #TRX-9982]**")
            st.markdown("💰 **Fatura Tutarı:** 15,000 TL")
            st.markdown("📍 **Konum:** İstanbul / Türkiye")
            st.markdown("🕒 **İşlem Tarihi:** 15/05/2026 - 02:45 AM")
            st.markdown("💳 **Kullanılan Cihaz:** Bilinmeyen IP Adresi")
            
        with col_det2:
            st.markdown("### Yapay Zeka Kararı")
            st.write("---")
            
            # مقياس الخطورة
            fig_gauge = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = 98,
                title = {'text': "Şüpheli İşlem Olasılığı"},
                gauge = {'axis': {'range': [0, 100]},
                         'bar': {'color': "darkred"},
                         'steps' : [
                             {'range': [0, 50], 'color': "lightgreen"},
                             {'range': [50, 80], 'color': "gold"},
                             {'range': [80, 100], 'color': "salmon"}]}
            ))
            fig_gauge.update_layout(height=250)
            st.plotly_chart(fig_gauge, use_container_width=True)
            
        st.divider()
        col_act1, col_act2, col_act3 = st.columns(3)
        with col_act1:
            if st.button("✅ Güvenli İşaretle (Onayla)", use_container_width=True):
                st.success("İşlem güvenli olarak veritabanına kaydedildi.")
        with col_act2:
            if st.button("❌ Dolandırıcılık Olarak İşaretle", type="primary", use_container_width=True):
                st.error("Kart bloke edildi ve yetkililere bildirildi!")
        with col_act3:
            st.button("Müşteriyle İletişime Geç", use_container_width=True)

    # --- AYARLAR (الإعدادات) ---
    elif st.session_state.current_page == "Ayarlar":
        st.title("⚙️ Hesap ve Sistem Ayarları")
        
        st.subheader("Görünüm Ayarları")
        st.info("💡 **Dark/Light Mode:** Sağ üst köşedeki (⋮) menüsüne tıklayın > Settings > Theme kısmından karanlık veya aydınlık modu seçebilirsiniz.")
        
        st.subheader("Bildirim Ayarları")
        st.toggle("Yeni şüpheli işlem algılandığında E-posta gönder", value=True)
        st.toggle("Sistem raporlarını haftalık olarak indir", value=False)
        
        st.divider()
        st.subheader("Tehlikeli Alan")
        if st.button("Veritabanı Önbelleğini Temizle"):
            st.warning("Önbellek temizlendi!")