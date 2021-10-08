import _thread
import time
import requests
import json

# 为线程定义一个函数
def post( threadName  ):

    SVC_TRAN_CODE = '2004'                                       
    url = "http://188.177.156.166:9013"   #开发

    timeStamp = str(int(time.time()))
    SEQ_NO = "SQ_SEQ_NO" + timeStamp  +"_" + threadName
    REQ_SEQ_NO = "SQ_REQ_SEQ_NO" + timeStamp + "_" + threadName
    
    data = {
        "BODY": { 

        },
 
        "APP_HEAD": {
    
        },

        "SYS_HEAD": {
 
        }
     
    }
    
    res = requests.post(url=url,json=data).json()
    # All = json.dumps(res, sort_keys=True,ensure_ascii =False, indent=2)
    State = json.dumps(res["SYS_HEAD"]["RSP_CODE"], sort_keys=True,ensure_ascii =False, indent=2)
    State = State.replace('"','')

    # print(All)
    # print(SEQ_NO)
    print(State + "_" + SEQ_NO)
    if(State == ""):
        All = json.dumps(res, sort_keys=True,ensure_ascii =False, indent=2)
        print(All)

if __name__=="__main__":
    # 创建线程
    try:
        for i in range(101,999):
            ThreadName = "Thread" + str(i)
            _thread.start_new_thread( post, (ThreadName, ) )
            # _thread.start_new_thread( print_time, ("Thread-2", ) )
    except:
        print ("Error: 无法启动线程")

    # time.sleep(120)
    while 1:
        pass
