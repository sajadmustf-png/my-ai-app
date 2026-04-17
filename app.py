import streamlit as st
from openai import OpenAI

# هذا مفتاحك اللي شفته بالتحذير.. حطيته الك هنا حتى يشتغل فوراً
client = OpenAI(api_key="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")

st.set_page_config(page_title="FestAI - 1% Mindset", layout="wide")

st.title("📊 نظام FestAI للتحليل الذكي")
st.markdown("---")

# الخانات اللي ردتها بالصور
col1, col2 = st.columns(2)
with col1:
    p_name = st.text_input("اسم المشروع")
    sector = st.selectbox("القطاع", ["تكنولوجيا", "عقارات", "تجارة", "زراعة"])
with col2:
    budget = st.text_input("الميزانية")
    location = st.text_input("المكان (بغداد/الدورة مثلاً)")

desc = st.text_area("وصف الفكرة (اشرح مشروعك هنا)")

if st.button("توليد التحليل بالذكاء الاصطناعي ✨"):
    if p_name and desc:
        with st.spinner("جاري التحليل بعقلية الـ 1%..."):
            try:
                prompt = f"حلل مشروع {p_name} في {location}. الميزانية: {budget}. الوصف: {desc}. اعطني نصيحة صريحة جداً."
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                st.success("النتيجة:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"اكو مشكلة بالمفتاح أو الاتصال: {e}")
    else:
        st.warning("املأ اسم المشروع والوصف أولاً.")
