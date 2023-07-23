import json
import time
import datetime
import six
from six import text_type
from django.http.response import StreamingHttpResponse

def stream(request):
    def event_stream():
        while True:
            time.sleep(3)
            t = datetime.datetime.now()
            print(t)
            yield 'data: The server time is: %s\n\n' % t
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')

if six.PY2:
    from dwebsocket.decorators import accept_websocket
    from django.http import HttpResponse
    from celery.result import AsyncResult
    import logging

    log = logging.getLogger("django")


    @accept_websocket
    def async_result(request, task_id):
        def pm(body):
            try:
                if body['status'] in ['FAILURE', 'REVOKED']:
                    body['result'] = text_type(body['result'])
                # print(body)
                request.websocket.send(('%s\r' % json.dumps(body)).encode('utf8'))
            except Exception:
                import traceback
                log.error("async_result dump json error, body: %s; error: %s", body, traceback.format_exc())

        rs = AsyncResult(task_id)
        if not request.is_websocket():
            body = {'status': rs.state, 'result': text_type(rs.result)}
            return HttpResponse(json.dumps(body))

        else:
            d = dict(
                task_id=rs.task_id,
                state=rs.state,
                status=rs.status,
                result=rs.status == 'FAILURE' and text_type(rs.result) or rs.result,
                traceback=rs.traceback
            )
            pm(d)
            try:
                r = rs.get(on_message=pm, propagate=False)
            except Exception as e:
                body = {'status': 'FAILURE', 'result': text_type(e)}
                request.websocket.send(('%s\r' % json.dumps(body)).encode('utf8'))
else:
    # import asyncio
    # import websockets

    # async def recv_msg(websocket):
    #     while True:
    #         recv_text = await websocket.recv()
    #         response_text = f"your submit context: {recv_text}"
    #         await websocket.send(response_text)
    #
    #
    # async def main_logic(websocket, path):
    #     #await check_permit(websocket)
    #     await recv_msg(websocket)

    #
    # start_server = websockets.serve(main_logic, '127.0.0.1', 5678)
    # asyncio.get_event_loop().run_until_complete(start_server)
    # asyncio.get_event_loop().run_forever()
    from celery.result import AsyncResult

    def async_result(request, task_id):
        # rs = AsyncResult(task_id)
        # events= []
        # def pm(body):
        #     try:
        #         if body['status'] in ['FAILURE', 'REVOKED']:
        #             body['result'] = text_type(body['result'])
        #         events.insert(0, json.dumps(body))
        #     except Exception:
        #         import traceback
        #         log.error("async_result dump json error, body: %s; error: %s", body, traceback.format_exc())

        # r = rs.get(on_message=pm, propagate=False)

        def event_stream():
            while True:
                time.sleep(3)
                print('event_stream')
                yield 'data: interval\n\n'
                # while events:
                #     text = events.pop()
                #     yield 'data: %s\n\n' % text
                # yield 'data: interval'

        return StreamingHttpResponse(event_stream(), content_type='text/event-stream')
