from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDFloatingActionButton
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config

class UI(ScreenManager):
    pass

class main(MDApp):
    def build(self):
        self.title= '*Mi Saldo#'
        Config.set('kivy', 'window_icon', 'img/icon.png')
        Config.set('graphics', 'resizable', False)
        Window.size = (450, 800)
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette= 'LightBlue'
        Builder.load_file('client/ui.kv')
        self.dialog_1 = MDDialog(
                                title = 'Servisio de adelanta saldo',
                                text = '¿Cuanto saldo desea solicitar?',
                                size_hint=(0.7, .3),
                                opacity =.5,
                                buttons=[
                                    MDFlatButton(
                                        text='$25 cup',
                                        on_release=self.sas25
                                    ),
                                    MDFlatButton(
                                        text='$50 cup',
                                        on_release=self.sas50
                                    )
                                ]
                            )
        self.dialog_2 = MDDialog(
                                title = 'tarifa por consumo',
                                text = '¿Desea activar la tarifa por consumo?',
                                size_hint=(0.7, .3),
                                opacity =.5,
                                buttons=[
                                    MDFlatButton(
                                        text='Si',
                                        on_release=self.tpc0
                                    ),
                                    MDFlatButton(
                                        text='No',
                                        on_release=self.tpc1
                                    )
                                ]
                            )
        self.dialog_3 = MDDialog(
                                title = 'bolsa de mensajeria',
                                text = '600MB solo para el uso de ToDus y correo nacional',
                                size_hint=(0.7, .3),
                                opacity =.5,
                                buttons=[
                                    MDFlatButton(
                                        text='Comprar\n$25cup',
                                        on_release=self.n12
                                    ),
                                    MDFlatButton(
                                        text='Cancelar',
                                        on_release=self.close_dialog3
                                    )
                                ]
                            )
        return UI()
    
    def close_dialog3(self,*args):
        self.dialog_3.dismiss()

    def n1(*args):
        print('*222#')
    def n2(*args):
        print('*222*266#')
    def n3(self,*agrs):
        num = self.root.ids.Num.text
        can = self.root.ids.Monto.text
        key = self.root.ids.Key.text
        print(f'*234*1*{num}*{key}*{can}*1#')
    def n4(self,*agrs):
        key = self.root.ids.AKey.text
        Nkey = self.root.ids.NKey.text
        Ckey = self.root.ids.CKey.text
        print(f'*234*2*{key}*{Nkey}*{Ckey}*1#')
    def n5(self,*args):
        self.dialog_1.open()
    def sas25(self,*args):
        print('*234*3*1*25*1#')
        self.dialog_1.dismiss()
    def sas50(self,*args):
        print('*234*3*1*50*1#')
        self.dialog_1.dismiss()
    def n6(self,*args):
        self.dialog_2.open()
    def tpc0(self,*args):
        print('*133*1*1*1*1#')
        self.dialog_2.dismiss()
    def tpc1(self,*args):
        print('*133*1*1*2*1#')
        self.dialog_2.dismiss()
    def n7(*args,value):
        if value == 0:
            print('*133*?*1*1#')
        elif value == 1:
            print('*133*?*2*1#')
        else:
            print('*133*?*3*1#')
    def n8(*args,value):
        if value == 0:
            print('*133*?*0#')
        elif value == 1:
            print('*133*?*1#')
        elif value == 2:
            print('*133*?*2#')
        elif value == 3:
            print('*133*?*3#')
        elif value == 4:
            print('*133*?*4#')
        elif value == 5:
            print('?')
    def n9(*args,value):
        if value == 0:
            print('*133*?*0#')
        elif value == 1:
            print('*133*?*1#')
        elif value == 2:
            print('*133*?*2#')
        elif value == 3:
            print('*133*?*3#')
        elif value == 4:
            print('?')
    def n10(*agrs):
        key = 0
        print(f'*234*1*{key}#')
    def n11(*args,value):
        if value == 0:
            print('*133*?*0#')
        elif value == 1:
            print('*133*?*1#')
        elif value == 2:
            print('*133*?*2#')
        elif value == 3:
            print('*133*?*3#')
        elif value == 4:
            print('*133*?*4#')
        elif value == 5:
            print('?')
        elif value == 6:
            print('?')  
    def n12(self,*args):
        self.dialog_3.open()

if __name__=="__main__":
    main().run()
