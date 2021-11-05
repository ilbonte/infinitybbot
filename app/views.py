import telegram  # this is from python-telegram-bot package
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializers import UserSerializer, PongSerializer


class PingView(APIView):

    def get(self, request, format=None):
        serializer = PongSerializer(data=request.GET)
        if serializer.is_valid():
            if serializer.data['ping'] == 'ping':
                return Response({'result': 'pong'})
            else:
                return Response({'result': "What's in your head?"})
        else:
            return Response({'error': serializer.errors})

    def post(self, request, format=None):
        bot = telegram.Bot(token=settings.BOT_TOKEN)

        update = telegram.Update.de_json(request.get_json(force=True), bot)

        chat_id = update.message.chat.id
        msg_id = update.message.message_id

        bot.sendMessage(chat_id=chat_id, text="Pong", reply_to_message_id=msg_id)

        return Response({'result': 'pong'})


class WebhookView(APIView):
    def get(self, request, format=None):
        token = settings.BOT_TOKEN
        url = settings.URL

        bot = telegram.Bot(token=token)

        s = bot.setWebhook('{URL}{HOOK}'.format(URL=url, HOOK=token))
        if s:
            return Response({'status': "webhook setup ok with url {}".format(url)})
        else:
            return Response({'status': "webhook setup failed"})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
