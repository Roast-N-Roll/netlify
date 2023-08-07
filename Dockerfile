FROM python:3.9

COPY ./.env ./.env

EXPOSE 8501
WORKDIR /netlify
ADD requirements.txt /netlify/requirements.txt
RUN pip3 install -r requirements.txt
ADD . /netlify

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]