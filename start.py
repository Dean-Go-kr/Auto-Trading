import pyupbit

access = "dCE40RsS1wFjL9kuxSrZcqvosNoFq539RDRRYTdn"          # 본인 값으로 변경
secret = "mXHsfd0vSUsWO53BXx2P5mXVoBL1c6bnArIwUsKC"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)


print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))  

print('완료')