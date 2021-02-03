import os
os.system('cls')
# 基礎設置(html)
print('----------基礎設置----------\n')
os.chdir('c:/Downloads')
name = input('請輸入檔案名稱：')
html = name + '.html'
chdir = 'c:/Downloads/'+name
os.mkdir(name)
os.chdir(chdir)
a = open(html, "w", encoding='utf8')
# 網頁基礎內容(body)
title = input('請輸入網頁標題：')
a.write("<!DOCTYPE html>\n<html lang='zh_TW'>\n<head>\n<meta charset='utf-8' />\n")
a.write("<link rel='stylesheet' href='style.css' />\n")
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
# 網頁樣式(css)
print('\n----------網頁樣式----------\n')
a = open('style.css', "w", encoding='utf8')
family = input('請輸入網頁字體：')
family = 'font-family:'+family+';\n'
bgc1 = input('請輸入主背景色：')
bgc1 = 'background-color:'+bgc1+';\n'+'}\n\n.kirito{\n'
bgc2 = input('請輸入副背景色：')
bgc2 = 'background-color:'+bgc2+';\n'
color = input('請輸入字體顏色：')
color = 'color:'+color+';\n}\n\n.kirito h1{\ntext-transform:uppercase;\n}'
a.write('body{\n')
a.write(family)
a.write(bgc1)
a.write(bgc2)
a.write('width:300px;\npadding:40px;\nposition:absolute;\ntop:50%;\nleft:50%;\ntransform:translate(-50%,-50%);\n')
a.write(color)
print('\n----------製作完成----------\n')
print('Enter後檔案將儲存於c:/Downloads')
input()
