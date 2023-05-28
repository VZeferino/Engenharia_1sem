<p>
    A implementação começa com a instalação das bibliotecas Ultralytics e Roboflow que servem para facilitar o treinamento de modelos e
  fornecer ferramentas de pré-processamento, por exemplo. 
  Em seguida, é importada a classe Roboflow e o modelo YOLO da biblioteca Ultralytics.
</p>

<p>
  O código solicita a chave da API do Roboflow, que deve ser pegada acessando sua conta,
  pegando a chave privada e colando como solicitado,
  e com essa informação, cria-se uma instância do objeto Roboflow usando essa chave. 
  É especificado o projeto "crack-bphdr" dentro do espaço de trabalho "university-bswxt" e é feito o download da versão 2 
  do conjunto de dados.
</p>

<p>
  Depois, é carregado o modelo YOLO, especificando o arquivo 'yolov8n.pt'. 
  Em seguida, é executado o treinamento do modelo usando o comando 'yolo task=detect' com os parâmetros apropriados, 
  como o número de epochs, tamanho das imagens entre outros.
</p>

<p>Por fim, algumas imagens são exibidas para visualizar os resultados do modelo treinado.</p>
