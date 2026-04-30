import os
import csv
import json


#task 1
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print('checking file ...')

        if os.path.exists(self.filename):
            print(f'file found: {self.filename}')
            return True
        else:
            print(f'Error {self.filename} not found. Please download the file from LMS')
            return False


    def create_output_folder(self, folder='output'):
        print('checking output folder...')
        if os.path.exists(folder):
            print(f'output folder already exists: {folder}/')
        else:
            os.makedirs(folder)
            print(f'output folder created: {folder}/')



#task 2

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print('loading data...')

        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    self.students.append(row)
            print(f'data loaded successfully: {len(self.students)} students')
        except FileNotFoundError:
            print(f'Error: File {self.filename} not found. Please check the filename')
        except Exception as e:
            print(f'Error: {e}')
        return self.students
    

    def preview(self, n = 5):
        print(f'first {n} rows:')
        print('-'* 30)

        for student in self.students[:5]:
            print(
                f"{student['student_id']} | "
                f"{student['age']} | "
                f"{student['gender']} | "
                f"{student['country']} | "
                f"GPA: {student['GPA']}"
            )
        print("-" * 30)

# task 3


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}


    def analyse(self):
        data  = {}

        for student in self.students:
            try:
                country = student['country']
                if country in data:
                    data[country] +=1
                else:
                    data[country] = 1
            except (KeyError, ValueError):
                print(f"Warning: could not convert value for student "
                      f"{student.get('student_id', '?')} — skipping row.")
                continue

        top_3 = sorted(data.items(), key=lambda x: x[1], reverse=True)[:3]

        self.result = {
            "total_students": len(self.students),
            "total_countries": len(data),
            "top_3": top_3,
            "all_countries": data
        }

        return self.result
    
    def print_results(self):
        print("-" * 30)
        print("Country Analysis")
        print("-" * 30)
        print(f"Total students   : {self.result['total_students']}")
        print(f"Total countries  : {self.result['total_countries']}")
        print("-" * 30)
        print("Top 3 Countries:")
        for i, (country, count) in enumerate(self.result['top_3'], 1):
            print(f"  {i}. {country} : {count}")
        print("-" * 30)


#task 4

class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):

        try:
            result_to_save = self.result.copy()
            result_to_save['top_3'] = [
                {'country': c, 'count': n} for c, n in self.result['top_3']
            ]

            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(result_to_save, f, indent=4)
            print(f'result saved to {self.output_path}')
        except Exception as e:
            print(f'error saving file: {e}')


#task 5

fm = FileManager('students.csv')
if not fm.check_file():
    print('stopping program')
    exit()

fm.create_output_folder()

d1 = DataLoader('students.csv')
d1.load()
d1.preview()

analyser = DataAnalyser(d1.students)
analyser.analyse()
analyser.print_results()

saver = ResultSaver(analyser.result, 'output/result.json')
saver.save_json()