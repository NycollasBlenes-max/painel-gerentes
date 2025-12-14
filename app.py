from flask import Flask, render_template
from datetime import datetime
import os
import unicodedata

app = Flask(__name__)

# Lista com nomes das gerências
gerencias = [
    'ANCHIETA', 'JARDIM CAMBURI', 'BOM JESUS DO ITABAPOANA', 'MASTERPLACE', 'ICONHA',
    'NORTE SUL', 'MIRACEMA', 'ITACIBA', 'PIUMA', 'JACARAÍPE',
    'QUISSAMA', 'LARANJEIRAS', 'SANTO ANTONIO DE PADUA', 'MARCILIO DE NORONHA', 'SAO FIDELIS',
    'MONTSERRAT', 'CENTRO VILA VELHA', 'PORTO CANOA', 'CENTRO VIX', 'SERRA SEDE', 'GLÓRIA'
]

def normalizar_nome_loja(nome):
    """
    Normaliza o nome da loja removendo acentos e convertendo para minúsculas
    Isso ajuda na comparação mesmo com acentos diferentes
    """
    if not nome:
        return ""
    
    # Remove acentos
    nome_nfd = unicodedata.normalize('NFD', nome)
    nome_sem_acentos = ''.join(char for char in nome_nfd if unicodedata.category(char) != 'Mn')
    
    return nome_sem_acentos.lower()

@app.route('/')
def index():
    """Página inicial com 21 botões"""
    try:
        print("=" * 80)
        print(f"📱 USUÁRIO ENTROU NO SISTEMA - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80 + "\n")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    # Renderizar página com os botões
    buttons = [
        {'id': i+1, 'label': gerencias[i], 'route': f'/gerencia/{i+1}'}
        for i in range(21)
    ]
    return render_template('index.html', buttons=buttons)

@app.route('/gerencia/<int:num>')
def gerencia(num):
    """Páginas individuais para cada gerência"""
    if 1 <= num <= 21:
        return render_template('gerencia.html', numero=num, nome=gerencias[num-1])
    return "Página não encontrada", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
