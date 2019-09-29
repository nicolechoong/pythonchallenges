# 1. Write a Boolean function between that takes two MyTime objects, t1 and t2, as arguments, and returns True if the invoking object falls between the two times. Assume t1 <= t2, and make the test closed at the lower bound and open at the upper bound, i.e. return True if t1 <= obj < t2.

class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
            The values of mins and secs may be outside the range 0-59,
            but the resulting MyTime object will be normalized.
        """

        # Calculate total seconds to represent
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600        # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60
        self.totalsecs = totalsecs

    def __str__(self):
        output = ""

        for i in [self.hours, self.minutes, self.seconds]:
            if i < 10:
                output += "0"+str(i)+":"
            else:
                output += str(i)+":"

        return output[:-1]

    def add_time(t1, t2):

        h = t1.hours + t2.hours
        m = t1.minutes + t2.minutes
        s = t1.seconds + t2.seconds

        if s >= 60:
            s -= 60
            m += 1

        if m >= 60:
            m -= 60
            h += 1

        sum_t = MyTime(h, m, s)
        return sum_t

    def increment(t, seconds):
        t.totalsecs += seconds

        h = t.totalsecs // 3600        # Split in h, m, s
        leftoversecs = t.totalsecs % 3600
        m = leftoversecs // 60
        s = leftoversecs % 60

        return MyTime(h, m, s)


    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.totalsecs

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        if self.hours > time2.hours:
            return True
        if self.hours < time2.hours:
            return False

        if self.minutes > time2.minutes:
            return True
        if self.minutes < time2.minutes:
            return False
        if self.seconds > time2.seconds:
            return True

        return False

    def between(self, t1, t2):

        if self.totalsecs >= t1.totalsecs and self.totalsecs < t2.totalsecs:
            return True
        else:
            return False

# 2. Turn the above function into a method in the MyTime class.

# 3. Overload the necessary operator(s) so that instead of having to write

# if t1.after(t2): ...
# we can use the more convenient
# if t1 > t2: ...

# 4. Rewrite increment as a method that uses our “Aha” insight.

# 5. Create some test cases for the increment method. Consider specifically the case where the number of seconds to add to the time is negative. Fix up increment so that it handles this case if it does not do so already. (You may assume that you will never subtract more seconds than are in the time object.)

print(MyTime(1,2,6).increment(+0))
print(MyTime(1,6,3).increment(+60))
print(MyTime(1,2,6).increment(-40))
