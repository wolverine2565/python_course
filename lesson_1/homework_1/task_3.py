"""3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета."""

ticket_number = int(input())

sum_first = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
sum_last = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])

if sum_first == sum_last:
    print("Yout ticket is lucky")
else:
    print("Yout ticket is not lucky")