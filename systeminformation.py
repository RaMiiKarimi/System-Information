from subprocess import check_output as cmd 

result = cmd(['systeminfo']).decode('utf-8')
print(result)