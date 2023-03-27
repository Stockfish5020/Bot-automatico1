import pyautogui
import time

posicion_btn_puntosSuspensivos = (461, 426)
posicion_btn_eliminarChat = (408, 890)
posicion_btn_confirmarEliminarChat = (1257, 666)
posicion_field_URL = (665, 81)

# while True:
#     mouseX, mouseY = pyautogui.position()
#     print(mouseX, mouseY)
#     time.sleep(1)

print("cambia a la ventana de msngr")

time.sleep(3)
while True:
    pyautogui.moveTo(
        posicion_field_URL[0],
        posicion_field_URL[1],
        duration=0.5,
        tween=pyautogui.easeInOutQuad
    )
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.write('https://www.facebook.com/messages')
    pyautogui.press('enter')
    time.sleep(7)
    pyautogui.moveTo(
        posicion_btn_puntosSuspensivos[0],
        posicion_btn_puntosSuspensivos[1],
        duration=0.5,
        tween=pyautogui.easeInOutQuad
    )
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(
        posicion_btn_eliminarChat[0],
        posicion_btn_eliminarChat[1],
        duration=0.5,
        tween=pyautogui.easeInOutQuad
    )
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(
        posicion_btn_confirmarEliminarChat[0],
        posicion_btn_confirmarEliminarChat[1],
        duration=0.5,
        tween=pyautogui.easeInOutQuad
    )
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)