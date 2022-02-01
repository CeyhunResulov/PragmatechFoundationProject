
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


def show_result(n):
    racers_results = []
    for i in range(0,n):
        if 2 <= n <= 10: 
            racer_result = int(input('xallar:'))
            if -100 <= racer_result <= 100:
                racers_results.append(racer_result)
            else:               
                print(f'{i+1}istirakci xali serti odemir!')                      
    racers_results.sort()
    print(racers_results[len(racers_results)-2])
show_result(int(input()))
