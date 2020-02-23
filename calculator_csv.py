import sys
import json
import csv

##计算函数
def calculator(income):
    """
    计算税后薪资的函数，参数为原始收入
    """
    start_point = 5000
    insurance = income * 0.165    
    shouldPay = income - insurance - start_point
    if shouldPay <= 0:
        tax = 0
    elif shouldPay <= 3000:
        tax = shouldPay * 0.03
    elif shouldPay <= 12000:
        tax = shouldPay * 0.1 - 210
    elif shouldPay <= 25000:
        tax = shouldPay * 0.2 - 1410
    elif shouldPay <= 35000:
        tax = shouldPay * 0.25 - 2660
    elif shouldPay <= 55000:
        tax = shouldPay * 0.3 - 4410
    elif shouldPay <= 800000:
        tax = shouldPay * 0.35 - 7160
    else:
        tax = shouldPay * 0.45 - 15160
    salary = income - insurance - tax
    salary = '{:.2f}'.format(salary)
    return salary

##存入字典的函数
def output(data_dic):
    '''
    字典存入函数
    '''
    str_json = json.dumps(data_dic)
    with open(sys.argv[2],'w') as f:
        f.write(str_json)

##执行函数
def main():
    '''执行函数
    '''
##定义空字典接收员信息
    dic_data = {}
##拿到csv文件的路径
    data_file = sys.argv[1]
##读取员工的工号和工资
    with open(data_file) as f:
        data_list = list(csv.reader(f))
    print(data_list)
##存入字典
    for item in data_list:
        try:
            id, income = item[0],item[1]
            income = float(income)
            income = calculator(income)
            dic_data[id] = income
        except ValueError:
            dic_data[id] = '工号{}工资请输入数字'.format(id)
            continue
    output(dic_data)

if __name__ == '__main__':
    main()
