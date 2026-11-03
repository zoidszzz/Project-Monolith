import machine
import time
import ubluetooth

barcode_uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))
feed_roller = machine.PWM(machine.Pin(14), freq=1000)
deal_flywheel = machine.PWM(machine.Pin(15), freq=1000)
gate_solenoid = machine.Pin(16, machine.Pin.OUT)

step_pins = [machine.Pin(2, machine.Pin.OUT), machine.Pin(3, machine.Pin.OUT),
             machine.Pin(4, machine.Pin.OUT), machine.Pin(5, machine.Pin.OUT)]
step_seq = [[1,0,0,1],[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1]]

class DealerCentral:
    def __init__(self):
        self.ble = ubluetooth.BLE()
        self.ble.active(True)
        self.current_angle = 0
        self.is_connected = True 

    def rotate_base(self, target_angle):
        delta = target_angle - self.current_angle
        steps = int((delta / 360) * 4096)
        direction = 1 if steps > 0 else -1
        steps = abs(steps)
        for _ in range(steps):
            for step in step_seq[::direction]:
                for pin, val in zip(step_pins, step):
                    pin.value(val)
                time.sleep_ms(2)
        self.current_angle = target_angle

    def dispatch_card(self, target_zone, angle, search_code=None):
        self.rotate_base(angle)
        deal_flywheel.duty_u16(65535)
        time.sleep_ms(150) 
        feed_roller.duty_u16(42000)
        
        scanned_barcode = ""
        start = time.ticks_ms()
        while time.ticks_diff(time.ticks_ms(), start) < 800:
            if barcode_uart.any():
                scanned_barcode = barcode_uart.read().decode('utf-8').strip()
                break
                
        if search_code and scanned_barcode == search_code:
            gate_solenoid.value(1)
            time.sleep_ms(100)
            gate_solenoid.value(0)
        else:
            time.sleep_ms(200)
            
        feed_roller.duty_u16(0)
        deal_flywheel.duty_u16(0)

hub = DealerCentral()
