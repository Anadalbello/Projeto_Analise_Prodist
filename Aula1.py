# valores das Harmonicas
H2 = float(input('Digite o valor de H2:'))
H3 = float(input('Digite o valor de H3:'))
H4 = float(input('Digite o valor de H4:'))
H5 = float(input('Digite o valor de H5:'))
H6 = float(input('Digite o valor de H6:'))
H7 = float(input('Digite o valor de H7:'))
H8 = float(input('Digite o valor de H8:'))
H9 = float(input('Digite o valor de H9:'))
H10 = float(input('Digite o valor de H10:'))
H11 = float(input('Digite o valor de H11:'))

# valor tensão fundamental U1:

U1 = float(input('Digite o valor de U1:'))

# somatoria das Harmonicas elevadas ao quadrado

somatoria = float((H2**2)+(H3**2)+(H4**2)+(H5**2)+(H6**2) +
                  (H7**2)+(H8**2)+(H9**2)+(H10**2)+(H11**2))

# Calculo
THDu = float((somatoria**0.5)/U1)
print('O resultado do calculo de THDu é:', THDu)
