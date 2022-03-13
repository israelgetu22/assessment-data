log_file = open("um-server-01.txt")  #Open the file 'um-server-01.txe' using 'open("filename")'


def sales_reports(log_file):  #Creating a function in a name of 'sales_reports'
    for line in log_file:     #loop or iteration of each log_file in variable line
        line = line.rstrip()  #removes any characters at the end a string
        day = line[0:3]       #slice from index 0 to index 3
        if day == "Tue":      #condition for only Tuesday : 'Tue
            print(line)       #output or console.log like js for variable 'line'


sales_reports(log_file)       #calling the python function and invoke 'log_file'


log_file = open("um-server-01.txt")  #Open the file 'um-server-01.txe' using 'open("filename")'


def sales_reports(log_file):  #Creating a function in a name of 'sales_reports'
    for line in log_file:     #loop or iteration of each log_file in variable line
        line = line.rstrip()  #removes any characters at the end a string
        day = line[0:3]       #slice from index 0 to index 3
        if day == "Mon":      #condition for only Monday : 'Mon
            print(line)       #output or console.log like js for variable 'line'


sales_reports(log_file)        #calling the python function and invoke 'log_file'

def over_10_mo(log_file):
    for line in log_file:
        line = line.rstrip()
      
        if  > 10:
            print(line)