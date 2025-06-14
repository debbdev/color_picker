import time
import colorama


class Printer():
    def __init__(self, AppName=__name__):
        colorama.init()
        self.Name = AppName
        
    def format(self, *args):
        return f"{colorama.Fore.BLUE}{self.Name}{colorama.Fore.RESET}{colorama.Fore.LIGHTYELLOW_EX}::{colorama.Fore.RESET}{colorama.Fore.LIGHTCYAN_EX}{time.strftime('%H:%M:%S', time.localtime())}{colorama.Fore.RESET} {' '.join(map(str, args))}"
         
    def print(self, *args, end="\n", **kw):
        print(
            self.format(*args),
            end=end,
            **kw
        )
        
    def error(self, *args, end="\n"):
        self.print(f"{colorama.Fore.LIGHTRED_EX}{' '.join(map(str, args))}{colorama.Fore.RESET}", end=end)

    def success(self, *args, end="\n"):
        self.print(f"{colorama.Fore.LIGHTGREEN_EX}{' '.join(map(str, args))}{colorama.Fore.RESET}", end=end)

    def warning(self, *args, end="\n"):
        self.print(f"{colorama.Fore.LIGHTYELLOW_EX}{' '.join(map(str, args))}{colorama.Fore.RESET}", end=end)
        

if __name__ == "__main__":
    printer = Printer("TestApp")
    printer.print("this is a Test")
    printer.error("this is an error")
    printer.success("this is success")
    printer.warning("this is a warning")