from mycroft import MycroftSkill, intent_file_handler


class AnamatronicDoll(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('doll.anamatronic.intent')
    def handle_doll_anamatronic(self, message):
        self.speak_dialog('doll.anamatronic')


def create_skill():
    return AnamatronicDoll()

