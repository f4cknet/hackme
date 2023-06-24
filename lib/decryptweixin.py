from lib.WXBizDataCrypt import WXBizDataCrypt

def decrypt(appid,sessionKey,encryptedData,iv):
    pc = WXBizDataCrypt(appid,sessionKey)
    result = pc.decrypt(encryptedData,iv)
    return result