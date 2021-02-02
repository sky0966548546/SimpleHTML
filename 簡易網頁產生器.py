import os
os.system('cls')
# 基礎設置
print('----------基礎設置----------\n')
os.chdir('c:/Downloads')
name = input('請輸入檔案名稱：')
files = name + '.html'
a = open(files, "w", encoding='utf8')
# 網頁基礎內容
title = input('請輸入網頁標題：')
a.write("<!DOCTYPE html>\n<html lang='zh_TW'>\n<head>\n<meta charset='utf-8' />\n")
a.write("<link rel='stylesheet' href='https://shark.bucky.tw/python.css' />\n")
title = "<title>"+title+"</title>\n</head>\n<body>\n<div class='kirito'>\n"
a.write(title)
print('\n----------網頁內容----------\n')
h1 = input('請輸入大標題：')
h3 = input('請輸入副標題：')
email = input('請輸入email：')
phone = input('請輸入電話號碼：')
h1 = '<h1>'+h1+'</h1>'
h3 = '<h3>'+h3+'</h3>'
email = '<p>我的email：'+email+'</p>'
phone = '<p>我的電話：'+phone+'</p>'
end = h1 + '\n' + h3 + '\n' + email + '\n' + phone + '\n'
a.write(end)
a.write('</div>\n</body>\n</html>')
print('\n----------製作完成----------\n')
print('Enter後檔案將儲存於c:/Downloads')
input()
