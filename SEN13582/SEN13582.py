import busio

from SEN13582.registers import *


class SEN13582:
    def __init__(self, i2c: busio.I2C, address=0x3E):
        self.i2c = i2c
        self.address = address
        
        testReg = self._read_reg_16(REG_INTERRUPT_MASK_A)
        print(f"{bin(testReg)}")
        
        if (testReg == 0xFF00):
            self._write_reg_8(REG_DIR_A, 0xFF)
            self._write_reg_8(REG_DIR_B, 0xFC)
            self._write_reg_8(REG_DATA_B, 0x01)
            
    def scan(self):
        self._write_reg_8(REG_DATA_B, 0x00)
        
        last_bar_raw = self._read_reg_8(REG_DATA_A)
        print(f"{bin(last_bar_raw)}")
        
    def _write_reg_8(self, reg, val):
        self.i2c.writeto(self.address, bytes([reg, val]))
  
    def _write_reg_16(self, reg, val):
        self.i2c.writeto(self.address, bytes([reg, ((val>>8)&(0xFF)), (val&0xFF)]))

    def _read_reg_8(self, reg):
        self.i2c.writeto(self.address, bytes([reg]))
        result = bytearray(1)
        self.i2c.readfrom_into(self.address, result)
        return result[0]
  
    def _read_reg_16(self, reg):
        self.i2c.writeto(self.address, bytes([reg]))
        result = bytearray(2)
        self.i2c.readfrom_into(self.address, result)
        return ((result[0]<<8) | result[1])