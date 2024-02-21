import DataProcessing
import DbUtils


def main():
    conn, cursor = DbUtils.open_db("Comp490Jobs.sqlite")
    DbUtils.setup_db(cursor)
    complete_data = DataProcessing.get_excel_data() + DataProcessing.get_multiple_pages_of_jobs(5)
    for job in complete_data:
        DbUtils.insert_job(cursor, job)
    DbUtils.close_db(conn)


def save_output(data_to_write: list[dict]):
    output_file = open("output.txt", "w")
    for job in data_to_write:
        print(job, file=output_file)
    output_file.close()


if __name__ == '__main__':
    main()
