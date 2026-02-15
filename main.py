from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.core.window import Window
import math

# تنظیم رنگ پس‌زمینه به خاکستری تیره برای زیبایی
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class FazeshApp(App):
    def build(self):
        self.title = "Fazesh Device"
        
        # پنل اصلی که تب‌ها را نگه می‌دارد
        tp = TabbedPanel()
        tp.do_default_tab = False  # حذف تب پیش‌فرض
        
        # --- تب ارتفاع سنج (Height) ---
        th_height = TabbedPanelItem(text='Ertefa (Height)')
        layout_h = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # ورودی زاویه
        layout_h.add_widget(Label(text='Zaviye (Angle - Degree):', size_hint_y=None, height=30))
        self.input_angle_h = TextInput(multiline=False, input_filter='float', size_hint_y=None, height=50)
        layout_h.add_widget(self.input_angle_h)
        
        # ورودی فاصله
        layout_h.add_widget(Label(text='Fasele (Distance/Number):', size_hint_y=None, height=30))
        self.input_dist_h = TextInput(multiline=False, input_filter='float', size_hint_y=None, height=50)
        layout_h.add_widget(self.input_dist_h)
        
        # دکمه محاسبه
        btn_calc_h = Button(text='Mohasebe (Calculate)', size_hint_y=None, height=60, background_color=(0, 0.5, 1, 1))
        btn_calc_h.bind(on_press=self.calculate_height)
        layout_h.add_widget(btn_calc_h)
        
        # نمایش نتیجه
        self.lbl_res_h = Label(text='Result: ---', font_size='20sp', color=(1, 1, 0, 1))
        layout_h.add_widget(self.lbl_res_h)
        
        th_height.content = layout_h
        
        # --- تب شیب سنج (Slope) ---
        th_slope = TabbedPanelItem(text='Shib (Slope)')
        layout_s = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # ورودی زاویه
        layout_s.add_widget(Label(text='Zaviye (Angle - Degree):', size_hint_y=None, height=30))
        self.input_angle_s = TextInput(multiline=False, input_filter='float', size_hint_y=None, height=50)
        layout_s.add_widget(self.input_angle_s)
        
        # دکمه محاسبه
        btn_calc_s = Button(text='Mohasebe (Calculate)', size_hint_y=None, height=60, background_color=(0, 0.8, 0, 1))
        btn_calc_s.bind(on_press=self.calculate_slope)
        layout_s.add_widget(btn_calc_s)
        
        # نمایش نتیجه
        self.lbl_res_s = Label(text='Result: ---', font_size='20sp', color=(0, 1, 0, 1))
        layout_s.add_widget(self.lbl_res_s)
        
        th_slope.content = layout_s
        
        # اضافه کردن تب‌ها به پنل
        tp.add_widget(th_height)
        tp.add_widget(th_slope)
        
        return tp

    def calculate_height(self, instance):
        try:
            angle = float(self.input_angle_h.text)
            dist = float(self.input_dist_h.text)
            
            # فرمول: distance * tan(angle)
            rad = math.radians(angle)
            res = dist * math.tan(rad)
            
            self.lbl_res_h.text = f"Ertefa: {res:.2f}"
        except ValueError:
            self.lbl_res_h.text = "Error: Lotfan adad vared konid"

    def calculate_slope(self, instance):
        try:
            angle = float(self.input_angle_s.text)
            
            # فرمول: tan(angle)
            rad = math.radians(angle)
            res = math.tan(rad)
            
            self.lbl_res_s.text = f"Shib: {res:.3f} ({res*100:.1f}%)"
        except ValueError:
            self.lbl_res_s.text = "Error: Lotfan adad vared konid"

if __name__ == '__main__':
    FazeshApp().run()
