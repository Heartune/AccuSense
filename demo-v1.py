import re


def load_sensitive_words(file_path):
    sensitive_words = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            sensitive_words.add(sline.strip())
    return sensitive_words


def replace_sensitive_words(text, sensitive_words):
    text = text.lower()
    for word in sensitive_words:
        pattern = re.compile(word, re.IGNORECASE)
        text = re.sub(pattern, '*' * len(word), text)
    return text


sensitive_words1 = load_sensitive_words('广告.txt')
sensitive_words2 = load_sensitive_words('色情类.txt')
sensitive_words3 = load_sensitive_words('网址.txt')

while True:
    inputText = input('请输入你要输入的语句：')
    output = replace_sensitive_words(inputText, sensitive_words1 | sensitive_words2 | sensitive_words3)
    print(output)
    print('输入exit以暂停程序')
    if inputText == 'exit':
        print('程序结束')
        break
