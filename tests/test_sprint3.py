import DbUtils
from main import main
import DataProcessing


# test to see if new table is there
def test_setup_db():
    main()
    conn, cursor = DbUtils.open_db("Comp490Jobs.sqlite")
    cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name = "jobs_listings";''')
    assert len(cursor.fetchone()) > 0
    conn.close()


def test_read_excel():
    data = DataProcessing.get_excel_data()
    assert len(data) == 750


def test_table_data():
    main()
    conn, cursor = DbUtils.open_db("Comp490Jobs.sqlite")
    cursor.execute('''SELECT * FROM jobs_listings ;''')
    assert len(cursor.fetchall()) == 728
    conn.close()
