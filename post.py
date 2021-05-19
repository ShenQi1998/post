import requests
import json
import time

rootPath = r"C:\脚本\post\输出报文/"

if __name__=="__main__":
   
   SVC_TRAN_CODE='2003'

   url = "http://188.177.176.97:9013"

   timeStamp = str(int(time.time()))
   SEQ_NO = "SQ_SEQ_NO" + timeStamp
   REQ_SEQ_NO = "SQ_REQ_SEQ_NO" + timeStamp

   data={
      "BODY":{
         
      },
      "SYS_HEAD":{

      },
      "APP_HEAD":{

      }
   }

   startTime = int(round(time.time()*1000))
   res = requests.post(url=url,json=data).json()
   endTime = int(round(time.time()*1000))

   requestBody = json.dumps(data,sort_keys=True,ensure_ascii=False,indent=2)
   All = json.dumps(res,sort_keys=True,ensure_ascii=False,indent=2)
   Body = json.dumps(res,sort_keys=True,ensure_ascii=False,indent=2)
   State = json.dumps(res["SYS_HEAD"]["RSP_CODE"],sort_keys=Trueensure_ascii=False,indent=2)
   State = State.replace('"','')

   if State == "S":
      print(Body)
      print('交易结果：成功')
   else:
      print(All)
      print('交易结果：成功')

   date = time.strftime("%Y%m%d",time.localtime())
   print(SEQ_NO)

   filePathAll = rootPath + State + "_" + str(SVC_TRAN_CODE) + "_" + date +  "_" + timeStamp + ".txt"
   fAll = open(filePathAll,"w",encoding='utf-8')
   fAll.write("------------------------------请求报文---------------------------------\n")
   fAll.write(requestBody + "\n")
   fAll.write("------------------------------响应报文---------------------------------\n")
   fAll.write(All)
   fAll.close()

   print('交易耗时：' + str(endTime - startTime) + '毫秒')