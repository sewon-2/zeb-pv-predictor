# 🚀 ZEB PV 시스템 설치 규모 예측 모델

## 📌 프로젝트 소개
사용자가 **건축 설계 스펙과 목표 자립률을 입력**하면, ZEB 인증 기준에 따라 **적정 태양광(PV) 설치 규모를 예측**하는 웹 서비스입니다.
웹 UI는 **Gradio**를 활용하여 간편한 입력 방식으로 예측이 가능하며,  
**사전 학습된 AI 모델을 로드하여 실시간 예측을 수행**합니다.  

## 🛠 사용 기술
- **프레임워크**: Gradio (웹 UI)  
- **머신러닝 모델**: TensorFlow (Keras 기반)  
- **데이터 처리**: NumPy, Scikit-learn  
- **모델 배포 환경**: Google Colab  

## 📂 프로젝트 구조
```
📁 프로젝트 폴더 
├── 📄 app.py # Gradio 기반 웹 서비스 코드 
├── 📄 README.md # 프로젝트 설명 문서 
├── 📄 requirements.txt # 필요한 라이브러리 목록 
└── 📄 my_final_best_model.h5 # 사전 학습된 AI 모델 (GitHub에 업로드)
```

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
GitHub에 업로드된 my_final_best_model.h5 파일을 실행 환경에 다운로드해야 합니다.
Colab에서 실행할 경우, /content/ 경로에 업로드하면 됩니다.
```python
from google.colab import files
uploaded = files.upload()  # 직접 파일 업로드
```
또는, GitHub에서 직접 다운로드하려면:
```bash
wget https://github.com/sewon-2/zeb-pv-predictor/releases/download/model/my_final_best_model.h5
```

### 4️⃣ Gradio 인터페이스 실행
```bash
python app.py
```

### 5️⃣ 웹 브라우저에서 실행
Gradio 실행 후 터미널에 표시된 public URL을 복사하여 웹 브라우저에서 접속하면 서비스를 사용할 수 있습니다.
예제:
Running on public URL: https://xxxxx.gradio.live


## 📊 모델 학습 데이터
- 표준화된 평균 & 표준편차 적용
- 입력값 (X): 연면적, 창면적비, 열관류율(지붕/벽체/바닥), 목표 자립률
- 출력값 (Y): PV 설치 규모

## 📋 표준화된 평균 및 표준편차
- 입력값 평균: [4707.96, 0.2429, 0.154, 0.6946, 0.1879, 0.4424]
- 입력값 표준편차: [6345.97, 0.0851, 0.0902, 0.2048, 0.1739, 0.2459]
- 출력값 평균: [106.55]
- 출력값 표준편차: [172.00]

## 📌 주요 기능
- ✅ ZEB 인증 기준 기반 예측  
- ✅ 표준화된 데이터 적용으로 실행 최적화  
- ✅ Gradio UI를 통한 간편한 사용자 입력  

## 📌 추가 정보
이 프로젝트는 Google Colab에서 실행될 수 있으며,
GitHub에는 모델 파일과 코드만 업로드되어 있습니다.
Colab 환경에서 실행 시, my_final_best_model.h5 파일을 /content/ 경로에 업로드한 후 실행해야 합니다.
