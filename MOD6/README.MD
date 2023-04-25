<h1> Passos inicias </h1>

O ROS necessita da instalação do WSL com o Ubuntu-22.04.
Após isso, é necessário instalar o ROS2 Humble para seguir.

Entao, precisamos executar o turtlesim e o nosso script para iniciar seu funcionamento.

<code>ros2 run turtlesim turtlesim_node</code>
(Em outro terminal para iniciar o script)

<code>python3 script.py</code>
Então já é possível rodar o projeto tranquilamente.

Obs: Caso dê problema de permissão basta rodar <code>chmod +x script.py</code>
Isso dará permissão de execução do arquivo para o usuário.

Se o ambiente não estiver configurado corretamente com todas as dependências instaladas, basta seguir as instruções: <a>https://github.com/Murilo-ZC/Questoes-Trabalhos-Inteli-M6/tree/main/ponderada1</a>
Eu estava com muitos problemas para a preparação, mas com essas etapas que vem desde a instalação até a intalações de todos os pacotes necessários para rodar o script

<b>Como foi feito? O que é o desenho?</b>
Basicamente a tartaruga irá desenhar uma casinha, assim como a maioria das pessoas desenhavam na quinta série. Foi um desenho simples, mas que me deu uma nocão de como funciona a programação orientada a objetos. Primeiramente pela função __init__ que são as configurações iniciais e depois o move_turtle que é o código principal que a todo momento chama um método que tem como parâmetros a nova posição em que a tartaruga deve ir.
