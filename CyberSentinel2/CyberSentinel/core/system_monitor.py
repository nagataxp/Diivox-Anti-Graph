import psutil


class SystemMonitor:

    _last_sent = 0
    _last_recv = 0

    @staticmethod
    def cpu():
        return round(
            psutil.cpu_percent(),
            1
        )

    @staticmethod
    def ram():
        return round(
            psutil.virtual_memory().percent,
            1
        )

    @staticmethod
    def disk():

        try:
            return round(
                psutil.disk_usage("/").percent,
                1
            )
        except:
            return round(
                psutil.disk_usage("C:\\").percent,
                1
            )

    @staticmethod
    def processes():
        return len(
            psutil.pids()
        )

    @staticmethod
    def threads():

        count = 0

        for proc in psutil.process_iter():

            try:
                count += proc.num_threads()
            except:
                pass

        return count

    @staticmethod
    def network():

        net = psutil.net_io_counters()

        sent = net.bytes_sent
        recv = net.bytes_recv

        upload = (
            sent -
            SystemMonitor._last_sent
        )

        download = (
            recv -
            SystemMonitor._last_recv
        )

        SystemMonitor._last_sent = sent
        SystemMonitor._last_recv = recv

        upload = round(
            upload / 1024,
            1
        )

        download = round(
            download / 1024,
            1
        )

        return upload, download

    @staticmethod
    def uptime():

        uptime_seconds = (
            psutil.boot_time()
        )

        return uptime_seconds