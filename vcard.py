

import streamlit as st
from datetime import date
import qrcode
import io

st.title("連絡帳への変換")

with st.form(key="vcardinfo"):
    family=st.text_input("姓:")
    name=st.text_input("名:")
    birth=st.date_input("生年月日:",
                        min_value=date(1900,1,1))
    email= st.text_input("E-mail:")
    button=st.form_submit_button("作成")

data=f"""BEGIN:VCARD
VERSION:3.0
N:{family};{name};;;
FN:{family} {name}
EMAIL:{email}
BDAY:{birth}
END:VCARD
"""

if button:
    img=qrcode.make(data)
    with io.BytesIO() as f:
        img.save(f,format="PNG")
        st.image(f.getvalue())
