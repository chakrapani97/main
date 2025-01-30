# import_excel_to_db.py
import pandas as pd
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Results.settings")
django.setup()

from testapp.models import student_results

def import_excel_data(file_path):
    df = pd.read_excel(file_path)  # Use the file_path parameter here
    for index, row in df.iterrows():
        student = student_results.objects.create(
            rollno=row['Roll No'],
            name=row['Name'],
            english=row['English'],
            sanskrit=row['Sanskrit'],
            maths1a=row['Maths1A'],
            maths1b=row['Maths1B'],
            physics=row['Physics'],
            chemistry=row['Chemistry']
        )
        student.save()

if __name__ == "__main__":
    file_path = r"C:\Users\calli\OneDrive\Desktop\marks.xlsx"
    import_excel_data(file_path)  # Use the file_path variable here
