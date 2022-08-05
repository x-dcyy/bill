import pandas as pd
import streamlit as st
import cv2
import numpy as np
from io import StringIO
from datetime import datetime

st.header('基于Tensorflow的图像识别器')

#导入文件
uploaded_file = st.file_uploader('从图片路径上传图片',type='jpg')
if uploaded_file is not None:
    # 将传入的文件转为Opencv格式
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    # 展示图片
    st.image(opencv_image, channels="BGR")
    # 保存图片
    cv2.imwrite('test.jpg', opencv_image)

st.markdown('我猜它是：')

#边栏
from PIL import Image
image = Image.open('Flower_Fairy.jpg')
st.sidebar.image(image)

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "选择一个模型OR重新训练一个模型?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )