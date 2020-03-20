import os
import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import argparse

def arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("-wt",help="work time(minute)",dest="work_time",type=int,
                        default="30")
    parser.add_argument("-rt",help="relex time(minute)",dest="relex_time",type=int,
                        default="10")
    parser.add_argument("-r",help="repeat times",dest="repeat_times",type=int,
                        default="1")
    args = parser.parse_args()
    return args

def progressbar(curr, total, duration=10, extra=''):
    frac = curr / total
    filled = round(frac * duration)
    print('\r', '🍅' * filled + '--' * (duration - filled), '[{:.0%}]'.format(frac), extra, end='')

def play_music(flag):
    filepath = ''
    if flag == 1:
        # 开始休息时放的音乐
        filepath = './end.mp3'
    else:
        # 开始工作时放的音乐
        filepath = './start.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play(start=0.0)
    time.sleep(10)
    pygame.mixer.music.stop()

def tomato(minutes):
    start_time = time.perf_counter()
    while True:
        diff_seconds = int(round(time.perf_counter() - start_time))
        left_seconds = minutes * 60 - diff_seconds
        if left_seconds <= 0:
            print('')
            break

        countdown = '{}:{} ⏰'.format(int(left_seconds / 60), int(left_seconds % 60))
        duration = min(minutes, 25)
        # duration = 10
        progressbar(diff_seconds, minutes * 60, duration, countdown)
        time.sleep(1)

if __name__ == "__main__":
    args = arg()
    print('work time(minute):%d'%(args.work_time))
    print('relex time(minute):%d'%(args.relex_time))
    print('repeat times:%d'%(args.repeat_times))
    for i in range(args.repeat_times):
        flag = 1
        tomato(args.work_time)
        play_music(flag)

        flag = 0
        tomato(args.relex_time)
        play_music(flag)