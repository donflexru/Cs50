request=input("where do you want to put your treasure? ")
# request_refined=request.split("")
box_1=["[]","[]","[]","[]","[]"]
box_2=["[]","[]","[]","[]","[]"]
box_3=["[]","[]","[]","[]","[]"]
box_4=["[]","[]","[]","[]","[]"]
box_5=["[]","[]","[]","[]","[]"]
cheese_board=[box_1, box_2, box_3, box_4, box_5]
print(f"{box_1}\n{box_2}\n{box_3}")
print("  ")
horizontal=int(request[0])
vertical=int(request[1])
cheese_board[horizontal-1][vertical-1]="x "
print(f"{box_1}\n{box_2}\n{box_3}\n{box_4}\n{box_5}")


