import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="FestAI - التحليل الذكي", layout="wide")

# واجهة إدخال المفتاح بشكل آمن
with st.sidebar:
    st.title("🔐 الإعدادات")
    api_key = st.text_input("ادخل مفتاح OpenAI الجديد هنا:", type="password")
    st.info("ملاحظة: المفتاح يُستخدم فقط لتشغيل هذا التحليل ولا يتم خزنه بشكل دائم.")

st.title("📊 نظام FestAI للتحليل بعقلية الـ 1%")
st.markdown("---")

if not api_key:
    st.warning("الرجاء إدخال مفتاح الـ API في القائمة الجانبية لتشغيل النظام.")
else:
    client = OpenAI(api_key=api_key)
    
    col1, col2 = st.columns(2)
    with col1:
        p_name = st.text_input("اسم المشروع")
        sector = st.selectbox("القطاع", ["تكنولوجيا", "عقارات", "تجارة", "زراعة", "صناعة"])
    with col2:
        budget = st.text_input("الميزانية التقديرية")
        location = st.text_input("موقع التنفيذ (مثلاً: بغداد - الدورة)")

    desc = st.text_area("اشرح فكرة مشروعك بالتفصيل (شنو اللي يميزه؟)")

    if st.button("توليد التحليل الذكي ✨"):
        if p_name and desc:
            with st.spinner("جاري التفكير بعقلية الـ 1%..."):
                try:
                    prompt = f"حلل مشروع {p_name} في {location}. القطاع: {sector}. الميزانية: {budget}. الوصف: {desc}. كن صريحاً جداً وحلل الفرص والمخاطر."
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "system", "content": "أنت مستشار أعمال خبير، لا تجامل، أعطِ الحقائق المرة قبل الحلوة."},
                                 {"role": "user", "content": prompt}]
                    )
                    st.success("تم التحليل بنجاح!")
                    st.markdown("### 📝 النتائج:")
                    st.write(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"حدث خطأ: {e}")
        else:
            st.error("لازم تملأ اسم المشروع والوصف حتى أقدر أحللك اياه.")
