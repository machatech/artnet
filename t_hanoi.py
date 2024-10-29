def printer(tower,disks):
    rods = ['A','B','C']
    for lvl in range(disks+2,0,-1):
        for rod in rods:
            if len(tower[rod]) >= lvl:
                print(f" {tower[rod][lvl-1]}   ",end = '')
            else:
                print('     ',end='')
        print()
    print('-------------')
    print(' A    B    C')
    # print('\n')
def t_hanoi(disks,from_rod,to_rod,aux_rod,tower):
    if disks == 0:
        return
    t_hanoi(disks-1,from_rod,aux_rod,to_rod,tower)
    print(f"Moved disk {disks}  from {from_rod} to {to_rod}")
    print()
    tower[to_rod].append(tower[from_rod].pop())
    # print(tower[to_rod], tower[from_rod])
    printer(tower,disks)
    t_hanoi(disks-1,aux_rod,to_rod,from_rod,tower)

def main():
    while True:
        print("Enter exit to EXIT the program") 
        print("We have 3 Towers  A , B , C")
        disks = input("Enter the no of Disks : ")
        if disks.lower() == 'exit':
            print("Exiting the program")
            break
        try:
            disks = int(disks)
            if disks < 0:
                raise ValueError("Enter Postive values.")
            elif disks == 0:
                raise ValueError("Enter values greater than 0.")
            tower = {
                'A' : list(range(disks,0,-1)),'B' : [],'C' : []
            }
            t_hanoi(disks,'A','C','B',tower)
            break
        except ValueError:
            print(f'Invalid Input. Enter the +ve values')
main()
    # || [disk {disks}]  {from_rod} -> {to_rod}