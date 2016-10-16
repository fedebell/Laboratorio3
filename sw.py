# -*- coding: cp1252 -*-


import numpy as np
import sympy as sp
import sys

var_num=0
variables=[]
errors=[]
row=[]

input_file_str=sys.argv[1]
input_func=sys.argv[2]

##input_file_str='dati_1a.txt'
##input_func="VC = VCC-(VCC/(1+ R1/R2 )-0.7)*RC/RE"
out_var=input_func.split()[0]
input_func=' '.join(input_func.split()[2:])

for line in open(input_file_str):
    if line.startswith('#'):
        params=line.split()
        params[0]=params[0][1:]
        variables = params[0::2]
        errors= params[1::2]
##        print variables, errors
    if not line.startswith('#'):
        row.append([float(item) for item in line.split()])
        
##print(row)
##symVariables=sp.symbols(variables)
##symErrors=sp.symbols(errors)

f=sp.sympify(input_func)
print("Function to propagate:\n")
sp.pprint(f)

var_in_expr=f.atoms(sp.Symbol)

print("\nVariables in the expression: "+ str(tuple(var_in_expr))+'\n')

var_symb = sp.symbols([str(item) for item in tuple(var_in_expr)])
err_symb = sp.symbols(['d'+str(item) for item in tuple(var_in_expr)])
##print var_symb, err_symb


f_np=sp.lambdify(tuple(var_in_expr), f, "numpy")
##print f_np(0.1, 1000)

##print np.array(row[0])

var_indices_list = [variables.index(str(item)) for item in var_symb]
##print var_indices_list

#
##coords_list=[row[0][index*2] for index in indices_list]
##print coords_list

result_values=[f_np(*tuple([row[i][index*2]
            for index in var_indices_list]))
            for i in range(len(row))]
##print result_values
#
##
##f2= f.diff(var_symb[0])
##print f2



df=sp.sqrt(sum([(f.diff(var_symb[i])*err_symb[i])**2 for i in range(len(var_symb))]))

##print df.simplify()

params_tot=[None]*(2*len(var_symb)) # stessa taglia
params_tot[::2]=var_symb
params_tot[1::2]=err_symb
df_np=sp.lambdify(tuple(params_tot), df, "numpy")

tot_indices_list = [params.index(str(item)) for item in params_tot]
##print tot_indices_list
result_errors=[df_np(*tuple([row[i][index] for index in tot_indices_list]))
               for i in range(len(row))]
##print result_errors


#output file
final_table=[[result_values[i], result_errors[i]] for i in range(len(result_values))]
# (!) generalizzare a piu' colonne di output

##np.set_printoptions(formatter={'float': '{: 0.3e}'.format})
result_values_str=map(str, result_values)
result_errors_str=map(str, result_errors)

final_table_str=[[result_values_str[i], result_errors_str[i]]
                 for i in range(len(result_values_str))]

final_to_str='#'+out_var+'\t'+'d'+out_var+'\n'

final_to_str+='\n'.join(['\t'.join(item) for item in final_table_str])

##print("Output table:\n\n"+final_to_str)

print("Output table:\n\n"+'#'+out_var+'\t'+'d'+out_var+'\n')
print(str(np.array(final_table)).replace('[', ' ').replace(']', ' '))


output_file=open(out_var+"_out_of_"+input_file_str, 'w')
output_file.write(final_to_str)

output_file.close()

'''
(!) problemi da risolvere:
. ancora non riconosce le unita' di misura e in particolare le scale.
. renderlo piu' elegante tutto il formalismo.
. renderlo piu' hidden, con input da terminale magari.
. rendere piu' "carini" (notazione ingegneristica)
    i numeri in output nella tabella (secondario). 
. fare in modo che dia in output più colonne (secondario).

per il resto e' una figata assurda!!
'''


