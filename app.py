# DESAFIO
 
''' Crie 5 pastas diferentes no seu diretório atual(manualmente):
 
   * Arquivos 2010
 
   * Documentação
 
   * Backup
 
   Agora crie 3 arquivos fora destas pastas
 
   * nomes.txt
 
   * inscrições.pdf
 
   * relatórios.xlsx
'''
import os
import shutil
 
 
arquivos1 = ['Arquivos 2010','Documentação','Backup']
 
for arquivo in arquivos1:
    os.makedirs(arquivo)
 
arquivos2 = ['nomes.txt','inscrições.pdf','relatórios.xlsx']
for arquivo in arquivos2:
    with open(arquivo,'w'):
        pass
   
 
 
# 1) Copie o arquivo nomes.txt para a pasta 'Arquivos 2010'
shutil.copy(src=os.getcwd()+os.sep+'nomes.txt',dst=os.getcwd()+ os.sep + 'Arquivos 2010')
 
 
#2) Mova o arquivo inscrições.pdf para a pasta 'Documentação'
shutil.move(src=os.getcwd()+os.sep+'inscrições.pdf',dst=os.getcwd()+os.sep+'Documentação')
 
 
#2) Faça uma cópia da pasta 'Arquivos 2010' e tudo que estiver contido nela para a pasta uma nova pasta chamada 'Backup Arquivos 2010'
shutil.copytree(src=os.getcwd()+os.sep+'Arquivos 2010',dst=os.getcwd()+os.sep+'Backup Arquivos 2010')
 
 
#3) Compacte todo o conteúdo da pasta 'Documentação' no formato zip
shutil.make_archive('Documentação','zip',os.getcwd())
 
 
#4) Mova o arquivo compactado para dentro da pasta 'Backup'
shutil.move(src=os.getcwd()+os.sep+'Documentação.zip',dst=os.getcwd()+os.sep+'Backup')
 
 
#4) Exclua o diretório 'Arquivos 2010' e 'Documentação' e seus conteúdos
shutil.rmtree(os.getcwd()+os.sep+'Arquivos 2010')
shutil.rmtree(os.getcwd()+os.sep+'Documentação')
 
 
#5) Compacte o diretório inteiro, para um arquivo chamado 'Backup Arquivos Python.zip'
shutil.make_archive('backup_desafio','zip',os.getcwd())