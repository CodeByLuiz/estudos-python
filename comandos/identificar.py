
#.lower() transforma todas as letras em minúsculas.
# .strip() remove espaços em branco do começo e do final.
#.split() divide a string em uma lista de palavras.

def interpretar_comando(texto):
    texto = texto.lower().strip()
    texto = texto.replace(",", "").replace(".", "")
    palavras = texto.split()
    acao_encontrada = None

    iniciadores = ["Alfred"]
    acoes = {
        "abrir": [
            "abrir",
            "iniciar",
            "executar",
                  ],
        "criar": [
            "criar",
            "fazer",
            "gerar" 
        ],
        
    }
    objetos = {
    "navegador": [
        "navegador",
        "browser",
        "chrome",
        "google chrome"
    ],

    "calculadora": [
        "calculadora",
        "calc",
        "calculadora do windows"
    ],

    "bloco_de_notas": [
        "bloco de notas",
        "notepad",
        "editor de texto"
    ]
}

    for acao, palavras in acoes.items():
        if any(palavra in texto for palavra in palavras):
            acao_encontrada = acao
            print(f"Ação encontrada: {acao_encontrada}")
            break

    for objeto, palavras in objetos.items():
        if any(palavra in texto for palavra in palavras):
            objeto_encontrado = objeto
            print(f"Objeto encontrado: {objeto_encontrado}")
            break
