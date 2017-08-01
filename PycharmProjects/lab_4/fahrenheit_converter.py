# -*- coding: utf-8 -*-

def input_celsius_value():
    print("변환하고 싶은 섭씨 온도를 입력해 주세요: ")
    celsius_value = float(input())
    return celsius_value

def convert_celsius_fahrenheit(celsius_value):
    fah_conv = ((9/5)*celsius_value) + 32
    return fah_conv

def print_fahrenheit_value(celsius_value, fah_conv):
    print("섭씨온도 : ", celsius_value)
    print("화씨온도 : ", fah_conv)

def main():
    print("본 프로그램은 섭씨를 화씨로로 변환해주는 프로그램입니다")
    print("============================")
    # ===Modify codes below=================
    celsius_value = input_celsius_value()
    fah_conv = convert_celsius_fahrenheit(celsius_value)
    print_fahrenheit_value(celsius_value, fah_conv)
    # ======================================
    print("===========================")
    print("프로그램이 종료 되었습니다.")


if __name__ == '__main__':
    main()