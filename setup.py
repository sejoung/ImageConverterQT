from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ImageConverterQT",  # 패키지 이름
    version="0.1.0",  # 버전 (형식: major.minor.patch)
    description="This is a first packaging",  # 패키지 설명
    author="sejoung kim",  # 개발자 이름
    author_email="sejoung@google.com",  # 이메일
    url="https://github.com/sejoung/ImageConverterQT",  # GitHub 또는 프로젝트 링크
    packages=find_packages(where="src"),  # 패키지 자동 검색
    package_dir={"": "src"},  # 패키지 디렉토리 설정
    install_requires=requirements,  # 필수 의존성 패키지
    classifiers=[  # PyPI에서 패키지 정보 제공
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Machine Learning :: Generative AI",
    ],
    python_requires=">=3.10",  # 최소 지원 Python 버전
)
