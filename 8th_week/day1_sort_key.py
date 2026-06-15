fruit_inventory = [
    ["사과", 50, 12],
    ["바나나", 120, 15],
    ["딸기", 30, 14],
    ["수박", 15, 11],
    ["포도", 80, 16]
]

# 💡 잘 동작하는 코드야! 한 가지만 알아두면 좋을 것 같아.
#    -x[2] 처럼 음수를 붙이는 방법 말고, reverse=True 라는 옵션도 있어.
#    .sort(key=lambda x: x[2], reverse=True) 이렇게 쓰면
#    "2번 인덱스 기준으로 내림차순 정렬해줘" 라고 더 직접적으로 표현할 수 있어.
#    결과는 완전히 똑같으니까, 나중에 한번 바꿔서 테스트해봐!
fruit_inventory.sort(key=lambda x: -x[2])
print(fruit_inventory)
