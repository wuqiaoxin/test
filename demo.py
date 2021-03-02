import requests
# response = requests.get(url="http://www.baidu.com")
# response.encoding = "utf-8"
# data = response.text
# f = open("百度.xml","w+",encoding="utf-8")
# f.write(data)


import unittest
class LoginTest(unittest.TestCase):

    def testLogin(self):
        # 准备数据
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet"
        data = {
            "method":"login",
            "loginname":"jason",
            "password":"admin"
        }
        # 调用被测接口
        expect = "狼腾"#期望数据
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
        data=response.text
        self.assertIn(expect,data)

    def testfindAllTeacher(self):
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllTeacher"
        data ={

        }
        expect = 200
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
#         取出状态码和响应数据
        code = response.status_code
        txt = response.text

#         断言
        print(txt)
        self.assertEqual(expect,code)

    def testSubmitEvaluate(self):
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=submitEvaluate"
        data = {

        }
        expect = 500
        response = requests.post(url=url,data=data)
        response.encoding ="utf-8"
        code = response.status_code
        txt = response.text

        print(txt)
        self.assertEqual(expect,code)

    def testModifyUserInfo(self):
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=modifyUserInfo"
        data = {"uid":"d67bee4a3058444480d73072fa333e62",
                "loginname":"wuqiaoxin",
                "username":"吴乔歆",
                "password":"123456",
                "age":"27",
                "sex":"女",
                "address":"",
                "phoneNumber":"18321456979",
                "email":"1981288305@qq.com",
                "carte":""
                }
        expect = "age"
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
        data=response.text
        self.assertIn(expect,data)

    def testFindAllStudent(self):
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllStudent"
        data = {

        }
        expect = "age"
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
        data=response.text
        self.assertIn(expect,data)

    def testFindByUsernameAndPhone(self):
        url = "http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findByUsernameAndPhone"
        data = {"username":"贾",
                "phoneNumber":""
                }
        expect = 500
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
        data = response.text
        code = response.status_code
        self.assertEqual(expect,code)

    def testFindAllCourse(self):
        url = "http://www.jasonisoft.cn:8080/HKR/CourseServlet?method=findAllCourse"
        data = {

        }
        expect = "测试开发"
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
        data = response.text
        self.assertIn(expect,data)

    def testReportAll(self):
        url = "http://www.jasonisoft.cn:8080/HKR/EvaluateServlet?method=reportAll"
        data = {

        }
        expect = 200
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
        code = response.status_code
        data = response.text
        self.assertEqual(expect,code)

    def testDetByDate(self):
        url = "http://www.jasonisoft.cn:8080/HKR/EvaluateServlet?method=getByDate"
        data = {

        }
        expect = 200
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
        code = response.status_code
        data=response.text
        self.assertEqual(expect,code)

    def testFindAllLog(self):
        url = "http://www.jasonisoft.cn:8080/HKR/LogServlet?method=findAllLog"
        data = {

        }
        expect =200
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
        data=response.text
        code = response.status_code
        self.assertEqual(expect,code)

    def testFindByDate(self):
        url = "http://www.jasonisoft.cn:8080/HKR/LogServlet?method=findByDate"
        data = {

        }
        expect = 200
        response = requests.post(url=url,data=data)
        response.encoding="utf-8"
        data=response.text
        code = response.status_code
        self.assertEqual(expect,code)
















