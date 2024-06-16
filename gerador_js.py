import os 

class Script:
    _nomeAula = "Aula"
    numeroAula = 0
    _formatacao_nome_arquivo = ""
    
    def criar_arquivo(self, estruturaArquivo, nomeArquivo):
            with open(nomeArquivo, "w") as arquivo:
                arquivo.write(f'"{estruturaArquivo}"')

    def criar_arquivo_recursivo(self, estrura, nomeArquivo, controlador):
        for numero_arquivo in range(controlador):
            with open(nomeArquivo, "w") as arquivo: 
                arquivo.write(f'"{estrura}')
        print(f"{numero_arquivo - 1} arquivos foram criados")


class ScriptJs(Script):
    _formatoJs = ".js"
    estrutura = "use strict"

    def criar_arquivoJs_aula(self):
        
        try:
            numeroAula_str = str(self.numeroAula)
        except ValueError as erroConversao:
            print(erroConversao)
        
        if self.numeroAula < 10: # atributo da class pai
            self._formatacao_nome_arquivo = f"{self._nomeAula + '0' + numeroAula_str + self._formatoJs}" # atributos da class pai (self._nomeAula, self.numeroAula)        
            super().criar_arquivo(self.estrutura, self._formatacao_nome_arquivo)
        
        else: 
            self._formatacao_nome_arquivo = f"{self._nomeAula + numeroAula_str + self._formatoJs}"
            super().criar_arquivo(self.estrutura, self._formatacao_nome_arquivo)

    def criar_arquivosJs_recursivos_aula(self, controle):
        try:
            numeroAula_str = str(self.numeroAula)
            int(controle)
        
        except ValueError as erroConversao:
            print(erroConversao)
        
        if self.numeroAula < 10: # atributo da class pai
            self._formatacao_nome_arquivo = f"{self._nomeAula + '0' + numeroAula_str + self._formatoJs}" # atributos da class pai (self._nomeAula, self.numeroAula)        
            super().criar_arquivo_recursivo(self.estrutura, self._formatacao_nome_arquivo, controle)
        
        else: 
            self._formatacao_nome_arquivo = f"{self._nomeAula + numeroAula_str + self._formatoJs}"
            super().criar_arquivo_recursivo(self.estrutura, self._formatacao_nome_arquivo, controle)


class ScriptHtml(Script):
    _formatoHtml = ".html"
    estrutura = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
    <script src = {}></script>
</body>
</html>"""

    def criar_arquivoHtml(self):
        super().criar_arquivo(self._formatoHtml, self.estrutura)
    


teste = ScriptJs()
teste.criar_arquivosJs_recursivos_aula(14)









            
