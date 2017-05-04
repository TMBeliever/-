def GetGrade(username,password):
    from bs4 import BeautifulSoup
    from PIL import Image
    import pymongo
    import requests
    import json

    client = pymongo.MongoClient('localhost',27017)
    grade = client['grade']
    get_grade = grade['get_grade']
    get_grade.remove({})

    post_url = 'http://kdjw.hnust.cn/kdjw/Logon.do?method=logon'





    #username = '1405020221'#input('输入用户名：')
    #password = '026517'#input('输入密码：')
    fontMods = []
    for i in range(1, 4):
        fontMods.append((str(i), Image.open("./image/%d.bmp" % i)))
    fontMods.append(('b', Image.open("./image/b.bmp")))
    fontMods.append(('c', Image.open("./image/c.bmp")))
    fontMods.append(('m', Image.open("./image/m.bmp")))
    fontMods.append(('n', Image.open("./image/n.bmp")))
    fontMods.append(('v', Image.open("./image/v.bmp")))
    fontMods.append(('x', Image.open("./image/x.bmp")))
    fontMods.append(('z', Image.open("./image/z.bmp")))
    yzm = []
    url = 'http://kdjw.hnust.cn/kdjw/verifycode.servlet'
    s = requests.session()
    img = s.get(url)
    with open('1.png', 'wb') as file:
        file.write(img.content)
    im = Image.open('1.png').convert('1')
    for i in range(4):
        x = 3 + i * 10
        y = 4
        target = im.crop((x, y, x + 10, y + 12))
        points = []
        for mod in fontMods:
            diffs = 0
            for yi in range(12):
                for xi in range(10):
                    if mod[1].getpixel((xi, yi)) != target.getpixel((xi, yi)):
                        diffs += 1
            points.append((diffs, mod[0]))
        points.sort()
        yzm.append(points[0][1])
    yzm1 = yzm[0] + yzm[1] + yzm[2] + yzm[3]

    data = {
        'USERNAME': username,
        'PASSWORD': password,
        'RANDOMCODE': yzm1
    }

    s.post(post_url, data=data)
    data2 = {
        'xsfs': 'qbcj'
    }
    p = s.post('http://kdjw.hnust.cn/kdjw/xszqcjglAction.do?method=queryxscj',data=data2)
    soup = BeautifulSoup(p.text, 'lxml')
    courses = soup.select('.smartTr')
    list = []
    list1= []
    list2= []
    for course in courses:
        # time = course.select('td:nth-of-type(5)')
        data = {
            'score': course.select('td:nth-of-type(7)')[0].text,
            'course':course.select('td:nth-of-type(6)')[0].text,
            'time' : course.select('td:nth-of-type(5)')[0].text,
            'credit':course.select('td:nth-of-type(12)')[0].text
        }
        list.append(data)

    list.sort(key=lambda x: x.get('time'),reverse=True)
    i = 0
    while i < len(list)-1:
        list1.append(list[i])
        if not list[i]['time'] == list[i+1]['time']:
            list2.append(list1)
            list1 = []
        i += 1
    try:
        list1.append(list[-1])
        list2.append(list1)
       # for i in list2:
        #    for m in i:
         #       get_grade.insert_one(m)
        return list2
    except:
        return 1
GetGrade('1405020221','026517')