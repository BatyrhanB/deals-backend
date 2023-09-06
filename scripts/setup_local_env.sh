#!/bin/sh
FILE=../src/.env

function setup_env(){
echo "Устанавливаются переменные окружения"
echo ALLOWED_HOSTS="*" >> $FILE
echo CORS_ALLOWED_ORIGINS="http://127.0.0.1:3000,http://127.0.0.1:3001" >> $FILE
echo DEBUG="True" >> $FILE
echo FILE_UPLOAD_MAX_MEMORY_SIZE="128M" >> $FILE
echo PRODUCTION="False" >> $FILE
echo SECRET_KEY="dsijfdsojfhd*&@)*^!@(*#^@!*(&YSHdhaskjk" >> $FILE
echo ADMIN_URL="admin/" >> $FILE
echo DOCS_URL="docs/" >> $FILE

echo "Переменные окружения установлены"
}

if [ -f "$FILE" ]; then
    rm $FILE
    setup_env
else
    setup_env
fi