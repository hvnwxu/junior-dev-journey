import sys
import argparse

def main():
    """
    이 해법은 parser 사용법과 input 을 그대로 사용하는 방법 2가지가 모두 포함된 방법임
    """
    parser = argparse.ArgumentParser(
        description="arguments 사용"
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