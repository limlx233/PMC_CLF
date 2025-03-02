import streamlit as st


pic1_path = "pics/Excel_Sheet名称.png"
pic2_path = "pics/字段.png"
pic3_path = "pics/唤醒app.png"


st.subheader("说明", divider="grey")
with st.container(border=True):
    st.write("1.要求上传Excel文件中应含有如图所示表单:")
    st.image(pic1_path)
    st.write("2.要求上传Excel文件中的Sheet应含有如图所示字段:")
    st.image(pic2_path)
    st.write("需包含:blue[日期、班级、产量定额、产量合计]四个必须字段。")
    st.write("3.:red[注意:]")
    st.write("当打开app如图表示程序处于休眠状态,点击下图蓝色按钮稍后即可唤醒。")
    st.image(pic3_path)
