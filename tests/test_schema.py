import os
import tempfile
import textwrap

from api.services.parser import validate_csv

def write_tmp_csv(text: str) -> str:
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    tmp.write(text.encode())
    tmp.close()
    return tmp.name

def test_good_csv_passes() -> None:
    csv = textwrap.dedent("""\
    sold_date,vehicle,sold_price,cost,profit,gross,lead_source,salesperson
    2025-04-01,Ford F150,30000,25000,5000,4500,Google,J. Doe
    """)
    path = write_tmp_csv(csv)
    rows = validate_csv(path)
    os.unlink(path)
    assert len(rows) == 1

def test_bad_column_fails() -> None:
    bad = "oops,bad\n1,2\n"
    path = write_tmp_csv(bad)
    try:
        validate_csv(path)
        assert False, "should have raised"
    except ValueError:
        pass
    finally:
        os.unlink(path) 