FROM python:3.9

RUN mkdir -p /opt/services/deals-backend

WORKDIR /opt/services/deals-backend

ADD . /opt/services/deals-backend/

RUN chmod 755 /opt/services/deals-backend/scripts/* && \
        chmod +x /opt/services/deals-backend/scripts/* && \
            export DJANGO_SETTINGS_MODULE=deals.settings && \
                pip install -r requirements.txt 