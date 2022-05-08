from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from lights import call_mqtt


def on_kitchen(instance):
    print('topic:', "zigbee2mqtt/kitchen/set")
    print('message:', 'ON')
    call_mqtt(topic="zigbee2mqtt/kitchen/set", payload='ON')

def on_living(instance):
    print('topic:', "zigbee2mqtt/living_room/set")
    print('message:', 'ON')
    call_mqtt(topic="zigbee2mqtt/living_room/set", payload='ON')

def off_kitchen(instance):
    print('topic:', "zigbee2mqtt/kitchen/set")
    print('message:', 'OFF')
    call_mqtt(topic="zigbee2mqtt/kitchen/set", payload='OFF')

def off_living(instance):
    print('topic:', "zigbee2mqtt/living_room/set")
    print('message:', 'OFF')
    call_mqtt(topic="zigbee2mqtt/living_room/set", payload='OFF')

class HelloWorldApp(App):
    def build(self):

        # base grid
        layout = GridLayout(cols=2)

        # buttons
        btn1 = Button(text='ON', background_color='green')
        btn2 = Button(text='OFF', background_color='red')
        btn3 = Button(text='ON', background_color='green')
        btn4 = Button(text='OFF', background_color='red')
        
        # add widgets
        layout.add_widget(Label(text="Kitchen"))
        layout.add_widget(Label(text="Living room"))
        layout.add_widget(btn1)
        layout.add_widget(btn3)
        layout.add_widget(btn2)
        layout.add_widget(btn4)

        btn1.bind(on_press=on_kitchen)
        btn3.bind(on_press=on_living)
        btn2.bind(on_press=off_kitchen)
        btn4.bind(on_press=off_living)

        return layout

if __name__ == '__main__':
    HelloWorldApp().run()