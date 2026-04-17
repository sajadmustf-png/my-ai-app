import streamlit as st
from openai import OpenAI

# ربط مفتاحك اللي دزيته مباشرة حتى ما يطلبه منك الموقع
client = OpenAI(api_key="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")

st.set_page_config(page_title="FestAI - نظام دراسة المشاريع", layout="wide")

st.title("📊 نظام FestAI للتحليل الذكي")
st.info("هذا النظام مبرمج لتحليل مشاريعك بعقلية الـ 1%")

# تقسيم الخانات حسب الصور اللي دزيتها (القائمة 1 و 2)
with st.expander("📝 خطوة 1 و 2: معلومات المشروع والسوق", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        p_name = st.text_input("اسم المشروع")
        sector = st.selectbox("القطاع", ["تكنولوجيا", "تجارة", "مطاعم", "عقارات", "زراعة"])
    with col2:
        desc = st.text_area("وصف المشروع (الفكرة والهدف)")
        stage = st.radio("مرحلة المشروع", ["فكرة", "تخطيط", "مرحلة مبكرة", "توسع"])

with st.expander("💰 خطوة 3 و 4: الموارد والمالية"):
    col3, col4 = st.columns(2)
    with col3:
        budget = st.text_input("الميزانية الإجمالية (بالدولار أو الدينار)")
        funding = st.multiselect("مصدر التمويل", ["ذاتي", "قرض", "مستثمرون"])
    with col4:
        staff = st.number_input("عدد الموظفين المتوقع", min_value=0)
        location = st.text_input("مكان المشروع (المدينة)")

with st.expander("⚖️ خطوة 5 و 6: القانون والتحليل"):
    legal = st.selectbox("حالة تسجيل النشاط", ["لم يبدأ", "قيد التنفيذ", "مكتمل"])
    risk = st.slider("مستوى تحمل المخاطر", 0, 100, 50)
    focus = st.multiselect("مجالات تركيز التحليل", ["مالي", "سوق", "تقني", "قانوني"])

# زر التشغيل
if st.button("توليد دراسة الجدوى بالذكاء الاصطناعي ✨"):
    if p_name and desc:
        with st.spinner("جاري التواصل مع الذكاء الاصطناعي..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "أنت خبير اقتصادي صريح جداً، تحلل المشاريع بعقلية الـ 1% وتكشف نقاط القوة والضعف بواقعية."},
                        {"role": "user", "content": f"حلل مشروع {p_name} في {location}. القطاع: {sector}. الميزانية: {budget}. الوصف: {description}. التركيز على: {focus}."}
                    ]
                )
                st.success("تم التحليل بنجاح!")
                st.markdown("### 📝 دراسة الجدوى الناتجة:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"خطأ في الاتصال: {e}")
    else:
        st.error("الرجاء إدخال اسم المشروع ووصفه على الأقل.")
