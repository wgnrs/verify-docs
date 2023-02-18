from file_mover import move_files_periodically

def main():

    origin = 'Directory of origin'
    destiny = 'Directory of destiny'
    # Hours on seconds
    wait = 24 * 60 * 60

    move_files_periodically(origin, destiny, wait)

if __name__ == '__main__':
    main()