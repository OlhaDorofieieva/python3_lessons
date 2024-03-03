# TODO: Зробити адаптер from_csv_to_html
import csv


class TxtAdaptor:

    @staticmethod
    def csv_to_json(file_path):
        with open(file_path) as f:
            res = f.readlines()
        header = [k.strip() for k in res[0].split(',')]
        rows = res[1:]
        res_list = []
        for row in rows:
            row = row.strip().split(',')  # ['Alex', '25', 'Support', '1000']
            res_list.append(dict(zip(header, row)))  # dict key from header, value from row
        return res_list

    @staticmethod
    def csv_to_html(file_path):
        with open(file_path) as f:
            res = f.readlines()
        html_output = ''

        rows = res[1:]
        for row in rows:
            row = row.strip().split(',')
            html_output += f" <name>{row[0]}</name>\n"
            html_output += f" <last_name>{row[1]}</last_name>\n"
            html_output += f" <age>{row[2]}</age>\n"
            html_output += f" <salary>{row[3]}</salary>\n"
            html_output += ".........................\n"
        return html_output

    @staticmethod
    def csv_to_html2(csv_file):
        """
        use module python csv https://docs.python.org/uk/3/library/csv.html
        """
        with open(csv_file, mode='r') as file:
            csv_reader = csv.DictReader(file)  # Create obj dict
            html = ''
            for row in csv_reader:
                for key, value in row.items():
                 html += f'<{key}>{value}</{key}>\n'
                html += '....................\n'
        return html


print(TxtAdaptor.csv_to_html('tst_file.txt'))
print(TxtAdaptor.csv_to_html2('tst_file.txt'))
