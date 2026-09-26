"""Test for issue #1: ordinal() returns wrong suffix for 11, 12, 13."""
import humanize


class TestOrdinalTeens:
    """Ordinal should return 'th' for 11, 12 and 13 (and their hundreds)."""

    def test_twelve(self) -> None:
        assert humanize.ordinal(12) == "12th"

    def test_eleven(self) -> None:
        assert humanize.ordinal(11) == "11th"

    def test_thirteen(self) -> None:
        assert humanize.ordinal(13) == "13th"

    def test_twenty_two(self) -> None:
        assert humanize.ordinal(22) == "22nd"

    def test_one_hundred_twelve(self) -> None:
        assert humanize.ordinal(112) == "112th"

    def test_one_hundred_eleven(self) -> None:
        assert humanize.ordinal(111) == "111th"
