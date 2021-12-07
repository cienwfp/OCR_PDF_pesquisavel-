# OCR_PDF_pesquisavel

Este código é feito em flask e cria um servidor para receber arquivos pdf scaneados e converte para arquivos pdf pesquisáveis. E envia o arquivo para o client solicitante.

Este pequeno código foi criado para resolver o problema de pdf gerados a partir de scaners que não possuem a tecnologia para converter a imagem para pdf que as soluções de search possam pesquísar entidades dentro dos documentos pdf oriundo de scaners.

Fui Utilizado o Python 3.8 com as bibliocetas relacionadas no arquivo requirements.txt. 

Para o usuário que queira ativar o serviço basta clonar o repositório através do comando no terminal:
1. <git clone>
2. cd ocr_pdf_pesquisavel
  2.1. sudo nano Dockerfile
    2.1.1. altere <port> para a porta que deseja espor do conteiner
  2.2. sudo nano docker-compose.yml
    2.2.1. altere <port1:port2>
      2.2.1.1. altere a port1 para a porta que será exposta na sua máquina física
      2.2.1.2. altere para o mesmo valor que colocou para <port> no passo 2.1.1
    2.2.2. altere <PWD> para o caminho da pasta que o conteiner vai compartillhar com a máquina física
3. sudo docker-compose up -d
  
Após estes passos o servidor irar fazer todas as instalações dentro do container e o serviço estará ativo na porta configurada acima.
