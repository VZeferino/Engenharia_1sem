<h1>Para executar o projeto, siga as etapas abaixo:</h1>

<h3>Abra um terminal no Ubuntu.</h3>

<h3>Navegue até o diretório raiz do projeto usando o comando "cd 'caminho'".</h3>

<h3>Execute o comando "colcon build --packages-select simu". Isso compilará o pacote simu e todas as suas dependências.</h3>

<h3>Após a conclusão da compilação, execute o comando "source install/setup.bash". Isso configurará o ambiente para que o ROS2 possa encontrar o pacote compilado.<h3>

<h3>Agora, você pode executar o nó do controlador com o comando "ros2 run simu run".</h3>

Enfim, o nó do controlador será iniciado e começará a receber as informações de posição do robô. Ele calculará as ações necessárias para o robô se mover em direção às posições desejadas da lista positions, definida por mim. Os comandos de velocidade serão publicados no tópico /cmd_vel, controlando o movimento do robô. Você poderá ver a posição atual do robô sendo exibida no console durante a execução.
é necessário que o ROS2 esteja instalado corretamente antes de executar esses comandos e também é preciso estar no diretório correto que contém o código fonte do projeto.
