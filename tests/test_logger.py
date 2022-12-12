from src.logdecoratorandhandler.log_decorator import TimeDecorator
from src.logdecoratorandhandler.options import Options

Options.log_level = 'DEBUG'


def test_should_print_time_used(capsys):
    """Test if decorator works."""

    @TimeDecorator()
    def to_be_decorated():
        captured = capsys.readouterr()
        assert '' in captured.out

    to_be_decorated()
