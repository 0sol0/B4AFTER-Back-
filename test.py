add_code = 25390 # book[7]
n = str(add_code)[-3]

# def categoryes(n):
if n == '0':
    c = '총류'
elif n == '1':
    c = '철학, 심리학, 윤리학'
elif n == '2':
    c = '종교'
elif n == '3':
    c = '사회 과학'
elif n == '4':
    c = '자연 과학'
elif n == '5':
    c = '기술 과학'
elif n == '6':
    c = '예술'
elif n == '7':
    c = '언어'
elif n == '8':
    c = '문학'
elif n == '9':
    c = '역사, 지리, 관광'
else:
    c = '기타'
category = c


# category = categoryes(n)

print(category)