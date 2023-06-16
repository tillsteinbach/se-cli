import asyncio
#from xknx import XKNX
#from xknx.telegram import Telegram
#from xknx.core import XknxConnectionState
#from xknx.io import ConnectionConfig, ConnectionType

import can
from se_python.stiebel_protocol import StiebelMessage, StiebelWriteMessage, OperationType, DeviceType
from se_python.se_python import SEPython
from se_python.se_variables import SEVariable



#async def telegram_received_cb(telegram: Telegram):
#    print("Telegram received: {0}".format(telegram), flush=True)


#async def connection_state_changed_cb(state: XknxConnectionState):
#    print("Callback received with state {0}".format(state.name), flush=True)


#connection_config = ConnectionConfig(
#    connection_type=ConnectionType.TUNNELING_TCP,
#    gateway_ip="10.11.2.200",
#    individual_address="1.1.14",
#)

def main():
    #xknx = XKNX(connection_config=connection_config,
    #            telegram_received_cb=telegram_received_cb,
    #            connection_state_changed_cb=connection_state_changed_cb,
    #            daemon_mode=True)
    #await xknx.start()
    #await xknx.stop()

    

    sepython = SEPython(bustype='socketcan', channel='can0')

    stiebelTemperature = StiebelWriteMessage(source=(DeviceType.DISPLAY, 30),
                                             target=(DeviceType.HEATCIRCLE, 1),
                                             variable=SEVariable.ERWEITERUNGSTELEGRAMM,
                                             variable_extension=SEVariable.RAUMISTTEMP,
                                             value=272)
    try:
        print(stiebelTemperature)
        print(stiebelTemperature.toCanMessage())
        sepython.bus.send(stiebelTemperature.toCanMessage())
        print(f"Message sent on {sepython.bus.channel_info}")
    except can.CanError:
        print("Message NOT sent")
    
    stiebelFeuchte = StiebelWriteMessage(source=(DeviceType.DISPLAY, 30),
                                             target=(DeviceType.HEATCIRCLE, 1),
                                             variable=SEVariable.ERWEITERUNGSTELEGRAMM,
                                             variable_extension=SEVariable.FEUCHTE,
                                             value=502)
    try:
        print(stiebelFeuchte)
        print(stiebelFeuchte.toCanMessage())
        sepython.bus.send(stiebelFeuchte.toCanMessage())
        print(f"Message sent on {sepython.bus.channel_info}")
    except can.CanError:
        print("Message NOT sent")

    
    sepython.start()


#asyncio.run(main())


    
