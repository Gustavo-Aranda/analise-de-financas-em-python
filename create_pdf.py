from fpdf import FPDF
import time


# função para o título
def titulo(pdf, title):

    # titulo principal
    pdf.set_font('Helvetica', 'b', 20)
    pdf.ln(10)
    pdf.write(5, title)
    pdf.ln(10)

    # adicionando a data de geração do relatório
    pdf.set_font('Helvetica', '', 14)
    pdf.set_text_color(r=128, g=128, b=128)
    today = time.strftime("%d/%m/%Y")
    pdf.write(4, f'{today}')

    # add line break
    pdf.ln(10)

# função para o texto
def texto(pdf, txt):

    # ajustando cor de texto, fonte e espaçamento
    pdf.set_text_color(0)
    pdf.set_font('Helvetica', '', 12)

    pdf.write(5, txt)
    

# variáveis globais
WIDTH = 210
HEIGHT = 297

# criando o documento PDF
pdf = FPDF() # A4 (210 x 297 mm)

# --------  página 1 --------  #
pdf.add_page()

# título
titulo(pdf, "Relatório do Desempenho de Vendas (2023)")

# título da tabela
texto(pdf, "1. Tabela das Vendas por mês da empresa em 2023")
pdf.ln(10)

# adicionando a tabela de vendas
pdf.image("tab_vendas_por_mes.png", WIDTH/2 - 20, w=40)
pdf.ln(20)

# adicionando o gráfico de vendas
pdf.image("vendas_por_mes.png", 10, 150, WIDTH - 20)
pdf.ln(90)

# texto explicativo
texto(pdf, "A visualização acima mostra a tendência das vendas da empresa durante o ano de 2023. Conseguimos notar " \
           "que em 5 meses no ano as vendas foram acima de 600 mil reais. Julho foi o mês com menor desempenho.")


# --------  página 2 --------  #
pdf.add_page()

# título da tabela 2
pdf.ln(20)
texto(pdf, "2. Tabela dos Lucros por Departamento em 2023")
pdf.ln(10)

# adicionando a tabela de lucro
pdf.image("tab_lucro_dpt.png", WIDTH/2 - 40, w=80)
pdf.ln(20)

# adicionando o gráfico de lucro
pdf.image("lucro_dpt.png", 10, WIDTH/2, WIDTH - 20)
pdf.ln(120)

# texto explicativo
texto(pdf, "O departamento que apresenta o maior lucro da empresa é o Automotivo. O resultado é esperado, visto que grande" \
           " parte dos produtos automotivos estão entre os mais caros por unidade. Na sequência temos os produtos de Jardinagem e" \
           " paisagismo, por fim, os materiais de construção com menos de R$ 30 mil de lucro em 2023.")

# --------  página 3 --------  #
pdf.add_page()

# título da tabela 3
pdf.ln(20)
texto(pdf, "3. Tabela da quantidade de produtos por Modo de Envio em São Paulo (2023)")
pdf.ln(10)

# adicionando a tabela de modo de envio
pdf.image("tab_envio_sp.png", WIDTH/2 - 40, w=60)
pdf.ln(20)

# adicionando o gráfico de modo de envio
pdf.image("envio_sp.png", 10, WIDTH/2, WIDTH - 20)
pdf.ln(120)

# texto explicativo
texto(pdf, "O modo de envio mais utilizado de forma disparada é a Entrega Padrão, corrrespondendo a quase 60% de todas as entregas em" \
           " São Paulo. Em seguida, temos a Econômica e Envio rápido e, por último, a de 24 horas com menos de 10% de entregas no estado.")

# gerando o PDF
pdf.output("Relatório 2023.pdf", 'F')