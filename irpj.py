def calcular_irpj(lucro_mensal):
    aliquota_basica = 0.15
    limite_adicional = 20000.00
    aliquota_adicional = 0.10
    
    # Cálculo do imposto básico
    imposto_basico = lucro_mensal * aliquota_basica
    
    # Cálculo do adicional
    if lucro_mensal > limite_adicional:
        parcela_adicional = lucro_mensal - limite_adicional
        imposto_adicional = parcela_adicional * aliquota_adicional
    else:
        imposto_adicional = 0.0
    
    # Cálculo total do imposto
    imposto_total = imposto_basico + imposto_adicional
    
    return imposto_total

if __name__ == "__main__":
    # Solicitar ao usuário que informe o lucro mensal
    lucro_mensal = float(input("Informe o lucro mensal: R$ "))
    
    # Calcular o IRPJ
    imposto_irpj = calcular_irpj(lucro_mensal)
    
    # Exibir o resultado
    print(f"Lucro mensal: R$ {lucro_mensal:.2f}")
    print(f"Imposto de Renda da Pessoa Jurídica (IRPJ) devido: R$ {imposto_irpj:.2f}")
