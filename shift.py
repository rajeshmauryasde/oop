import datetime


class ShiftTimeUtil:
    @staticmethod
    def shift_str(start_time: datetime.time, end_time: datetime.time) -> str:
        return f"{start_time} to {end_time}"


class MorningShift:
    start_time = datetime.time(9, 00)
    end_time = datetime.time(18, 00)

    def get_shift_details(self) -> str:
        return ShiftTimeUtil.shift_str(start_time=self.start_time, end_time=self.end_time)


class AfternoonShift:
    start_time = datetime.time(14, 00)
    end_time = datetime.time(22, 00)

    def get_shift_details(self) -> str:
        return ShiftTimeUtil.shift_str(start_time=self.start_time, end_time=self.end_time)
