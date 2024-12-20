import pandas as pd
import matplotlib.pyplot as plt
import dataframe_image as dfi



vendas = pd.read_csv("vendas.csv")
vendas["data_pedido"] = pd.to_datetime(vendas["data_pedido"], format="%Y-%m-%d") #forçando todas as datas para este formato
#print(vendas)



vendas_por_mes = vendas[["data_pedido","vendas"]] #criando a tabela de vendas por mes a partir da coluna data_pedido e as vendas
vendas_por_mes.set_index("data_pedido", inplace=True) #setando a data da venda como o índice daquela venda para utilizar a func. resample
vendas_por_mes = vendas_por_mes.resample("ME").sum() #agrupa os dados diários em seus respectivos meses e soma os resultados 
vendas_por_mes = vendas_por_mes.rename_axis("Mês").reset_index() #renomeando a coluna "data_pedido" por "Mês"

vendas_por_mes["Mês"] = vendas_por_mes["Mês"].dt.strftime("%b") #transforma o retorno padrão (que seria a data do último dia do mês) em abreviação do mês (30 Abril -> Apr)
vendas_por_mes["vendas"] = (vendas_por_mes["vendas"] / 1e3).round(2) #transformando os dados em milhares 
#print(vendas_por_mes)

#criando gráfico de linhas
def grafico_vendas_por_mes(df, filename):
    #                            larg, alt qualid. da imagem 
    fig, ax = plt.subplots(figsize=(12,6),dpi=100) #área do gráfico
    
    #        x do graf   y do graf  lineweight  
    ax.plot(df["Mês"], df["vendas"], lw = 3, marker = "o") #construção do gráfico de linha

    # personalizando o gráfico
    ax.set_title('Total de Vendas em 2023', fontsize = 18, loc='left')
    ax.set_xlabel('Mês')
    ax.set_ylabel('Vendas (em milhares de reais)')
    ax.set_frame_on(False)
    ax.grid(True, color="grey", ls='--')

    # remover todos os ticks do eixo x e y
    ax.tick_params(axis='both', which='both', length=0)
    
    # limitando a área para não distorcer o gráfico (de 0 ao maior valor+100)
    plt.ylim(0, df["vendas"].max() + 100)

    plt.savefig(filename, dpi=100, bbox_inches='tight', pad_inches=0)
    plt.show()
grafico_vendas_por_mes(vendas_por_mes, "vendas_por_mes.png")



#criando uma tabela para informar o lucro de cada departamento
lucro_dpt = vendas[["departamento","lucro"]]

lucro_dpt = lucro_dpt.groupby("departamento").sum() #agrupando os departamentos separadamente e somando cada um
lucro_dpt = lucro_dpt.reset_index() #limpando índice
#print(lucro_dpt)

#criando gráfico de barras horizontais
def grafico_lucro_por_departamento(df, filename):
    # área do gráfico
    fig, ax = plt.subplots(figsize=(12,6),dpi=100)
    
    #  criar gráfico de colunas horizontais
    ax.barh(df["departamento"], df["lucro"])

    # personalizando o gráfico
    ax.set_title('Lucro por Departamento em 2023', fontsize = 18, loc='left')
    ax.set_frame_on(False)
    ax.set_xticklabels([]) #remove os valores do eixo x

    # remover todos os ticks do eixo x e y
    ax.tick_params(axis='both', which='both', length=0)

    # add os valores nas barras
    for i, v in enumerate(df["lucro"]):
        ax.text(df["lucro"][i] + 1e3, i, f'R$ {df["lucro"][i]:,.2f}', fontsize = 12, ha = 'left', va='center')

    plt.savefig(filename, dpi=100, bbox_inches='tight', pad_inches=0)
    plt.show()
grafico_lucro_por_departamento(lucro_dpt, "lucro_dpt.png")



# criando um df com os dados desejados (o modo de envio somente do estado de São Paulo)
envio_sp = vendas.query('estado == "São Paulo"')[["modo_envio"]]

# contando a quantidade de cada modo de envio
envio_sp = envio_sp.value_counts().to_frame()
envio_sp = envio_sp.reset_index()
#print(envio_sp)

#criando gráfico de barras verticais
def grafico_modo_envio(df, filename):
    # Área do gráfico
    fig, ax = plt.subplots(figsize=(12,6),dpi=100)

    ax.bar(df["modo_envio"], df["count"])

    ## Personalizando o gráfico
    ax.set_title('Modos de Envio mais utilizados em São Paulo (2023)', fontsize = 18, loc='left')
    ax.set_frame_on(False)
    ax.set_yticklabels([])

    # remover todos os ticks do eixo x e y
    ax.tick_params(axis='both', which='both', length=0)

    # Valores nas barras
    for i, v in enumerate(df["count"]):
        ax.text(i, df["count"][i], df["count"][i], fontsize = 12, ha = 'center', va='bottom')

    plt.savefig(filename, dpi=100, bbox_inches='tight', pad_inches=0)
    plt.show()
grafico_modo_envio(envio_sp, "envio_sp.png")



dfi.export(vendas_por_mes, "tab_vendas_por_mes.png", table_conversion="matplotlib")
dfi.export(lucro_dpt, "tab_lucro_dpt.png", table_conversion="matplotlib")
dfi.export(envio_sp, "tab_envio_sp.png", table_conversion="matplotlib") 