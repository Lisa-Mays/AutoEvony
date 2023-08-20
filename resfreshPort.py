import psutil

class Resfresh_Port():
    def __init__(self, Status_Resfresh=0, name="HD-Player.exe"):
        self.Status_Resfresh = Status_Resfresh
        self.name = name

    def ResfreshPort(self):
        if self.Status_Resfresh == 1:
            bluestacks_processes = []
            for process in psutil.process_iter():
                if process.name() == self.name:
                    bluestacks_processes.append(process)

            ports_in_use = set()
            for process in bluestacks_processes:
                for connection in process.connections():
                    if connection.status == psutil.CONN_LISTEN and connection.laddr.port != 0:
                        ports_in_use.add(connection.laddr.port)

            if len(ports_in_use) == 0:
                return 0
            else:
                return ports_in_use