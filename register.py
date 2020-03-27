import requests
import random
import time


char1 = "1234567890"
char2 = "qwertyuiopasdfghjklzxcvbnm"
char3 = "QWERTYUIOPASDFGHJKLZXCVBNM"

while True:
    try:
        account = ""
        password = "@"

        for i in range(0, 8):
            account += random.choice(char2)
            password += random.choice(char1) + random.choice(char2) + random.choice(char3)

        print(account, password)
        email = input("email(enter q to quit): ")

        if email == "q":
            break

        r = requests.post("https://accounts.goorm.io/api/signup/send_verification_email", data={
            "email_for_verification": email
        })

        response = r.json()
        print(response)
        if not response['result']:
            raise Exception("无效的邮箱.")

        while True:
            r = requests.post("https://accounts.goorm.io/api/signup", json={
                "email": email,
                "pw": password,
                "name": account,
                "mailing": False,
                "signup_language": "zh-CN",
                "role": "student",
                "ticket": "",
                "currentDate": time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime()),
                "inviteCode": "",
                "host": "ide"
            })

            response = r.json()
            print(response)
            if not response['result']:
                if response['code'] == 1004:
                    print("等待验证邮箱...")
            else:
                break
            time.sleep(5)

        print("注册成功!")
        with open("account_" + account + ".txt", "w") as f:
            f.write(account + "-" + password + "-" + email)

    except Exception as e:
        print("Error: " + str(e))
