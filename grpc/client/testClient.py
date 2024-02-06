import grpc

import pythonStudygRPC_pb2
import pythonStudygRPC_pb2_grpc

def connectServer(serverIP="localhost", serverPort="55555" , nickName = "unknown"):
    chatChannel = grpc.insecure_channel(serverIP + ":" + serverPort)
    stub = pythonStudygRPC_pb2_grpc.ChatStub(chatChannel)
    return chatChannel, stub

if __name__ == '__main__':
    serverIP = 'localhost'
    serverPort = '55555'
    print('클라이언트가 시작되었습니다.')
    nickName = input("이름을 입력하세요 : ")
    chatChannel, stub = connectServer(serverIP,serverPort, nickName)
    print('{0}서버와 연결되었습니다.'.format(serverIP))
    try:
            while True:
                msg = input('보낼 메세지 : ')
                response = stub.send(pythonStudygRPC_pb2.messageData(nickName=nickName,msg=msg))
                print("{0} : {1}".format(response.nickName, response.msg))
    except KeyboardInterrupt:
        chatChannel.close()
        print('사용자 입력으로 인하여 서버와 연결이 끊어졌습니다.')
    finally:
        chatChannel.close()
        print('서버와 연결이 끊어졌습니다.')
