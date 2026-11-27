from pathlib import Path

import pandas as pd

def 정제(df):
	정제본 = df.copy()

	# 점수가 비어 있는 행을 삭제한다.
	정제본 = 정제본.dropna(subset=["점수"])
	print(f"결측 점수 제거 후: {len(정제본)}행")

	# 모든 열의 값이 같은 중복 행을 삭제한다.
	정제본 = 정제본.drop_duplicates()
	print(f"중복 행 제거 후: {len(정제본)}행")

	# 반과 과목의 앞뒤 공백을 제거한다.
	정제본["반"] = 정제본["반"].str.strip()
	정제본["과목"] = 정제본["과목"].str.strip()
	print(f"공백 제거 후: {len(정제본)}행")

	# 점수를 정수로 바꾸고 0~100 범위 밖의 행을 삭제한다.
	정제본["점수"] = 정제본["점수"].astype(int)
	정제본 = 정제본[정제본["점수"].between(0, 100)]
	print(f"점수 범위 확인 후: {len(정제본)}행")

	return 정제본.reset_index(drop=True)

import pandas as pd

df = pd.read_csv(Path(__file__).with_name("scores_2026.csv"))
df=정제(df)


# 수학, 영어, 프로그래밍 과목의 1반과 2반만 남기기
df = df[
	df["과목"].isin(["수학", "영어", "프로그래밍"])
	& df["반"].isin(["1반", "2반"])
]
print(f"세 과목과 두 반만 남긴 후: {len(df)}행")

# 반별 통계
반별_통계 = df.groupby("반")["점수"].agg(["count", "mean", "median", "max"]).round(2)
print("반별 통계")
print(반별_통계)

# 과목별 통계
과목별_통계 = df.groupby("과목")["점수"].agg(["count", "mean", "median", "max"]).round(2)
print("과목별 통계")
print(과목별_통계)
