import gradio as gr
import tensorflow as tf
import numpy as np

# ✅ 모델 로드 (학습 데이터 제거)
MODEL_PATH = "/content/drive/MyDrive/my_final_best_model.h5"  # Google Drive에서 모델 로드
model = tf.keras.models.load_model(MODEL_PATH)

# ✅ 표준화된 평균 & 표준편차 적용 (학습 데이터 필요 없음)
mean_X = np.array([4707.96, 0.24296, 0.15408, 0.69463, 0.18795, 0.44247])  # 입력값 평균
std_X = np.array([6345.97, 0.08511, 0.09024, 0.20482, 0.17395, 0.24592])  # 입력값 표준편차

mean_Y = np.array([106.55])  # 출력값 평균
std_Y = np.array([172.00])  # 출력값 표준편차

# ✅ 예측 함수 (학습 데이터 없이 실행 가능)
def predict_pv_with_grade(area, window_ratio, roof_U, wall_U, floor_U, target):
    """ 예측된 PV 설치 규모와 ZEB 인증 등급 반환 """

    # 표준화 변환 (평균 & 표준편차를 직접 사용)
    input_data = np.array([[area, window_ratio / 100 - 0.01, roof_U, wall_U, floor_U, target / 100]])
    input_scaled = (input_data - mean_X) / std_X  # 표준화 적용

    # 예측 수행
    predicted_pv_scaled = model.predict(input_scaled)
    predicted_pv = predicted_pv_scaled * std_Y + mean_Y  # 역변환 (표준화 해제)

    # ✅ ZEB 인증 등급 판별
    zeb_grade = (
        "ZEB 인증 1등급" if target >= 100 else
        "ZEB 인증 2등급" if 80 <= target < 100 else
        "ZEB 인증 3등급" if 60 <= target < 80 else
        "ZEB 인증 4등급" if 40 <= target < 60 else
        "ZEB 인증 5등급" if 20 <= target < 40 else
        "ZEB 인증 불가"
    )
    return f"{predicted_pv[0][0]:.2f} kW", zeb_grade

# ✅ Gradio UI 실행
iface = gr.Interface(
    fn=predict_pv_with_grade,
    inputs=[
        gr.Number(label="연면적 (m²)"), gr.Number(label="창면적비 (%)"),
        gr.Number(label="열관류율 (지붕, W/m²K)"), gr.Number(label="열관류율 (벽체, W/m²K)"),
        gr.Number(label="열관류율 (바닥, W/m²K)"), gr.Number(label="목표 에너지 자립률 (%)")
    ],
    outputs=[gr.Textbox(label="예측된 PV 설치 규모 (kW)"), gr.Textbox(label="ZEB 인증 등급")],
    title="ZEB PV 시스템 설치 규모 예측",
    description="건물 정보를 입력하면 태양광 설치 규모를 예측하고, ZEB 인증 등급을 제공합니다.",
)

iface.launch()
