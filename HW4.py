class Date:
    def __ne__(self, other) -> bool:
        """
             :param other: An object of type date
             :return:Returns true if the current date is not equal to the received date
             """
        if not self.__eq__(other): return True
        return False

    def __ge__(self, other) -> bool:
        """
             :param other: An object of type date
             :return:Returns true if the current date is greater or equals than the received date
             """
        if self.__eq__(other):
            return True
        else:
            return self.__gt__(other)

    def __le__(self, other) -> bool:
        """
              :param other: An object of type date
               :return:Returns true if the current date is less or equals than the received date
               """
        if self.__eq__(other):
            return True
        else:
            return self.__lt__(other)

    @staticmethod
    def stam(m1: int, other, count: int) -> int:
        """
        :param m1:month
        :param other:An object of type date containing the month
        :param count:The number of months between these two months
        :return: Returns the number of days between two months
        """
        days = 0
        for i in range(count):
            days += Date.getMonthDay1(m1, other.y)
            if Date.getMonthDay1(m1, other.y) == 29: days -= 1
            if m1 == 12:
                m1 = 1
            else:
                m1 += 1
        return days

    def __sub__(self, other) -> None:
        """
        :param other: An object of type date
        :return: Prints the number of days between two dates
        """
        big = self
        small = other
        if big < small:
            small = self
            big = other
        x = 0
        for i in range(small.y, big.y + 1):
            if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
                x += 1
        a = big.d - small.d
        b = big.m - small.m
        c = big.y - small.y
        if a < 0:
            a = (big.d + 30) - small.d
            b = big.m - 1 - small.m
        if b < 0:
            b = (b + 12)
            c = big.y - 1 - small.y
        print(f"days:{a + x},Month:{b},years:{c}")
        sums = a + x + big.stam(small.m, small, b) + c * 365
        print("Count of Days is:", sums)

    def __gt__(self, other) -> bool:
        """
        :param other: An object of type date
        :return:Returns true if the current date is greater than the received date
        """
        if self.__eq__(other):
            return False
        elif self.y > other.y:
            return True
        elif self.y == other.y and self.m > other.m:
            return True
        elif self.y == other.y and self.m == other.m and self.d > other.d:
            return True
        else:
            return False

    def __lt__(self, other) -> bool:
        """
        :param other: An object of type date
        :return:Returns true if the current date is less than the received date
        """
        if self.__eq__(other):
            return False
        elif self.y < other.y:
            return True
        elif self.y == other.y and self.m < other.m:
            return True
        elif self.y == other.y and self.m == other.m and self.d < other.d:
            return True
        else:
            return False

    def __eq__(self, other) -> bool:
        """
        :param other: An object of type date
        :return:Returns true if the current date is equal to the received date
        """
        if self.d != other.d:
            return False
        elif self.m != other.m:
            return False
        elif self.y != other.y:
            return False
        else:
            return True

    def __init__(self, d: int, m: int, y: int):
        """
        constructor for Date
        :param d: day
        :param m: month
        :param y: year
        """
        if not isinstance(d, int) or not isinstance(m, int) or not isinstance(y, int):
            raise TypeError("day,month and year must be int")
        elif m > 12 or m < 1:
            raise ValueError("the month is not correct")
        elif y > 9999 or y < 1000:
            raise ValueError("the year is not correct")
        else:
            if d <= Date.getMonthDay1(m, y):
                self.d = d
                self.m = m
                self.y = y
            else:
                raise ValueError("the day is not correct")

    def __str__(self) -> str:
        """
        :return: ToStrnig for Date
        """
        return f"{self.d}/{self.m}/{self.y}"

    def isValid(self) -> bool:
        """
        :return:Check if the date is real
        """
        if self.m > 12 or self.m < 1:
            return False
        elif self.y > 9999 or self.y < 1000:
            return False
        days = self.getMonthDay()
        return self.d <= days

    def getNextDay(self):
        """
        :return: Returns the next date without any change to the current date
        """
        if self.d == 31 and self.m == 12:
            return Date(1, 1, self.y + 1)
        x = self.d
        self.d = self.d + 1
        if self.isValid():
            st = Date(self.d, self.m, self.y)
            self.d = x
            return st
        else:
            self.d = x
            return Date(1, self.m + 1, self.y)

    @staticmethod
    def getMonthDay1(month: int, year: int) -> int:
        """ static function
        :param month: month
        :param year:year
        :return: Return the number of days in this month
        """
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            days = 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            days = 30
        else:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                days = 29
            else:
                days = 28
        return days

    def getMonthDay(self) -> int:
        """
        :return: Return the number of days in this month
        """
        days = 0
        if self.m == 1 or self.m == 3 or self.m == 5 or self.m == 7 or self.m == 8 or self.m == 10 or self.m == 12:
            days = 31
        elif self.m == 4 or self.m == 6 or self.m == 9 or self.m == 11:
            days = 30
        else:
            if (self.y % 4 == 0 and self.y % 100 != 0) or (self.y % 400 == 0):
                days = 29
            else:
                days = 28
        return days

    def getNextDays(self, daysToAdd: int):
        """
        :param daysToAdd: Receive the number of days to be added to the date
        :return:Returns the new date without changing the current date
        """
        if daysToAdd >= 365:
            years = daysToAdd // 365
            daysToAdd = daysToAdd % 365
            x = 0
            for i in range(self.y, self.y + years + 1):
                if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
                    x -= 1
            daysToAdd += x
        else:
            years = 0
        for i in range(1, daysToAdd + 1):
            self.d += 1
            if (self.d > self.getMonthDay()):
                self.d = 1
                self.m += 1
                if self.m > 12:
                    self.m = 1
                    self.y += 1
        return Date(self.d, self.m, self.y + years)


date = Date(29, 12, 1956)
date1 = Date(22, 10, 2019)
print(date <= date1)
print(date >= date1)
print(date != date1)
print(date.isValid())
print(date.getNextDay())
print(date1.__sub__(date))
print(date.__sub__(date1))
print(date == date1)
print(date < date1)
print(date > date1)
print(date.getNextDays(5000))
