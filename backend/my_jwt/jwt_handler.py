import jwt,time

key = "sadnasl"
verification_failed_err = 'Signature verification failed'
time_out_err = 'Signature has expired'
# // 包括需要传递的用户信息；
# { "iss": "Online JWT Builder",       #该JWT的签发者，是否使用是可选的；
#   "iat": 1416797419,                #在什么时候签发的(UNIX时间)，是否使用是可选的；
#   "exp": 1448333419,                #什么时候过期，这里是一个Unix时间戳，是否使用是可选的；
#   "aud": "www.gusibi.com",           #接收该JWT的一方，是否使用是可选的；
#   "sub": "uid",                        #该JWT所面向的用户，是否使用是可选的；
#   "nickname": "goodspeed",
#   "username": "goodspeed",
#   "scopes": [ "admin", "user" ]
# }
def create_token(wx_number, t):
    # wx_number：微信号
    # time：有效时间，以秒为单位
    payload = {
        "iss": "VoiceAcquisition",
        "iat": int(time.time()),
        "exp": int(time.time()) + t,
        "wx_number": wx_number,
    }
    token = jwt.encode(payload, key, algorithm='HS256').decode('utf-8')
    return token


def verify_token(tk):
    try:
        info = jwt.decode(tk, key, True, algorithm='HS256') # 第三个参数为true则进行校验，为False则不进行校验
        return True, info
    except Exception as e:
        return False, e.__str__()