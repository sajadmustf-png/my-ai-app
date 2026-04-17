import streamlit as st
import google.generativeai as genai

# إعداد مفتاح الذكاء الاصطناعي اللي دزيته أنت
genai.configure(api_key="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")

st.set_page_config(page_title="محلل المشاريع الاحترافي", layout="wide")

st.title("📊 نظام دراسة الجدوى الذكي (AI)")

# تبويبات لتقسيم الخانات مثل الصور (7 خطوات)
tab1, tab2, tab3 = st.tabs(["المعلومات الأساسية والسوق", "العمليات والمالية", "التحليل النهائي"])

with tab1:
    st.subheader("Step 1 & 2: نظرة عامة والسوق")
    project_name = st.text_input("اسم المشروع", placeholder="مثال: مقهى ذكي")
    sector = st.selectbox("القطاع", ["تكنولوجيا", "أغذية ومشروبات", "تجارة إلكترونية", "تعليم", "صحة"])
    country = st.text_input("الدولة")
    description = st.text_area("وصف المشروع", help="صف فكرة مشروعك وأهدافه باختصار")
    target = st.multiselect("العملاء المستهدفون", ["أفراد (B2C)", "شركات (B2B)", "حكومة (B2G)", "مختلط"])
    market_size = st.radio("حجم السوق المقدر", ["صغير", "متوسط", "كبير", "كبير جداً"])

with tab2:
    st.subheader("Step 3 & 4: العمليات والموارد والمالية")
    staff_count = st.number_input("عدد الموظفين المطلوب", min_value=0)
    location_type = st.selectbox("الموقع الفعلي", ["عبر الإنترنت فقط", "مكتب صغير", "مستودع", "مصنع", "متجر"])
    total_budget = st.number_input("الميزانية الإجمالية (الإجمالي)", min_value=0)
    currency = st.selectbox("العملة", ["USD", "SAR", "IQD", "AED"])
    funding = st.multiselect("مصدر التمويل", ["تمويل ذاتي", "قرض بنكي", "مستثمرون", "منحة حكومية"])

with tab3:
    st.subheader("Step 5 & 6: الجوانب القانونية والتحليل")
    legal_status = st.selectbox("تسجيل النشاط التجاري", ["لم يبدأ", "قيد التنفيذ", "مكتمل"])
    risk_level = st.slider("تحمل المخاطر", 0, 100, 50) # معتدل
    focus_areas = st.multiselect("مجالات التركيز", ["مالي", "سوق", "تقني", "تشغيلي", "قانوني", "مخاطر", "بيئي"])
    report_lang = st.selectbox("لغة التقرير", ["Arabic", "English"])

# زر التشغيل ودمج الذكاء الاصطناعي
if st.button("توليد دراسة الجدوى باحترافية ✨"):
    if project_name and description:
        with st.spinner("انتظر ثواني.. الذكاء الاصطناعي يحلل بياناتك..."):
            model = genai.GenerativeModel('gemini-pro')
            prompt = f"""
            أنت خبير اقتصادي ومحلل مشاريع لـ 1% من نخبة المستثمرين. 
            حلل هذا المشروع: {project_name}.
            القطاع: {sector} في {country}.
            الوصف: {description}.
            الميزانية: {total_budget} {currency}.
            المخاطر: {risk_level}%.
            ركز في تحليلك على: {focus_areas}.
            اللغة المطلوبة للرد: {report_lang}.
            اجعل التحليل صريحاً جداً، واقعياً، ويفكر خارج الصندوق.
            """
            response = model.generate_content(prompt)
            st.success("تم التوليد بنجاح!")
            st.markdown("---")
            st.markdown(response.text)
    else:
        st.error("الرجاء ملء اسم المشروع ووصفه أولاً!")
