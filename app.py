import gradio as gr
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# ✅ 모델 & 데이터 로드 (현재 Colab 경로에 맞춤)
model = tf.keras.models.load_model("/content/drive/MyDrive/my_final_best_model.h5")
df = pd.read_excel("/content/drive/MyDrive/학습.xlsx", sheet_name="차트_정리")

# ✅ 데이터 정규화
scaler_X = StandardScaler().fit(df[['연면적', '창면적비', '열관류율_지붕', '열관류율_벽체', '열관류율_바닥', '에너지 자립률']])
scaler_Y = StandardScaler().fit(df[['PV 설치 규모']])

# ✅ 예측 함수
def predict_pv_with_grade(area, window_ratio, roof_U, wall_U, floor_U, target):
    """ 예측된 PV 설치 규모와 ZEB 인증 등급 반환 """
    input_data = np.array([[area, window_ratio / 100 - 0.01, roof_U, wall_U, floor_U, target / 100]])
    input_scaled = scaler_X.transform(input_data)
    predicted_pv_scaled = model.predict(input_scaled)
    predicted_pv = scaler_Y.inverse_transform(predicted_pv_scaled)

    # ✅ ZEB 인증 등급 판별
    if target >= 100:
        zeb_grade = "ZEB 인증 1등급"
    elif 80 <= target < 100:
        zeb_grade = "ZEB 인증 2등급"
    elif 60 <= target < 80:
        zeb_grade = "ZEB 인증 3등급"
    elif 40 <= target < 60:
        zeb_grade = "ZEB 인증 4등급"
    elif 20 <= target < 40:
        zeb_grade = "ZEB 인증 5등급"
    else:
        zeb_grade = "ZEB 인증 불가"

    return f"{predicted_pv[0][0]:.2f} kW", zeb_grade

# ✅ Gradio 인터페이스 생성
iface = gr.Interface(
    fn=predict_pv_with_grade,
    inputs=[
        gr.Number(label="연면적 (m²) (연면적 500 이상)"),
        gr.Number(label="창면적비 (%) (평균값 24.3%)"),
        gr.Number(label="열관류율 (지붕, W/m²K) (평균값 0.154)"),
        gr.Number(label="열관류율 (벽체, W/m²K) (평균값 0.195)"),
        gr.Number(label="열관류율 (바닥, W/m²K) (평균값 0.188)"),
        gr.Number(label="목표 에너지 자립률 (%) (자립률 20 이상)")
    ],
    outputs=[
        gr.Textbox(label="예측된 PV 설치 규모 (kW)"),
        gr.Textbox(label="ZEB 인증 등급")
    ],
    title="ZEB PV 시스템 설치 규모 예측",
    description="건물 정보를 입력하면 태양광 설치 규모를 예측하고, ZEB 인증 등급을 제공합니다.",
    theme="default"
)

# ✅ Gradio 실행
iface.launch(share=True)