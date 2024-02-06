from concurrent import futures

import grpc

import time

import pythonStudygRPC_pb2
import pythonStudygRPC_pb2_grpc

class Chat(pythonStudygRPC_pb2_grpc.ChatServicer):
    def send(self, request, context):
        # return super().send(request, context)
        print("{0} : {1}".format(request.nickName, request.msg))
        # return request
        return pythonStudygRPC_pb2.messageData(nickName=request.nickName, msg=request.msg)
    
def serverStart():
    chatServer = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    pythonStudygRPC_pb2_grpc.add_ChatServicer_to_server(Chat(),chatServer)
    chatServer.add_insecure_port("localhost:55555")
    chatServer.start()
    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        chatServer.stop(0)

if __name__ == '__main__':
    print('서버가 시작되었습니다.')
    serverStart()