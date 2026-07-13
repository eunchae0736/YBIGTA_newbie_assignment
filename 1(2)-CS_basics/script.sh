
# anaconda(또는 miniconda)가 존재하지 않을 경우 설치해주세요!
## TODO
if ! command -v conda &> /dev/null; then
    echo "[INFO] conda가 설치되어 있지 않습니다."
fi


# Conda 환셩 생성 및 활성화
## TODO
conda create -y -n myenv python=3.11
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate myenv

## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "[INFO] 가상환경 활성화: 성공"
else
    echo "[INFO] 가상환경 활성화: 실패"
    exit 1 
fi

# 필요한 패키지 설치
## TODO
pip install mypy

# Submission 폴더 파일 실행
cd submission || { echo "[INFO] submission 디렉토리로 이동 실패"; exit 1; }

for file in *.py; do
    ## TODO
    file_name=$(basename "$file" .py) #1_1260
    problem_num=${file_name#*_} #_제거하기 1260

    python "$file" \
    < "../input/${problem_num}_input" \
    > "../output/${problem_num}_output"

done

# mypy 테스트 실행 및 mypy_log.txt 저장
## TODO
mypy *.py > ../mypy_log.txt 2>&1

# conda.yml 파일 생성
## TODO
conda env export > ../conda.yml

# 가상환경 비활성화
## TODO
conda deactivate