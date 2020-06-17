#this will save this cell as file

from mrjob.job import MRJob

class MRTopSalaries(MRJob):
    def mapper(self, _, line):
        print ("in mapper")
        with open('Baltimore_City_Employee_Salaries_FY2014.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
                yield(row, row["AnnualSalary"])
                yield(row, row["GrossPay"])
 
    def reducer(self, word, pay):
        yield(word, max(pay))
        
if __name__ == '__main__':
    MRTopSalaries.run()
