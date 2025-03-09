# 🚀 ZEB PV 시스템 설치 규모 예측 모델

## 📌 프로젝트 소개
사용자가 간단한 **건축 설계 스펙 및 목표 자립률을 입력**하면, **제로에너지건축물(ZEB)인증 규격에 근거하는 재생에너지 설비 규모를 도출**하는 웹 서비스 
웹 UI는 **Gradio**를 활용하여 간편한 입력 방식으로 예측이 가능하며,  
**Google Drive에 저장된 학습된 AI 모델과 데이터 파일을 불러와 연산을 수행**합니다.  

## 🛠 사용 기술
- **프레임워크**: Flask (백엔드), Gradio (웹 UI)  
- **머신러닝 모델**: TensorFlow (Keras 기반)  
- **데이터 처리**: pandas, scikit-learn  
- **저장소**: Google Drive (모델 및 학습 데이터 저장)  

## 📂 프로젝트 구조
```
📁 프로젝트 폴더 
├── 📄 app.py # Gradio 기반 웹 서비스 코드 
├── 📄 README.md # 프로젝트 설명 문서 
└── 📄 requirements.txt # 필요한 라이브러리 목록
```
  **⚠️ 주의:**  
  AI 모델 파일 (`my_final_best_model.h5`)과 학습 데이터 파일 (`학습.xlsx`)은 **Google Drive에서 직접 불러오도록 설정됨**  
  따라서, 실행 전 **해당 파일이 Google Drive에 업로드되어 있어야 합니다.**  

## 🚀 실행 방법
### 1️⃣ 저장소 클론
```bash
git clone https://github.com/sewon-2/zeb-pv-predictor.git
cd zeb-pv-predictor
```

### 2️⃣ 가상 환경 설정 및 패키지 설치
```bash
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

### 3️⃣ Google Drive에서 모델 & 데이터 로드
Google Colab에서 실행할 경우, Google Drive를 마운트해야 합니다.
```python
from google.colab import drive
drive.mount('/content/drive')
```

### 4️⃣ Gradio 인터페이스 실행
```bash
python app.py
```

### 5️⃣ 웹 브라우저에서 실행
[http://127.0.0.1:5000/](http://127.0.0.1:5000/) 에 접속하여 서비스 확인

## 📊 모델 학습 데이터
- 데이터셋 파일: 학습.xlsx (Google Drive에 저장)
- 학습 변수:
  - 입력값: 연면적, 창면적비, 열관류율(지붕/벽체/바닥), 목표 자립률
  - 출력값: PV 설치 규모

## 📌 추가 정보
✅ 이 프로젝트는 Google Colab + Gradio 기반으로 실행되며, AI 모델과 학습 데이터는 Google Drive에서 직접 불러옵니다.
✅ GitHub에는 코드만 업로드되어 있으며, 실행 시 Google Drive에서 필요한 리소스를 로드하는 방식입니다.
✅ Gradio 실행 시 브라우저가 자동으로 열리므로, 별도로 Flask 서버를 실행할 필요가 없습니다.
