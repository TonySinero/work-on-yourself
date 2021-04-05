import time
import sys

def hmsToSecs(h,m,s):
    return h*3600 + m*60 + s

def secsToHms(secs):
    hours = secs//3600
    secs -= hours*3600
    mins = secs//60
    secs -= mins*60
    return hours,mins,secs

def countdown(h,m,s):
    seconds = hmsToSecs(h,m,s)
    while seconds > 0:
         print ("%02d:%02d:%02d"%secsToHms(seconds))
         seconds -= 1
         time.sleep(1)
    print("Done!")

countdown(2,15,5)
#--------------------------------------------------
def pomo(w,s,b):
    w, s, b = (int(w*60), int(s*60), int(b))
    while True:
        for _ in range(3):
            print('work!')
            time.sleep(w)
            print('short break!')
            time.sleep(s)
        print('work!')
        time.sleep(w)
        print('short break!')
        time.sleep(s)
        print('Break Time! ')
        time.sleep(b)
        break


#------------------------------------------
import sys

def timer(hour, min, sec):
    c = ":"
    while hour > 0:
        while min > 0:
            while sec > 0:
                sec = sec-1
                time.sleep(1)
                sys.stdout.write('\r' + str(hour) + c + str(min) + c + str(sec))

            min = min-1
            sec = 60
        hour = hour-1
        min = 59
    print('final')

#-----------------------------------------
#
def pomodoro():
  print("Pomodoro starts now!")
  for i in range(4):
    t = 25*60
    while t:
      mins = t // 60
      secs = t % 60
      print(f'{mins}:{secs}', end="\r")
      time.sleep(1)
      t -= 1
    print("Break Time!!")

    t = 5*60
    while t:
      mins = t // 60
      secs = t % 60
      print( f'{mins}:{secs}', end="\r")
      time.sleep(1)
      t -= 1
    print("Work Time!!")
  print('final')
# -----------------------------------------------------
from abc import abstractmethod, ABC


class LoggerInterface(ABC):
    @abstractmethod
    def log(self, message: str):
        raise NotImplemented


class FileLogger(LoggerInterface):
    def __init__(self, pathToFile: str):
        with open(pathToFile, 'a') as file:
            self.file = file

    def log(self, message: str):
        self.file.write(message)


class DatabaseLogger(LoggerInterface):
    def __init__(self, pathToFile: str):
        with open(pathToFile, 'a') as file:
            self.file = file

    def log(self, message: str):
        self.file.write(message)


class Pomodoro:
    def __init__(self, logger: LoggerInterface, task):
        self.logger = logger
        self.task = task

    checkmark = 0
    total_mins = 0

    def tasks(self):
        global checkmark
        global total_mins
        mins = 0
        print('Timer for ', self.task, ' is 25 mins.')
        start = input('Press Enter to start the timer.')
        while mins <= 25:
            time.sleep(60)
            mins = + 1
            total_mins += 1
            print(mins, " minutes work completed.")
        print('End of Pomodoro')
        checkmark += 1
        print('Total check mark is ', checkmark)

    def breaks(self):
        global checkmark
        mins = 0
        if checkmark < 4:
            print('Take a short break.')
            while mins != 5:
                time.sleep(60)
                mins = mins + 1
                print(mins, " minutes break completed.")
            print('Break over')

        elif checkmark >= 4:
            print('Take a long break.')
            while mins != 10:
                time.sleep(60)
                mins = mins + 1
                print(mins, " minutes break completed.")
            checkmark = 0
            print('Break over.')

    def main(self):
        carry_on = 'y'
        task = input('Welcome to Pomodoro Timer\n What task do you want to work on? ')
        while carry_on == 'y' or carry_on == 'Y':
            # tasks(task)
            # breaks()
            carry_on = input("Do you want ot carry on?(y/n)")

        print("End of task ", task, ". \nTotal time worked was minutes ", total_mins, " minutes.")

if __name__ == '__main__':
    file_logger = FileLogger('log.txt')
    file_logger.log('john')

    # pomodoro = Pomodoro(file_logger)
