#!/bin/sh
WARNING_MESSAGE="Процесс пошел, ничего не трогай!"
CODE_DIR="../"

echo "Ооо, ты попал в TBM Music."
echo 
echo "Добро пожаловать!"
echo
echo "Короче, выбери вариант и погнали:"
echo
echo "1. Первый раз? Этот вариант твой"
echo "2. Второй раз? Тогда этот"
echo

read -n1 -p "Что выберешь? [1,2]: " doit
echo
case $doit in
  1) echo "Запускаю Dockerfile!"
     echo "$WARNING_MESSAGE"
        cd ../docker && \
            docker-compose -f docker-compose.dev.yml  up --build;;

  2) echo "Запускаю проект!"
     echo "$WARNING_MESSAGE"
        cd ../docker && \
            docker-compose -f docker-compose.dev.yml up;;
  *) echo "${Red} Такого варианта нет, читать не умеешь? ${NC}" ;; 
esac