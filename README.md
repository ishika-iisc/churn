# Customer Churn Prediction API

A machine learning API built with FastAPI that predicts customer churn using a Random Forest classifier. The project includes data preprocessing, model training, and a REST API for real-time predictions.

## Project Structure

```
churn_prediction/
├── app/                    # FastAPI application
│   ├── main.py            # API endpoints
│   ├── model_loader.py    # Model loading utilities
│   ├── schema.py          # Data validation schemas
│   └── __init__.py
├── data/                  # Dataset and processed data
│   ├── Teleco-Customer-churn.csv
│   ├── X_train.csv
│   ├── X_test.csv
│   ├── y_train.csv
│   └── y_test.csv
├── model/                 # Trained models
│   ├── churn_model.pkl
│   └── features.pkl
├── notebooks/             # Jupyter notebooks for EDA
├── plots/                 # Generated visualizations
├── preprocess.py          # Data preprocessing script
├── train_model.py         # Model training script
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
└── README.md
```

## How We Built This Project

### 1. Data Preprocessing (`preprocess.py`)
- Loaded telecom customer data from CSV
- Handled missing values in TotalCharges column
- Removed duplicates and customer IDs
- Created visualizations for numeric features vs churn
- Encoded categorical variables using one-hot encoding
- Split data into training and testing sets (80/20)

### 2. Model Training (`train_model.py`)
- Used Random Forest Classifier with 100 estimators
- Trained on preprocessed data
- Evaluated model performance with accuracy and classification report
- Saved trained model and feature list using joblib

### 3. API Development (`app/`)
- Built FastAPI application with prediction endpoint
- Created data validation schemas
- Implemented model loading utilities
- Added health check endpoint

## Setup and Installation

### Prerequisites
- Python 3.10+
- Git
- Docker (optional)

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd churn_prediction
```

### Step 2: Create Virtual Environment

**Linux/macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows Command Prompt:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**Windows PowerShell:**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Project

### Option 1: Run Locally

1. **Preprocess Data:**
```bash
python preprocess.py
```

2. **Train Model:**
```bash
python train_model.py
```

3. **Start API Server:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

4. **Access API:**
- API: http://localhost:8000
- Documentation: http://localhost:8000/docs

### Option 2: Run with Docker

1. **Build Docker Image:**
```bash
docker build -t ml-api .
```

2. **Run Container:**
```bash
docker run -p 8000:8000 ml-api
```

## API Usage

### Health Check
```bash
curl http://localhost:8000/
```

### Make Prediction
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "tenure": 12,
       "MonthlyCharges": 70.5,
       "TotalCharges": 846.0,
       "gender_Male": 1,
       "SeniorCitizen": 0,
       "Partner_Yes": 1,
       "Dependents_Yes": 0
     }'
```

## AWS Deployment (Optional)

### Configure AWS CLI
```bash
aws configure
# Enter your access key and secret key when prompted
```

### Verify AWS Configuration
```bash
aws sts get-caller-identity
```

## Development Tools

### GitHub CLI Setup
**Windows (PowerShell as Administrator):**
```powershell
winget install --id GitHub.cli
```

**Verify Installation:**
```bash
gh --version
gh auth login
```

## Model Performance

The Random Forest model achieves good performance on the telecom churn dataset:
- Uses 100 decision trees
- Handles both numerical and categorical features
- Provides feature importance insights
- Robust against overfitting

## Dependencies

- **pandas**: Data manipulation
- **numpy**: Numerical operations
- **scikit-learn**: Machine learning algorithms
- **matplotlib/seaborn**: Data visualization
- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **joblib**: Model serialization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.
