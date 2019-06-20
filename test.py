class Flight(object):

    def __init__(self,name):
        self.name= name

    def check_status(self):
        print("check flight %s's status"%self.name)
        return 2

    @property
    def flight_status(self):
        status = self.check_status()
        if status == 0:
            print("flight got canceled...")
        elif status == 1:
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cann't confirm the flight status")

    @flight_status.setter
    def flight_status(self,status):
        # status = self.check_status()
        status_dic = {
            0: "canceled",
            1: "arrived",
            2: "departured"
        }
        print("航班状态",status_dic.get(status))


    @flight_status.deleter
    def flight_status(self):
        print("status got removed...")

f = Flight('CA980')
f.flight_status
# f.flight_status = 1





