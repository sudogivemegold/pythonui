import streamlit as st
import requests as rq
import json

msg = st.text_input("rr", placeholder="!")

url = "https://webhook.site/1516b98c-e099-4876-aa0c-fba1d2035663"#이거 진짜서버주소로 바꿔라 다온아

# 보낼 데이터 (JSON 형식)
data = {
    "test": msg
}

if st.button("button"):
    response = rq.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    st.success("성공{msg}")
#python -m streamlit run web.py