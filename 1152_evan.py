import sys
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="범용 NMAPE 개선 분석 보고서 생성 스크립트"
    )

    parser.add_argument(
        "--text", required=False
    )
    args = parser.parse_args()

    text = args.text
    print(f"text: {args.text}")
    if text is None:
        input = sys.stdin.readline
        text = input()
    
    line = text.strip()
    words = line.split()

    print(f"text: {text}")
    print(len(words))


if __name__ == "__main__":
    main()