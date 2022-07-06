from src.logdecoratorandhandler.log_decorator import LogDecorator
from src.logdecoratorandhandler.options import Options

Options.log_level = 'DEBUG'


@LogDecorator('DEBUG - test a function')
def a_function():
    return


if __name__ == '__main__':
    a_function()
